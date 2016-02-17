#!/usr/bin/env python3
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from pandas import DataFrame  # sudo pip install pandas
from numpy import NAN  # sudo pip install numpy

from os.path import join
from os import walk
from re import compile
from optparse import OptionParser

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


def charge_options():
    parser = OptionParser()

    parser.add_option(
        "-l", "--list",
        help="Print a list of the languages whose have solutions",
        dest="list",
        default=False,
        nargs=0
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
        default=False,
        nargs=0
    )

    parser.add_option(
        "-p", "--path",
        help="Print the path of each solution",
        dest='path',
        default=False,
        nargs=0
    )

    parser.add_option(
        "-a", "--all",
        help="Select all the languages for search",
        dest='all',
        default=False,
        nargs=0

    )

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
        if problem.match(x[0]):
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
    solution = compile("solution_[0-9]")

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
    Returns: pandas.DataFrame
    """
    return DataFrame.from_dict(parse_solutions(walk_problems()), orient='index')


def solutions_paths(df):
    """
    Function: load_filepaths
    Summary: Get each filepath of solutions based on DataFrame
    Examples:
        >>> df = load_dataframe()
        >>> py = df[["CommonLisp"]]
        >>> load_filepaths(py)
        ["]

    Attributes:
        @param (df): pandas.DataFrame
    Returns: list of file paths
    """
    paths = []
    for column in df.columns:
        solutions = df[df[column].notnull()][column]
        lang = solutions.name
        problems = solutions.index
        for problem in problems:
            paths.extend(join(problem, lang, s) for s in solutions[problem])

    return paths


def count_solutions(df):
    """
    Function: count_solutions
    Summary: Count the number of solutions of each problem and language
    Examples: I'm tired...
    Attributes:
        @param (df): pandas.DataFrame
    Returns: InsertHere
    """
    _df = DataFrame()
    for column in df.columns:
        _df[column] = df[column].map(lambda x: len(x) if x is not NAN else 0)

    if len(df.columns) > 1:
        _df["Solutions"] = _df[_df.columns].apply(tuple, axis=1).map(sum)

    return _df


def filter_nan(df):
    """
    Function: filter_nan
    Summary: Filter all rows whose all them are numpy.NaN
    Examples: not yet
    Attributes:
        @param (df): pandas.DataFrame
    Returns: rows whose all are nan excluded
    """
    pass


def main():
    parser = charge_options()
    options, _ = parser.parse_args()
    df = load_dataframe()
    langs = {x.lower(): x for x in df.columns}
    query = [x.lower() for x in options.search]

    if options.all is not False:
        langs_selected = [x for x in langs.values()]
    else:
        langs_selected = [langs[x] for x in search_language(query, langs)]

    if options.list is not False:
        if options.count is not False:
            c = count_solutions(df)
            count = [sum(c[lang]) for lang in df.columns]
            table = DataFrame(count, index=df.columns, columns=["Solutions"])
            print(table.sort_values("Solutions", ascending=False))

        else:
            for lang in sorted(df):
                print(lang)

    elif options.count is not False:
        print(count_solutions(df[langs_selected]))

    elif options.path is not False:
        for path in solutions_paths(df[langs_selected]):
            print(path)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
