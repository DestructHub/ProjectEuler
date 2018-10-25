let rec range i j = if i > j then [] else i :: (range (i+1) j)

let is_prime n =
  let is_divisor d p =
    if p mod d = 0 then 1 else 0
  in
  let targets = range 2 (int_of_float(sqrt(float_of_int(n))))
  in
  let rec test_targets k targets =
    match targets with
      | [] -> 1
      | x::trg -> if is_divisor x k = 1 then 0 else test_targets k trg
  in
  test_targets n targets

let rec mxpow i top prod =
  if prod > top then
    (prod / i)
  else
    mxpow i top (prod * i)


let rec solve n i prod =
  if i = n then
    prod
  else
    if (is_prime i) = 1 then solve n (i + 1) (prod * (mxpow i n 1))
    else solve n (i + 1) prod



let solution =
  solve 20 2 1;;


print_int (solution);;
print_newline ();;