defmodule Solve do
  def part1() do
    File.stream!("in") 
    |> Enum.map(&String.trim/1)
    |> Enum.map(&String.to_integer/1)
    |> Enum.sort()
    |> find_addends(2020)
  end
  def part2() do
    nums = parseinput("in")
    indexed_nums =  Enum.with_index(nums)
    find_three_addends(indexed_nums, nums, 2020)
  end
  defp parseinput(args) do
    File.stream!(args) 
    |> Enum.map(&String.trim/1)
    |> Enum.map(&String.to_integer/1)
    |> Enum.sort()
  end
  def find_addends(nums, target) do
    result = 
      Enum.reduce_while(nums, MapSet.new(), fn n, found ->
        complement = target - n
        cond do
          complement > n -> {:cont, MapSet.put(found,n)}
          complement in found -> {:halt, {complement, n}}
          true -> {:cont, found}
        end
        end)
    case result do
      {a,b} -> a*b
      _ -> nil
    end
  end
  def find_three_addends([{n,i} | rest ], nums, target) do
    nums
    |> Enum.drop(i+1)
    |> find_addends(target-n)
    |>  case do
      nil -> find_three_addends(rest, nums, target)
      m -> n*m
    end
  end
end


