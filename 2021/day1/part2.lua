file = io.open("input.txt")
lines = file:lines()

vals = {};

for line in lines
	do
		vals[#vals+1] = tonumber(line);
	end

current_val = 99999999999;
sum_window = 0;
sol = 0;
sliding_i = 0;

for i=1,#vals-2,1 do
	for windows_i=i,i+2,1 do
		sum_window = sum_window + vals[windows_i];
	end
	if sum_window > current_val
		then
			sol = sol+1;
		end
	current_val = sum_window;
	sum_window = 0;
end

print("SOLUTION: ", sol);
