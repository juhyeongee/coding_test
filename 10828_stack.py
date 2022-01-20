import re
stack = []

input_ = input("Order me \n")

push_pattern = re.compile('(\D*)(\d*)?')
m = push_pattern.search(input_)
# == m = re.match('push \D*', input_)
order = m.group(1)
push_num = m.group(2)

print(order)

