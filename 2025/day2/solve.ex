defmodule Solve do
  defp parse_contents(contents) do
      contents
      |> String.replace("\n", "")
      |> String.split(",", trim: true)
  end
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    parsed = contents
      |> parse_contents()
    sol1 = part1(parsed)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = part2(parsed)
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def isInvalid(n) do
    Integer.to_string(n) |> String.match?(~r/\b^(?!0)([0-9]+)\1\b/)
  end
  def isInvalid2(n) do
    Integer.to_string(n) |> String.match?(~r/\b^(?!0)([0-9]+)\1+\b/)
  end
  def expandRange(range) do
    [min,max] = String.split(range, "-")
    Enum.to_list(String.to_integer(min)..String.to_integer(max))
  end
  def part1(parsed) do
    parsed
    |> Enum.map(&expandRange(&1))
    |> Enum.map(&Enum.filter(&1, fn x -> isInvalid(x) end))
    |> List.flatten()
    |> Enum.sum()
  end
  def part2(parsed) do
    parsed
    |> Enum.map(&expandRange(&1))
    |> Enum.map(&Enum.filter(&1, fn x -> isInvalid2(x) end))
    |> List.flatten()
    |> Enum.sum()
  end
end

Solve.solve("in")
