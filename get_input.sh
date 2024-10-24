SESSION=$(cat ~/vboxshare/aoc_session.txt)
YEAR=$1
DAY=$2

if [ ! -d "$YEAR/$DAY" ];
then
	mkdir $YEAR/day$DAY
fi
curl https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$SESSION" > "$YEAR/day$DAY/in"
cp template.py $YEAR/day$DAY/solve.py

