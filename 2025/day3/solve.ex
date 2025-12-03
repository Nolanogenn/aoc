defmodule Solve do
  defp parse_contents(contents) do
      contents
      |> String.split("\n", trim: true)
      |> Enum.map(&parseNum(&1))
  end
  def parseNum(n) do
    n |> String.to_integer()
    |> Integer.digits()
  end
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    parsed = contents
      |> parse_contents()
    sol1 = part1(parsed)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
#    sol2 = part2(parsed)
#    IO.puts "Part 2 solution: "
#    IO.inspect sol2
  end
  def getMax([d|ds], len \\ 2) do
    getMax(ds, [d], len-1)
  end
  def getMax(ds, d, l) do
   if length(d) == l do
    d
   else
     case length(ds) <= l do
        true -> d ++ ds
        _ -> {m, rem} = findMaxIndex(ds)
              getMax(rem, Enum.reverse([m|d]), l-1)
     end
   end
  end
  def findMaxIndex([d|ds]) do
    findMaxIndex(ds, d, ds)
  end
  def findMaxIndex([], d, ds) do
    {d, ds} 
  end
  def findMaxIndex([d|ds], n, xs) do
    case d > n do
      true -> findMaxIndex(ds, d, ds)
      _ -> findMaxIndex(ds, n, xs)
    end
  end
  def part1(parsed) do
    Enum.map(parsed, &getMax(&1)) |> Enum.sum()
  end
#  def part2(parsed) do
#    parsed
#  end
end

Solve.solve("test")
