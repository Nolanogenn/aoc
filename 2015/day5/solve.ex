defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&part1(&1))
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
  def check_vowels(s) do
    if Regex.scan(~r/[aeiou]/, s) |> length() >= 3 do
      1
    else
      0
    end
  end
  def check_repeating([s|ss]) do
    check_repeating(ss, s)
  end
  def check_repeating([s|ss], c) do
    case c == s do
      true -> 1
      _ -> check_repeating(ss, s)
    end
  end
  def check_repeating([], _) do
    0
  end
  def check_filters(s) do
    case String.contains?(s, ["ab", "cd", "pq", "xy"]) do
      true -> 0
      _ -> 1
    end
  end
  def part1(s) do
    checks = [
      check_vowels(s),
      check_repeating(String.split(s,"", trim: true)),
      check_filters(s)
      ]
    case Enum.sum(checks) do
      3 -> 1
      _ -> 0
    end
  end
  def check_distance({:ok, pos1}, pos2, [n|ss], seen) do
    case pos2-pos1 do
      1 -> check_pairs([n|ss], seen)
      _ -> 1
    end
  end
  def check_pairs([s|[n|ss]],seen) do
    pos = elem(n,1)
    sn = elem(s,0) <> elem(n,0)
    sn_v = Map.fetch(seen, sn)
    case sn_v do
      {:ok, _} -> check_distance(sn_v, pos, [n|ss], seen)
      _ -> check_pairs([n|ss], Map.put_new(seen, sn, pos))
    end
  end
  def check_pairs([_], _) do
    0
  end
  def check_pairs(s) do
    check_pairs(String.split(s,"",trim: true)|>Enum.with_index(), %{})
  end
  def check_one_between(s) do
    check_one_between(String.split(s,"", trim: true),0)
  end
  def check_one_between([x|[y|[z|ss]]], n) do
    case x == z do
      true -> check_one_between([y|[z|ss]], n+1)
      _ -> check_one_between([y|[z|ss]], n)
    end
  end
  def check_one_between([_,_], n) do
    case n do
      0 -> 0
      _ -> 1
    end
  end
  def part2(s) do
    checks = [check_pairs(s), check_one_between(s)]
    IO.inspect({s,checks})
    case checks do
      [1, 1] -> 1
      _ -> 0
    end
  end
end

Solve.solve("in")
