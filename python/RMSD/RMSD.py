#-*- coding: utf-8 -*-

import numpy as np
import xlrd
import matplotlib.pyplot as pl

 
# Use numpy to load the data contained in the file

# ’mof5.txt’ into a 2-D array called data

# import the data
data = xlrd.open_workbook('RMSD.xlsx')
table = data.sheet_by_name('Sheet1')
# get values
x1 = table.col_values(0)
y1 = table.col_values(1)
#y2 = table.col_values(2)
#y3 = table.col_values(3)
#y4 = table.col_values(4)
#y5 = table.col_values(5)

# drop the 1st line of the data, which is the name of the data
x1.pop(0)
y1.pop(0)
#y2.pop(0)
#y3.pop(0)
#y5.pop(0)
#y4.pop(0)
 
# plot the first column as x, and second column as y

p1=pl.plot(x1, y1,'r-',label='Complex')# use pylab to plot x and y
#p1=pl.plot(x1, y2,'k-',label='$espilon_{1zz}$')# use pylab to plot x and y
#p1=pl.plot(x1, y3,'bo-',label='N2/273K Ads')
#p1=pl.plot(x1, y5,'yv-',label='CH3CH2OH/273K Ads')
#p1=pl.plot(x1, y4,'k*-',label='H2O/273K Ads')



pl.title('pure-$Bi_2O_3$',color="w",fontweight="bold", fontsize=10)# give plot a title
pl.ylabel('RMSD(Angstrom)',fontweight="bold", fontsize=10)# make axis labels
pl.xlabel('t(ps)',fontweight="bold", fontsize=10)
pl.subplots_adjust(left=0.18, bottom=None, right=None, top=None, wspace=None, hspace=None)
#pl.xlim(50, 800)# set axis limits
#pl.ylim(0.0, 1.0)
pl.legend(loc = 0)# make legend
#pl.show()# show the plot on the screen
pl.savefig('RMSD.png',dpi = 600)

