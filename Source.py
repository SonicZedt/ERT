import os
import docx
import pandas

lab = (input("Lab: "))
minggu = int(input("Minggu ke-: "))

days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
classes = ["2KB", "3KB", "2DC", "3DC"]
shift = ["Shift 1", "Shift 2", "Shift 3", "Shift 4"]
year = "PTA 2021/2022"

fileDAsLoc = "Data/"
fileBAPLoc = "BAP/Minggu_{n}/".format(n = minggu)
fileTXTLoc = "Recap/"
dataAssistant = pandas.read_excel(fileDAsLoc + "Data_Assistant.xlsx").to_dict()
fileTarget = "{TXTLoc}Rekap VLab {labName} minggu {n}{type}".format(TXTLoc = fileTXTLoc, labName = lab, n = minggu, type = ".txt")

def LoadFile(): # Load all .docx files
    fileList = []
    detectedFiles = os.listdir(fileBAPLoc)

    for file in detectedFiles:
        fileList.append(fileBAPLoc + file)
    
    return fileList

def GetFullText(fileIndex):
    fileList = LoadFile()
    source = fileList[fileIndex]
    doc = docx.Document(source)
    fullText = []

    for paragraph in doc.paragraphs:
        fullText.append(paragraph.text)
    
    return fullText

def GetParagraph(str, fileIndex): # Return paragraph contais str
    paragraph = GetFullText(fileIndex)
    for i, j in enumerate(paragraph):
        if str in j:
            return(paragraph[i])
