Mix.install([{:jason, "~> 1.4"}])

defmodule Solve do
  defp parse_contents(contents) do
      contents
      |> String.split("\n", trim: true)
  end
  defp findNums(row) do
    Regex.scan(~r/[-]*[0-9]+/, row)
    |> Enum.map(&Enum.at(&1,0))
    |> Enum.map(&String.to_integer(&1))
  end
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    parsed = contents
      |> parse_contents()
    IO.puts "Part 1 solution: "
    IO.inspect parsed |> Enum.map(&findNums(&1)) |> part1
    sol2 = part2(parsed)
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def part1(parsed) do
    parsed |> Enum.map(&Enum.sum(&1))
  end
  def getVs(structure) when is_integer(structure) do
    structure
  end
  def getVs(structure) when is_list(structure) do
    elems = for elem <- structure, do: getVs(elem)
    Enum.sum(elems)
  end
  def getVs(structure) when is_map(structure) do
    case Enum.member?(Map.values(structure), "red") do
      true -> 0
      _ -> getVs(Map.values(structure))
    end
  end
  def getVs(structure) when is_bitstring(structure) do
    0
  end
  def part2(parsed) do
    parsed |> Jason.decode!() |> getVs()
  end
end

Solve.solve("in")
