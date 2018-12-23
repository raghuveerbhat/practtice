use strict;
#use warnings;

my $file = 'a.txt';
open my $info, $file or die "Could not open $file: $!";
my @array;
while( my $line = <$info>)  { 
	my($dcr_no, $status, $creation, $last_modified) = $line =~ m/(^XXX_.{10}).*(OPEN_[A-Z]*).*([0-9]+-[A-Z][a-z]*-2018).*([0-9]+-[A-Z][a-z]*-2018)/g;
	#print $line;
	if ($line =~ m/(^XXX_.{10}).*(OPEN_[A-Z]*).*([0-9]+-[A-Z][a-z]*-2018).*([0-9]+-[A-Z][a-z]*-2018)/g) {
		push @array, [$dcr_no, $status, $creation, $last_modified];
	}
}
foreach my $i (0 .. $#array) {
	print "$i: \nDCR=$array[$i]->[0]\nStatus=$array[$i]->[1]\nCreation=$array[$i]->[2]\nLast_Modified=$array[$i]->[3]\n";
}
close $info;