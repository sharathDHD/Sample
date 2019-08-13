import sys
testcases=int(input())
outputs=[]
data =[]
for x in range(testcases):
    state=False
    for x in range(int(input())):
        t=input()[0]
        if (t not in data) or not state :
            data.append(t)
        elif t in data:
            state=True
    if not state:
        outputs.append('YES')
    else:
        outputs.append('NO')
        
print(outputs,sep='\n')    
