use strict;
#use warnings;

my $file = 'a.txt';
open my $info, $file or die "Could not open $file: $!";
my @array;
#my $team_name = 'NA';
my $dcr_no = 'NA';
my $status = 'NA';
my $creation = 'NA';
my $last_modified = 'NA';
my $title = '';

while( my $line = <$info>){
	$_ = $line;
	if( m/Main Development Team: (.*)/g) {
		my($team_name) = $line =~ m/Main Development Team: (.*)/g;
		print "Team name:$team_name\n";
	}
	elsif ( m/(^EBX_.{10}).*(OPEN_[A-Z]*).*([0-9]+-[A-Z][a-z]*-2018).*([0-9]+-[A-Z][a-z]*-2018)/g) {
		($dcr_no, $status, $creation, $last_modified) = $line =~ m/(^EBX_.{10}).*(OPEN_[A-Z]*).*([0-9]+-[A-Z][a-z]*-2018).*([0-9]+-[A-Z][a-z]*-2018)/g;
		last;
	}
}

while( my $line = <$info>)  { 
	#print $line;
	$_ = $line;
	if ( m/(^EBX_.{10}).*(OPEN_[A-Z]*).*([0-9]+-[A-Z][a-z]*-2018).*([0-9]+-[A-Z][a-z]*-2018)/g) {
		push @array, [$dcr_no, $status, $creation, $last_modified, $title];
		$title = '';
		($dcr_no, $status, $creation, $last_modified) = $line =~ m/(^EBX_.{10}).*(OPEN_[A-Z]*).*([0-9]+-[A-Z][a-z]*-2018).*([0-9]+-[A-Z][a-z]*-2018)/g;
		
	}
	elsif ( m/([\[\(]*\w+.*\w+[\.]*)/g) {
		my($t) = $line =~ m/([\[\(]*\w+.*\w+[\.]*)/g;
		$title .= $t;
	}
}
push @array, [$dcr_no, $status, $creation, $last_modified, $title];
foreach my $i (0 .. $#array) {
	print "$i: \nDCR=$array[$i]->[0]\nStatus=$array[$i]->[1]\nCreation=$array[$i]->[2]\nLast_Modified=$array[$i]->[3]\nTitle=$array[$i]->[4]\n";
}
close $info;