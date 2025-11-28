defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&part1/1)
        |> Enum.sum()
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&part2/1)
        |> Enum.sum()
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def getInMemoryLength([_], acc) do
    acc+1
  end
  def getInMemoryLength([c1|[c2|cs]], acc) do
    case {c1,c2} do
      {"\\", "x"} -> getInMemoryLength([c2|cs], acc-2)
      {"\\", "\\"} -> getInMemoryLength(cs, acc+1)
      {"\\", "\""} -> getInMemoryLength(cs, acc+1)
      {_,_} -> getInMemoryLength([c2|cs], acc+1)
    end
  end
  def getInMemoryLength(line) do
    getInMemoryLength(String.split(line, "", trim: true), -2)
  end
  def part1(line) do
      String.length(line) - getInMemoryLength(line)
  end
  def getActualLen([_], acc) do
    acc+2
  end
  def getActualLen([c1|cs], acc) do
    case c1 do
      "\\" -> getActualLen(cs, acc+2)
      "\"" -> getActualLen(cs, acc+2)
      _ -> getActualLen(cs, acc+1)
    end
  end
  def getActualLen(line) do
    getActualLen(String.split(line, "", trim: true), 2)
  end
  def part2(line) do
      getActualLen(line) - String.length(line)
  end
end

Solve.solve("in")
