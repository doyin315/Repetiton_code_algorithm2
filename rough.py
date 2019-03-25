import random
n=9
def gen_code():
    code=[]
    for i in range(n):
        code.append(random.randint(0,1))
    return code

def gen_repeated_code(code_sent):
    repeated_format,x = [],[]
    for i in code_sent:
        x.append(i)
        repeated_format.append(x * 3)
        x.clear()
    return repeated_format


def error_generator(code_repeated):
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
def error_correction(errors):
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
    print('corrected' ,code_correction)
    return code_correction

def transcode(corrected_code):
    code_received = []
    div = len(corrected_code) // 3
    t = 0
    for i in range(div):
        code_received.append(corrected_code[t])
        t += 3
    print(code_received)


sent_code=gen_code()
print("Sent code: ",sent_code)
repeated_code=gen_repeated_code(sent_code)
print("Repeated code: ",repeated_code)
error_code=error_generator(repeated_code.copy())
print("Error code: ",error_code)
corrected_repeated_code=error_correction(error_code)
print("Corrected code: ",corrected_repeated_code)
transcode(corrected_repeated_code)

