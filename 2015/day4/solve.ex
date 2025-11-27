defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.replace("\n", "")
        |> part1(0)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = contents
        |> String.replace("\n", "")
        |> part2(0)
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def check(hash, startingWith) do
    String.starts_with?(hash, startingWith)
  end
  def part1(password, num) do
    hashed = :crypto.hash(:md5, password <> Integer.to_string(num)) |> Base.encode16()
    case check(hashed, "00000") do
      true -> num
      _ -> part1(password, num+1)
    end
  end
  def part2(password, num) do
    hashed = :crypto.hash(:md5, password <> Integer.to_string(num)) |> Base.encode16()
    case check(hashed, "000000") do
      true -> num
      _ -> part2(password, num+1)
    end
  end
end

Solve.solve("in")
