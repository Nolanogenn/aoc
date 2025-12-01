defmodule Solve do
  defp parse_contents(contents) do
      |> String.split("\n", trim: true)
      |> Enum.map(&String.to_integer/1)
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
  def part1(parsed) do
    num
  end
  def part2(parsed) do
    num
  end
end

Solve.solve("test")
