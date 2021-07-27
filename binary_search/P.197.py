n = int(input())
store_array = list(map(int,input().split()))
store_array.sort()
m = int(input())
customer_array = list(map(int,input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end )//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1
    return None




for i in customer_array:

    result = binary_search(store_array,i,0,n-1)
    if result != None:
        print('yes ')
    else:
        print('no ')
