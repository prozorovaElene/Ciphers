# ----------------------Index Sub Cipher----------------------


dictionary = {'a':'01', 'b':'02', 'c':'03', 'd':'04', 'e':'05', 'f':'06', 'g':'07', 'h':'08', 'i':'09'}
def encryptIndexSubstitutionCipher(text):
    y = ''
    for a in text:
        if (ord(a)-96)<10:
            y = y + dictionary[a] + ' '

        elif (ord(a)-96)>=10:
            y = y + str(ord(a)-96) + ' '
    return(y)


    
def decryptIndexSubstitutionCipher(text):
    chars = text.split()
    i = 0
    for c in chars:
        b = int(c)
        chars[i] = chr(96+b)
        i+=1    

    y = " "
    for text in chars:
        y+= text
    return(y)
 


# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}

def encryptMorseCode(text):
    z = []
    y = ''
    for a in text:
        z.append(morseCode[a]+' ')
    for b in z:
        y+=b
    return(y)   


   

def decryptMorseCode(text):
    global morseCode
    morseCode = {v: k for k, v in morseCode.items()}
    y=''
    z=text.split()
    for a in z:
        y = y + morseCode[a]
    return(y)



# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    y=''
    for k in text:
        k=chr(((a*(ord(k)-97) + b) % 26)+97)
        y+=k
    return(y)
    

def decryptAffineCipher(text, a, b):
    y=''
    for k in text:
        k=chr(((pow(a,-1,26) * ((ord(k)-97) - b)) % 26)+97)
        y+=k
    return(y)
   
   
    

# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    y=''
    for l in range(0, len(text)):
        if l%2!=0: 
            if text[l].isalpha():
                if text[l].isupper():
                    y=y+chr(((ord(text[l]) + key2-65) % 26) + 65) 
                    
                else:
                    y=y+chr(((ord(text[l]) + key2 - 97) % 26) + 97)        
            elif text[l].isdigit():
                y=y+str((int(text[l])+key2)%10)
            else:
                y=y+str(text[l])

        else:
            if text[l].isalpha():
                if text[l].isupper():
                    y=y+chr(((ord(text[l]) + key1-65) % 26) + 65) 
                    
                else:
                    y=y+chr(((ord(text[l]) + key1 - 97) % 26) + 97)
            elif text[l].isdigit():
                y=y+str((int(text[l])+key1)%10)
            else:
                y=y+str(text[l])       
    return(y) 
                 
    

def decryptCaesarCipher(text, key1, key2):
    y=''
    for l in range(0, len(text)):
        if l%2!=0: 
            if text[l].isalpha():
                if text[l].isupper():
                    y=y+chr(((ord(text[l]) - key2-65) % 26) + 65) 
                    
                else:
                    y=y+chr(((ord(text[l]) - key2 - 97) % 26) + 97)        
            elif text[l].isdigit():
                y=y+str((int(text[l])-key2)%10)
            else:
                y=y+str(text[l])

        else:
            if text[l].isalpha():
                if text[l].isupper():
                    y=y+chr(((ord(text[l]) - key1-65) % 26) + 65) 
                    
                else:
                    y=y+chr(((ord(text[l]) - key1 - 97) % 26) + 97)
            elif text[l].isdigit():
                y=y+str((int(text[l])-key1)%10)
            else:
                y=y+str(text[l])       
    return(y)  

    


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    z=[]
    y=''
    for a in range(0, key):
        for b in range(a, len(text), key):
            z.append(text[b])
    for c in z:
        y=y+c
    return(y)       
    
def decryptTranspositionCipher(text, key):
   pass
    
