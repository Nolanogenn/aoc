defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    range = contents
        |> String.trim()
        |> String.split("-", trim: true)
        |> Enum.map(&String.to_integer/1)
    sol1 = part1(range)
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = part2(range)
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def part1([range_start,range_end]) do
    range(range_start, range_end)
    |> Enum.map(&checkNum/1)
    |> Enum.sum()
  end
  def part2([range_start, range_end]) do
    range(range_start, range_end)
    |> Enum.map(&checkNum2/1)
    |> Enum.sum()
  end
  def countElem(elem, [x|xs], c) when x != elem do
    countElem(elem, xs, c)
  end
  def countElem(elem, [elem|xs], c) do
    c2 = c+1
    countElem(elem, xs, c2)
  end
  def countElem(_, [], c) do
    c
  end
  def countElem(elem,l) do
    countElem(elem,l,0)
  end
  def range(b,e) do
    range(b,e,[])
  end
  def range(b,e,xs) when b != e do
    b1 = b+1
    range(b1,e,[b|xs])
  end
  def range(b,e,xs) when b == e do
    xs
  end
  def checkNum(num) do
    checkDigits(Integer.digits(num),0,0)
  end
  def checkDigits([n|ns],currDigit,foundPrev) do
    cond do
      n < currDigit -> 0
      n == currDigit -> checkDigits(ns, n, 1)
      true -> checkDigits(ns, n, foundPrev)
    end
  end
  def checkDigits([], _, ret) do
    ret
  end
  def checkNum2(num) do
    checkDigits2(Integer.digits(num),0,%{})
  end
  def checkDigits2([n|ns],currDigit,counts) do
    cond do
      n < currDigit -> 0
      true -> 
        countsNew = Map.put_new(counts, n, 0)
        currCount = countsNew[n] + 1
        countsUpdated = %{countsNew | n => currCount}
        checkDigits2(ns, n, countsUpdated)
    end
  end
  def checkDigits2([], _, counts) do
    checks = counts
    |> Map.values()
    |> Enum.map(fn v -> v == 2 end)
    cond do
      true in checks -> 1
      true -> 0
    end
  end
end
