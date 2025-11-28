defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    sol1 = contents
        |> String.split("\n", trim: true)
        |> part1()
    IO.puts "Part 1 solution: "
    IO.inspect sol1
#    sol2 = contents
#        |> String.split("\n", trim: true)
#        |> Enum.map(&String.to_integer/1)
#        |> Enum.map(&part2/1)
#        |> Enum.sum()
#    IO.puts "Part 2 solution: "
#    IO.inspect sol2
  end
  def handleDistance([], locations, pairs) do
    {locations |> Enum.uniq(), pairs}
  end
  def handleDistance([d|ds], locations, pairs) do
    [p1, p2] = String.split(d, " = ", trim: true)
    cost = String.to_integer(p2)
    [source, target] = String.split(p1, " to ", trim: true)
    handleDistance(
    ds,
    [source | [target | locations]],
    [{{source, target}, cost}|[{{target,source},cost}| pairs]]
    )
  end
  def handleDistances(distances) do
    handleDistance(distances, [],[])
  end
  def findAllRoutes([], _, _, cost) do
    cost
  end
  def findAllRoutes([current|ls], locations, pairs, cost) do
    IO.puts("FIND ALL ROUTES")
    IO.inspect({current, cost})
    minimalCost = findMinimalCost(current, pairs, cost)
    case minimalCost < cost do
      true -> findAllRoutes(ls, locations, pairs, minimalCost)
      _ -> findAllRoutes(ls, locations, pairs, cost)
    end
  end
  def findAllRoutes(locations, pairs) do
    findAllRoutes(locations, locations, pairs, 999999)
  end
  def findMinimalCost(starting, pairs, minimal) do
    visitable = getRoutesStartingFrom(starting,pairs,[])
    costs = findAllRoutesFrom(pairs, [{[starting],visitable,0}],[], minimal)
    Enum.min(costs)
  end
  def findAllRoutesFrom(pairs, [{visited,tovisit,currCost}|ps], costs, minimal) do
    next = nextStep(pairs, visited, tovisit, currCost, minimal)
    case next do
      [] -> findAllRoutesFrom(pairs, ps, [currCost+findCost(Enum.at(visited,0),Enum.at(tovisit,0),pairs)|costs], minimal)
      _ -> findAllRoutesFrom(pairs, next++ps, costs, minimal)
    end
  end
  def findAllRoutesFrom(_, [], costs, _) do
    costs
  end
  def nextStep(pairs, visited, tovisit, currCost, minimal) do
    nextStep(pairs, visited, tovisit, currCost, [], minimal)
  end
  def nextStep(_, _, [], _, toret, _) do
    toret
  end
  def nextStep(pairs, visited, [n|ns], currCost, toret, minimal) do
    routes = getRoutesStartingFrom(n, pairs, visited)
    toret = addRoutes(Enum.at(visited,0), routes, toret, pairs, currCost, visited, n, minimal)
    nextStep(pairs, visited, ns, currCost, toret, minimal)
  end
  def addRoutes(starting, [r|rs], toret, pairs, currCost, visited, to, minimal) do
    newVisited = [r|visited]
    newCost = currCost + findCost(starting, to,pairs)
    case newCost >= minimal do
      true -> addRoutes(starting, rs, toret, pairs, currCost, visited, to, minimal)
      _ ->addRoutes(starting, rs,[{newVisited, getRoutesStartingFrom(r, pairs, visited), currCost+findCost(starting,to,pairs)}|toret], pairs, currCost, visited, to, minimal)   end
  end
  def addRoutes(_, [], toret, _, _, _,_, _) do
    toret
  end
  def getRoutesStartingFrom(starting,pairs,visited) do
    Enum.filter(pairs, fn {{x,y}, _} -> x == starting and !Enum.member?(visited,y) end) |> Enum.map(&elem(&1,0)) |> Enum.map(&elem(&1,1)) 
  end
  def findCost(from, to, list) do
    Enum.filter(list, fn {{x,y}, _} -> x == from and y == to end)
    |> Enum.map(&elem(&1,1)) |> Enum.at(0)
  end
  def part1(distances) do
    {locations, pairs} = handleDistances(distances)
    findAllRoutes(locations, pairs)
  end
end

Solve.solve("in")
