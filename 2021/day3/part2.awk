func common(k, arr, i, c){
	for (i in arr) { c += arr[i][k]*2-1}
	return c>=0
	}
func cull(k,v, arr,i){
	for (i in arr) { if (arr[i][k] != v) { delete arr[i] }}
	}

func to_n(arr,i, j,c){
	for (i in arr) {
		for (j in arr[i]) {
			c = lshift(c,1)+arr[i][j]
			}
		}
	return c
	}

BEGIN {FS=""}
{ for (i=1; i<=NF; i++) { o2[NR][i]=$i; co2[NR][i]=$i }}
END {
	for (i=1; i<=NF; i++){
		cull(i,common(i,o2), o2)
		if (length(o2) == 1) {break}
		}
	for (i=1; i<=NF; i++){
		cull(i, common(i,co2), co2)
		if (length(co2) == 1) {break}
		}
	print to_n(o2)*to_n(co2)	
	}
