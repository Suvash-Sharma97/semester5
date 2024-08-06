import csv

with open('/home/suvash/Desktop/python/reviews/test.csv', 'r') as file:
    reader = csv.reader(file)


    with open('/home/suvash/Desktop/python/reviews/test_write.csv', 'w') as f:

        writer = csv.writer(f)

        for line in reader:
            writer.writerow(line)