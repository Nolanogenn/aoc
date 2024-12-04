defmodule Solve do
  defp get_combinations(n,m) do
    get_combinations(m-n,n,m,(for x <- n..m, do: [x])) 
  end
  defp get_combinations(0,_,_, acc), do: acc
  defp get_combinations(remaining,n,m, acc) do
    get_combinations(remaining-1,n,m, (for x<-n..m, y <- acc, do: [x|y]))
  end
  defp get_non_repeating(l) do
    get_non_repeating(l,[])
  end
  defp get_non_repeating([x|xs], seen) do
    cond do
      Enum.member?(seen, x) -> false
      true -> get_non_repeating(xs, [x|seen])
    end
  end
  defp get_non_repeating([], _) do
    true
  end
  def compute_comb_2(poss, filename) do
    IO.inspect {"CURRENT INPUTS: ", poss}
    {:ok, contents} = File.read(filename)
    s = contents
        |> String.trim()
        |> String.split(",", trim: true)
        |> Enum.map(&String.to_integer/1)
        |> Enum.with_index(0) 
        |> Enum.map(fn {k,v}->{v,k} end)
        |> Map.new
    compute_comb_2(poss, poss, [s,s,s,s,s],[s,s,s,s,s],0)
  end
  defp compute_comb_2([p|ps], poss, [map|ss], maps,input) do
    {:ok,v,m} = part1({[p,input], map})
    IO.inspect v
    compute_comb_2(ps, poss,ss,[m|maps],v)
  end
  defp compute_comb_2([], poss, [], maps, input) do
    IO.inspect {"====END LOOP, V: ", input, "===="}
#    tmpMaps = Enum.reverse(maps)
#    IO.inspect maps
    compute_comb_2(poss, poss, maps, [], input)
  end
  defp compute_comb(poss, filename) do
    compute_comb(poss, filename, 0)
  end
  defp compute_comb([phase|ps], filename, input) do
    {:ok, v, _} = solve(filename, [phase,input])
    compute_comb(ps, filename, v)
  end
  defp compute_comb([], _, thruster) do
    thruster
  end
  defp getMax(l) do
    getMax(l, 0)
  end
  defp getMax([x|xs], curr) do
    cond do
      x > curr -> getMax(xs, x)
      true -> getMax(xs, curr)
    end
  end
  defp getMax([], m) do
    m
  end
  def find_best_2(filename) do
    possibilities = get_combinations(5,9)
                    |> Enum.filter(&get_non_repeating(&1)) 
                    |> Enum.map(&compute_comb_2(&1, filename))
    m = getMax(possibilities)
    m
  end
  def find_best(filename) do
    possibilities = get_combinations(0,4)
                    |> Enum.filter(&get_non_repeating(&1)) 
                    |> Enum.map(&compute_comb(&1, filename))
    m = getMax(possibilities)
    m
  end
  def solve(filename, input) do
    {:ok, contents} = File.read(filename)
    in1 = contents
        |> String.trim()
        |> String.split(",", trim: true)
        |> Enum.map(&String.to_integer/1)
        |> Enum.with_index(0) 
        |> Enum.map(fn {k,v}->{v,k} end)
        |> Map.new
    part1({input,in1})
  end
  def part1({input,m}) do
    k = m[0]
    part1({input,m,0},0,k)
  end
  def part1({input,m,output}, i, instruction) do
    {command, params} = get_params(instruction)
    n = get_offset(command)
    part1({input,m,output}, i, command, params,n)
  end
  def get_params(instruction) do
    digits = Integer.digits(instruction)
    digits = add_leading(digits)
    {command,_} = Enum.take(digits,-2) |> Enum.join("") |> Integer.parse()
    {command, Enum.reverse(Enum.take(digits,3))}
  end
  def add_leading(digits) when length(digits) < 5 do
    add_leading([0|digits])
  end
  def add_leading(digits) when length(digits) == 5 do
    digits
  end
  def get_offset(command) do
    case command do
      1 -> 4
      2 -> 4
      3 -> 2
      4 -> 2
      5 -> 3
      6 -> 3
      7 -> 4
      8 -> 4
      _ -> :error
    end
  end
  def get_inputs(m,i,params) do
    get_inputs(m,i,params,[])
  end
  def get_inputs(_,_,[],inputs) do
    Enum.reverse(inputs)
  end
  def get_inputs(m,i,[0|ps],inputs) do
    tmpi = i+1
    v = m[m[tmpi]]
    get_inputs(m,tmpi,ps,[v|inputs])
  end
  def get_inputs(m,i,[1|ps], inputs) do
    tmpi = i+1
    v = m[tmpi]
    get_inputs(m,tmpi,ps,[v|inputs])
  end
  def part1({input,m,output},i,1,params,n) do #sum
    [v1,v2,_] = get_inputs(m,i,params)
    x = v1 + v2
    z = m[i+3]
    #IO.inspect {1,v1,v2,z}
    m2 = Map.replace!(m, z, x) 
    part1({input,m2,output}, i+n, m2[i+n]) 
  end
  def part1({input,m,output},i,2,params,n) do #multiply
    [v1, v2, _]= get_inputs(m,i,params)
    x = v1 * v2
    z = m[i+3]
    #IO.inspect {2, v1,v2, z}
    m2 = Map.replace!(m, z, x) 
    part1({input,m2,output},i+n,m2[i+n]) 
  end
  def part1({[phase,input],m,output},i,3,_,n) do #set value for phase setting
    z = m[i+1]
    m2 = Map.replace!(m, z, phase) 
    #IO.inspect {3, " phase: ", phase, z}
    part1({input,m2,output}, i+n, m2[i+n]) 
  end
  def part1({input,m,output},i,3,_,n) do #set value for the input
    z = m[i+1]
    m2 = Map.replace!(m, z, input) 
    #IO.inspect {3, "input: ", input, z}
    part1({input,m2,output}, i+n, m2[i+n]) 
  end
  def part1({input,m,_},i,4,params,n) do #return
    [z,_,_] = get_inputs(m,i,params)
    #IO.inspect {params, 4,m[i+1],z}
    part1({input,m,z},i+n,m[i+n])
  end
  def part1({input,m,output},i,5,params,n) do #jump-if-true
    [v1,v2,_] = get_inputs(m,i,params)
    #IO.inspect {5,v1,v2}
    case v1 do
      0 -> part1({input,m,output}, i+n, m[i+n])
      _ -> part1({input,m,output},v2,m[v2])
    end
  end
  def part1({input,m,output}, i,6, params,n) do #jump-if-false
    [v1,v2,_] = get_inputs(m,i,params)
    #IO.inspect {6,v1,v2,i+n, m[i+n]}
    case v1 do
      0 -> part1({input,m,output},v2,m[v2])
      _ -> part1({input,m,output},i+n,m[i+n])
    end
  end
  def part1({input,m,output}, i,7, params,n) do #less-then
    [v1,v2,_] = get_inputs(m,i,params)
    v3 = m[i+3]
    #IO.inspect {7,v1,v2,v3}
    case v1 < v2 do
      true -> 
        m2 = Map.replace!(m,v3,1)
        part1({input,m2,output},i+n,m2[i+n])
      _ -> 
        m2 = Map.replace!(m,v3,0)
        part1({input,m2,output},i+n,m2[i+n])
    end
  end
  def part1({input,m,output}, i,8, params,n) do #equals
    [v1,v2,_] = get_inputs(m,i,params)
    v3 = m[i+3]
    #IO.inspect {i, 8,v1,v2,v3}
    case v1 == v2 do
      true -> 
        m2 = Map.replace!(m,v3,1)
        part1({input,m2,output},i+n,m2[i+n])
      _ -> 
        m2 = Map.replace!(m,v3,0)
        part1({input,m2,output},i+n,m2[i+n])
    end
  end
  def part1({_,m,output}, _,99,_,_) do
    {:ok, output, m}
  end
  def part1({_,_,output}, _,_,_,_) do
    {:error, output}
  end
end
