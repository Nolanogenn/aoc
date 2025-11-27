defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.to_integer/1)
        |> Enum.map(&part1/1)
        |> Enum.sum()
    IO.puts "Part 1 solution: "
    IO.puts sol1
    sol2 = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.to_integer/1)
        |> Enum.map(&part2/1)
        |> Enum.sum()
    IO.puts "Part 2 solution: "
    IO.puts sol2
  end
  def part1(num) do
    num
  end
  def part2(num) do
    num
  end
end

Solve.solve('test')
