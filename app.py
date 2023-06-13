import csv


def trade(path: str) -> float:
    capital = 500
    purchasePrice = 0
    takeProfit = 100
    amount = 0
    profit = 0
    actualPrice = 0
    delta = 0
    with open(path, 'r', newline='') as file:
        reader = csv.reader(file)
        for price in reader:
            actualPrice = float(price[4])
            print(actualPrice)
            if amount == 0:
                amount = capital/actualPrice
                purchasePrice = actualPrice
                capital = 0
            delta = amount*actualPrice - purchasePrice*amount
            if delta < 0:
                print(delta)
            elif delta > 0:
                print("+"+str(delta))
            if delta >= takeProfit:
                amount = 0
                capital = amount*actualPrice - delta
                profit += delta
    return profit


def main():
    print(trade("1.csv"))


if __name__ == "__main__":
    main()
