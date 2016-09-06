defmodule Solution do
  def nth_prime(n) do
    prime_sequence
    |> Stream.take(n)
    |> Enum.to_list
    |> List.last
  end

  def prime_sequence do
    Stream.unfold(2, fn(x) ->
      if(x |> prime?) do
        {x, x+1}
      else
        {nil, x+1}
      end
    end)
    |> Stream.reject(&is_nil/1)
  end

  def prime?(x) when x == 2, do: true
  def prime?(x) when x in [1, 4], do: false
  def prime?(x) do
    2..round(:math.sqrt(x))
    |> Enum.reduce_while(true, fn(e, acc) ->
      if(0 == rem(x, e)) do
        {:halt, false}
      else
        {:cont, true}
      end
    end)
  end
end

Solution.nth_prime(10_001) |> IO.puts
