#!/bin/bash

for inf in *.lsf

do 

bsub ${inf}

done

