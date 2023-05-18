#import dependencies and load working directory 
import os
from snapgene_reader import snapgene_file_to_seqrecord
from os import walk
abspath = os.path.abspath(__file__)
current_dir = os.path.dirname(abspath) 
os.chdir(os.path.dirname(abspath))

#Walk directory and exclude __file__ from list 
inputFileNames = next(walk(current_dir), (None, None, []))[2]  # [] if no file
inputFileNames.remove("Fasta Converter.py")
seqSizesList = []

#Convert DNA file to fasta format and record DNA size
for x in range(len(inputFileNames)):
    currentPlamsid = inputFileNames[x]
    if currentPlamsid[-3:] == "dna":
        readSeqRecord = snapgene_file_to_seqrecord(current_dir + "\\" + currentPlamsid)
        seqRecord = readSeqRecord.seq
        with open(currentPlamsid[:-4]+".fa", "w") as f:
            f.write(">"+currentPlamsid[:-4]+"\n"+str(seqRecord))
        seqSizesList.append(inputFileNames[x] +": " +str(len(seqRecord)))

#Print DNA size to screen
for line in seqSizesList:
    print(line)
input("")