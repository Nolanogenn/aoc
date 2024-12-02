defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    direct_conn = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.split(&1, ")", trim: true))
        |> Enum.map(fn [k,v] -> {v, k} end)
        |> Map.new
    planets = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.split(&1, ")", trim: true))
        |> Enum.map(fn [_, v] -> v end)
        |> unique
    sol1 = part1(planets,direct_conn)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    #sol2 = contents
    #    |> String.split("\n", trim: true)
    #    |> Enum.map(&String.to_integer/1)
    #    |> Enum.map(&part2/1)
    #    |> Enum.sum()
    #IO.puts "Part 2 solution: "
    #IO.puts sol2
  end
  def unique(l) do
    unique(l, [])
  end
  def unique([x|xs], ret) do
    cond do
      Enum.member?(ret, x) -> unique(xs, ret)
      true -> unique(xs, [x|ret])
    end
  end
  def unique([], ret) do
    ret
  end
  def part1(planets, connections) do
    part1(planets,connections,0)
  end
  def part1([], _, n) do
    n
  end
  def part1([p|ps], connections, n) do
    to_add = get_connections(p,connections)
    IO.inspect p
    IO.inspect to_add
    part1(ps, connections, n+to_add)
  end
  def get_connections("COM",_) do
    0
  end
  def get_connections(p,connections) do
    1 + get_connections(connections[p], connections)
  end
  def part2(num) do
    num
  end
end
