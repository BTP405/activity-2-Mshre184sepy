#4
#Write a Python function printStats(t) which retrives data in a text file t which reads in lines of numbers. For each line read in, the function must call a decorator function which prints
#the numbers read
#the count of the numbers read
#the average of the numbers
#the maximum of the numbers'''
def stats_decorator(func):
    def wrapper(line):
        numbers = list(map(float, line.strip().split()))
        count = len(numbers)
        average = sum(numbers) / count
        maximum = max(numbers)


        print(f"Numbers read: {numbers}")
        print(f"Count of numbers: {count}")
        print(f"Average of numbers: {average:.2f}")
        print(f"Maximum of numbers: {maximum}")

        return func(line)

    return wrapper

@stats_decorator
def process_line(line):
    pass

def printStats(t):
    #Retrieves data from a text file t and calls a decorator function for each line."""
    with open(t, 'r') as file:
        for line in file:
            process_line(line)

#testing the code
text_file = 'numbers.txt'
printStats(text_file)

