defmodule Summations do
  def count([],_,vals),  do: vals
  def count([way|ways],lim,vals) when length(ways) >= 0 do
    count(ways,lim,sums(way,way,lim,vals))
  end

  def sums(num,_,  lim,vals) when num > lim, do: vals
  def sums(num,way,lim,vals) when num <= lim do
    sums(num+1,way,lim,ad(way,num,vals))
  end

  def ad(a,b,c), do: Map.put(c,b,(Map.get(c,b) + Map.get(c,(b-a))))
end

vals = Map.put(Enum.into(Enum.zip(Enum.to_list(0..100),List.duplicate(0,101)),Map.new),0,1)
(1..99)
  |> Enum.to_list()
  |> Summations.count(100,vals)
  |> Map.values()
  |> Enum.max()
  |> IO.puts
