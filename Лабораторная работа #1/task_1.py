numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

missing_index = 4
num_sum = sum(numbers[:missing_index] + numbers[missing_index+1:])
num_amount = len(numbers)
num_average = num_sum / num_amount

numbers[4] = num_average

print("Измененный список:", numbers)
