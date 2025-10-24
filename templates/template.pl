sol_1(_, "first answer") .
sol_2(_, "second answer") .

parse_lines(_, _, _).

split_lines(String, Lines) :-
	split_string(String, "\n", "\n", Lines).

parse_input(Input, Ans1, Ans2) :-
	split_lines(Input, Lines),
	parse_lines(Lines, _, _),
	sol_1(Lines, Ans1),
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
