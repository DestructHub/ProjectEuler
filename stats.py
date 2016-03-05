#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

import pandas as pd  # sudo pip install pandas
import numpy as np  # sudo pip install numpy

from os.path import join
from os import walk, _exit
from re import compile
from optparse import OptionParser
from subprocess import Popen, PIPE
from time import time
import threading
from itertools import cycle
from sys import stdout
from time import sleep


ERASE_LINE = '\x1b[2K'
BUILD_SUPPORT = [
    "Python",  # you need the python interpreter | pacman -Su python
    "Go",  # you need the golang compiler | pacman -Su golang
    "Clojure",  # you need lein && clojure | pacman -Su clojure
    "CommonLisp",  # you need clisp | pacman -Su clisp
    "Haskell",  # you need ghc | pacman -Su ghc
    # "C",
    # "C++"
]

# CLI INTERFACE
# -l (list languages with solutions)
# -c (do count solutions)
# -p (print the path)
# -a all languages selected
# -s language (search)

# Examples of usage:
# python stats.py --list
# python stats.py --list --count
# python stats.py --all --path
# python stats.py --all --count
# python stats.py -s Python -s Haskell -c


def debugorator(fn):
    """Useful decorator to debugorator functions/methods

    :param fn: function
    """
    from functools import wraps

    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        for key, value in kwargs.items():
            args += ('='.join(map(str, [key, value])),)
        if len(args) == 1:
            args = '({})'.format(args[0])
        print('@{0}{1} -> {2}\n'.format(fn.__name__, args, result))
        return result
    return wrapper


class Build(object):

    def __init__(self, args, path):
        self.bin = args
        self.path = path

    def execute(self):
        before = time()
        program = Popen(self.bin + [self.path], stdout=PIPE)
        out, err = program.communicate()
        time_passed = time() - before
        return out, err, time_passed


def charge_options():
    parser = OptionParser()

    parser.add_option(
        "-l", "--list",
        help="Print a list of the languages whose have solutions",
        dest="list",
        action='store_true',
        default=False,
    )

    parser.add_option(
        "-s", "--search",
        help="Choose the languages for print information",
        dest='search',
        action='append',
        default=[],
        nargs=1
    )

    parser.add_option(
        "-c", "--count",
        help="Print the count of each solution",
        dest='count',
        action='store_true',
        default=False,
    )

    parser.add_option(
        "-b", "--build",
        help="Execute the solutions and print each solution",
        dest='build',
        action='store_true',
        default=False,
    )

    parser.add_option(
        "-p", "--path",
        help="Print the path of each solution",
        dest='path',
        action='store_true',
        default=False,
    )

    parser.add_option(
        "-a", "--all",
        help="Select all the languages for search",
        dest='all',
        action='store_true',
        default=False,
    )

    parser.usage = "%prog [-s language] [-al] [-cp] "

    return parser


def walk_problems():
    """
    Function: walk_problems
    Summary: Walking for repository to get each content of ProblemXXX
    Examples: Uniq behavior
    Returns: list of 3-uples of strings <list ('1', '2', '3'), ...>
    """
    problem = compile("./Problem[0-9]{3}/")
    problems = []
    for x in walk("."):
        if problem.match(x[0]) and "pycache" not in x[0]:
            problems.append(x)
    return problems


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


# @debugorator
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
    return path.strip('./').split('/')


def parse_solutions(problems):
    """
    Function: parse_solutions
    Summary: Organize the solutions of problems
    Examples: <NONE>
    Attributes:
        @param (problems): os.walk functions output
    Returns: problem:lang -> [solutions] <dict>
    """
    solution = compile("solution_*")

    map_solutions = {}
    for path, dirs, files in problems:
        problem, lang = split_problem_language(path)
        map_solutions.setdefault(problem, {}).setdefault(lang, [])
        for file in files:
            if solution.match(file):
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
    return pd.DataFrame.from_dict(parse_solutions(walk_problems()), 'index')


def solutions_paths(df):
    """
    Function: load_filepaths
    Summary: Get each filepath of solutions based on pd.DataFrame
    Examples:
        >>> df = load_dataframe()
        >>> py = df[["CommonLisp"]]
        >>> load_filepaths(py)
        ["]

    Attributes:
        @param (df): pd.DataFrame
    Returns: list of file paths
    """
    paths = []
    for column in df.columns:
        solutions = df[df[column].notnull()][column]
        lang = solutions.name
        problems = solutions.index
        for problem in problems:
            p = ((lang, join(problem, lang, s)) for s in solutions[problem])
            paths.extend(p)

    return paths


def count_solutions(df):
    """
    Function: count_solutions
    Summary: Count the number of solutions of each problem and language
    Examples: I'm tired...
    Attributes:
        @param (df): pandas.pd.DataFrame
    Returns: InsertHere
    """
    df_ = pd.DataFrame()
    for column in df.columns:
        df_[column] = df[column].map(
            lambda x: len(x) if x is not np.NAN else 0)

    if len(df.columns) > 1:
        df_["Solutions"] = df_[df_.columns].apply(tuple, axis=1).map(sum)
        df_ = df_[df_.Solutions > 0]

    return df_


def spinner(signal):
    animation = r'|/\-'
    stdout.write(3 * ' ')
    t = time()
    for c in cycle(animation):
        if signal.run:
            message = '(' + c + ')' + ' t: {:.2f}'.format(time() - t)
            stdout.write(message)
            sleep(0.1)
            stdout.write(len(message) * '\010')
            stdout.flush()
        else:
            t = time()


# need docs
def choose_builder(lang, path):
    if lang == "Python":
        b = Build(['python'], path)
    elif lang == "Go":
        b = Build(['go', 'run'], path)
    elif lang == "Clojure":
        b = Build(['clojure'], path)
    elif lang == "CommonLisp":
        b = Build(["clisp"], path)
    elif lang == "Haskell":
        b = Build(["runhaskell"], path)
    else:
        raise Exception("Error; U have the {!r} compilers?".format(lang))
        exit(1)
    return b


# need docs
def execute_builder(b, signal):
    signal.run = True
    out, err, t = b.execute()
    signal.run = False
    answer = out.decode('utf-8').strip('\n')
    if err:
        exit(1)
    stdout.write(ERASE_LINE)
    building = '\rBuilded {}: Answer: '.format(b.path)
    stdout.write(building)
    output = "{}: {:.2f}s @Loading next:     ".format(answer, t)
    stdout.write(output)
    stdout.flush()

    return answer, t


# need docs
def build_result(df, ignore_errors=False):
    class signal:
        run = False

    columns = ['Problem', 'Language', 'Time', 'Answer']
    data = []
    spin_thread = threading.Thread(target=spinner, args=[signal])
    spin_thread.start()
    for lang, path in solutions_paths(df):
        if lang in BUILD_SUPPORT and 'slow' not in path:
            b = choose_builder(lang, path)
            answer, t = execute_builder(b, signal)
            problem = split_problem_language(path)[0]
            data.append([problem, lang, t, answer])
        elif 'slow' in path:
            stdout.write("\rIgnored: {}: bad solution (slow).".format(path))
        elif not ignore_errors:
            stdout.write("\rDon't have support yet for {!r}!\n".format(lang))
    stdout.write("\r\n")
    stdout.flush()
    final_df = pd.DataFrame(data, columns=columns)
    pd.set_option('display.max_rows', len(df))
    print(final_df.sort_values('Time'))
    pd.reset_option('display.max_rows')
    _exit(0)


def list_by_count(df):
    c = count_solutions(df)
    count = [sum(c[lang]) for lang in df.columns]
    table = pd.DataFrame(count, index=df.columns,
                         columns=["Solutions"])
    print(table.sort_values("Solutions", ascending=False))


def handle_options(options):
    df = load_dataframe()
    langs = {x.lower(): x for x in df.columns}
    query = [x.lower() for x in options.search]

    if options.all:
        langs_selected = [x for x in langs.values()]
    else:
        langs_selected = [langs[x] for x in search_language(query, langs)]
    
    if options.list:
        if options.count:
            list_by_count(df)

        elif options.path:
            langs_selected = [x for x in langs.values()]

        else:
            for lang in sorted(df):
                print(lang)

    if options.count and not options.list:
        print(count_solutions(df[langs_selected]))

    elif options.build:
        try:
            build_result(df[langs_selected], options.all)
        except(SystemExit, KeyboardInterrupt):
            _exit(1)

    elif options.path:
        for _, path in solutions_paths(df[langs_selected]):
            print(path)

    elif not any(options.__dict__.values()):
        parser.print_help()


def main():
    parser = charge_options()
    options, _ = parser.parse_args()
    handle_options(options)

if __name__ == '__main__':
    main()
