defmodule PowerfulDigits do
  def counts(_,_,count,len_bool) when len_bool == false, do: count

  def counts(exp,num,count,len_bool) when len_bool == true do
    [num,count] = cond do
      num != 9 ->
        exps(num,num,exp,count)
      true ->
        [num,count + 1]
    end

    counts(exp + 1,num,count,same_len?(9,exp))
  end

  def exps(num,n,_,count) when n > 9 do
    [num,count]
  end

  def exps(num,n,exp,count) when n <= 9 do
    [num|count] = cond do
      same_len?(n,exp) ->
        [num|count + 1]
      true ->
        greater_than_n?(num,n,count)
    end


    exps(num,n + 1,exp,count)
  end

  def greater_than_n?(num,n,count) do
    cond do
      n > num ->
        [num|count]
      true ->
        [n|count]
    end
  end

  def same_len?(n,exp), do: exp == round(:math.pow(n,exp)) |> to_string |> String.length()
end

IO.puts PowerfulDigits.counts(1,1,0,true)