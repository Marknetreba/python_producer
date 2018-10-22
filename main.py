import csv
import random
from datetime import datetime
import socket


def main():
    year = random.randint(1950, 2018)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    hours = random.randint(0, 23)
    minutes = random.randint(0, 59)
    path = './orders.csv'

    with open(path, mode='w') as file:
        for i in range(6000):
            orders = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            orders.writerow(["sneakers", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "wear", random_ip()])
            orders.writerow(["hat", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "wear", random_ip()])
            orders.writerow(["macbook", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "electronics", random_ip()])
            orders.writerow(["socks", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "men's footwear", random_ip()])
            orders.writerow(["basketball ball", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "sports", random_ip()])
            orders.writerow(["spoon", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "kitchen", random_ip()])
            orders.writerow(["book", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "science", random_ip()])
            orders.writerow(["ring", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "jewellery", random_ip()])
            orders.writerow(["macbook", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "electronics", random_ip()])
            orders.writerow(["jersey", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "sports", random_ip()])
            orders.writerow(["sneakers", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "wear", random_ip()])
            orders.writerow(["hat", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "wear", random_ip()])
            orders.writerow(["jersey", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "sports", random_ip()])
            orders.writerow(["macbook", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "electronics", random_ip()])
            orders.writerow(["socks", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "men's footwear", random_ip()])
            orders.writerow(["basketball ball", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "sports", random_ip()])
            orders.writerow(["spoon", random.randint(1, 1000), datetime(year, month, day, hours, minutes), "kitchen", random_ip()])

    nc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nc.connect(('localhost', 41414))
    path = './orders.csv'

    with open(path) as f:
        for line in f:
            out = line.encode('utf-8')
            print('Sending line', line)
            nc.send(out)


def random_ip():
    octets = []
    for x in range(4):
        octets.append(str(random.randint(0, 255)))
    return '.'.join(octets)


if __name__ == '__main__':
    main()
