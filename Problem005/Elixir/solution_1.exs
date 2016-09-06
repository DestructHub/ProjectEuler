defmodule Solution do
  def solve(n) do
    dvs = 2..n |> Enum.to_list
    find_recur(n, dvs, n)
  end

  defp find_recur(n, dvs, inc_rate) do
    if Enum.all?(dvs, &(0 == rem(n, &1))) do
      n
    else
      find_recur(n + inc_rate, dvs, inc_rate)
    end
  end
end

Solution.solve(20)
