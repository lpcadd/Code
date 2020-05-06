#!/bin/bash

sed -i "s/,/\ /g" a.txt

for inf in $(cat a.txt)

do 

echo Running ${inf}...

time wget https://files.rcsb.org/download/${inf}.pdb

echo ${inf} is finished

echo

done

