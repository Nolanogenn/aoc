import Bitwise
defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("\n", trim: true)
        |> part1()
    IO.puts "Part 1 solution: "
    IO.inspect Map.get(sol1, "a")
    sol2 = contents
        |> String.split("\n", trim: true)
        |> part2(sol1)
    IO.puts "Part 2 solution: "
    IO.inspect Map.get(sol2, "a")
  end
  def getFromWires(node, wires) do
    case Map.fetch(wires, node) do
      {:ok, v} -> v
      _ -> String.to_integer(node)
    end
  end
  def handleAnd(ins, wires) do
    [l, r] = String.split(ins, " AND ", trim: true)
    getFromWires(l, wires) &&& getFromWires(r,wires)
  end
  def handleOr(ins, wires) do
    [l, r] = String.split(ins, " OR ", trim: true)
    bor(getFromWires(l,wires), getFromWires(r,wires))
  end
  def handleLshift(ins,wires) do
    [l, by] = String.split(ins, " LSHIFT ", trim: true)
    bsl(getFromWires(l, wires), String.to_integer(by))
  end
  def handleRshift(ins,wires) do
    [l, by] = String.split(ins, " RSHIFT ", trim: true)
    bsr(getFromWires(l, wires), String.to_integer(by))
  end
  def handleNot(ins,wires) do
    [_, k] = String.split(ins, " ", trim: true)
    bnot(Map.get(wires,k))
  end
  def handleInstruction(ins, wires) do
    cond do
      String.contains?(ins, " AND ") -> handleAnd(ins, wires)
      String.contains?(ins, " OR ") -> handleOr(ins, wires)
      String.contains?(ins, " LSHIFT ") -> handleLshift(ins, wires)
      String.contains?(ins, " RSHIFT ") -> handleRshift(ins, wires)
      String.contains?(ins, "NOT ") -> handleNot(ins, wires)
      true -> getFromWires(ins, wires)
    end
  end
  def sendSignals([], wires) do
    wires
  end
  def sendSignals([instruction|is], wires) do
    [instr, tar] = String.split(instruction, " -> ", trim: true)
    sendSignals(
    is,
    Map.put(wires, tar, handleInstruction(instr, wires))
    )
  end
  def getTarget(instruction) do
    String.split(instruction, " -> ", trim: true) |> Enum.at(1)
  end
  def getStarting(instruction) do
    splittedString = String.split(instruction, " -> " , trim: true)
    |> Enum.at(0)
    Regex.scan(~r/([a-z]+)/, splittedString)
    |> Enum.map(&Enum.at(&1, 0))
  end
  def orderSignals([], ordered, _) do
    ordered
  end
  def orderSignals(tocheck, ordered, unlockedNodes) do
    next = Enum.filter(tocheck, fn x -> contains(getStarting(x),unlockedNodes) end)
    tocheck = Enum.reject(tocheck, fn x -> contains(getStarting(x),unlockedNodes) end)
    newUnlocked = next |> Enum.map(&getTarget(&1))
    orderSignals(tocheck, ordered ++ next, unlockedNodes ++ newUnlocked)
  end
  def contains([elem|l1], l2) do
    case Enum.member?(l2, elem) do
      true -> contains(l1, l2)
      _ -> false
    end
  end
  def contains([], _) do
    true
  end
  def part1(instructions) do
    independentInstructions = Enum.filter(instructions, fn x -> Regex.match?(~r/^([0-9]+ ->)/,x) end)
    tocheck = Enum.reject(instructions, fn x -> Regex.match?(~r/^([0-9]+ ->)/,x) end)
    orderedSignals = orderSignals(
    tocheck,
    independentInstructions,
    independentInstructions |> Enum.map(&getTarget(&1))
    )
    sendSignals(orderedSignals, %{})
  end
  def part2(instructions, wires) do
    newWires = %{"b" => Map.get(wires,"a")}
    filtered = Enum.reject(instructions, fn x-> String.ends_with?(x, " -> b") end)
    independentInstructions = Enum.filter(filtered, fn x -> Regex.match?(~r/^([0-9]+ ->)/,x) end)
    tocheck = Enum.reject(filtered, fn x -> Regex.match?(~r/^([0-9]+ ->)/,x) end)
    unlocked = ["b"] ++ Enum.map(independentInstructions, &getTarget(&1))
    orderedSignals = orderSignals(
    tocheck,
    independentInstructions,
    unlocked
    )
    sendSignals(orderedSignals, newWires)
  end
end

Solve.solve("in")
