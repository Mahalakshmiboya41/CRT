arr=[1,2,3,4,2,3,4,4,5]
freq={}
for num in arr:
        freq[num]=freq.get(num,0)+1
print(freq)
maxi=max(freq,key=freq.get)
print("max freq of element:",maxi)
mini=min(freq,key=freq.get)
print("min freq of element:",mini)