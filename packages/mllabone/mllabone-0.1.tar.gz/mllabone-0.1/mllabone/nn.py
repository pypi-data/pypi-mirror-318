import csv
hypo = ['%', '%', '%', '%', '%', '%']

with open('trainingdata.csv') as csv_file:
    readcsv = csv.reader(csv_file, delimiter = ",")

    data = []
    print("The given training example are:\n")
    for row in readcsv:
        print(row)
        if row[len(row)-1].upper() == "YES":
            data.append(row)

print("\nThe positive examples are:\n");
for x in data:
    print(x)

hypo = ['%', '%', '%', '%', '%', '%']
print("\nThe steps of the Find-S algorithm are:\n")
print(hypo)

hypo = data[0][:-1]

print(hypo)
for i in range(1, len(data)):
    for j in range(len(hypo)):
        if hypo[j] != data[i][j]:
            hypo[j] = '?'
    print(hypo)

print("\nThe maximally specific Find-S hypothesis for the given training example is:\n");
print(hypo)
