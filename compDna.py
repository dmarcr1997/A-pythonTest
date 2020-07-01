def split(word): 
    return [char for char in word]  
        
def DNA_strand(dna):
    # code here
    dna_array = split(dna)
    print(dna_array)
    comp_strand = []
    for x in dna_array:
      
      if x == "A": 
          comp_strand.append("T")
                
      elif x == "T":
          comp_strand.append("A")
                
      elif x == "C": 
          comp_strand.append("G")
              
      elif x == "G": 
          comp_strand.append("C")
    return ''.join(comp_strand)


print(DNA_strand("ATTGC"))
print(DNA_strand("GTAT"))
