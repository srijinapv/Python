#!/Users/srijina/opt/miniconda3/bin/python

starting_number = int(input('Enter Starting range : '))
ending_number = int(input('Enter Ending range : '))
odd_numbers = []
for value in range(starting_number, ending_number+1):
    if value % 2 != 0:
        
        odd_numbers.append(value)
print(odd_numbers)
count_odd_number = len(odd_numbers)
print(count_odd_number)
largest_odd_number = odd_numbers[-1]
print(largest_odd_number)