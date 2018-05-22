import string
from random import sample

element = string.digits+string.ascii_uppercase
Coupon_list = []
i = 1
while i <= 50:
    Coupon_list.append( ''.join(sample(element,10)))
    i += 1