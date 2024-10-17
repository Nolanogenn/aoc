BEGIN {FS=""}
{ for (i=1; i<=NF; i++) { b[i] += $i*2-1 }}
END {
	for (i=1; i<=NF; i++){
		g=lshift(g,1)+(b[i]>0)
		e=lshift(e,1)+(b[i]<0)
		}
	print g*e
	}
