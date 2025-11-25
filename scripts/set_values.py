import os
import numpy as np
import argparse

def s2b(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def load_bin_file(fileName: str = 'tp0'):
    with open(fileName, mode='rb') as file: # b is important -> binary
        fileContent = file.read()
        fileContent = bytearray(fileContent)
    return fileContent

def changeLogo(fileContent):
    numBytes = 780
    offset=828
    logo_width = 12
    fileContent1[offset:(offset+numBytes)]=bytes(np.arange(numBytes,dtype='uint8')%logo_width)
    #fileContent1[offset:(offset+numBytes)]=bytes(255*np.ones(numBytes,dtype='uint8'))
    return fileContent

def messTheNames(fileContent):
    offset=1608 
    modN=22*6 # Six rows, 22 columns for names
    numBytes = 132*12 # Twelve player
    
    numBytes = 132 # Twelve players
    
    for i in range(12):
        
        fileContent[offset:(offset+numBytes)] = bytes(np.arange(numBytes,dtype='uint8')%modN)
        fileContent[offset:(offset+numBytes)] = bytes(255*np.ones(numBytes,dtype='uint8')%modN)
        offset += 132
        
    return fileContent, offset

def parse_int(value):
    """Parser to allow decimal or hex input."""
    value = value.strip().lower()
    if value.startswith("0x"):
        return int(value, 16)
    return int(value)

def main():
    parser = argparse.ArgumentParser(
        description="Visualize 4-bit nibble data from a binary file."
    )

    parser.add_argument("file", help="Input binary file")
    parser.add_argument("--offset", required=True, type=parse_int,
                        help="Starting byte offset (decimal or hex like 0x200)")
    parser.add_argument("--length", required=True, type=parse_int,
                        help="Number of bytes to read")
    parser.add_argument("--values", required=True, type=str,
                        help="Values to fill in",default="ff")
    
    args = parser.parse_args()

    fileContent1=load_bin_file(args.file)
    offset = args.offset
    
    modN=20
    numBytes = 3
    #fileContent1[offset:(offset+numBytes)]=bytes(128*np.ones(numBytes,dtype='uint8')%modN)
    #2 Cambells

    #data=s2b("11111111"*12)
    #data=bytes.(16)
    #data=bytes(255*np.ones(12,dtype='uint8')%modN)

    string_to_put = args.values*(args.length//len(args.values))
    data = bytes.fromhex(string_to_put)
    
    #print(f"The location of the bytes: {offset} -  {(offset+len(data))}")
    #print("Previous:", fileContent1[offset:(offset+len(data))])
    
    fileContent1[offset:(offset+len(data))]=data
    #print("After:", fileContent1[offset:(offset+len(data))])
    
    newFile = open(args.file, "wb")
    newFile.write(fileContent1)
    newFile.close()


if __name__ == "__main__":
    main()