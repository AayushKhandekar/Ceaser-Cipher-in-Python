def encode(string, key):
    
    encodedString = '' 
    for i in string:
        x = ord(i)      
        if i.isupper():
            if key + x > 90 and x!= 32:
                x = x + key - 26 
            elif x != 32:
                x = x + key
        else:
            if key + x > 122 and x != 32:
                x = x + key - 26 
            elif x != 32:
                x = x + key
        encodedString += chr(x)
    print("Encoded String : ", encodedString)

# Decoding error needs to be solved!
# def decode(string, key):
    
#     decodedString = ''
#     for i in string:
#         x = ord(i)
#         if i.isupper():
#             if abs(x - key) < 65 and x!= 32:
#                 x = x - key + 26 
#             elif x != 32:
#                 x = x - key
#         else:
#             if key + x < 97 and x != 32:
#                 x = x + key - 26 
#             elif x != 32:
#                 x = x + key
#         decodedString += chr(x)
#     print("Decoded String : ", decodedString)

def switch(choice, string, key):
    if choice == 1:
        encode(string, key)
    # elif choice == 2:
        # decode(string, key)

if __name__ == "__main__":
    
    string = input("Enter a String : ")
    key = int(input("Enter a Key : "))    
    choice = int(input("1. Encode \n2. Decode \n"))
    switch(choice, string, key)
