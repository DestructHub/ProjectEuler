[![Coverage](https://codecov.io/github/DestructHub/ProjectEuler/coverage.svg?branch=master)](https://codecov.io/github/DestructHub/ProjectEuler?branch=master)
[![Build Status](https://travis-ci.org/DestructHub/ProjectEuler.svg?branch=master)](https://travis-ci.org/DestructHub/ProjectEuler)

# ProjectEuler
Compilation of some solutions of the challenges existent in the website www.projecteuler.net

## Status - Next 10 Problems 

We are currently solving the problems **Problem041 ~ Problem050** and you can check it in details here: [STATUS.md](updates/STATUS.md)

## Next Goals

- [ ] Fix #1
- [ ] 50 first problems solved (need only the next 10 problems!)
- [ ] 100 first problems solved

## Guidelines

* Do not write solutions reading from stdin in any ways! That would make more harder to generate a script for time measurement.

* Please update the [STATUS.md](updates/STATUS.md), in order to us know what you are doing. That way we can attack more solutions in parallel. 

* CamelCase for folders and underscore for files. For each solution keep ever that architecture example:

```
Problem00X/
..	Python/
	..	 solution_1.py
..	README.md 
```

``` 
$ cat README.md
[The original source of problem](https://projecteuler.net/problem=29)
```

*  On push if you get  `! [rejected]        master -> master (fetch first)`, **PLEASE**, don't create a useless fucking merge with `git pull`, instead this execute `git pull --rebase`. The history line of repository will be glad with this.

### Rules

We wants good solutions for the problems. A good solution can be relative, but until one minute was okay yet.

If your solution breaks the one-minute rule of project euler, the file solution can be pushed with one condition: use the suffix `slow` like  `solution_slow_1.xy`. That way the `stats.py` don't will execute that.

### Authors and Contributors

Check the ProjectEuler badges and tables by nickname: [SOLVERS.md](SOLVERS.md)