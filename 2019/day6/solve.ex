defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    direct_conn = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.split(&1, ")", trim: true))
        |> Enum.map(fn [k,v] -> {v, k} end)
        |> Map.new
    forward_conn = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.split(&1, ")", trim: true))
        |> Enum.group_by(&List.first/1, &List.last/1)
        |> Map.new
    planets = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.split(&1, ")", trim: true))
        |> Enum.map(fn [_, v] -> v end)
        |> unique
    sol1 = part1(planets,direct_conn)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = part2(direct_conn, forward_conn, [{"YOU",0}], "SAN",[])
    IO.puts "Part 2 solution: "
    IO.inspect sol2
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
    part1(ps, connections, n+to_add)
  end
  def get_connections("COM",_) do
    0
  end
  def get_connections(p,connections) do
    1 + get_connections(connections[p], connections)
  end
  def part2(backward_conn, forward_conn, [{current,steps}|xs], finish, seen) do
    cond do
      current == finish -> {current, steps-2}
      current == nil -> part2(backward_conn, forward_conn, xs, finish, seen)
      Enum.member?(seen,current) -> part2(backward_conn, forward_conn, xs, finish, seen)
      true ->
        forward = get_forward(forward_conn[current], [], steps+1)
        tocheck = [{backward_conn[current], steps+1}| forward]
        next = tocheck ++ xs
        tmpSeen = [current|seen]
        part2(backward_conn, forward_conn, next, finish, tmpSeen)
    end
  end
  def part2(_, _, [], _,_) do
    {:error, "cannot find connection"}
  end
  def get_forward([conn|conns], ret, step) do
    get_forward(conns, [{conn,step}|ret], step)
  end
  def get_forward([], ret,_) do
    ret
  end
  def get_forward(nil, _, _) do
    []
  end
end
