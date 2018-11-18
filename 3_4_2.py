with open('c:\\temp\\dataset_3363_2.txt') as inf:
    s1 = inf.readline()

m =''
r=''
for i in range(len(s1)):
    if s1[i].isdigit() and s1[i+1].isdigit():
        r+= s1[i-1]*int(s1[i]+s1[i+1])
    elif s1[i].isdigit() and not s1[i-1].isdigit():
        r+= s1[i-1]*int(s1[i])
print(r)
        
        
