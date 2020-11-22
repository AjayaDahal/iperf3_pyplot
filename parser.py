'''Created by Ajaya Dahal
Mississippi State Universtity
A python script that plots graph for the iperf3 test
'''

import matplotlib.pyplot as plt

def index(a_list, value):
    try:
        return a_list.index(value)
    except ValueError:
        return None

fileName = "File1.txt"      #Our output is in this file
file = open('C:/Users/ajaya/Desktop/'+fileName, 'r')

Lines = file.readlines()
title = Lines[1]
if(fileName=="File1.txt"): #File1.txt has a pattern of : first line tells the Test Runtime, Second line tells
    Lines.pop(0)            # Title of the graph and third line is the title of the table which is copied
    Lines.pop(1)            # copied from the terminal after testing. First 3 lines are not used after extracting
    Lines.pop(2)            # all the required information

transfer = []
bitrate = []
for line in Lines:
    if(line!=''):
        words = line.split(' ')
        indTransfer = index(words, "MBytes")
        mByteFound = False
        if(indTransfer!=None ):
            mByteFound = True
            transfer.append(float(words[indTransfer-1]))
        if(mByteFound==False): # if MBytes is not in the table, that means the transfer rate is in KByte and so on. We have not encounter anything other than KBytes and MBytes, that's why we are accounting only those 2
            indTransfer = index(words, "KBytes") #Because some of the output is in KBytes, it is important to account for it.
            if (indTransfer != None):
                transfer.append(float(words[indTransfer - 1])/1024.0)
        indBitrate = index(words, 'Mbits/sec') #Bitrate or Bandwidth
        if(indBitrate !=None):
            bitrate.append(float(words[indBitrate - 1]))
print(transfer)
print(bitrate)
plt.plot(transfer)
plt.plot(bitrate)
print('Transfer: ',len(transfer))
print('Bitrate: ', len(bitrate))
print('lines: ', len(Lines))
plt.ylabel('Transfer in MBytes OR MBytes/sec')
plt.legend(["Transfer", "Bitrate"])
plt.title(title)
plt.show()
