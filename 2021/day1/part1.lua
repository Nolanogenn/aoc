file = io.open("input.txt")
lines = file:lines()

current_val = 99999999999;
sol = 0;
for line in lines
	do
		line_number = tonumber(line);
		if line_number > current_val then sol = sol + 1 end
		current_val = line_number;
	end

print(sol);
