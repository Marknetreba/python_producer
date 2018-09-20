import csv
import socket


def main():
    with open('./orders.csv', mode='w') as file:
        orders = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        orders.writerow(["sneakers", "100", "1994-09-19", "wear", "1.2.4.0/22"])
        orders.writerow(["hat", "92", "2012-02-14", "wear", "1.2.8.0/21"])
        orders.writerow(["macbook", "1200", "2012-03-14", "electronics", "1.2.16.0/20"])
        orders.writerow(["socks", "10", "2017-02-14", "men's footwear", "1.2.32.0/19"])
        orders.writerow(["basketball ball", "150", "2017-02-14", "sports", "1.32.192.0/23"])
        orders.writerow(["spoon", "5", "2012-03-14", "kitchen", "1.32.194.0/24"])
        orders.writerow(["book", "300", "2015-07-08", "science", "1.32.195.0/24"])
        orders.writerow(["ring", "450", "2015-07-08", "jewellery", "1.32.196.0/24"])
        orders.writerow(["macbook", "1200", "2012-04-14", "electronics", "1.32.197.0/24"])
        orders.writerow(["jersey", "50", "2012-05-14", "sports", "1.32.198.0/23"])
        orders.writerow(["sneakers", "100", "1994-08-19", "wear", "1.32.224.0/21"])
        orders.writerow(["hat", "92", "2012-02-18", "wear", "1.32.232.0/21"])
        orders.writerow(["jersey", "70", "2012-05-14", "sports", "1.32.240.0/20"])
        orders.writerow(["macbook", "1200", "2012-03-14", "electronics", "1.33.0.0/16"])
        orders.writerow(["socks", "10", "2017-02-14", "men's footwear", "1.34.0.16/28"])
        orders.writerow(["basketball ball", "150", "2017-02-14", "sports", "1.34.0.32/27"])
        orders.writerow(["spoon", "5", "2012-03-14", "kitchen", "1.34.0.64/26"])

    nc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    nc.connect(('localhost', 41414))
    path = './orders.csv'

    with open(path) as f:
        for line in f:
            out = line.encode('utf-8')
            print('Sending line',line)
            nc.send(out)


if __name__ == '__main__':
    main()
