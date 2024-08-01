#algorithm to fond the sum of a given set of numbers
s=5
add=0
for i in range(1,s):
    add=add+i
print(add)

#sequential search algorithm
def seq_search(arr,ele):
    pos=0
    found=False
    while pos<len(arr) and not found:
        if arr[pos]==ele:
            found=True
        else:
            pos+=1
    return found
print(seq_search([1,2,3,4,5,6,78,9],2))

#hellow world










def s_search(arr,num):
    for i in arr:
        if num==arr[i]:
            return True
        else:
            return False
print(s_search([1,2,3,4,5],5))