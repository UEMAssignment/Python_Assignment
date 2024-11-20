# Reverse the elements in an array of integers without using a second array.

arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))

left = 0  
right = len(arr) - 1  

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print("Reversed array:", arr)