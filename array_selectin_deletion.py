# Description: Array selection, insertion and deletion


#create array
arr = [1,2,3,4,5,6,7,8]

print("original Array:", arr)

print("===ARRAY SELECTION===")
#ARRAY SELECTION (select the value)
print("element_1:", arr[0])
print("element_2:", arr[-1])
print("slice(2:5):", arr[2:5])

print("===ARRAY INSERTION===")
#ARRAY INSERTION(add values and position it anywhere)
x = int(input("Enter position for insertion:  "))
y = int(input("Enter value: "))

if 0 <= x <= len(arr):
    arr.insert(x, y)
    print("Array after insertion: ", arr)
else:
    print("Position Error!")

#ARRAY DELETION (removes value locared  in any position )
print("===ARRAY DELETION===")

#removes last value on array
removed_last_value = arr.pop()
print("deleted last value:", removed_last_value)
print("Array after removing last value:", arr)

#deletes value on array
value = int(input("Enter value to remove: "))
if value in arr:
    arr.remove(value)
    print("After removing value:", arr)
else:
    print("value not on Array!")
    

#clears the arr
arr.clear()
print("cleared Array():", arr)
