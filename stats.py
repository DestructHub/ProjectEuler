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

from os import walk, remove, _exit
from os.path import join, dirname, abspath
from re import compile
from optparse import OptionParser
from subprocess import Popen, PIPE
from time import time
import threading
from itertools import cycle
from sys import stdout
from time import sleep


ERASE_LINE = "\x1b[2K"
BUILD_SUPPORT = [
    "Python",  # you need the python interpreter | pacman -Su python
    "Go",  # you need the golang compiler | pacman -Su golang
    "Clojure",  # you need lein && clojure | pacman -Su clojure
    "CommonLisp",  # you need clisp | pacman -Su clisp
    "Haskell",  # you need ghc | pacman -Su ghc
    "Lua",
    "Ruby",
    "C",
    "C++",
    "Bash",
    "Elixir"
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


# #
# Cmdline parsing definitions
# #

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
    nargs=1
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

parser.usage = "%prog [-s language] [-al] [-cp] "


# #
# Bulding class
# #


class Build(object):

    """Interactive languages building"""

    def __init__(self, args, path):
        self.bin = args.split()
        self.path = path

    def execute(self):
        before = time()
        program = Popen(self.bin + [self.path], stdout=PIPE)
        out, _ = program.communicate()
        time_passed = time() - before
        return out, program.returncode, time_passed


class SpecialBuild(object):

    """For compiled languages
    C++, C at example
    """

    fout = "compiled.out"

    def __init__(self, compiler, path):
        self.compiler = compiler.split()
        self.path = path
        self.output = join(dirname(self.path), self.fout)

    def compile(self):
        args = self.compiler + [self.path, "-o", self.output]
        program = Popen(args, stdout=PIPE)
        return program.wait() == 0

    def execute(self):
        if self.compile():
            compiled = abspath(self.output)
            program = Build("bash -c", "{!r}".format(compiled))
            output = program.execute()
            remove(compiled)
            return output
        return b"compiles fails", EnvironmentError, 0


def walk_problems():
    """
    Function: walk_problems
    Summary: Walking for repository to get each content of ProblemXXX
    Examples: Uniq behavior
    Returns: list of 3-uples of strings <list ("1", "2", "3"), ...>
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
    return path.strip("./").split("/")


def parse_solutions(problems):
    """
    Function: parse_solutions
    Summary: Organize the solutions of problems
    Examples: <NONE>
    Attributes:
        @param (problems): os.walk functions output
    Returns: problem:lang -> [solutions] <dict>
    """
    solution = compile("solution_+(?!out)")

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
    return pd.DataFrame.from_dict(parse_solutions(walk_problems()), "index")


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
    Examples: Iam tired...
    Attributes:
        @param (df): pd.DataFrame
    Returns: pd.DataFrame
    """
    df_ = pd.DataFrame()
    for column in df.columns:
        df_[column] = df[column].map(
            lambda x: len(x) if x is not np.NAN else 0)

    if len(df.columns) > 1:
        df_["Solutions"] = df_[df_.columns].apply(tuple, axis=1).map(sum)
        df_ = df_[df_.Solutions > 0]

    return df_


# docs?
def spinner(control):
    animation = r"|/\-"
    stdout.write(3 * " ")
    for c in cycle(animation):
        message = "(" + c + ")" + " t: {:.2f}".format(time() - control.time)
        stdout.write(message)
        sleep(0.1)
        stdout.write(len(message) * "\010")
        stdout.flush()
        if control.done:
            break


# need docs
def choose_builder(lang, path):
    if lang == "Python":
        b = Build("python", path)
    elif lang == "Go":
        b = Build("go run", path)
    elif lang == "Clojure":
        b = Build("clojure", path)
    elif lang == "CommonLisp":
        b = Build("clisp", path)
    elif lang == "Haskell":
        b = Build("runhaskell", path)
    elif lang == "C":
        b = SpecialBuild("gcc -lm", path)
    elif lang == "C++":
        b = SpecialBuild("g++ -lm", path)
    elif lang == "Lua":
        b = Build("lua", path)
    elif lang == "Ruby":
        b = Build("ruby", path)
    elif lang == "Bash":
        b = Build("bash -c", path)
    elif lang == "Elixir":
        b = Build("elixir", path)
    else:
        raise Exception("Error; U have the {!r} compilers?".format(lang))
        exit(1)
    return b


# need docs
def execute_builder(b):
    out, err, t = b.execute()
    answer = out.decode("utf-8").strip("\n")
    if err:
        _exit(1)
    stdout.write(ERASE_LINE)
    building = "\rBuilded {}: Answer: {}: {:.2f}s\n".format(b.path, answer, t)
    stdout.write(building)
    stdout.flush()

    return answer, t


# need docs
def build_result(df, ignore_errors=False):
    class Control:  # to handle the spinner time at each solution
        time = time()
        done = False

    control = Control()
    columns = ["Problem", "Language", "Time", "Answer"]
    data = []
    spin_thread = threading.Thread(target=spinner, args=(control,))
    spin_thread.start()
    for lang, path in solutions_paths(df):
        if lang in BUILD_SUPPORT and "slow" not in path:
            # WHY THESE spaces woRKS?
            stdout.write("@Loading next {}: {}".format(path, 12 * ' '))
            b = choose_builder(lang, path)
            control.time = time()
            answer, t = execute_builder(b)
            problem = split_problem_language(path)[0]
            data.append([problem, lang, t, answer])
        elif "slow" in path:
            stdout.write("\rIgnored: {}: bad solution (slow).\n".format(path))
        elif not ignore_errors:
            stdout.write("\rDon't have support yet for {!r}!\n".format(lang))
    stdout.write("\r\n")
    stdout.flush()
    control.done = True
    spin_thread.join()

    final_df = pd.DataFrame(data, columns=columns)
    return final_df.sort_values("Problem")


def list_by_count(df):
    c = count_solutions(df)
    count = [sum(c[lang]) for lang in df.columns]
    table = pd.DataFrame(count, index=df.columns,
                         columns=["Solutions"])
    return table.sort_values("Solutions", ascending=False)


def handle_options(options):
    df = load_dataframe()
    langs = {x.lower(): x for x in df.columns}
    query = [x.lower() for x in options.search]

    langs_selected = [langs[x] for x in search_language(query, langs)]
    if options.all:
        langs_selected = [x for x in langs.values()]

    if options.list:
        if options.count:
            df = list_by_count(df)

        elif options.path:
            langs_selected = [x for x in langs.values()]

        else:
            df = '\n'.join(sorted(langs.values()))
    else:
        df = df[langs_selected]

    if options.count and not options.list:
        df = count_solutions(df[langs_selected])

    elif options.build:
        try:
            df = build_result(df[langs_selected], options.all)
        except(SystemExit, KeyboardInterrupt):
            _exit(1)

    elif options.path:
        df = '\n'.join(path for _, path in solutions_paths(df[langs_selected]))

    elif not any(options.__dict__.values()):
        parser.print_help()

    pd.set_option("display.max_rows", len(df))
    print(df)


def main():
    options, _ = parser.parse_args()
    handle_options(options)

if __name__ == "__main__":
    main()
