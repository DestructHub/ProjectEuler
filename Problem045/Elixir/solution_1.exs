defmodule PolygonNumbers do
  def tri_pent_hex(_,final) when final > 0,  do: final
  def tri_pent_hex(i,final) when final == 0  do
    hex   = gen(i)
    final = cond do
      pent?(hex) ->
        hex
      true ->
        final 
    end

    tri_pent_hex(i+1,final)
  end

  def gen(n),  do: n * ((n * 2) - 1)
  def pent?(n) do
    m = (:math.sqrt((24 * n) + 1) + 1)
    (rem(round(Float.floor(m)),6) == 0) and (rem(round(Float.ceil(m)),6) == 0)
  end
end

IO.inspect PolygonNumbers.tri_pent_hex(144,0)