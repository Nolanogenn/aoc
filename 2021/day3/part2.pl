use strict;
use warnings;

my $file = 'test.txt';
open my $handle, $file or die "could not open file";
chomp(my @lines = <$handle>);
close $handle;

my $most_common=0;
my @co2 = ();
my @o2 = ();

for my $i (0 .. $#lines){
	$most_common += substr($lines[$i],0,1)*2 -1;
	push(@co2, $i);
	push(@o2, $i);
}

my $b = 0;
if ($most_common >= 0){
	$b = 1;
}

my $current_i = 0;
while (scalar @co2 > 1){
	my @new_co2 = ();
	for my $i (@co2){
		if(substr($lines[$i], $current_i, $current_i+1) == $b){
		push(@new_co2, $i);
		}
		}
	@co2 = @new_co2;
	print scalar @co2;
	$current_i += 1;
}
print @co2
