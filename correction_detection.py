import random
import math
n=3
def gen_code(): #generates random bit codes to be sent
    code=[]
    for i in range(n):
        code.append(random.randint(0,1))
    return code

def gen_repeated_code(code_sent): #converts sent bit codes to repeated codes(usually repeated in 3s)
    repeated_format,x = [],[]
    for i in code_sent:
        x.append(i)
        repeated_format.append(x * 3)
        x.clear()
    return repeated_format

def error_generator(code_repeated): #flips bits to complements based on probability using the random function
    probability = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    for i in  code_repeated:
        for x in range(3):
            random_no = random.randint(0, 10)
            p_selector = probability[random_no]
            if p_selector > 0.2:
                continue
            else:
                if i[x] is 0:
                    i[x] = 1
                else:
                    i[x] = 0
    return  code_repeated

def error_correction(errors): #Uses repetition technique to correct the flipped bits
    code_correction,x,y=[],[],[]
    for i in errors:
        for l in range(3):
            if i[l] == 0:
                x.append(0)
            elif i[l] == 1:
                y.append(1)
            else:
                print("invalid bit!!")
        if len(x) > len(y):
            for l in range(3):
                i[l] = 0
        else:
            for l in range(3):
                i[l] = 1
        for l in range(3):
            code_correction.append(i[l])
        x.clear()
        y.clear()
    return code_correction

def transcode(corrected_code): #converts the bits back to their unrepeated formats(this is the final received bit code)
    code_received = []
    div = len(corrected_code) // 3 # the // symbols makes sure the division returns an int value
    t = 0
    for i in range(div):
        code_received.append(corrected_code[t])
        t += 3
    return  code_received

"""This is basic function calls just like we did in c++"""
sent_code=gen_code()
print("Sent code: ",sent_code)
print("Analysing code...")
repeated_code=gen_repeated_code(sent_code)
print("Repeated code: ",repeated_code)
print("Transmitting data...")
error_code=error_generator(repeated_code.copy())
print("Error detected!!!")
print("Error code: ",error_code)
print("Correcting error...")
corrected_repeated_code=error_correction(error_code)
print("Corrected code: ",corrected_repeated_code)
received_code=transcode(corrected_repeated_code)
print("Received code: ",received_code)
print("Transmission complete!!!")

"""Limitation of repetiton method is that when consecutive bits are flipped/altered,
the algorithm tends to make mistakes since its method is based on detecting the majority bits"""