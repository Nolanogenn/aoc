defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("\n", trim: true)
        |> part1()
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = contents
        |> String.split("\n", trim: true)
        |> part2()
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def part1(rotations) do
    countZeroes(rotations,50,0)
  end
  def countZeroes([], _, zeroes) do
    zeroes
  end
  def countZeroes([rot|rotations], pos, zeroes) do
    {mov,by} = getValues(rot)
    {newPos, zeroes} = moveDial(pos, mov, by, zeroes)
    countZeroes(rotations, newPos, zeroes)
  end
  def getValues(rot) do
    {
      String.slice(rot,0..0),
      String.slice(rot,1..-1//1)
    }
  end
  def moveBy(pos, mov, by) do
    case mov == "R" do
      true -> Integer.mod(pos+by,100)
      _ -> Integer.mod(pos-by,100)
    end
  end
  def moveDial(pos, mov, by, zeroes) do
    byInt = String.to_integer(by)
    toret = moveBy(pos, mov, byInt)
    case toret == 0 do
      true -> {toret, zeroes+1}
      _ -> {toret, zeroes}
    end
  end
  def part2(rotations) do
    countZeroes2(rotations,50,0)
  end
  def countZeroes2([], _, zeroes) do
    zeroes
  end
  def countZeroes2([rot|rotations], pos, zeroes) do
    {mov,by} = getValues(rot)
    {newPos, zeroes} = moveDial2(pos, mov, by, zeroes)
    countZeroes2(rotations, newPos, zeroes)
  end
  def moveDial2(pos, mov, by, zeroes) do
    byInt = String.to_integer(by)
    {toret,passesAtZero} = moveBy2(pos, mov, byInt)
    {toret, zeroes+passesAtZero}
  end
  def moveBy2(pos, mov, by) do
    case mov == "R" do
      true -> {Integer.mod(pos+by,100), Integer.floor_div(pos+by, 100)}
      _ -> {Integer.mod(pos-by,100), -Integer.floor_div(pos-by, 100)}
    end
  end
end

Solve.solve("in")
