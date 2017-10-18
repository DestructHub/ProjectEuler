%Autor: machad0

-module(solution_1).
-export([euler001/0]).

euler001() -> 
  lists:sum([Num || Num <- lists:seq(0, 999), (Num rem 3 =:= 0) or (Num rem 4 =:= 0)]).
