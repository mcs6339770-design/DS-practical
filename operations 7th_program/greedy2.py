n = int(input("Enter number of items: "))

items = []

for i in range(n):

    weight = int(input("Enter weight: "))
    value = int(input("Enter value: "))

    ratio = value / weight

    items.append((ratio, weight, value))

capacity = int(input("Enter knapsack capacity: "))

items.sort(reverse=True)

profit = 0

for ratio, weight, value in items:

    if capacity >= weight:
        capacity -= weight
        profit += value

        print("Selected item:", weight, value)

    else:
        fraction = capacity / weight
        profit += value * fraction

        print("Fraction selected:", fraction)

        break

print("Maximum Profit =", profit)