program author:

    Weihang Chen
    101084865

###############################################################################
purpose:

    particing the process of encryption and decryption
    particing the bitwise operation in C


###############################################################################
list of source files:

    encrypt.c
    decrypt.c
    bit_manipulation.h
    bit_manipulation.c
    README.txt

###############################################################################
compilation command:
    for encrypt:
        gcc -g -o encrypt encrypt.c bit_manipulation.c
        
    for decrypt:
        gcc -g -o decrypt decrypt.c bit_manipulation.c

###############################################################################
launching and operating instructions:

    by using the command:

        ./encrypt      
            -----to encode a piece of message
        
        ./decrypt
            -----to translate the encoded message into natural language

