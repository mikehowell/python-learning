credit_card = int(input("Please enter a credit card number to check: "))
credit_card_length = len(str(credit_card))

credit_card_checksum = 0

if credit_card_length % 2 == 0:
    for i in range(1, credit_card_length + 1):
        if i % 2 != 0:
            credit_card_checksum += 2 * int(str(credit_card)[i - 1])
        else:
            credit_card_checksum += int(str(credit_card)[i - 1])
else:
    for i in range(1, credit_card_length + 1):
        if i % 2 == 0:
            credit_card_checksum += 2 * int(str(credit_card)[i - 1])
        else:
            credit_card_checksum += int(str(credit_card)[i - 1])

if credit_card_checksum > 9:
    credit_card_checksum -= 9

if credit_card_checksum % 10 == 0:
    print("Valid Credit Card Number")
else:
    print("Invalid Credit Card Number")

