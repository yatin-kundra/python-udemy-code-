import module01  # created by me
import random    # inbuild

# random module contains function that generates random numbers

rand_num = random.random()  # generates random flaoting point number between 0to 1 , 0 include and 1 not included

print(rand_num)

rand_int = random.randint(0,9)
print(rand_int)

rand_decimal_int = rand_int + rand_num
print(rand_decimal_int)

# you just need brain if you want to use it like you want

print(module01.name)