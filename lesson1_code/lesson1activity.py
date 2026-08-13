# Activity 1: Python Fundamentals

students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 90, 82, 70]
# Rounded 81.6 to 82
average = sum(scores) / len(scores)
print("The average is", average)

Alice = 85
Bob = 90
Charlie = 82
David = 70
33
if Alice > average:
    print("Alice scored higher than the average.")
else:
    print("Alice did not score higher than the average.")

if Bob > average:
    print("Bob scored higher than the average.")
else:
    print("Bob did not score higher than the average.")

if Charlie > average:
    print("Charlie scored higher than the average.")
else:
    print("Charlie did not score higher than the average.")

if David > average:
    print("David scored higher than the average.")
else:
    print("David did not score higher than the average.")

# Activity 2: Debugging Real-World Data

scores2 = [85, 90, "N/A", 70]
scores3 = [85, 90, 82, 70] # Fixed One

# 1. The program would break because 85, 90, and 70 are all integers, but "N/A" is a string.

for score in scores2:
    if score == "N/A":
        continue
    print(score)

# Activity 3: Data Cleaning with Pandas

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 90, 82, 70]
})

print(df)

# Activity 4: Mini Machine Learning Task

# Unfortunately, I do not know how to do this activity, and I will need some help with it at a later time, if possible. Sorry, and thank you!