defmodule Champernowne do
  def constant(lim) do
    (0..lim)
      |> Enum.map(fn x -> Integer.to_string(x) end)
      |> Enum.join()
      |> String.codepoints
      |> find(0,1,1)
      |> IO.inspect
  end

  def find(_,_,tens,final) when tens > 1_000_000 do
    final
  end

  def find([digit|digits],count,tens,final) when tens <= 1_000_000 do
    [final|tens] = cond do
      count == tens ->
        [final * String.to_integer(digit)|tens  * 10]
      true ->
        [final|tens]
    end

    find(digits,count+1,tens,final)
  end
end

Champernowne.constant(1_000_000)
