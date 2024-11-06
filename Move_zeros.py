def move_zeros(numbers):
    count = 0# Pointer to track the position for next non-zero element   
    for i in range(len(numbers)):#Loop that iterates over each index i in the numbers list    
        if numbers[i] != 0: # If the current element is non-zero
            numbers[i], numbers[count] = numbers[count], numbers[i]# Swap the current element with the 0 at index 'count'
            count += 1# Move 'count' pointer to the next position

numbers = [1, 2, 0, 4, 3, 0, 5, 0]
move_zeros(numbers)
for num in numbers:
    print(num, end=" ")
