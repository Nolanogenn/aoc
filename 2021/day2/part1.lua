file = io.open("input.txt");
lines = file:lines()

vals = {}
for line in lines
	do
		vals[#vals+1] = line;
	end

x = 0; --horizontal
y = 0; --depth

for i=1,#vals,1
	do
		line = vals[i];
		val = tonumber(string.match(line, "%d"));
		if string.find(line, "forward") then x = x+val end;
		if string.find(line, "down") then y = y+val end;
		if string.find(line, "up") then y = y-val end;
		print(x,y);
	end

sol = y*x;
print(sol)
		
