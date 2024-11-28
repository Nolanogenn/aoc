defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    wires = contents
        |> String.split("\n", trim: true)
        |> Enum.map(&String.split(&1, ","))
    {sol1, intersections, steps1, steps2} = part1(wires) 
    IO.puts "Part 1 solution: "
    IO.puts sol1
    IO.puts "==="
    sol2 = part2(intersections, steps1, steps2)
    IO.puts "Part 2 solution: "
    IO.puts sol2
    IO.puts "==="
  end
  def part1(wires) do
      part1(Enum.at(wires,0), Enum.at(wires,1), [], [], {0,0}, {0,0}, %{}, %{})
  end
  def part1([],[], steps1, steps2,  _, _,stepsDict1,stepsDict2) do
    intersections = commonElems(steps1, steps2, [])
                    |> deleteVal({0,0}, [])
    sol = intersections
          |> Enum.map(&manhDist(&1, {0,0}))
          |> Enum.sort()
          |> Enum.at(0)
    {sol, intersections, stepsDict1, stepsDict2}
  end
  def part1([x|xs], ys, p1,p2,pos1,pos2,steps1,steps2) do
    dir = String.first(x)
    val = String.to_integer(String.slice(x, 1..-1))
    newPos = mov(dir, val, pos1)
    {newP1,newSteps1} = updateSteps(p1, pos1, newPos,steps1)
    part1(xs,ys,newP1, p2, newPos, pos2, newSteps1, steps2)
  end
  def part1([], [y|ys], p1, p2, pos1, pos2, steps1, steps2) do
    dir = String.first(y)
    val = String.to_integer(String.slice(y, 1..-1))
    newPos = mov(dir, val, pos2)
    {newP2, newSteps2} = updateSteps(p2, pos2, newPos,steps2)
    part1([], ys, p1, newP2, pos1, newPos, steps1, newSteps2)
  end
  def updateSteps(steps, newPos, newPos,stepsDict) do
    {steps, stepsDict}
  end
  def updateSteps(steps, {x,y1}, {x,y2}, stepsDict)  when y2 > y1 do
    newSteps = [{x,y1}|steps]
    stepsDict = Map.put_new(stepsDict, {x, y1}, length(steps))
    updateSteps(newSteps, {x,y1+1}, {x, y2}, stepsDict) 
  end
  def updateSteps(steps, {x,y1}, {x,y2}, stepsDict)  when y2 < y1 do
    newSteps = [{x,y1}|steps]
    stepsDict = Map.put_new(stepsDict, {x,y1}, length(steps))
    updateSteps(newSteps, {x,y1-1}, {x, y2}, stepsDict) 
  end
  def updateSteps(steps, {x1,y}, {x2,y}, stepsDict) when x2 > x1 do
    newSteps = [{x1,y}|steps]
    stepsDict = Map.put_new(stepsDict, {x1,y}, length(steps))
    updateSteps(newSteps, {x1+1,y}, {x2,y}, stepsDict) 
  end
  def updateSteps(steps, {x1,y}, {x2,y},stepsDict) when x2 < x1 do
    newSteps = [{x1,y}|steps]
    stepsDict = Map.put_new(stepsDict, {x1,y}, length(steps))
    updateSteps(newSteps, {x1-1,y}, {x2,y}, stepsDict) 
  end
  def commonElems([], _, ret) do
    ret
  end
  def commonElems([x|xs], y, ret) do
    case x in y do
      true -> commonElems(xs, y, [x|ret])
      false -> commonElems(xs, y, ret)
    end
  end
  def part2(intersections, steps1, steps2) do
    part2(intersections, steps1, steps2, 9999999)
  end
  def part2([x|xs], steps1, steps2, currMin) do
    val = steps1[x] + steps2[x]
    cond do
      val < currMin -> part2(xs, steps1, steps2, val)
      true -> part2(xs, steps1, steps2, currMin)
    end
  end
  def part2([], _,_, min) do
    min
  end
  def mov(dir,val,pos) do
    case dir do
      "R" -> {elem(pos, 0), elem(pos,1)+val} 
      "L" -> {elem(pos, 0), elem(pos,1)-val} 
      "U" -> {elem(pos, 0)+val, elem(pos,1)} 
      "D" -> {elem(pos, 0)-val, elem(pos,1)} 
    end
  end
  def manhDist(p1, p2) do
    x1 = elem(p1, 0)
    x2 = elem(p2, 0)
    y1 = elem(p1, 1)
    y2 = elem(p2, 1)
    abs(x1-x2) + abs(y1-y2)
  end
  def deleteVal([], _, l2) do
    l2
  end
  def deleteVal([x|xs],x, l2) do
    deleteVal(xs,x, l2)
  end
  def deleteVal([y|xs],x,l2) do
    deleteVal(xs,x,[y|l2])
  end
end
