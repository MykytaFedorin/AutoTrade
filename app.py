import csv

capital = 500
purchasePrice = 0
takeProfit = 20
amount = 0
profit = 0
actualPrice = 0
delta = 0


def printStatus():
    global actualPrice, delta
    print("actPr ", actualPrice, end=' ')
    print("amnt ", amount, end=' ')
    print("cptl ", capital, end=' ')
    print("pP ", purchasePrice, end=' ')
    print("prof ", profit, end=' ')
    print("delta ", end=' ')
    if delta < 0:
        print(delta)
    elif delta > 0:
        print("+"+str(delta))
    else:
        print(delta)


def sale():
    print("sale")
    global amount, capital, profit
    capital = amount*actualPrice - delta
    amount = 0
    profit += delta


def buy():
    print("bought")
    global amount, purchasePrice, capital
    amount = capital/actualPrice
    purchasePrice = actualPrice
    capital = 0


def getPrices():
    res = []
    for i in range(1, 6):
        with open(str(i)+".csv", 'r', newline='') as file:
            reader = csv.reader(file)
            res = res + [float(price[4]) for price in reader]
    return res


def trade():
    global amount, capital, purchasePrice, profit, actualPrice, delta
    prices = getPrices()
    for price in prices:
        printStatus()
        actualPrice = price
        if amount == 0:
            buy()
        delta = amount*actualPrice - purchasePrice*amount
        if delta >= takeProfit:
            sale()


def main():
    trade()
    print(profit)


if __name__ == "__main__":
    main()
