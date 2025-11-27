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
  def followInstructions([instruction|instructions], lights) do
    followInstructions(instructions, handleLights(instruction, lights))
  end
  def followInstructions([], lights) do
    lights
  end
  def getInvolved({x1,y1}, {x2,y2}, baseX, acc) do
    checks = {x1 == x2, y1 == y2}
    case checks do
      {true, true} -> [{x1,y1}|acc]
      {false, _} -> getInvolved({x1+1, y1}, {x2,y2}, baseX, [{x1,y1}|acc])
      {true, false} -> getInvolved({baseX,y1+1}, {x2,y2}, baseX, [{x1,y1}|acc])
    end
  end
  def getInvolved({x1,y1}, {x2,y2}) do
    getInvolved(
    {
      String.to_integer(Enum.at(x1,0)),
      String.to_integer(Enum.at(y1,0))
    },
    {
      String.to_integer(Enum.at(x2,0)),
      String.to_integer(Enum.at(y2,0))
    },
    String.to_integer(Enum.at(x1,0)),
    [])
  end
  def turn([l|ls], lights, to) do
    turn(ls, Map.update(lights, l, to, fn _ -> to end), to)
  end
  def turn([], lights, _) do
    lights
  end
  def bitSwitch(b) do
    case b do
      0 -> 1
      1 -> 0
    end
  end
  def switch([], lights) do
    lights
  end
  def switch([l|ls], lights) do
    switch(ls, Map.update(lights, l, 1, fn x -> bitSwitch(x) end))
  end
  def handleOrder(order, involved, lights) do
    case order do
      "turn on " -> turn(involved, lights, 1)
      "turn off " -> turn(involved, lights, 0)
      _ -> switch(involved, lights)
    end
  end
  def handleLights(instruction, lights) do
    [startX, startY, endX, endY] = Regex.scan(~r/[0-9]+/, instruction)
    involved = getInvolved({startX, startY}, {endX, endY})
    [order, _] = Regex.scan(~r/[a-z ]+/, instruction)
    handleOrder(Enum.at(order,0), involved, lights)
  end
  def part1(instructions) do
    followInstructions(instructions, %{})
    |> Enum.to_list()
    |> Enum.map(fn {_, x} -> x end)
    |> Enum.sum()
  end
  def turnUp([l|ls], lights) do
    turnUp(ls, Map.update(lights, l, 1, fn x -> x+1 end))
  end
  def turnUp([], lights) do
    lights
  end
  def turnDown([l|ls], lights) do
    turnDown(ls, Map.update(lights, l, 0, fn x -> max(0, x-1) end))
  end
  def turnDown([], lights) do
    lights
  end
  def switchUp([l|ls], lights) do
    switchUp(ls, Map.update(lights, l, 2, fn x -> x+2 end))
  end
  def switchUp([], lights) do
    lights
  end
  def handleOrder2(order, involved, lights) do
    case order do
      "turn on " -> turnUp(involved, lights)
      "turn off " -> turnDown(involved, lights)
      _ -> switchUp(involved, lights)
    end
  end
  def handleLights2(instruction, lights) do
    [startX, startY, endX, endY] = Regex.scan(~r/[0-9]+/, instruction)
    involved = getInvolved({startX, startY}, {endX, endY})
    [order, _] = Regex.scan(~r/[a-z ]+/, instruction)
    handleOrder2(Enum.at(order,0), involved, lights)
  end
  def followInstructions2([instruction|instructions], lights) do
    followInstructions2(instructions, handleLights2(instruction, lights))
  end
  def followInstructions2([], lights) do
    lights
  end
  def part2(instructions) do
    followInstructions2(instructions, %{})
    |> Enum.to_list()
    |> Enum.map(fn {_, x} -> x end)
    |> Enum.sum()
  end
end

Solve.solve("in")
