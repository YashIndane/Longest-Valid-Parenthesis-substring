#Given a string containing just the characters '(' and ')', 
#find the length of the longest valid (well-formed) parentheses substring.
#LeetCode


def check(p):
    z=str(2)

    for f in p:
        if(f==z):
            x=True
        else:
            x=False
            break
    return x        



p=input("Enter your string:")

q=[]  #storing the indexes where () is found
y=""
sub_array=[]
all_comb=[]
fin_2_array=[]
fin_2_str=""




for x in range(0,len(p)-1):

    if(p[x:x+2]=="()"):
        q.append(x)
    else:
        pass

   
for g in range(1,len(q)):
    sub_array.append(str(q[g]-q[g-1]))
    # saving the diff of adjacent elements in q[]
    #in sub_array[]




   
sub_str=y.join(sub_array)

for w in range(0,len(sub_str)):
    for i in range(w+1,len(sub_str)+1):
        all_comb.append(sub_str[w:i])


       
for e in all_comb:#
    if(check(e)):
        fin_2_array.append(e)
        # check() returns true if e is composed of 
        # 2's only
    else:
        pass        

for t in fin_2_array:
    if(len(fin_2_str)<len(t)):
        fin_2_str=t
    else:
        pass
    
if(len(p)==1):
    pass
else:   
      x=len(fin_2_str)+1
      print(2*x)



    






















 

    