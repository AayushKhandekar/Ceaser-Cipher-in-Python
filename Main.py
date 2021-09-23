def encode(string, key):
    
    encodedString = '' 
    for i in string:
        x = ord(i) 
        # Upper Case      
        if i.isupper():
            if key + x > 90 and x!= 32:
                x = x + key - 26 
            # Space 
            elif x != 32:
                x = x + key
        # Lower Case 
        else:
            if key + x > 122 and x != 32:
                x = x + key - 26 
            # Space 
            elif x != 32:
                x = x + key
        encodedString += chr(x)
    print("Encoded String : ", encodedString)

def decode(string, key):
    
    decodedString = ''
    for i in string:
        x = ord(i)
        # Upper Case 
        if i.isupper():
            if (x - key) < 65 and x != 32:
                x = x - key + 26
                print(x)
            # Space
            elif x != 32:
                x = x - key
        # Lower Case 
        else:
            if (x - key) < 97 and x != 32:
                x = x - key + 26 
            # Space
            elif x != 32:
                x = x - key
        decodedString += chr(x)
    print("Decoded String : ", decodedString)

# Switch Case
def switch(choice, string, key):

    if choice == 1:
        encode(string, key)
    elif choice == 2:
        decode(string, key)

if __name__ == "__main__": 

    string = input("Enter a String : ")
    key = int(input("Enter a Key : "))  

    # Modifying 'key' into values less than 26
    # Key values above 26 follow a circular pattern and again start from 1.
    # To simplify, key = 1 is same as key = 27
    key = key % 26  
    choice = int(input("1. Encode \n2. Decode \n"))
    switch(choice, string, key)
