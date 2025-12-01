defmodule Solve do
  def solve(filename) do
    {:ok, contents} = File.read(filename)
    parsed = contents |> String.replace("\n", "")
    sol1 = part1(parsed,40,%{})
    IO.puts "Part 1 solution: "
    IO.inspect sol1
    sol2 = part1(parsed,50,%{})
    IO.puts "Part 2 solution: "
    IO.inspect sol2
  end
  def groupSequence([c|cs]) do
    groupSequence(cs, c, c, [])
  end
  def groupSequence([], _, currSeq, toret) do
    [currSeq | toret]
  end
  def groupSequence([c|cs], currC, currSeq, toret) do 
    case c == currC do
      true -> groupSequence(cs, currC, currSeq <> c, toret)
      _ -> groupSequence(cs, c, c, [currSeq|toret])
    end
  end
  def joinTuple(t) do
    Integer.to_string(elem(t,1)) <> elem(t,0)
  end
  def computeSeq(s) do
    s
    |> String.split("", trim: true)
    |> Enum.frequencies()
    |> Enum.to_list()
    |> Enum.at(0)
    |> joinTuple()
  end
  def genSeq([],s,m) do
    {Enum.join(s),m}
  end
  def genSeq([s|ss],seqs, m) do
    case Map.has_key?(m,s) do
      true -> genSeq(ss, [Map.get(m,s) | seqs], m)
      _ -> mappedSeq = computeSeq(s)
          genSeq(ss, [mappedSeq | seqs], Map.update(m, s, mappedSeq, fn _ -> mappedSeq end))
    end
  end
  def genSeq(sequences, m) do
    genSeq(sequences, [], m) 
  end
  def part1(sequence,n,m) do
    case n > 0 do
      true -> {newSeq, newM} = String.split(sequence, "", trim: true)
              |> groupSequence()
              |> genSeq(m)
        part1(newSeq,n-1,newM)
      _ -> String.length(sequence)
    end
  end
end

Solve.solve("in")
