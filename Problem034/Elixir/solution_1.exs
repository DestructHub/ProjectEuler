defmodule Factorial do 
  def find(count,facts) when count > 9, do: [Enum.reverse(facts),facts]
  def find(count,[last|facts]) when count <= 9 do
    find(count + 1,[count*last] ++ [last] ++ facts)
  end
end

defmodule DigitFactorials do
  def find(count,_,lim,sum) when count > lim do
    sum
  end

  def find(count,facts,lim,sum) when count <= lim do
    sum = cond do
      digit_factorial?(count,facts) ->
        sum + count
      true ->
        count
    end

    find(count + 1,facts,lim,sum)
  end

  def digit_factorial?(num,facts) do
    num == Integer.to_string(num)
      |> String.split("",trim: true)
      |> Enum.map(fn n -> Enum.at(facts,String.to_integer(n)) end)
      |> Enum.reduce(fn a,b -> a + b end)
  end
end

[facts,[lim|_]] = Factorial.find(1,[1])
IO.puts DigitFactorials.find(3,facts,lim,0)