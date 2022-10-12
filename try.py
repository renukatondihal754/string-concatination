import itertools as it 
res=''
s1="hehi"
s2="worldhi"
# min_lenght=len(s1) if len(s1)<len(s2) else len(s2)
# i=0
# bigger=s1 if len(s1)>len(s2) else s2
# for i in range(min_lenght):
for c1,c2 in it.zip_longest(s1,s2,fillvalue=''):
    res+=c1+c2
    # i+=1

# print(res+bigger[i:])
print(res)