defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    lists = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&splitLine(&1))
    sol1 = part1(lists)
    IO.puts "Part 1 solution: "
    IO.puts sol1
    sol2 = part2(lists)
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def splitLine(line) do
    String.split(line, " ", trim: true)
  end
  def splitLists(l) do
    {
      Enum.sort(Enum.map(l, &Enum.at(&1,0)|>String.to_integer())),
      Enum.sort(Enum.map(l, &Enum.at(&1,1)|>String.to_integer()))
      }
  end
  def addPart1(l1, l2) do
    Enum.zip(l1,l2) |> Enum.map(fn {x,y} -> abs(x-y) end)
  end
  def part1(nums) do
    {l1, l2} = splitLists(nums)
    Enum.sum(addPart1(l1,l2))
  end
  def part2(nums) do
    {l1, l2} = splitLists(nums)
    freql2 = Enum.frequencies(l2)
    Enum.map(l1,fn x -> x*Map.get(freql2,x,0) end) |> Enum.sum()
  end
end

Solve.solve("in")
