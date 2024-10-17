/up/ {d-=$2}
/down/ {d+=$2}
/forward/ {h+=$2}
END {print d*h}


