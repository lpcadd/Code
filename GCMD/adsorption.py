file = open('./adsorption.log','r')

readline = file.readlines()

i = 1
for line in readline:
    i = i + 1
    if i%1==0:
        new_line = line.split('cell]')[1].split('+/-')[0]
        new_file = open('./adsorption.txt','a')
        new_file.write(new_line+'\n')
        
       		
	
	print new_line
   
