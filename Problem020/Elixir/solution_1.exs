# Author: lubien

1..100
  |> Enum.reduce(&(&1 * &2))
  |> Integer.digits
  |> Enum.reduce(&(&1 + &2))
  |> IO.inspect

