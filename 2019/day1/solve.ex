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
  def part1(mass) do
    mass/3 |> Float.floor(0) |> Kernel.-(2)
  end
  def part2(mass) when mass <= 6 do
    0
  end
  def part2(mass) do
    fuel = mass/3
    |> Float.floor(0)
    |> Kernel.-(2)
    fuel + part2(fuel)
  end
end
