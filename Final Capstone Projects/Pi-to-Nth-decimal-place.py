from decimal import Decimal, setcontext, Context

# print(getcontext())

while True:
    decimal_places = int(
        input(
            "Please enter the number of decimal places (less than 51) to display Pi to: "
        )
    )
    if decimal_places > 50:
        print("Please choose a lower number of decimal places.")
    else:
        break

precision_context = Context(prec=decimal_places + 1)
setcontext(precision_context)
print(
    "Pi to {0} decimal places is {1}".format(
        decimal_places, (Decimal("22") / Decimal("7"))
    )
)

# import math

# while True:
#     decimal_places = int(
#         input(
#             "Please enter the number of decimal places (less than 15) to display Pi to: "
#         )
#     )
#     if decimal_places > 15:
#         print("Please choose a lower number of decimal places.")
#     else:
#         break

# print(
#     "Pi to {0} decimal places is {1}".format(
#         decimal_places, (round(math.pi,decimal_places))
#     )
# )
