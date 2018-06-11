a_z_key = %{
  "A" => 1,
  "B" => 2,
  "C" => 3,
  "D" => 4,
  "E" => 5,
  "F" => 6,
  "G" => 7,
  "H" => 8,
  "I" => 9,
  "J" => 10,
  "K" => 11,
  "L" => 12,
  "M" => 13,
  "N" => 14,
  "O" => 15,
  "P" => 16,
  "Q" => 17,
  "R" => 18,
  "S" => 19,
  "T" => 20,
  "U" => 21,
  "V" => 22,
  "W" => 23,
  "X" => 24,
  "Y" => 25,
  "Z" => 26
}

defmodule TriangleWords do
  def words(file,a_z_key) do
    case File.read(file) do
      {:ok, body}     ->
        body
         |> parse(a_z_key)
         |> IO.inspect
      {:error,reason} ->
        :file.format_error(reason)
    end
  end

  def parse(body,a_z_key) do
    body
      |> String.replace(~r/\W+/,",")
      |> String.split(",")
      |> Enum.slice(1,2000)
      |> Stream.map(fn x -> String.split(x, "", trim: true) end)
      |> Enum.map(fn y -> Enum.map(y, fn z -> a_z_key[z]  end)
        |> Enum.reduce(0,fn a,b -> a + b end) end)
      |> triangle_numbers()
  end

  def find([],count,_), do: count
  def find([word|words],count,tri_nums) when length(words) >= 0 do
    find(words,triangle?(word,tri_nums,count),tri_nums)
  end

  def triangle_numbers(words) do
    tri_nums = for n <- (1..round(:math.sqrt(Enum.max(words)*2))), do: div(((n*n)+n),2)
    find(words,0,tri_nums)
  end

  def triangle?(word,tri_nums,count) do
    cond do
      Enum.member?(tri_nums,word) ->
        count + 1
      true ->
        count
      end
  end
end

TriangleWords.words("../p042_words.txt",a_z_key)
