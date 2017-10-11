let rec ispalind s =
  if String.length s <= 1 then true
  else if s.[0] = s.[String.length s - 1] then ispalind (String.sub s 1 (String.length s - 2))
  else false;;

let solve =
  let mx= ref 0 in
  for i = 100 to 999 do
    for j = 100 to 999 do
      if ispalind (string_of_int(i * j)) && (i * j) > !mx then mx := (i * j)
    done
  done;
  !mx

let rec solve i j prod=
  if i = 100 then
    prod
  else if j = 100 then
    solve (i - 1) 999 prod
  else
      if ispalind (string_of_int(i * j)) && (i * j) > prod  then solve i (j-1) (i * j)
      else solve i (j-1) prod

let solution =
  solve 999 999 0;;

print_int (solution);;
