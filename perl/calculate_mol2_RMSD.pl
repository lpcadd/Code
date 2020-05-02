#!/usr/bin/perl

use strict;

my $file1 = shift;
my $file2 = shift;

my $chainID = shift;

my @x1 = qw();
my @y1 = qw();
my @z1 = qw();
my @x2 = qw();
my @y2 = qw();
my @z2 = qw();

open(FILE, $file1) || $!;
while(<FILE>) {
      chomp $_;
      if(m/^\s+\d+/ & substr($_,6,2) =~ /\d\s/) {
         my @info = split(/\s+/, substr($_,8,38));
         push @x1, $info[1];
         push @y1, $info[2];
         push @z1, $info[3];         
      }
}
close FILE;


open(FILE, $file2) || $!;
while(<FILE>) {
      chomp $_;
      if(m/^\s+\d+/ & substr($_,6,2) =~ /\d\s/) {
         my @info = split(/\s+/, substr($_,8,38));
         push @x2, $info[1];
         push @y2, $info[2];
         push @z2, $info[3]; 
      }

}
close FILE;

if($#x1 != $#x2) {
#   print "$file1 $file2 $#x1 $#x2 number of atoms is not consistent!!\n";
  print "$file1 $file2 0\n";
} else {
  my $square_sum = 0;
  for(my $i=0;$i<@x1;$i++) {
      $square_sum += ($x1[$i]-$x2[$i])**2 + ($y1[$i]-$y2[$i])**2 + ($z1[$i]-$z2[$i])**2;
  }
  my $L_rmsd = sqrt($square_sum/($#x1+1));
  print "$file1 $file2 $L_rmsd\n";
}
