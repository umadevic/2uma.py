um=list(input())
d1=len(um)
new=''
for l in range (0,d1,2):
    um[l],um[l+1]=um[l+1],um[l]
print(*um,sep='')
