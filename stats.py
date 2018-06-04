#!/usr/bin/env python3
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

import pandas as pd  # sudo pip install pandas
import numpy as np  # sudo pip install numpy

from distutils.spawn import find_executable
from optparse import OptionParser
from os import path
import os
import time
import itertools
import threading
import subprocess
import re
import sys
import hashlib
import fileinput
import signal

# #
# Bulding classes
# #


SOLUTION_TIMEOUT_VALUE = 60


class TimeOutController:
    class TimeOut(Exception):
        pass

    def __init__(self, sec=SOLUTION_TIMEOUT_VALUE):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(sec)

    def cancel(self):
        signal.alarm(0)  # disable alarm

    def raise_timeout(self, a, n):
        raise TimeOutController.TimeOut()


class Checker(object):

    checked = []

    def __init__(self, compiler, path):
        self.compiler = compiler.split()
        self.path = path
        self.check()

    def check(self):
        binary = self.compiler[0]
        if binary not in self.checked and not find_executable(binary):
            raise EnvironmentError("{!r} not found. Do you have the compilers?".format(binary))  # noqa
        elif binary not in self.checked:
            self.checked += binary


class Execute(Checker):

    """Interactive languages building"""

    def enter_dir(self):
        self.old_dir = os.getcwd()
        os.chdir(path.dirname(self.path))

    def exit_dir(self):
        os.chdir(self.old_dir)

    def execute(self):
        self.enter_dir()
        before = time.time()
        args = self.compiler
        args += [path.basename(self.path)]
        try:
            toc = TimeOutController()
            program = subprocess.Popen(args, stdout=subprocess.PIPE)
            out, _ = program.communicate()
        except TimeOutController.TimeOut:
            out = b"TIMEOUT"
            program.kill()
        finally:
            toc.cancel()
        time_passed = time.time() - before
        self.exit_dir()
        return out, program.returncode, time_passed


class Build(Checker):

    """For compiled languages: C++, C for example"""

    fout = "compiled.out"

    def compile(self):
        args = [self.compiler[0], self.path, "-o", self.output] + self.compiler[1:]
        program = subprocess.Popen(args, stdout=subprocess.PIPE)
        return program.wait() == 0

    def execute(self):
        self.output = path.join(path.dirname(self.path), self.fout)
        if self.compile():
            compiled = path.abspath(self.output)
            program = Execute("bash -c", "{!r}".format(compiled))
            output = program.execute()
            os.remove(compiled)
            return output

        return b"compiles fails", EnvironmentError, 0


ERASE_LINE = "\x1b[2K"
BUILD_SUPPORT = [
    "Python",      # you need python | pacman -Su python
    "Go",          # you need golang | pacman -Su golang
    "Clojure",     # you need clojure | pacman -Su clojure
    "CommonLisp",  # you need clisp | pacman -Su clisp
    "Haskell",     # you need ghc | pacman -Su ghc
    "Lua",         # you need lua | pacman -Su lua5.3
    "Ruby",        # you need ruby | pacman -Su ruby
    "C",           # you need gcc | pacman -Su gcc
    "C++",         # you need | pacman -Su g++
    "Elixir",      # you need elixir | pacman -Su elixir
    "PHP",         # you need php | pacman -Su php
    # "Swift",       # you need swift | yaourt -Su swift
    # "Objective-C",  # you need gcc-objc | pacman -Su gcc-objc
    "Bash",        # hmm, i think you already have this
]

BUILD_FILES = ["stats.py", "stats.exs", "test", "add"]

BUILD_MACHINE = {

    "Python": {
        "cmdline": "python3",
        "builder": Execute
    },

    "Go": {
        "cmdline": "go run",
        "builder": Execute
    },

    "Clojure": {
        "cmdline": "clojure",
        "builder": Execute
    },

    "CommonLisp": {
        "cmdline": "sbcl --script",
        "builder": Execute
    },

    "Haskell": {
        "cmdline": "runhaskell",
        "builder": Execute
    },

    "C": {
        "cmdline": "gcc -std=c99 -lm",
        "builder": Build
    },

    "C++": {
        "cmdline": "g++ -std=c++0x",
        "builder": Build
    },

    "Lua": {
        "cmdline": "lua",
        "builder": Execute
    },

    "Ruby": {
        "cmdline": "ruby",
        "builder": Execute
    },

    "Bash": {
        "cmdline": "bash",
        "builder": Execute
    },

    "Elixir": {
        "cmdline": "elixir",
        "builder": Execute
    },

    "Objective-C": {
        "cmdline": "gcc -Wall -lm -lobjc",
        "builder": Build
    },

    "PHP": {
        "cmdline": "php",
        "builder": Execute
    },

    "Swift": {
        "cmdline": "swift",
        "builder": Execute
    }

}


# CLI INTERFACE
# -l (list languages with solutions)
# -c (do count solutions)
# -p (print the path)
# -a all languages selected
# -s language (search)
# -b (build)

# Examples of usage:
# python stats.py --list
# python stats.py --list --count
# python stats.py --all --path
# python stats.py --all --count
# python stats.py -s Python -s Haskell -c


# #
# Cmdline parsing definitions
# #

def _callback(option, opt_str, value, parser):
    """
    Used to parse several arguments for one option, knowing that arguments
    never start with a `-` and `--`
    """
    assert value is None
    value = []
    for arg in parser.rargs:
        # stop on --foo like options
        if arg[:2] == "--" and len(arg) > 2:
            break
        if arg[:1] == "-" and len(arg) > 1:
            break
        value.append(arg)
    del parser.rargs[:len(value)]
    setattr(parser.values, option.dest, value)

parser = OptionParser()

parser.add_option(
    "-l", "--list",
    help="Print a list of the languages whose have solutions",
    dest="list",
    action="store_true",
    default=False,
)

parser.add_option(
    "-s", "--search",
    help="Choose the languages for print information",
    dest="search",
    action="append",
    default=[],
    nargs=1,
)

parser.add_option(
    "-f", "--files",
    help="Receive a list of file paths to build them",
    dest="files",
    action="callback",
    callback=_callback,
)

parser.add_option(
    "-c", "--count",
    help="Print the count of each solution",
    dest="count",
    action="store_true",
    default=False,
)

parser.add_option(
    "-b", "--build",
    help="Execute the solutions and print each solution",
    dest="build",
    action="store_true",
    default=False,
)

parser.add_option(
    "-p", "--path",
    help="Print the path of each solution",
    dest="path",
    action="store_true",
    default=False,
)

parser.add_option(
    "-a", "--all",
    help="Select all the languages for search",
    dest="all",
    action="store_true",
    default=False,
)


parser.add_option(
    "-m", "--blame",
    help="Show the slowest solutions that needs help",
    dest="blame",
    action="store_true",
    default=False,
)

parser.add_option(
    "-g", "--graph",
    help="Make a cool graph with the final DataFrame data",
    dest="graph",
    action="store_true",
    default=False,

)

parser.usage = "%prog [-s language] [-al] [-cpb] [--blame] [-g]"


def walk_problems():
    """
    Function: walk_problems
    Summary: Walking for repository to get each content of ProblemXXX
    Examples: Uniq behavior
    Returns: list of 3-uples of strings <list ("1", "2", "3"), ...>
    """
    problem = re.compile("./Problem[0-9]{3}/")
    problems = []
    for x in os.walk("."):
        if problem.match(x[0]) and "pycache" not in x[0]:
            problems.append(x)
    return problems


def read_hashfile(fpath):
    """Read .hash based on fpath and clean the weird chars"""
    return open(fpath).read().strip(' -\n')


def get_problem_hashes():
    """
    Function: get_problem_hashes
    Summary: Walking from each problem and return a tuple
            (problem_name, hash_content)
    Returns: list of tuples <problem_name: string, hash_content: string>
    """
    hash_pattern = re.compile("./Problem[0-9]{3}")
    hashes = {}
    for file_tuple in os.walk("."):
        if hash_pattern.match(file_tuple[0]) and ".hash" in file_tuple[-1]:
            problem = file_tuple[0]
            hash_path = path.join(problem, '.hash')
            hash_content = read_hashfile(hash_path)
            hashes[problem.strip('./')] = hash_content

    return hashes


def digest_answer(answer):
    clean_answer = answer.strip(' \n')
    return hashlib.md5(clean_answer.encode('utf-8')).hexdigest()


def search_language(query, languages):
    """
    Function: search_language
    Summary: Search for languages based on regex
    Examples:
        >>> search_language(["C"], ["C", "C++", "Python"])
            ["C", "C++"]
    Attributes:
        @param (query): list of languages for search
        @param (languages): collections of languages normalized
    Returns: list of results as strings <list (string)>
    """

    return set(query) & set(languages)


def split_problem_language(path):
    """
    Function: split_problem_language
    Summary: Get a path and split into problem and language
    Examples:
        >>> split_problem_language("./Problem001/Python")
        ["Problem001", "Python]

    Attributes:
        @param (path): path like ./Folder/Language
    Returns: [Problem, Language] <(string, string)>
    """
    return path.strip("./").split("/")


def is_solution(string):
    solution = re.compile("solution_+(?!out)")
    return solution.match(string)


def parse_solutions(problems):
    """
    Function: parse_solutions
    Summary: Organize the solutions of problems
    Examples: <NONE>
    Attributes:
        @param (problems): os.walk functions output
    Returns: problem:lang -> [solutions] <dict>
    """
    map_solutions = {}
    for problem_path, dirs, files in problems:
        problem, lang = split_problem_language(problem_path)
        map_solutions.setdefault(problem, {}).setdefault(lang, [])
        for file in files:
            if is_solution(file):
                map_solutions[problem][lang].append(file)

    return map_solutions


def load_dataframe():
    """
    Function: load_dataframe
    Summary: Load all solutions of repository at dataframe
    Examples:
        >>> df = load_dataframe()[]
        >>> py = df["Python"]
                            Python
            Problem001      [solution_1.py, solution_2.py]
            Problem002                      [solution_1.py]
            Problem003                      [solution_1.py]
            Problem004                      [solution_1.py]

        If you observe: (index + column_name) <- list_solutions -> filepaths!
    Returns: pd.DataFrame
    """
    return pd.DataFrame.from_dict(parse_solutions(walk_problems()), "index")


def solutions_paths(df, from_files=None):
    """
    Function: load_filepaths
    Summary: Get each filepath of solutions based on pd.DataFrame
    Examples:
        >>> df = load_dataframe()
        >>> py = df[["CommonLisp"]]
        >>> load_filepaths(py)
        ["..."]

    Attributes:
        @param (df): pd.DataFrame
    Returns: list of file paths
    """
    paths = []
    if from_files:
        for problem, lang, s in from_files:
            paths.append((lang, path.join(problem, lang, s)))
        return paths
    for column in df.columns:
        solutions = df[df[column].notnull()][column]
        lang = solutions.name
        problems = solutions.index
        for problem in problems:
            p = ((lang, path.join(problem, lang, s))
                 for s in solutions[problem])
            paths.extend(p)
    return paths


def count_solutions(df, solutions=True):
    """
    Function: count_solutions
    Summary: Count the number of solutions of each problem and language
    Examples: Iam tired...
    Attributes:
        @param (df): pd.DataFrame
    Returns: pd.DataFrame
    """
    df = df.dropna(axis=1, how='all')  # columns all nan
    df = df.dropna(how='all')  # rows all nan
    df_ = pd.DataFrame()
    df_ = df.applymap(lambda x: len(x) if x is not np.NAN else 0)

    if len(df.columns) > 1 and solutions:
        df_["Solutions"] = df_[df_.columns].apply(tuple, axis=1).map(sum)
        df_ = df_[df_.Solutions > 0]

    return df_

def handle_files(files):
    """
    Analyse files to return two lists :
        - solutions : list of files as 3-uple of strings that are more likely solutions
          on the format: (ProblemXXX, 'Lang', 'solution_x.y')
        - build_files : list of files that are more build files (stats.py,
          stats.exs, ...)
    """
    solutions = []
    build_files = []
    for f in files:
        if f.count("/") == 2:
            solutions.append(tuple(f.split("/")))
        elif f.count("/") == 0 and f in BUILD_FILES:
            build_files.append(f)
    return list(filter(lambda x: is_solution(x[2]), solutions)), build_files

# docs?
def spinner(control):
    animation = r"⣾⣽⣻⢿⡿⣟⣯"
    sys.stdout.write(3 * " ")
    for c in itertools.cycle(animation):
        current_time = time.time() - control.time
        message = "(" + c + ")" + " t: {:.2f}".format(current_time)
        sys.stdout.write(message)
        time.sleep(0.1)
        sys.stdout.write(len(message) * "\010")
        sys.stdout.flush()
        if control.done:
            break


# need docs
def choose_builder(lang, fpath):
    try:
        if lang in BUILD_MACHINE:
            builder = BUILD_MACHINE[lang]['builder']
            cmdline = BUILD_MACHINE[lang]['cmdline']
            b = builder(cmdline, fpath)
        else:
            raise Exception("Builder not configured for {!r}! Call the developer".format(lang))  # noqa
    except Exception as e:
        print("\n", e)
        os._exit(1)
    finally:
        return b


# need docs
def execute_builder(b):
    out, err, t = b.execute()
    answer = out.decode("utf-8").strip("\n")
    if err:
        print(err)
        os._exit(1)
    sys.stdout.write(ERASE_LINE)
    building = "\rBuilt {}: Answer: {}: {:.2f}s\n".format(b.path, answer, t)
    sys.stdout.write(building)
    sys.stdout.flush()

    return answer, t

# need docs
def build_result(df, ignore_errors=False, blame=False, only=()):

    class Control:  # to handle the spinner time at each solution
        time = time.time()
        done = False

    control = Control()
    columns = ["Problem", "Language", "Time", "Answer", "Correct"]
    data = []
    hashes = get_problem_hashes()
    spin_thread = threading.Thread(target=spinner, args=(control,))
    spin_thread.start()
    _problems = only if only else solutions_paths(df)
    for lang, spath in _problems:
        if "slow" in spath and not blame:
            sys.stdout.write("\rIgnored {}: bad solution (slow).\n".format(spath))  # noqa
            continue

        if lang in BUILD_SUPPORT:
            sys.stdout.write("@Building next {}: {}".format(spath, 12 * ' '))
            b = choose_builder(lang, spath)
            problem = split_problem_language(spath)[0]
            outtimed = False
            correct = False
            control.time = time.time()
            answer, t = execute_builder(b)
            outtimed = answer == "TIMEOUT"
            if (not outtimed) and problem in hashes:
                answer_hash = digest_answer(answer)
                correct = answer_hash == hashes[problem]

            data.append([problem, lang, t, answer, correct])

        elif not ignore_errors:
            sys.stdout.write("\r{}: Don't have support yet for {!r}!\n".format(spath, lang))  # noqa
    sys.stdout.write("\r\n")
    sys.stdout.flush()
    control.done = True
    spin_thread.join()
    final_df = pd.DataFrame(data, columns=columns)
    return final_df.sort_values("Problem")


def list_by_count(df):
    df_ = count_solutions(df, solutions=False)
    count = [sum(df_[lang]) for lang in df_.columns]
    table = pd.DataFrame(count, index=df_.columns,
                         columns=["Solutions"])
    return table.sort_values("Solutions", ascending=False)


def blame_solutions(df):
    df_ = df.applymap(
        lambda solutions:
        [x for x in solutions if 'slow' in x] or np.NAN
        if solutions is not np.NAN else np.NAN
    )

    return df_


# Problem015 -> 15
def remove_problem(df):
    df_ = df
    df_.Problem = df.Problem.map(lambda x: x.replace("Problem", "").strip('0'))
    return df_


def build_per_language(df):
    index = df.Problem.map(int).max()
    languages = set(df.Language)

    data = {lang: np.full(index, np.nan) for lang in languages}
    for _, row in df.iterrows():
        data[row['Language']][int(row['Problem']) - 1] = row['Time']

    df_ = pd.DataFrame(data, index=range(1, index + 1)).dropna(how='all')
    df_.index.name = 'Problems'

    return df_


def header(opts):
    return "Command: " + ' '.join([x.capitalize() for x in opts if opts[x]])


def handle_graph(df, options):
    import matplotlib.pyplot as plt
    import matplotlib
    cicle_colors = itertools.cycle(['b', 'r', 'g', 'y', 'k'])
    my_colors = itertools.islice(cicle_colors, None, len(df))
    matplotlib.style.use('ggplot')
    if options.build:
        df = build_per_language(remove_problem(df))
        df.plot()
    elif options.list and options.count:
        # Make a list by cycling through the colors you care about
        # to match the length of your data.
        df.plot(kind='barh', stacked=True, color=list(my_colors))
    plt.show()


def handle_options(options):
    df = load_dataframe()
    langs = {x.lower(): x for x in df.columns}
    query = [x.lower() for x in options.search]
    uncommited_solutions = []
    uncommited_core_files = []
    tbsolutions = []

    langs_selected = [langs[x] for x in search_language(query, langs)]

    if options.files:
        uncommited_solutions, uncommited_core_files = handle_files(options.files)
        if not uncommited_solutions and uncommited_core_files:
            sys.stdout.write(
                "\rForced to exit: No solutions to build\nChanged_core_files : \n {}".format(
                uncommited_core_files)
            )
            sys.exit(0)
        tbsolutions = solutions_paths(df, from_files=uncommited_solutions)

    if options.all:
        langs_selected = [x for x in langs.values()]

    if options.blame:
        df = blame_solutions(df)

    if options.list:
        if options.count:
            df = list_by_count(df)

        elif options.path:
            langs_selected = [x for x in langs.values()]

        else:
            df = '\n'.join(sorted(df.dropna(axis=1, how='all').columns))
    else:
        df = df[langs_selected]

    if options.count and not options.list:
        df = count_solutions(df)

    elif options.build:
        try:
            df = build_result(df[langs_selected],
                              options.all,
                              options.blame,
                              only=tbsolutions)
        except(SystemExit, KeyboardInterrupt):
            os._exit(1)

    elif options.path:
        df = '\n'.join(path for _, path in solutions_paths(df[langs_selected]))

    pd.set_option("display.max_rows", len(df))
    print(df)

    count_ws = list(df["Correct"]).count(False)
    correct_ratio = 1 - count_ws/len(df) if count_ws else 1

    sys.stdout.write(
        "Correct solutions ratio : {0}% \n".format(correct_ratio * 100)
    )
    if count_ws:
        sys.exit(1)

    if options.graph:
        handle_graph(df, options)


def main():
    options, _ = parser.parse_args()

    if not any(options.__dict__.values()):
        parser.print_help()
        os._exit(0)

    print(header(options.__dict__))
    handle_options(options)


if __name__ == "__main__":
    main()
