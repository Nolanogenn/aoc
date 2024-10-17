use strict;
use warnings;

my $file = 'in';
open my $handle, $file or die "could not open file";
chomp(my @lines = <$handle>);
close $handle;

my $most_common=0;
my @co2 = ();
my @o = ();

for my $i (0 .. $#lines){
	push(@co2, $i);
	push(@o, $i);
}

sub findMostCommon {
	my ($isRef, $linesRef, $start) = @_;
	my $most_common=0;
	my $b = 0;
	foreach my $i (@{$isRef}){
		$most_common += substr($lines[$i],$start,1)*2-1;
	};
	if ($most_common >= 0){
		$b = 1;
	};
	return $b
}

my $current_i = 0;
while (scalar @o > 1){
	my $b = findMostCommon(\@o, \@lines,$current_i);
	my @new_o = ();
	for my $i (@o){
		if(substr($lines[$i], $current_i, 1) eq $b){
		push(@new_o, $i);
		}
		}
	@o = @new_o;
	$current_i += 1;
};

$current_i = 0;
while (scalar @co2 > 1){
	my $b = findMostCommon(\@co2, \@lines,$current_i);
	my @new_co2 = ();
	for my $i (@co2){
		if(!(substr($lines[$i], $current_i, 1) eq $b)){
		push(@new_co2, $i);
		}
		}
	@co2 = @new_co2;
	$current_i += 1;
}

my $oxygen = oct("0b".$lines[$o[0]]);
my $scrubber = oct("0b".$lines[$co2[0]]);
my $solution = $oxygen*$scrubber;
print "OXYGEN: $oxygen\n";
print "CO2: $scrubber\n";
print "SOLUTION: $solution\n";
