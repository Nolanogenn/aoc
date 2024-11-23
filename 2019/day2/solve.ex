defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    in1 = contents
        |> String.trim()
        |> String.split(",", trim: true)
        |> Enum.map(&String.to_integer/1)
        |> Enum.with_index(0) 
        |> Enum.map(fn {k,v}->{v,k} end)
        |> Map.new
    in1 = Map.replace!(in1,1,12)
    in1 = Map.replace!(in1,2,2)
    sol1 = part1(in1)
    IO.puts "Part 1 solution: "
    IO.inspect(sol1)
    sol2 = part2(in1, 19690720)
    IO.puts "Part 2 solution: "
    IO.inspect(sol2)
  end
  def part1(m) do
    k = m[0]
    part1(m,0,k)
  end
  def part1(m,i,1) do
    x = m[m[i+1]]+m[m[i+2]]
    z = m[i+3]
    m2 = Map.replace!(m, z, x) 
    new_i = i+4
    new_k = m[i+4]
    part1(m2, new_i, new_k) 
  end
  def part1(m, i, 2) do
    x = m[m[i+1]]*m[m[i+2]]
    z = m[i+3]
    m2 = Map.replace!(m, z, x) 
    new_i = i+4
    new_k = m[new_i]
    part1(m2, new_i, new_k) 
  end
  def part1(m, _, n) when n !== 1 and n !== 2 do
    m[0]
  end
  def part2(m, target) do
    res = 
    for n <- 0..99, v <- 0..99, into: %{} do
      proc = m 
            |> Map.merge(%{1=> n, 2=> v})
            |> part1()
      {proc, {n, v}}
    end
    {n, v}  = res[target]
    100 * n + v
  end

end
