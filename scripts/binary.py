    import os
    import numpy as np
    cmd="cp ../../lakers-vs-celtics-and-the-nba-playoffs_bkp/nba/* ./"
    os.system(cmd)

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


    #fileName='tp1' # Boston Celtics    
    fileContent1=load_bin_file('tp5')

    #fileName='tp2' # East All Stars
    fileName='tp1' # Boston Celtics
    fileContent2=load_bin_file('tp1')
    print(len(fileContent1))

    #python scripts/binary.py
    dest = 'tp5' 

    #offset=1600
    #fileContent1[offset:(offset+numBytes)]=bytes(np.arange(numBytes//8))

    fileContent1=changeLogo(fileContent1)
    #fileContent1,offset=messTheNames(fileContent1)
    #print(fileContent1[offset:(offset+numBytes)])
    #fileContent1[offset:(offset+numBytes)]=fileContent2[offset:(offset+numBytes)]
    offset = 3192
    modN=20
    numBytes = 3
    #fileContent1[offset:(offset+numBytes)]=bytes(128*np.ones(numBytes,dtype='uint8')%modN)
    #2 Cambells

    #data=s2b("11111111"*12)
    #data=bytes.(16)
    #data=bytes(255*np.ones(12,dtype='uint8')%modN)
    offset=5212 # 12 bytes setting the color of the skin either 00 or 01, nothing else
    offset=5212+12 # Jump 
    data = bytes.fromhex("00 ff"*6)  # 
    #data = bytes(np.arange(60,dtype='uint8'))

    print("Los locations del buitos",offset, (offset+len(data)))
    print("Previous:", fileContent1[offset:(offset+len(data))])
    fileContent1[offset:(offset+len(data))]=data
    print("After:", fileContent1[offset:(offset+len(data))])

    offset+=3216 # Jump 
    # This works for the game although they or
    
    
    offset+=12 # Is this the shirt colour!
    #data = bytes.fromhex("0e"*11) # Surely this affects
    
    offset+=12 # What is this now?
    #data = bytes.fromhex("0e"*11)
    
    #fileContent1[offset:(offset+len(data))]=data
    
    print(len(fileContent1))

    newFile = open(dest, "wb")
    newFile.write(fileContent1)
    newFile.close()

    data = bytes.fromhex("A1 EF 00 1F")

    with open("output.bin", "wb") as f:
        f.write(data)
