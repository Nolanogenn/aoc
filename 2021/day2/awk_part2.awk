/down/ {aim+=$2}
/up/ {aim-=$2}
/forward/ {x+=$2}
/forward/ {d+=aim*$2}
END {print d*x} 
