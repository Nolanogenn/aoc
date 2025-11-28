defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("\n", trim: true)
        |> part1()
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = contents
        |> String.split("\n", trim: true)
        |> part2()
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def handleDistance([], locations, pairs) do
    {locations |> Enum.uniq(), pairs}
  end
  def handleDistance([d|ds], locations, pairs) do
    [p1, p2] = String.split(d, " = ", trim: true)
    cost = String.to_integer(p2)
    [source, target] = String.split(p1, " to ", trim: true)
    handleDistance(
    ds,
    [source | [target | locations]],
    [{{source, target}, cost}|[{{target,source},cost}| pairs]]
    )
  end
  def handleDistances(distances) do
    handleDistance(distances, [],[])
  end
  def getPaths([]) do
    [[]]
  end
  def getPaths(x) do
    for elem <- x,
      rest = x -- [elem],
      p <- getPaths(rest),
      do: [elem | p]
  end
  def findCost(from, to, list) do
    Enum.filter(list, fn {{x,y}, _} -> x == from and y == to end)
    |> Enum.map(&elem(&1,1)) |> Enum.at(0)
  end
  def computeCost(path, pairs) do
    computeCost(path, pairs,0) 
  end
  def computeCost([_], _, cost) do
    cost
  end
  def computeCost([c,n|cs], pairs, cost) do
    computeCost([n|cs], pairs, cost+findCost(c,n,pairs))
  end
  def part1(distances) do
    {locations, pairs} = handleDistances(distances)
    paths = getPaths(locations)
    Enum.map(paths, fn x -> computeCost(x, pairs) end) |> Enum.min()
  end
  def part2(distances) do
    {locations, pairs} = handleDistances(distances)
    paths = getPaths(locations)
    Enum.map(paths, fn x -> computeCost(x, pairs) end) |> Enum.max()
  end
end

Solve.solve("in")
