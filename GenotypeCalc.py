#Final Genotype Thing
#Matan and Will

genotype1 = str(input("Input the first genotype here!"))
genotype2 = str(input("Input the second genotype here!"))
split_genes_list1 = []
split_genes_list2 = []
possible_genotype_list1 = []
possible_genotype_list2 = []
genotype_offspring=[]

def make_strings_lists(parent_genotype, split_genes_list):
    index1 = 0
    index2 = 1
    while index2 < len(genotype1):
        split_genes_list.append(parent_genotype[index1]+parent_genotype[index2])
        index1+=2
        index2+=2

def foil(first_gene, second_gene, list_to_store_results):
    list_to_store_results.append(first_gene[0] + second_gene[0])
    list_to_store_results.append(first_gene[0] + second_gene[1])
    list_to_store_results.append(first_gene[1] + second_gene[0])
    list_to_store_results.append(first_gene[1] + second_gene[1])
    
def distribute(gene, list_to_store_results): #list of current genotype possibilities
    list_to_store_results.extend(list_to_store_results) # duplicate the list
    for i in range(0, int(len(list_to_store_results)/2)):
        list_to_store_results[i]+=gene[0]
    for i in range(0, int(len(list_to_store_results)/2)):
        list_to_store_results[int(len(list_to_store_results)/2) + i] += gene[1]


def get_all_combinations(parent, split_genes_list, list_to_store_results): #get all combinations of each parent
    make_strings_lists(parent, split_genes_list)
    if len(split_genes_list) == 1:
        list_to_store_results.append(split_genes_list[0][0])
        list_to_store_results.append(split_genes_list[0][1])
    elif len(split_genes_list) == 2:
        foil(split_genes_list[0], split_genes_list[1], list_to_store_results) #foil the first two binomiasls
    elif len(split_genes_list) > 2: #if there are more than two binomials...
        foil(split_genes_list[0], split_genes_list[1], list_to_store_results)
        for i in range (0, int(len(genotype1)/2)-2): #Loop the following the integer of half of the length of a parent's genotype
            distribute(split_genes_list[2+i], list_to_store_results)
            
def get_all_possible_offspring_genotypes():
    for z in range (0,len(possible_genotype_list2)):
        for i in range(0,len(possible_genotype_list1)):
            string = possible_genotype_list1[z] + possible_genotype_list2[i]
            character_list = []
            final_sorted_string_list = []
            for i in range (0, len(string)):
                character_list.append(string[i])
            sorted_string_list = sorted(character_list,key=(lambda x: x.upper()))
            for i in range(0, int(len(sorted_string_list)),2):
                final_sorted_string_list.append("".join(sorted(sorted_string_list[i] + sorted_string_list[i+1])))
            genotype_offspring.append("".join(final_sorted_string_list))
#def print_genotype():
#    to_print = int(input("Press 1 to print, 2 to not print"))
#        row1 = (" " * len(genotype1) + "|")*len(possible_genotype_list1)
#        row2 = " "*len(genotype1) + "|"
#        for i in range(0, len(possible_genotype_list1)):
#            row2 += possible_genotype_list1[i] + " | "
        
#        print(row1)
#        print(row2)
def find_percentages():
    genotype_list = []
    genotype_frequency = []
    i = 0
    list_length = len(genotype_offspring)
    while list_length>0:
        genotype = genotype_offspring[i]
        genotype_list.append(genotype_offspring[i])
        genotype_frequency.append(genotype_offspring.count(genotype_offspring[i]))
        while genotype_frequency.count(genotype) > 0:
            genotype_offspring.remove(genotype)
            list_length-=1
            print(z)
            print(genotype_offspring.count(genotype))
        i+=1
        print(genotype_list)
        print(genotype_frequency)

        

    
        
                
    

# TESTING............
get_all_combinations(genotype1, split_genes_list1, possible_genotype_list1)
get_all_combinations(genotype2, split_genes_list2, possible_genotype_list2)
get_all_possible_offspring_genotypes()
print(genotype_offspring)
find_percentages()






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
