#1. Student Marks Analyzer

import numpy as np

marks = []

n = int(input("How many students?:"))

for i in range(n):
  mark = float(input(f"Enter marks of student {i+1}:"))
  marks.append(mark)

marks_array = np.array(marks)

print("\n Student Marks Analysis")
print("------------")

print("Marks:", marks_array)
print("Total Marks:", np.sum(marks_array))
print("Average Marks:", np.mean(marks_array))
print("Highest Marks:", np.max(marks_array))
print("Lowest Marks:", np.min(marks_array))
print("Sorted Marks", np.sort(marks_array))