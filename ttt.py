visa = r'^4[0-9]{12}(?:[0-9]{3})?$'
mastercard = r'^5[1-5][0-9]{14}$'
am_express = r'^3[47][0-9]{13}$'
diners_club = '^3(?:0[0-5]|[68][0-9])[0-9]{11}$'
discover = r'^6(?:011|5[0-9]{2})[0-9]{12}$'
jcb = r'^(?:2131|1800|35\d{3})\d{11}$'

cards = [visa, mastercard, am_express, diners_club, discover, jcb]

print(cards[0])