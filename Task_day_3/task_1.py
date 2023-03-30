# 1. Write a program to reverse a number without using any inbuit function.

num = 2002
final_num = 0
nagative = False

if num <0:
    num = -num                       
    nagative = True

while num != 0:
        final_num = (final_num * 10) + (num % 10)
        num = num // 10

if nagative:
        final_num = -final_num
print(final_num)



# Approch 2:
def reverse(given_input):
        string = str(given_input)
        result = ""
        if string[0] == "-":
            result = "-"+string[:0:-1]
        else:
            result = string[::-1]
        if isinstance(given_input, int):
            return int(result)
        elif isinstance(given_input,str):
            return result
        elif isinstance(given_input,float):
            return float(result)
print(reverse(20.002))
                


# Approch 3:

num = -00.055
con_str = str(num)
out_put = ""
if con_str[0] == "-":
        out_put+="-"

length = len(con_str)-1

while length>=0:
    if con_str[length]!="-":
        out_put += con_str[length]
        length-=1
        continue
    length-=1
print(out_put)
        