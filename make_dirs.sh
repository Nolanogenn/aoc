YEAR=$1
if [ -d "$YEAR" ];
then
	echo "DIRECTORY FOR $YEAR ALREADY EXISTS DAWG";
else
	mkdir $1;
	for i in {1..25}; do 
		mkdir $1/day$i;
	done
fi

