defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.replace("\n", "")
        |> part1(3)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
#    sol2 = contents
#        |> String.split("\n", trim: true)
#        |> Enum.map(&String.to_integer/1)
#        |> Enum.map(&part2/1)
#        |> Enum.sum()
#    IO.puts "Part 2 solution: "
#    IO.inspect sol2
  end
  def mapSequence([c|cs], out, lastSeen, n) do
    case c == lastSeen do
      true -> mapSequence(cs, out, lastSeen, n+1)
      _ -> 
    end
  end
  def mapsequence([], out, _) do
    out
  end
  def part1(sequence,n) do
    case n>0 do
    true -> 
      mapSequence(String.split(sequence, "", trim: true), "", "", 0)
    _ ->
      IO.inspect(sequence)
      String.length(sequence)
      end
    end
end

Solve.solve("test")
