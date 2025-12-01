defmodule Solve do
  defp parse_contents(contents) do
      contents
      |> String.replace("\n", "")
      |> String.to_charlist()
      |> Enum.reverse()
  end
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    parsed = contents
      |> parse_contents()
    sol1 = part1(parsed)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = part1(sol1|>Enum.reverse()|>nextPassword())
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def nextPassword([p|ps]) do
      case p+1 > 122 do
      true -> [(97)|nextPassword(ps)]
      _ -> [(p+1)|ps]
      end
  end
  def check_straight([c|cs], p,n) do
    if n == 3 do
      1
    else
      case c == p-1 do
        true -> check_straight(cs,c,n+1)
        _ -> check_straight(cs, c, 1)
      end
    end
  end
  def check_straight([],_,n) do
    if n == 3 do
      1
    else
      0
    end
  end
  def check_confusing([c|_]) do
    Enum.member?([105,111,108], c)
  end
  def check_pairs([c|cs], prev, n) do
    case c == prev do
      true -> check_pairs(cs, "", n+1)
      _ -> check_pairs(cs, c, n)
    end
  end
  def check_pairs([], _, n) do
    case n > 1 do
      true -> 1
      _ -> 0
    end
  end
  def check_confusing_all([c|cs]) do
    case check_confusing([c|cs]) do
      true -> 1
      _ -> check_confusing_all(cs)
    end
  end
  def check_confusing_all([]) do
    1
  end
  def checkPassword([p|ps]) do
    [
      check_straight(ps,p,1), 
      check_pairs(ps,p,0),
      check_confusing_all(ps)
    ]
  end
  def fixConfusing([]) do
    []    
  end
  def fixConfusing([p|ps]) do
    case check_confusing([p|ps]) do
      true -> nextPassword([p|ps]) |> fixConfusing()
      _ -> [p|fixConfusing(ps)]
    end
  end
  def part1(parsed) do
    checks = checkPassword(parsed)
    case Enum.sum(checks) do
      3 -> Enum.reverse(parsed)
      _ -> parsed |> nextPassword() |> fixConfusing() |> part1()
    end
  end
end

Solve.solve("in")
