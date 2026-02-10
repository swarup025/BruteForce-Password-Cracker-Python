import itertools
import string
import time

print("Hey, I’m testing and cracking weak passwords as part of ethical security assessments to help improve system security")
chars = string.printable

password = input("enter a password : ")

max_length = 10 # 

start_time = time.time()

for length in range(1, max_length + 1):
    for combination in itertools.product(chars, repeat=length):
        candidate = "".join(combination)
        print("Trying password:", candidate)
        if candidate == password:
            end_time = time.time()
            print("Hey 😄 I think I found your password!:", candidate)
            time_taken = end_time - start_time
            print("Time taken:", time_taken, "seconds")
            raise SystemExit
        

