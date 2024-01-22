# make a def function 
def similarity_checker(numbers):
    first_num = numbers[0]
    second_num = numbers[-1]

    # make an if statement
    if first_num != second_num:
        return False
    else:
        return True
    
# declare a list of number
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]   

# print the numbers_x given
print(f"Given lists: {numbers_x}")
print("result is", similarity_checker(numbers_x))

