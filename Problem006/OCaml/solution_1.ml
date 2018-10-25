let rec pow n x =
  if n=0 then 1. else x *. pow (n-1) x;;

let f x = pow 2 (float_of_int ((x * (x + 1)) / 2))
let ff x = (x * (x + 1) * ((2 * x) + 1)) / 6

let solve n = -(ff n) + (int_of_float (f n))

let __kappa__ =
solve 100;;

print_int(__kappa__);;
print_newline ();;