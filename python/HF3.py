file = open('./a.txt','r')

readline = file.readlines()

i = 1
for line in readline:
    i = i + 1
    if i%1==0:
        new_line = line.split('HF=')[1].split('\R')[0]
        new_file = open('./b.txt','a')
        new_file.write(new_line+'\n')
        
       		
	
print(new_line)
