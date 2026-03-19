#NAME:SAMSON NYAGA  AIIM/01403/2024
#Date:19/03/2026
#Description: string reversal and character frequency

#user_input string
user_input = input("Enter string:  ")

#prints error if user_input is empty
if user_input == "":
    print("Error: NO user_input")
else:
    print("=== STRING REVERSAL ===")
     
 #String Reversal Techniques
 #method 1: Slicing Method    
    reverse_slicing = user_input[::-1]
    print(f"slicing method: {reverse_slicing}")

#method 2: loop method
    reverse_loop= ""
    for char in user_input:
        reverse_loop = char + reverse_loop
    print(f"loop method: {reverse_loop}")

#character frequency count
    print("===CHARACTER FREQUENCY===")

#using Dictionary count method
    def dictionary_count(user_input):
        frequency = {}
        for char in user_input:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        return frequency
    

    count_result=dictionary_count(user_input)
    print ("charcter | count")
    print("-----------")

#display results in formatted table
    for char in sorted(count_result):
        print(f"'{char}'   | {count_result[char]}")

#total number of characters
    print("total character:", len(user_input))    
    print("unique characters:", len(count_result))

