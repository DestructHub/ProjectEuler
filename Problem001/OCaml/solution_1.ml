let check x =
  if x mod 3 = 0 || x mod 5 = 0 then
    1
  else
    0

let rec solve current top count =
  if current = top then count
  else
    if check current = 1 then
      solve (current + 1) top (count + current)
    else
      solve (current + 1) top (count);;

let solution =
  solve 0 1000 0;;

print_int (solution);;
print_newline ()