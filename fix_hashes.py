# This is just a fix script
# Do not merge with this file on PR
import os
import subprocess
import time
import hashlib
import timeout_decorator

RUNTIME_LIMIT = 70

# Since this is just a fix attemp lets assume we run this file from ProjectEuler
# directory.

PE_PATH = os.getcwd()
PE_HASH = "{0}/{1}/.hash"

# You can add languages be carefull with languages that need compilation before
# need to implemented that in _run_solution_script

_supported_languages = {'Python' : '.py',
                        'Elixir' : '.exs',
                        'Ruby' : '.rb',
                        'CommonLisp' : '.lisp'}

_starters = {'Ruby' : 'ruby',
             'Python' : 'python3',
             'CommonLisp' : 'clisp',
             'Elixir' : 'elixir'}

def _problem_data(n, env=None):
    sn = str(n)
    while(len(sn)) < 3:
        sn = "0{0}".format(sn)
    if env:
        return "Problem{0}/{1}".format(sn, env)
    return "Problem{0}".format(sn)

_cbtr = lambda x : x.decode('utf-8')
hash_path = lambda n : PE_HASH.format(PE_PATH, _problem_data(n))

_solution = lambda n, env:  "{0}/{1}/solution_1{2}".format(
                PE_PATH,_problem_data(n, env), _supported_languages[env]
            )
_solution_slow = lambda n, env:  "{0}/{1}/solution_slow_1{2}".format(
                PE_PATH,_problem_data(n, env), _supported_languages[env]
            )

_hash_file = lambda x : "{0}/{1}/.hash".format(PE_PATH, _problem_data(x))

def _hash_answer(answer):
    """
    hash execution result using md5
    """
    answer = answer.encode('utf-8')[:-1]
    hashed_answer = hashlib.md5(answer).hexdigest()
    return hashed_answer


###############################################################################
def _subprocess_call_with_communicate(cmd):
    """
    execute command line
    """
    c = cmd.split(' ')
    p = subprocess.Popen(c, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    return _cbtr(stdout), _cbtr(stderr), p.returncode

###############################################################################

def find_solution_for_problem(n, slow=False):
    found = False
    for lang in _supported_languages.keys():
        if slow:
            path = _solution_slow(n, lang)
        else:
            path = _solution(n, lang)
        if os.path.exists(path):
            return lang, path
    return False, False

@timeout_decorator.timeout(RUNTIME_LIMIT, timeout_exception=StopIteration)
def _run_solution_script(lang, path):
    """
    lets assume all the problems have a python script solution,
    and they have correct answer. Generating and picking correctly
    those answer can help us rewriting new correct hashes
    """
    cmd_line = "{0} {1}".format(_starters[lang], path)
    op, err, es = _subprocess_call_with_communicate(cmd_line)
    # ('233168\n', '', 0)
    return op[:-1], err, es

@timeout_decorator.timeout(RUNTIME_LIMIT - 50, timeout_exception=StopIteration)
def _no_pitty_run_solution(lang, path):
    cmd_line = "{0} {1}".format(_starters[lang], path)
    op, err, es = _subprocess_call_with_communicate(cmd_line)
    # ('233168\n', '', 0)
    return op[:-1], err, es


###############################################################################

def _rewrite_hash_file(problem_n, answer):
    """
    rewrite hash
    """
    with open(_hash_file(problem_n), 'w') as f:
        f.write(_hash_answer(answer))
    print('   === > fixed .hash file for problem {0}'.format(problem_n))


def run_solution(lang, path, no_pitty=False):
    try:
        if no_pitty:
            answer, err, es = _no_pitty_run_solution(lang, path)
        else:
            answer, err, es = _run_solution_script(lang, path)
        if not answer:
            print("   === > SKIPPED NO ANSWER [ es : {0} ]".format(es))
            return -1
        print('   === > answer : {0}'.format(answer))
        return answer
    except:
        print('   === > Time run out ')
        return False

###############################################################################
def run_fix_for_all_problems(p, q):
    """
    fix hash files for all problems between p, q
    """
    a, b, s = None, None, None
    total_fixed_hashes = 0
    unfixed_hashes = []
    timed_out_solutions = []
    no_pitty_club = []
    time_1 = time.time()
    for i in range(p, q):
        if not os.path.exists("{0}/{1}".format(PE_PATH, _problem_data(i))):
            continue
        a, b = find_solution_for_problem(i)
        if a:
            print('=== > found solution for problem {0} in {1}'.format(i, a))
            s = run_solution(a, b)
            if s == -1:
                unfixed_hashes += [i]
                continue
            if s:
                _rewrite_hash_file(i, s)
                total_fixed_hashes += 1
            else:
                timed_out_solutions += [i]
                unfixed_hashes += [i]
        else:
            a, b = find_solution_for_problem(i, slow=True)
            if a:
                print('   === > found slow solution for problem {0} in {1}'.format(i, a))
                if i > 145:
                    print('   === > NO PITTY mode on for this problem')
                    no_pitty_club += [i]
                    s = run_solution(a, b, no_pitty=True)
                else:
                    s = run_solution(a, b)
                if s == -1:
                    unfixed_hashes += [i]
                    continue
                if s:
                    _rewrite_hash_file(i, s)
                    total_fixed_hashes += 1
                else:
                    timed_out_solutions += [i]
                    unfixed_hashes += [i]
            else:
                print('   === > No solution found for problem {0}'.format(i))
                unfixed_hashes += [i]
    time_2 = time.time()
    print('      ======= > Total runtime :  {0}'.format(time_2 - time_1))
    print('      ======= > Total fixed hashes {0}'.format(total_fixed_hashes))
    print('      ======= > Unsolved hashes : \n{0}'.format(
        ''.join(['       - ' + str(i) + '\n' for i in unfixed_hashes])
    ))
    print('      ======= > Timeout out solutions : \n{0}'.format(
        ''.join(['       - ' + str(i) + '\n' for i in timed_out_solutions])
    ))
    print('      ======= > No pitty solutions (too slow to test) : \n{0}'.format(
        ''.join(['       - ' + str(i) + '\n' for i in no_pitty_club])
    ))


if __name__ == "__main__":
    run_fix_for_all_problems(1, 600)
