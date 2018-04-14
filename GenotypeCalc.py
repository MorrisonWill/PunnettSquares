#Final Genotype Thing
#Matan and Will

genotype1 = str(input("Input the first genotype here!"))
genotype2 = str(input("Input the second genotype here!"))
split_genes_list1 = []
split_genes_list2 = []
genotype_list=[]
genotype_offspring=[]

def make_strings_lists():
    index1 = 0
    index2 = 1
    while index2 < len(genotype1):
        split_genes_list1.append(genotype1[index1]+genotype1[index2])
        split_genes_list2.append(genotype2[index1]+genotype1[index2])
        index1+=2
        index2+=2
    return(split_genes_list1)

def get_all_combinations(parent):
    make_strings_lists()


            








'''# Punnet Square Calculator
# Will Morrison

#Will Morrison can be reached at iamwillmorrison@gmail.com


.______    __    __  .__   __. .__   __.  _______ .___________.        _______.  ______       __    __       ___      .______       _______      _______.
|   _  \  |  |  |  | |  \ |  | |  \ |  | |   ____||           |       /       | /  __  \     |  |  |  |     /   \     |   _  \     |   ____|    /       |
|  |_)  | |  |  |  | |   \|  | |   \|  | |  |__   `---|  |----`      |   (----`|  |  |  |    |  |  |  |    /  ^  \    |  |_)  |    |  |__      |   (----`
|   ___/  |  |  |  | |  . `  | |  . `  | |   __|      |  |            \   \    |  |  |  |    |  |  |  |   /  /_\  \   |      /     |   __|      \   \    
|  |      |  `--'  | |  |\   | |  |\   | |  |____     |  |        .----)   |   |  `--'  '--. |  `--'  |  /  _____  \  |  |\  \----.|  |____ .----)   |   
| _|       \______/  |__| \__| |__| \__| |_______|    |__|        |_______/     \_____\_____\ \______/  /__/     \__\ | _| `._____||_______||_______/    
                                                                                                                                                        

import datetime	



#This finds all combinations
def get_all_combinations(parent): 
	if len(parent) == 1:
		return [parent[0][0], parent[0][1]]
	else:
		genlist = []
		for x in get_all_combinations(parent[1:]):
			genlist.append(parent[0][0] + x)
			genlist.append(parent[0][1] + x)
		return genlist                                                          

def make_row(genotype, allele):
	row = []
	for a in genotype:
		row.append(a + allele)
	return row                                                            

def make_table(parent1, parent2):
	table = []
	for a in parent1:
		table.append(make_row(parent2, a))
	return table
                                                              
def print_table(table, c1, c2):
	latextable = []
	#I don't know what the hell this is it's just from some thing I found about how to calculate punnet squares
	divlength = (len(c1[0])*2+4)*2**(len(c1[0]))
	print('')
	print('', end=' ')
	for a in c2:
		print(' '*(len(c1[0])+3) + a + '', end=' ')
		latextable.append('& ' + a + ' ')
	print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
	latextable.append('\\\ \n\\hline\fn')
	
	for i, row in enumerate(table):
		print(c1[table.index(row)], end=' ')
		latextable.append(c1[table.index(row)] + ' & ')
		print('|', end=' ')
		for j, cell in enumerate(row):
			print(cell + ' | ', end=' ')
			if j != len(row)-1:
				latextable.append(cell + ' & ')
			else:
				latextable.append(cell + ' ')
		print('\n' + ' '*(len(c1[0])+1) + '-'*(divlength))
		if i != len(table)-1:
			latextable.append('\\\ \n')	
	return latextable		


                                                              



def print_genotype_frequencies(table):
	freqtable = []
	freqtable.append('\n')
	calculated = []
	genotypes = [a for b in table for a in b]
	for k, x in enumerate(genotypes):
		count = 0
		for y in genotypes:
			if sorted(x) == sorted(y):
				count += 1
		if sorted(x) not in calculated:
			print("The frequency of the " + x + " genotype is " + str(float(count)/float((len(genotypes)))*100) + "%.")
			freqtable.append(x + ' & ' + str(float(count)/float((len(genotypes)))*100) + '\\% \\\ \\hline \n')	
		calculated.append(sorted(x))
	return freqtable	

print('') 
print('==========   Will\'s Super Duper Homework Solving Machine ==============')
print('') 
print('Hello. This is where will does his Biology homework.')
print('') 
print('=====================================================================')
print('')
while True:
	p1 = input("Please enter the genotype of the first parent: ").split(' ')
	p2 = input("Please enter the gentype of the second parent: ").split(' ')
	c1 = get_all_combinations(p1)
	c2 = get_all_combinations(p2)
	a = make_table(c1, c2)
	latextable = print_table(a, c1, c2)
	freqtable = print_genotype_frequencies(a)
	print('')
	action = input("Enter (A) to make another or any key to quit!\n")
	if action == "A":
		print('')
		print("Again!\n")
	else:	
		quit()
'''
