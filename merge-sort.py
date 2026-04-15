def merge_sort(arr):
    arr=arr.copy()
    ans=[]
    while len(arr)>0:
        min_index=0
        for i in range(1,len(arr)):
            if arr[i]<arr[min_index]:
                min_index=i
        ans.append(arr[min_index])
        print(ans)
        arr.pop(min_index)
    return ans

array=[5,2,9,1,5,6]
merge_sort(array)