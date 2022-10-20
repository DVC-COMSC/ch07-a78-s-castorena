
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []


# ******************************
# Make your Code
# ******************************

for i in range(len(words)):
    for j in range(len(are)):
        if j == 0:
            prev_idx = 0
        else:
            prev_idx = j-1
    x = words[i].find(are[j])
    if x > 0:
       idxlst.append(words[i])  



    
        
   
      

print("the words that has 'a', 'r', 'e' in sequence", idxlst)

