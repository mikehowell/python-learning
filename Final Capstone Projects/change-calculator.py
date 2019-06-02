from decimal import Decimal

cost_of_item = Decimal(input("Please enter the amount of the item: "))
cash_given = 0

while cost_of_item > cash_given:
    cash_given = Decimal(input("Please enter the cash paid: "))
    if cash_given < cost_of_item:
        print("You are short by {}".format(cost_of_item - cash_given))
    else:
        break

change = cash_given - cost_of_item
print("You change is {}".format(change))

monetary_denominations_dollars = [100, 50, 20, 10, 5, 2, 1]
monetary_denominations_cents = [50, 20, 10]

change_breakdown_dollars = list()
change_breakdown_cents = list()

while change > monetary_denominations_dollars[-1]:
    for dollar in monetary_denominations_dollars:
        if change >= dollar:
            change_breakdown_dollars.append(dollar)
            change -= dollar

            if change == dollar:
                change_breakdown_dollars.append(dollar)
                change -= dollar

            if change == 0:
                break

if change > 0:
    change *= 100

    while change > monetary_denominations_cents[-1]:
        for cent in monetary_denominations_cents:
            if change >= cent:
                change_breakdown_cents.append(cent)
                change -= cent

                if change == cent:
                    change_breakdown_cents.append(cent)
                    change -= cent

                if change == 0:
                    break

print(
    "Change given as,\nDollars:{}\nCents:{}".format(
        change_breakdown_dollars, change_breakdown_cents
    )
)

