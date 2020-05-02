#!/usr/bin/perl

use strict;

`rm mol2_list RMSD_list RMSD_noh_list`;
`ls ligand/*mol2 >mol2_list`;

my $file = "mol2_list";
my @pdbcodes = qw();
my @files = qw();
open(FILE, $file) || $!;
while(<FILE>) {
      chomp $_;
      if(m/^ligand\/(\w+)_min/) {
        push @pdbcodes, substr($1,0,4); 
#        print "$1\n";
        push @files, $1;
      }
}
close FILE;

for(my $i=0;$i<@pdbcodes;$i++) {
    my $file_temp1 = "./ligand/$files[$i]\_min_ligand.mol2";
    for(my $j=0;$j<@pdbcodes;$j++) {
        my $file_temp2 = "$pdbcodes[$j]/$files[$i]\_-_hbond-opt_ligand.mol2";
        `./calculate_mol2_RMSD.pl $file_temp1 $file_temp2 >>RMSD_list`;
        `./calculate_mol2_RMSD_noh.pl $file_temp1 $file_temp2 >>RMSD_noh_list`;        
    }
}
