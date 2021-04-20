# This is a python program calculating digits of the fibonacci sequence.
# Users can input an index and find the fibonacci's number attached to it.
from time import sleep

index = [i for i in range(1, 30000+1)]
old_number = 1
new_number = 1
numfibo = int()
fibonacci = {}

for i in index:
    numfibo = old_number + new_number
    fibonacci.update({i: numfibo})
    old_number = new_number
    new_number = numfibo

print(fibonacci)
