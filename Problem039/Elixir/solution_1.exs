defmodule RightInteger do
  def ways(vals,i,_,_) when i > 399 do
    vals
  end

  def ways(vals,i,j,_) when j > 399 do
    ways(vals,i+1,i+1,i+1)
  end

  def ways(vals,i,j,k) when k > 399 do
    ways(vals,i,j+1,j+1)
  end

  def ways(vals,i,j,k) when k <= 399 do
    vals = cond do
      ((i*i) + (j*j) == (k*k)) and ((i+j+k) < 1_000) ->
        ad((i+j+k),vals)
      true ->
        vals
    end

    ways(vals,i,j,k+1)
  end

  def ad(a,b), do: Map.put(b,a,(Map.get(b,a) + 1))
end

Enum.into(Enum.zip(Enum.to_list(1..1_000),List.duplicate(0,1_000)),Map.new)
  |> RightInteger.ways(1,1,1)
  |> Enum.max_by(fn {_,y} -> y end)
  |> elem(0)
  |> IO.puts