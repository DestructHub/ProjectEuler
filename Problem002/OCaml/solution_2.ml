let rec solve a b top sum =
  if a > top then
    sum
  else if b mod 2 = 0 then
    solve b (a + b) top (sum + b)
  else
    solve b (a + b) top sum

let solution =
    solve 0 1 4000000 0;;

print_int (solution);;
