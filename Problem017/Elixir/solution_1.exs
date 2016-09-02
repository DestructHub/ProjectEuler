# Author: lubien

defmodule Euler17 do
  def solve(n) do
    1..n
      |> Stream.map(&num_to_str/1)
      |> Stream.map(&String.length/1)
      |> Enum.reduce(&(&1 + &2))
  end

  # Since 1_000 isn't parsed right by my rules :p
  def num_to_str(1000), do: "onethousand"
  # Separate the number in a List of digits
  def num_to_str(n), do: num_to_str(Integer.digits(n), [])

  # When we've parsed all digits, make the word
  defp num_to_str([], acc) do
    case acc do
      # "ten_name" is something like "twenty", "fourty", "ninety"
      # and "unit_name" is empty because of a 0 unit
      ["", ten_name] -> ten_name
      [unit_name, ten_name] -> ten_name <> "and" <> unit_name
      _ -> acc |> Enum.reduce(&(&1 <> &2))
    end
  end
  # Parse a digit
  # It's important to you know that whenever we have 2 digits,
  # we parse both together using ten_text/1
  # units are only parsed alone for 1 digit sized numbers (1..9)
  defp num_to_str([x | xs] = digits, acc) do
    digits_length = length(digits)

    text = case digits_length do
      3 -> unit(x) <> "hundred"
      2 -> ten_text(digits)
      1 -> unit(x)
    end

    # Empty tail when we have 2 digits (see the comment above)
    tail = if digits_length == 2 do [] else xs end

    num_to_str(tail, [text | acc])
  end

  # Knowing that there's two digits at the tail
  # let's parse it
  defp ten_text([x | xs]) do
    y = List.first xs

    # For numbers in the "1y" pattern
    if x == 1 do
      cond do
        y == 0 -> "ten"
        y == 1 -> "eleven"
        y == 2 -> "twelve"
        y == 3 -> "thirteen"
        y == 5 -> "fifteen"
        y == 8 -> "eighteen"
        y <= 9 -> unit(y) <> "teen"
      end
    else
      case y do
        0 -> ten(x)
        _ -> ten(x) <> unit(y)
      end
    end
  end

  # Given a number "n", return the name of (n * 10)
  # Excludes: 0, 1
  def ten(n) do
    {"", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"}
      |> elem(n)
  end

  # Given a number, return it's name
  def unit(n) do
    {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
      |> elem(n)
  end
end

Euler17.solve(1_000)
  |> IO.inspect

