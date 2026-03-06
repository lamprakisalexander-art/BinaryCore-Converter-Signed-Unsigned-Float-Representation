def manual_binary_change(number):
    if number == 0:
        return 0
    # if the number is 0 then its going to also be 0 in binary form
    temp = number
    #temp is a temporary value that represents the number
    binary_number = ""
    #binary number represents the value that the binary number will be stored at and its a string since we append 0s and 1s into the value
    while temp > 0:
        remainder = temp % 2 # we need to find the mod of temp with 2 like the number with 2, lets say 4, 4mod2 is 0, or 5, 5mod2 is 1
        binary_number = str(remainder) + binary_number #you need to add the binary after because you want the MSB to be the first digit
        temp = temp // 2    # we want the result in int like 5/2 is 2.5 but we want 2 so we can continue with the mod2 and the division again
    return binary_number


print("Give 2 numbers and see how they are in binary form")
#The user will first give numbers type int
x1 = int(input("Enter x \n"))
#the user inputs the 1rst number type int
print(f"The number you have given is: {x1} and is: {type(x1)}")
print(f"Your first number in binary form is: {manual_binary_change(x1)}\n")
y1 = int(input("Enter y \n"))
#the user inputs the second number type int
print(f"The number you have given is: {y1} and is: {type(y1)}")
print(f"Your second number in binary form is: {manual_binary_change(y1)}\n")

print("Now enter float numbers\n")

def float_to_binary(number, loop = 8):
    # firstly we need to divide the number between the int and the float part
    # example: 3.7 between 3 and 7 or 89.23 between 89 and 23
    integer_number = int(number) #divide the int part of the number
    float_number = number - integer_number #find the remaining part of the number and seperate it
    binary_integer = manual_binary_change(integer_number)
    #if there is no float part like lets say 3.0 or 45.0
    if float_number == 0:
        return binary_integer

    number_remainder = ""
    while float_number > 0 and loop > 0:
        float_number *= 2
        bit = int(float_number)
        number_remainder += str(bit)
        float_number -= bit
        loop -= 1
    return f"{binary_integer}.{number_remainder}"


x2 = float(input("Enter a float number: "))
#the user inputs the 1rst number type float
print(f"The number you have given is: {x2} and is: {type(x2)}")
print(f"Your first float number in binary form is: {float_to_binary(x2)}\n")
y2 = float(input("Enter another float number: "))
#the user inputs the second number type float
print(f"The number you have given is: {y2} and is: {type(y2)}")
print(f"Your second float number in binary form is: {float_to_binary(y2)}\n")

x = int(input("Give a number (preferably negative) \n"))
bits = int(input("Give how many bits you want your number to have:  \n"))


def negative_numbers(number, bits):
    #with n bits you can represent (2**n -1) -1 positive numbers and -2**(n -1) negative numbers, if you dont have enough bits to represent it, an overflow error occurs
    # upper bound
    max_bit = 2 ** (bits - 1) - 1
    # lower bound
    min_bit = -(2 ** (bits - 1))
    #checking for overflow
    if number < min_bit or number > max_bit:
        return f"Error, due to overflow, the number {number} is out of range from ({min_bit}, {max_bit})\n"

    if number >= 0:
        binary = manual_binary_change(number)
        #if the number is positive then its going to return the number with the bits the user has given to represent it
        return f"The number is: {binary.zfill(bits)}\n"
    #if the number is negative we need to find the absolute of the number like -5 to 5 and then change it into binary form
    positive_bin = manual_binary_change(abs(number)).zfill(bits)
    #1 complement, we change every bit like an xor, every 0 becomes 1 and every 1 becomes 0
    ones_complement = "".join(['1' if b == '0' else '0' for b in positive_bin])
    #complement 2, we basically add 1 to the 1 complement or we leave the main number as it is until we spot the 1rst 1, and then we reverse the numbers/ change them like 0 to 1 or 1 to 0
    twos_complement = bin(int(ones_complement, 2) + 1)[2:].zfill(bits)

    return f"The negative number represented in complement 2 is: {twos_complement[-bits:]}\n"

#call the function and add the parameters of the bitwidth the user has given and the number
print(negative_numbers(x, bits))