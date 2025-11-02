sol_1(L1, L2, Ans1) :-
	quicksort(L1, SortedL1),
	quicksort(L2, SortedL2),
	solve1(SortedL1, SortedL2, Ans1).

sol_2(_, "second answer") .

solve1(L1, L2, Ans) :-
	solve1(L1, L2, 0, Ans).
solve1([],[],Ans, Ans).
solve1([N|Ns], [M|Ms], Acc, Ans) :-
	dabs(N-M, K),
	NewAcc is Acc + K,
	solve1(Ns, Ms, NewAcc, Ans).

dabs(N, NA) :-
	N < 0,
	NA = - N.
dabs(N, N) :-
	N >= 0.

quicksort([X|Xs], Ys) :-
	partition(Xs, X, Left, Right),
	quicksort(Left, Ls),
	quicksort(Right, Rs),
	append(Ls, [X|Rs], Ys).
quicksort([],[]).
partition([X|Xs], Y, [X|Ls], Rs) :-
	X =< Y, partition(Xs, Y, Ls, Rs).
partition([X|Xs], Y, Ls, [X|Rs]) :-
	X > Y, partition(Xs, Y, Ls, Rs).
partition([], Y, [], []).

print_list([]) :-
	format("END OF THE LIST ~n").
print_list([A|B]) :-
	format("curr elem = ~w ~n", A),
	print_list(B).

parse_lines([],[],[]).

parse_lines([Line|Lines], [N1|L1], [N2|L2]) :-
	split_string(Line, "\s", "\s", [NS1,NS2]),
	number_string(N1, NS1),
	number_string(N2, NS2),
	parse_lines(Lines, L1, L2).

split_lines(String, Lines) :-
	split_string(String, "\n", "\n", Lines).

parse_input(Input, Ans1, Ans2) :-
	split_lines(Input, Lines),
	parse_lines(Lines, L1, L2),
	sol_1(L1, L2, Ans1),
	sol_2(Lines, Ans2).

read_file_to_string(Filepath, Input) :-
	open(Filepath, read, Stream),
	read_string(Stream, _, Input),
	close(Stream).

run(Input) :-
	parse_input(Input, Ans1, Ans2),
	format("SOLUTION FOR PART 1: ~w ~n", [Ans1]),
	format("SOLUTION FOR PART 2: ~w ~n", [Ans2]).

run() :- 
	read_file_to_string("in", Input),
	run(Input).
