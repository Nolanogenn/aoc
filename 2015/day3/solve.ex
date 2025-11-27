defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("", trim: true)
        |> part1({0,0}, [{0,0}])
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = contents
        |> String.split("", trim: true)
        |> Enum.with_index()
        |> part2({0,0},{0,0},[{0,0}])
    IO.puts "Part 2 solution: "
    IO.puts sol2
  end
  def part2([{nextMove, idx}| movs], posSanta, posBot, visited) do
    {newPosSanta, newPosBot, newVisited} = 
    if rem(idx,2) == 0 do
      newPosBot = move(nextMove, posBot)
      newVisited = addIfNotPresent(visited, newPosBot)
      {posSanta, newPosBot, newVisited}
    else
      newPosSanta = move(nextMove, posSanta)
      newVisited = addIfNotPresent(visited, newPosSanta)
      {newPosSanta, posBot, newVisited}
    end
    part2(movs, newPosSanta, newPosBot, newVisited)
  end
  def part2([], _, _, visited) do
    length(visited)  
  end
  def addIfNotPresent(t, newValue) do
    case Enum.member?(t, newValue) do
      true -> t
      _ -> [newValue|t]
    end
  end
  def move(dir, currPos) do
    case dir do 
      ">" -> {elem(currPos,0)+1, elem(currPos,1)}
      "<" -> {elem(currPos,0)-1, elem(currPos,1)}
      "v" -> {elem(currPos,0), elem(currPos,1)-1}
      "^" -> {elem(currPos,0), elem(currPos,1)+1}
      _ -> currPos
    end
  end
  def part1([nextMov|movs], currPos, visited) do
    nextPos = move(nextMov, currPos)
    newVisited = addIfNotPresent(visited, nextPos)
    part1(movs, nextPos, newVisited)
  end
  def part1([], _, visited) do
    length(visited)
  end
end

Solve.solve("in")
