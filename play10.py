uma,de=map(str,input().split())
uma=list(uma)
de=list(de)
kow=0
for f in range(0,len(uma)):
        if(uma[f]!=de[f]):
            kow=kow+1
if(kow==1):
    print("yes")
else:
    print("no")
