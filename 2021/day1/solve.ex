defmodule Solve do
  defp parse(input) do
    Enum.map(input, &(String.to_integer(&1)))
  end
  def part1(pathfile) do
    parse(pathfile)
    |> Enum.reduce({:infinity, 0}, fn e, {prev, acc} ->
      if e > prev do 
        {e, acc+1}
      else
        {e, acc}
      end
    end)
    |> elem(1)
  end
end

Solve.part1("testinput")
