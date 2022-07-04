    
#### The longest prefix

strs = ["reflower","flow","flight"]

strs.sort(key=len)
print(strs)
pref = strs[0].lower()


for i in range(0,len(strs)+1): 
    b=True
    for j in range(1,len(strs)):         
        if pref != strs[j][:len(pref)].lower():
            print(strs[j][:len(pref)].lower(),pref)
            b=False
            break
    if b==False:
        pref = pref[:len(pref)-1] if len(pref)>1 else ""
        
print(pref)    