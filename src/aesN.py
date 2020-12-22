#!/usr/bin/python3
import os

STable = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

SInverseTable = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)



def shiftMatrixRows(CMat):
    """
        moves cells to the left for row i , i iterations
    """
    'second row'
    temp = CMat[0][1]
    CMat[0][1] = CMat[1][1]
    CMat[1][1] = CMat[2][1]
    CMat[2][1] = CMat[3][1]
    CMat[3][1] = temp

    'third row'
    temp = CMat[0][2]
    CMat[0][2] = CMat[2][2]
    CMat[2][2] = temp
    temp = CMat[1][2]
    CMat[1][2] = CMat[3][2]
    CMat[3][2] = temp

    'fourth row'
    temp = CMat[3][3]
    CMat[3][3] = CMat[2][3]
    CMat[2][3] = CMat[1][3]
    CMat[1][3] = CMat[0][3]
    CMat[0][3] = temp

    return CMat


def textPadding(text):
    textPad = 16 - len(text)%16
    for i in range(textPad):
        text += chr(textPad)
    return text

def removePadding(text):
    textPad = text[-1]
    return text[:-textPad]



def inverseShiftMatrixRows(CMat):
    """
        moves cells to the right for row i , i iterations
    """
    'second row'
    CMat[0][1], CMat[1][1], CMat[2][1], CMat[3][1] = CMat[3][1], CMat[0][1], CMat[1][1], CMat[2][1]

    'third row'
    temp = CMat[0][2]
    CMat[0][2] = CMat[2][2]
    CMat[2][2] = temp
    temp = CMat[1][2]
    CMat[1][2] = CMat[3][2]
    CMat[3][2] = temp

    'fourth row'
    temp = CMat[0][3]
    CMat[0][3] = CMat[1][3]
    CMat[1][3] = CMat[2][3]
    CMat[2][3] = CMat[3][3]
    CMat[3][3] = temp
    return CMat

def Encrypt(TextBlock,key):
    """
        Aes encryption method, does all of the stages for the aes algorithm by iterations
    """
    if isinstance(TextBlock, str):
        TextBlock = TextBlock.encode('utf-8')
    print(TextBlock)
    MText = [['' for i in range(0,4)] for j in range(0,4)]
    for i in range(0,4):
        for j in range(0,4):
            MText[i][j] = TextBlock[i*4 + j]
    msg = sum(MText,[])
    Ckey = keyExpand(key)
    MText = roundKey(Ckey,MText,0)
 
    for iteration in range(1,10):
        MText = subBytes(MText)
        MText = shiftMatrixRows(MText)
        MText = mixCol(MText)
        MText = roundKey(Ckey,MText,iteration)

        


    MText = subBytes(MText)
    MText = shiftMatrixRows(MText)
    MText = roundKey(Ckey,MText,10)
    msg = ['' for i in range(0,16)]
    for i in range(0,4):
        for j in range(0,4):
            msg[i*4 + j] = MText[i][j]
    return msg

def Decryption(EncryptedText,key):
    """
        Aes Decryption method, does all of the stages for the aes encryption but backwards ,algorithm works by iterations
    """
    if isinstance(EncryptedText, str):
        EncryptedText = EncryptedText.encode('utf-8')
    MText = [['' for i in range(0,4)] for j in range(0,4)]
    for i in range(0,4):
        for j in range(0,4):
            MText[i][j] = EncryptedText[i*4 + j]
    
    Ckey = keyExpand(key)
    MText = roundKey(Ckey,MText,10)
    MText = inverseShiftMatrixRows(MText)
    MText = invSubBytes(MText)


    
    for iteration in range(9,0,-1):
        MText = roundKey(Ckey,MText,iteration)
        MText = invMixCol(MText)
        MText = inverseShiftMatrixRows(MText)
        MText = invSubBytes(MText)
 
    MText = roundKey(Ckey,MText,0)
    msg =bytes(sum(MText,[]))

    return msg



def subBytes(CMat):
    """
    subtitute bytes: replaces the each cell in the matrix with one from the STable
    """
    for i in range(len(CMat)):
        for j in range(len(CMat[i])):
            CMat[i][j] = STable[CMat[i][j]]
    return CMat

def invSubBytes(CMat):
    """
    subtitute bytes: replaces the each cell in the matrix with one from the STable
    """
    for i in range(len(CMat)):
        for j in range(len(CMat[i])):
            CMat[i][j] = SInverseTable[CMat[i][j]]
    return CMat

def keyExpand(currentKey):
    """
        expands the key for the entire encryption/decryption to use for add round key
    """
    
    Mkey = [['' for i in range(0,4)] for j in range(0,4)]
    for i in range(0,4):
        for j in range(0,4):
            Mkey[i][j] = currentKey[i*4 + j]

 
    H=1
    for c in range(4,4 *( 10 + 1 )):
        if c % 4 == 0 :
            nCol = [ Mkey[i][c-1]  for i in range(0,4)]


            temp =    nCol[0]
            nCol[0] = nCol[1]
            nCol[1] = nCol[2]
            nCol[2] = nCol[3]
            nCol[3] = temp

           

            for i in range(0,4):
                nCol[i] = STable[nCol[i]]  

            for i in range(0,4):
                if i == 0 :
                    Mkey[i].append((Mkey[i][c-4]) ^ (nCol[i]) ^ (Rcon[H]))
                else:
                    Mkey[i].append((Mkey[i][c-4]) ^ (nCol[i]) ^ 0x00)

            H+=1

        else:
            for i in range(0,4):
                Mkey[i].append((Mkey[i][c-4]) ^ (Mkey[i][c-1]))
        

    return Mkey

def roundKey(MKey,MText,rnd=0):
    """
        gets matrix text and matrix key and xor by the round position
    """
    for c in range(0,4):
        MText[c][0] = MText[c][0] ^ MKey[0][4*rnd + c]
        MText[c][1] = MText[c][1] ^ MKey[1][4*rnd + c]
        MText[c][2] = MText[c][2] ^ MKey[2][4*rnd + c]
        MText[c][3] = MText[c][3] ^ MKey[3][4*rnd + c]

    return MText



def binaryMultiply3(cell):
    return gaussMultiplier(cell,3)


def gaussMultiplier(a,b):
    """
        famous gauss multiplier algorithm
    """
    p = 0
    hi_bit_set = 0
    for i in range(8):
        if b & 1 == 1: p ^= a
        hi_bit_set = a & 0x80
        a <<= 1
        if hi_bit_set == 0x80: a ^= 0x1b
        b >>= 1
    return p % 256


def binaryMultiply2(cell):
    return gaussMultiplier(cell,2)

def mixCol(MText):
    """
    algorithm aes encryption mixing action is multiplying by a matrix
    {
        02  03  01  01 
        01  02  03  01  
        01  01  02  03  
        03  01  01  02
    }
    Xor action is equal to addition
    """
    for c in range(0,4):
        check = binaryMultiply2(MText[c][0])
        cell1 = binaryMultiply2(MText[c][0]) ^ binaryMultiply3(MText[c][1])  ^ gaussMultiplier(MText[c][2],1) ^ gaussMultiplier(MText[c][3],1)
        cell2 = MText[c][0] ^ binaryMultiply2(MText[c][1]) ^ binaryMultiply3(MText[c][2]) ^ MText[c][3]
        cell3 = MText[c][0] ^ MText[c][1] ^ binaryMultiply2( MText[c][2]) ^ binaryMultiply3(MText[c][3])
        cell4 = binaryMultiply3(MText[c][0]) ^ MText[c][1] ^ MText[c][2] ^ binaryMultiply2(MText[c][3])

        MText[c][0] = cell1
        MText[c][1] = cell2
        MText[c][2] = cell3
        MText[c][3] = cell4

    return MText

def invMixCol(MText):
    """
    algorithm aes decryption mixing action is multiplying by a matrix
    {
        14  11  13  9
        9   14  11  13  
        13  9   14  11  
        11  13  9   14
    }
    Xor action is equal to addition
    """


    for c in range(0,4):


        cell1 = gaussMultiplier(MText[c][0],14) ^ gaussMultiplier(MText[c][1],11)  ^ gaussMultiplier(MText[c][2],13) ^ gaussMultiplier(MText[c][3],9)
        cell2 = gaussMultiplier(MText[c][0],9) ^ gaussMultiplier(MText[c][1],14)  ^ gaussMultiplier(MText[c][2],11 ) ^ gaussMultiplier(MText[c][3],13)
        cell3 = gaussMultiplier(MText[c][0],13) ^ gaussMultiplier( MText[c][1],9)  ^gaussMultiplier(MText[c][2],14) ^ gaussMultiplier(MText[c][3],11)
        cell4 = gaussMultiplier(MText[c][0],11) ^ gaussMultiplier(MText[c][1],13)  ^ gaussMultiplier(MText[c][2],9) ^ gaussMultiplier(MText[c][3],14)

        MText[c][0] = cell1
        MText[c][1] = cell2
        MText[c][2] = cell3
        MText[c][3] = cell4

    return MText

def splitBlocks(text):
    """
        splits long text to sections of 16 length, if it short of that padd with the chars are the value of the missing characters

    """
    bList = []
    for i in range(int(len(text)/16)):
        bList.append(text[(i*16):((i+1)*16)])
    return bList


def aesCbcEncrypt(text,key):
    """
        Custom aes cbc mode, (doesn't function like the main goal of the original algorithm),
        splits the text to sections, each section is first being Xor with the last section(key if it's the first),
        Encrypted by aes and added to one big list which is returned
    """
    paddedText = textPadding(text)
    blockList =  splitBlocks(paddedText)
    encBlockList = []
    prv = key
    for block in blockList:
        currTextblock = [ord(i) for i in block]
        for i in range(len(currTextblock)):
            currTextblock[i] = currTextblock[i] ^ prv[i]
        encBlock = Encrypt(currTextblock,key)
        encBlockList.extend(encBlock)
        prv = encBlock

    return bytes(encBlockList)

def aesCbcDecrypt(text,key):
    """
        Custom aes cbc mode, (doesn't function like the main goal of the original algorithm),
        splits the text to sections, each section is first Decrypted with the key,
        then xor'd with the last section (key if it's the first) , and added into the main list
        which is returned
    """
    blockList =  splitBlocks(text)
    DecBlockList = []
    prv = key
    for block in blockList:
        currTextblock = [i for i in block]
        decBlock = Decryption(currTextblock,key)
        ordBlock = [i for i in decBlock]
        for i in range(len(ordBlock)):
            ordBlock[i] = ordBlock[i] ^ prv[i]
        DecBlockList.extend(ordBlock)
        prv = currTextblock
    msg = removePadding(DecBlockList)
    return ''.join(chr(i) for i in msg)



#random_key = os.urandom(16)
#x=aesCbcEncrypt("kljhfgjkldfgkjl",random_key)
#print(x)
#print(str(aesCbcDecrypt(x,random_key)))

#random_key =b'6\x05\x07\xa6\x89\x18\xbb\xea\xac\x00\xe0c\xbe\x05M\xc2'
#x = Encrypt("helworld2adsdasd",random_key)
#print(x)
#print(str(Decryption(x,random_key)))
