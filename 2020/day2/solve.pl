use strict;
use warnings;

my $file = "in";
open my $info, $file or die;

my $firstans = 0;

while (my $line = <$info>){
	my @arr = split ' ', $line;
	my @minmax = split '-', $arr[0];
	my $letter = substr $arr[1],0, 1;
	my $string =  $arr[2];
	my $count = length( $string =~ s/[^\Q$letter\E]//rg );
	$firstans += 1 if($count >= $minmax[0] && $count <= $minmax[1]);
}

print "$firstans\n";
close $info;

my $secondans = 0;

open my $info, $file or die;
while (my $line = <$info>){
	my @arr = split ' ', $line;
	my @pos = split '-', $arr[0];
	my $letter = substr $arr[1],0, 1;
	my $string =  $arr[2];
	my $letterfirst = substr $string,$pos[0]-1,1;
	my $lettersecond = substr $string,$pos[1]-1,1;
	$secondans += 1 if(($letterfirst eq $letter || $lettersecond eq $letter) && $letterfirst ne $lettersecond);
}

print "$secondans\n";

close $info;
