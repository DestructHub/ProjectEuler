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
    answer = answer.encode('utf-8')
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


###############################################################################

def _manual_rehash_script(n):
    path = _hash_file(n)


def _rewrite_hash_file(problem_n, answer):
    """
    rewrite hash
    """
    with open(_hash_file(problem_n), 'w') as f:
        f.write(_hash_answer(answer))
    print('   === > fixed .hash file for problem {0}'.format(problem_n))


def run_solution(lang, path):
    try:
        answer, _, _ = _run_solution_script(lang, path)
        print('   === > answer : {0}'.format(answer))
        return answer
    except:
        print(' TOOO LONG RUNTIME ')
        return False

###############################################################################
def run_fix_for_all_problems(p, q):
    """
    fix hash problem for all problems between p, q
    """
    a, b, s = None, None, None
    time_1 = time.time()
    for i in range(p, q):
        if not os.path.exists("{0}/{1}".format(PE_PATH, _problem_data(i))):
            continue
        a, b = find_solution_for_problem(i)
        if a:
            print('   === > found solution for problem {0} in {1}'.format(i, a))
            s = run_solution(a, b)
            if s:
                _rewrite_hash_file(i, s)
        else:
            a, b = find_solution_for_problem(i, slow=True)
            if a:
                print('   === > found slow solution for problem {0} in {1}'.format(i, a))
                s = run_solution(a, b)
                if s:
                    _rewrite_hash_file(i, s)
            else:
                print('   === > No solution found for problem {0}'.format(i))
    time_2 = time.time()
    print('      ======= > Total runtime :  {0}'.format(time_2 - time_1))


if __name__ == "__main__":
    run_fix_for_all_problems(1, 600)
