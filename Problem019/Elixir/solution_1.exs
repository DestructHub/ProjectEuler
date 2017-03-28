defmodule Sundays do
  def count(final,[year|[_|[count|_]]],_) when year == final do
    count + 1
  end

  def count(final,[year|[day|count]],months) when year < final do
    count(final,calendar(year,months, day,List.first(count)), months)
  end

  def calendar(year,months,day,count) when length(months) <= 0 do
    [year + 1, day, count]
  end

  def calendar(year,months,day,count) when length(months) > 0 do
    [month|rem_months] = months
    [count|month]      = check_day_and_month(count, day, month, year)

    calendar(year, rem_months, (rem((month + day), 7)), count)
  end

  def check_day_and_month(count,day,month,year) do
    count = cond do
      day == 0 ->
        count + 1
      day != 0 ->
        count
    end

    month = cond do
      month == 28 and leap_year?(year) ->
        29
      true ->
        month
    end

    [count|month]
  end

  def leap_year?(year) do
    unless((rem(year, 100) == 0 and rem(year, 400) != 0), do: rem(year, 4) == 0)
  end
end

IO.puts Sundays.count(2000,[1901,2,0],[31,28,31,30,31,30,31,31,30,31,30,31])