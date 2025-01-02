import csv

a = []
with open('finds.csv') as csfile:
    reader = csv.reader(csfile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes = len(a[0]) - 1

print(["?"] * num_attributes)
print(["0"] * num_attributes)

hypothesis = a[0][:-1]
for i in range(len(a)):
    if a[i][num_attributes] == "Yes":
        for j in range(num_attributes):
            if a[i][j] != hypothesis[j]:
                hypothesis[j] = '?'
    print(i + 1, hypothesis)

print(hypothesis)