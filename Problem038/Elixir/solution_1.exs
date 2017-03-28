defmodule Pandigital do
  def multiples(current,lim,pandigitals) when current > lim do
    pandigitals
      |> Enum.max()
  end

  def multiples(current,lim,pandigitals) when current <= lim do
    multiples(current+1,lim,products(2,4,Integer.to_string(current),pandigitals))
  end

  def products(start,finish,_,pandigitals) when start > finish do
    pandigitals
  end

  def products(start,finish,current,pandigitals) when start <= finish do
    pan = current <> Integer.to_string(start*String.to_integer(current))
    
    pandigitals = cond do
      pandigital?(pan) ->
        [pan] ++ pandigitals
      true -> 
        pandigitals
    end

    products(start+1,finish,pan,pandigitals)
  end

  def pandigital?(n) do
    ~w(1 2 3 4 5 6 7 8 9) == n
      |> String.split("", trim: true)
      |> Enum.sort()
  end
end

IO.puts Pandigital.multiples(9_000,9_999,[])