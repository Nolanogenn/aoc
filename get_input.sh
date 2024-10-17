SESSION=$(cat ~/vboxshare/aoc_session.txt)
YEAR=$1
DAY=$2
curl https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$SESSION" > "$YEAR/day$DAY/in"
