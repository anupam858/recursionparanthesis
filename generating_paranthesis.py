def generate_paranthesis(list_of_sequences, left, right,sequence,c):
    
    if left<0 or right < left:
        return(0)
    
    if left==0 and right == 0:
        
        list_of_sequences.append(sequence)
        return 0
        
    else:
        
        if(left>0):
            
            sequence = sequence[:c] + "(" + sequence[c+1 : ]
            
            generate_paranthesis(list_of_sequences, left-1, right, sequence,c+1)
            
            
        if(right>left):
            
            sequence = sequence[:c] + ")" + sequence[c+1 : ]
            generate_paranthesis(list_of_sequences, left, right-1, sequence,c+1)
            
            
            
count = int(input())
l = []
generate_paranthesis(l,count, count, "#"*count*2,0)
print(l)
        
        
        
    
