'''
1. Create a function that returns the protein ID of the shortest protein. 
2. Create a function that receives a gene name and returns the protein ID. 
3. Create a function that receives protein ID and returns the PDB IDs. If the protein 
doesn’t have PDBs reported, the function should return False. 
4. Create a function that prints the proteins IDs and the number of reported genes. The 
list should be sorted by the number of genes. 
5. Create a function that prints a list of pairs of all the reported combinations of genes 
and PDBs
'''


text = """Entry	Gene names	Cross-reference (PDB)	Length
O95813	CER1 DAND4		267
Q8N907	DAND5 CER2 CKTSF1B3 GREM3 SP1		189
O60565	GREM1 CKTSF1B1 DAND2 DRM PIG2		184
P41271	NBL1 DAN DAND1	4X1J;	181
Q96S42	NODAL	4N1D;	347
Q15465	SHH	3HO5;3M1N;3MXW;	462"""


#Building dictionary to store dataset
protdict = {}
text = text.split('\n')
protein_lengths = []
for line in text[1:]:
    entries = line.split('\t')
    protein = entries[0]
    gene_names = entries[1].split(' ')
    xref_pdb_ids = entries[2].split(';')
    protein_length = int(entries[3])
    protein_lengths.append(protein_length)
    protdict[protein] = [gene_names, xref_pdb_ids, protein_length]

#Question1

def longestProtein():
    result = []
    #Returns the longest protein id(s)
    max_len = max(protein_lengths)
    for protein in protdict.keys():
        if protdict[protein][2] == max_len:
            result.append(protein)
    return ' '.join(result)

#print(longestProtein())

#Question2
def getProtfromGene():
    gene = input('Enter protein name: ')
    for protein in protdict.keys():
        if gene in protdict[protein][0]:
            return protein

#print(getProtfromGene())

#Question3
def getPDBfromProtein():
    proteinid = input('Enter protein id: ')
    result = protdict[proteinid][1]
    if len(result[0]) == 0:
        return False
    else:
        return ' '.join(result)

#print(getPDBfromProtein())

#Question4
def sortProtByGeneCount(): 
    prot_gene_counts = []
    for protein in protdict:
        prot_gene_counts.append((len(protdict[protein][0]), protein))
    
    for prot in sorted(prot_gene_counts):
        print(prot[1], prot[0])

#sortProtByGeneCount() 

#Question5
def genePDBpairs():
    for protein in protdict:
        #Returns gene/pdb pairs
        genes = protdict[protein][0]
        xref_pdb_ids = protdict[protein][1]
        for gene in genes:
            for pdbid in xref_pdb_ids:
                if pdbid != '':
                    print(gene, pdbid)
#genePDBpairs()
