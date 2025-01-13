declare -A EXTENSIONS

EXTENSIONS["python"]=".py"
EXTENSIONS["elixir"]=".ex"
EXTENSIONS["go"]=".go"

SESSION=$(cat ~/vboxshare/aoc_session.txt)
YEAR=$1
DAY=$2
EXT=${EXTENSIONS["${3:-python}"]}

SOLVEFILE="solve$EXT"
TEMPLATE="templates/template$EXT"

if [ ! -d "$YEAR/day$DAY" ];
then
	mkdir $YEAR/day$DAY
fi
curl https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$SESSION" > "$YEAR/day$DAY/in"
if [ ! -f "$YEAR/day$DAY/$SOLVEFILE" ];
then
	cp $TEMPLATE $YEAR/day$DAY/$SOLVEFILE
fi
