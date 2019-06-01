"""
How to check if a credit card is valid:
http://www.tech-faq.com/how-to-determine-if-i-have-a-valid-credit-card-number.html
"""

credit_card = input("Please enter a credit card number to check: ")
credit_card_length = len(credit_card)
even_digits = credit_card[1::2]
odd_digits = credit_card[::2]

credit_card_checksum = 0

if credit_card_length % 2 == 0:
    for num in even_digits:
        credit_card_checksum += int(num) * 2

    for num in odd_digits:
        credit_card_checksum += int(num)
else:
    for num in even_digits:
        credit_card_checksum += int(num)

    for num in odd_digits:
        credit_card_checksum += int(num) * 2

if credit_card_checksum > 9:
    credit_card_checksum -= 9

print("check sum = : {}".format(credit_card_checksum))

if credit_card_checksum % 10 == 0:
    print("Valid Credit Card Number")
else:
    print("Invalid Credit Card Number")

