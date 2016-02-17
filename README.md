[![Coverage](https://codecov.io/github/DestructHub/ProjectEuler/coverage.svg?branch=master)](https://codecov.io/github/DestructHub/ProjectEuler?branch=master)
[![Build Status](https://travis-ci.org/DestructHub/ProjectEuler.svg?branch=master)](https://travis-ci.org/DestructHub/ProjectEuler)

# ProjectEuler
Compilation of some solutions of the challenges existent in the website www.projecteuler.net


## The 10 Next Problems

<<[updates/STATUS.md]

## Next Goals

<<[updates/GOALS.md]

## Guidelines

* Do not write solutions reading from stdin in any ways! That would be harder to generate a script for time measurement.

* Please update the updates/STATUS.md, in order to us know what you are doing. That way we can attack more solutions in parallel. 

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

*  On push if you get  `! [rejected]        master -> master (fetch first)`, PLEASE, don't create a useless fucking merge with `git pull`, instead this execute `git pull --rebase`. The history line of repository will be glad with this.


