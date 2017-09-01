# Repository Rules

1. We want good solutions for the problems. A good solution can be relative, but until one minute is acceptable.
If your solution breaks the one-minute rule of project euler, the file solution can be pushed with one condition: use the suffix `slow` like  `solution_slow_1.xy`. That way, the `stats.py` will not execute that.

2. Please update the [STATUS.md](STATUS.md) in order for us to know what you are doing. That way we can attack more solutions in parallel. 

3. CamelCase for folders and underscore for files. For each solution keep ever like the example of final of this document.

4.  On push if you get  `! [rejected]        master -> master (fetch first)`, **PLEASE**, don't create a useless fucking merge with `git pull`, instead this, execute `git pull --rebase`. The repository's history line will be glad with this.

5. Do not write solutions reading from stdin in any ways! That would make harder to generate a script for time measurement.

6. Always send PR with info about your processor and the time in which your solution takes to finish.


# Example
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

