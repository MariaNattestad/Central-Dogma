# from the intro materials

def list_to_str(mylist):
    mystring = str()
    for item in mylist:
        mystring+=item
    return mystring
   
   
# from Project 2

def reverse_complement(DNA):
    DNA = DNA.upper()
    
    complement = str()
    
    complement_dictionary = {
    "A":"T", 
    "T":"A", 
    "G":"C",
    "C":"G"
    }
    
    for base in DNA:
        complement+=complement_dictionary.get(base,"N")
    
    revcomp = complement[::-1]
    return revcomp


def DNA_to_RNA(DNA):
    DNA=DNA.upper()
    RNA = str()
    for i in xrange(len(DNA)):
        if DNA[i]=="T":
            RNA+="U"
        else:
            RNA+=DNA[i]
    return RNA
    
 
def RNA_to_protein(RNA,frame):
    decoder = {'ACC': 'T', 'GCA': 'A', 'ACA': 'T', 'ACG': 'T', 'GUU': 'V', 
    'AAC': 'N', 'AGG': 'R', 'UGG': 'W', 'GUC': 'V', 'AGC': 'S', 'AUC': 'I', 
    'AGA': 'R', 'AAU': 'N', 'ACU': 'T', 'GUG': 'V', 'CAC': 'H', 'AAA': 'K', 
    'CCG': 'P', 'CCA': 'P', 'AGU': 'S', 'AAG': 'K', 'GGU': 'G', 'UCU': 'S', 
    'GCG': 'A', 'CGA': 'R', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 
    'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 'GGA': 'G', 'CCC': 'P', 'GGC': 'G', 
    'GAA': 'E', 'UAA': '*', 'UCC': 'S', 'UAC': 'Y', 'GAC': 'D', 'UGU': 'C', 
    'AUA': 'I', 'CUU': 'L', 'UCA': 'S', 'AUG': 'M', 'CGC': 'R', 'CUG': 'L', 
    'GAG': 'E', 'AUU': 'I', 'CAU': 'H', 'CUA': 'L', 'GCC': 'A', 'CAA': 'Q', 
    'UUU': 'F', 'CGU': 'R', 'GUA': 'V', 'UGC': 'C', 'GCU': 'A', 'UAG': '*', 
    'CUC': 'L', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}

    protein = []
    for i in xrange(frame,len(RNA)-2,3):
        codon=RNA[i:i+3]
        protein.append(decoder.get(codon,"?"))
    return list_to_str(protein)

def find_coding_regions(protein):
    
    ORFs=[]
    started = False
    start_indx=-1
    for i in xrange(len(protein)):
        aa=protein[i]    # aa means amino acid
        
        #if the protein is started
        if started==True: 
            if aa=='*':
                started=False
                ORFs.append(protein[start_indx:i])
        # if the protein hasn't started
        elif aa=="M":
            started = True
            start_indx=i
            
    
    return ORFs
    
def translate(DNA):
    DNA_forward=DNA
    DNA_reverse=reverse_complement(DNA)
    RNA_forward=DNA_to_RNA(DNA_forward)
    RNA_reverse=DNA_to_RNA(DNA_reverse)
    
    allproteins=[]
    for frame in xrange(3):
        allproteins.append(RNA_to_protein(RNA_forward,frame))
        allproteins.append(RNA_to_protein(RNA_reverse,frame))
    
    all_ORFs=[]
    for protein in allproteins:
        all_ORFs.append(find_coding_regions(protein))
        
    return all_ORFs

def translate_only_longest_ORF(DNA):
    proteins=translate(DNA)

    lengths=[]
    for i in xrange(len(proteins)):
        if len(proteins[i]) < 1:
            lengths.append(0)
        else:
            lengths.append(len(proteins[i][0]))

    import numpy as np 
    lengths=np.array(lengths)
    if max(lengths) > 0:
        return proteins[np.argmax(lengths)][0]
    else:
        return "No open reading frames"









