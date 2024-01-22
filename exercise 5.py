# make a def function 
def similarity_checker(numbers):
    first_num = numbers[0]
    second_num = numbers[-1]

    # make an if statement
    if first_num != second_num:
        return False
    else:
        return True
