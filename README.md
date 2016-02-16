# ProjectEuler
Compilation of some solutions of the challenges existent in the website www.projecteuler.net


## The 10 Next Problems

- [ ] [Problem041](https://projecteuler.net/problem=41)
- [ ] [Problem042](https://projecteuler.net/problem=42)
- [ ] [Problem043](https://projecteuler.net/problem=43)
- [ ] [Problem044](https://projecteuler.net/problem=44)
- [ ] [Problem045](https://projecteuler.net/problem=45)
- [ ] [Problem046](https://projecteuler.net/problem=46) 
- [ ] [Problem047](https://projecteuler.net/problem=47)
- [X] [Problem048](https://projecteuler.net/problem=48)
- [ ] [Problem049](https://projecteuler.net/problem=49)
- [ ] [Problem050](https://projecteuler.net/problem=50)

## Next Goals

- [ ] Fix #1
- [ ] 50 first problems solved (need only the next 10 problems!)
- [ ] 100 first problems solved


## Guidelines

* Doesn't write solutions which read something from stdin! That way makes more hard to generate a script for time measurement

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