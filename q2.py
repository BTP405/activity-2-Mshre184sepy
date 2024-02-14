#2
#Write a Python function graphSnowfall(t) which retrieves data from a text file t
#and displays that information in a bar chart. The file will have a single number
#on each line representing the amount of snowfall accumulation for a given day.
#Aggregate these values so that each one contributes to a particular 10 cm range.
#For example, a file containing 10 15 45 5 20 25 would have 2 between 0-10cms,
#2 between 11-20cms, 1 between 21-30cms, 0 between 31-40cms, 1 between 41-50cms.
#Use module matplotlib to plot a bar graph showing your results. The x-axis should
#show the ranges and the y-axis should show the number of occurrences in that range.

import matplotlib.pyplot as plt

def graphSnowfall(t):
    #Function to read snowfall data from the chosen file and displays it in a bar chart.
    snowfall_ranges = {'0-10cms': 0, '11-20cms': 0, '21-30cms': 0, '31-40cms': 0, '41-50cms': 0}

    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())

            # checking the range and update the count
            if 0 <= snowfall <= 10:
                snowfall_ranges['0-10cms'] += 1
            elif 11 <= snowfall <= 20:
                snowfall_ranges['11-20cms'] += 1
            elif 21 <= snowfall <= 30:
                snowfall_ranges['21-30cms'] += 1
            elif 31 <= snowfall <= 40:
                snowfall_ranges['31-40cms'] += 1
            elif 41 <= snowfall <= 50:
                snowfall_ranges['41-50cms'] += 1

    # Plotting the bar chart using matplotlib.pyplot
    ranges = list(snowfall_ranges.keys())
    counts = list(snowfall_ranges.values())

    plt.bar(ranges, counts, color='orange')
    plt.xlabel('Snowfall Range (in cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.show()

# Example usage:
text_file = 'snowfall.txt'
graphSnowfall(text_file)

