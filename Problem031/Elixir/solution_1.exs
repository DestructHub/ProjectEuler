defmodule Coins do
  def count([],_,vals),  do: vals
  def count([coin|coins],lim,vals) when length(coins) >= 0 do
    count(coins,lim,ways(coin,coin,lim,vals))
  end

  def ways(num,_,   lim,vals) when num > lim, do: vals
  def ways(num,coin,lim,vals) when num <= lim do
    ways(num+1,coin,lim,ad(coin,num,vals))
  end

  def ad(a,b,c), do: Map.put(c,b,(Map.get(c,b) + Map.get(c,(b-a))))
end

vals = Map.put(Enum.into(Enum.zip(Enum.to_list(0..200),List.duplicate(0,201)),Map.new),0,1)
Coins.count([1,2,5,10,20,50,100,200],200,vals)
  |> Map.values()
  |> Enum.max()
  |> IO.inspect
