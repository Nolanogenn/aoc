declare -A EXTENSIONS

EXTENSIONS["python"]=".py"
EXTENSIONS["elixir"]=".ex"
EXTENSIONS["go"]=".go"
EXTENSIONS["prolog"]=".pl"

SESSION=$(cat ~/vboxshare/aoc_session.txt)
YEAR=$1
DAY=$2
LANGUAGE=$3
EXT=${EXTENSIONS["$LANGUAGE"]}

SOLVEFILE="solve$EXT"
TEMPLATE="templates/template$EXT"

echo "command: cp $TEMPLATE $SOLVEFILE for day $2 year $1"

if [ ! -d "$YEAR/day$DAY" ];
then
	mkdir $YEAR/day$DAY
fi
curl https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$SESSION" > "$YEAR/day$DAY/in"
if [ ! -f "$YEAR/day$DAY/$SOLVEFILE" ];
then
	cp $TEMPLATE $YEAR/day$DAY/$SOLVEFILE
fi
