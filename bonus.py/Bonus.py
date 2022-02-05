#Generate list of 100 random numbers from 1-200a
import random
randomlist = random.sample(range(1,200),100)
print(randomlist)

# Calculate Variance and Standard Deviation of List
import statistics

Variance = statistics.pvariance(randomlist)
StandardDeviation = statistics.pstdev(randomlist)

# Print Data
print('Variance is: ',Variance)
print('Standard Deviation is: ',StandardDeviation)