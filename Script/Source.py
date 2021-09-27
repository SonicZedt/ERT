import os
import docx
import pandas

labList = [

    #index  : purpose
    #0      : txt file name and header
    #1      : docx file name and header
    #2      : docx subheader

    ["eldas", "ELEKTRONIKA DASAR", "Elektronika Dasar"],
    ["sisdig", "SISTEM DIGITAL", "Sistem Digital"],
    ["mp", "MIRKOPROSESOR", "Mikroprosesor"],
    ["sister", "SISTEM TERTANAM", "Sistem Tertanam"],
    ["iface", "INTERFACE", "Interface"]
]
days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
classes = ["2KB", "3KB", "2DC", "3DC"]
shift = ["Shift 1", "Shift 2", "Shift 3", "Shift 4"]
year = "PTA 2021/2022"

def InputCheck(inp, src):
    for i in src:
        for j in i:
            if inp == j:
                return True

    print("Invalid input!")
    return False

def GetUserInput():
    global lab, minggu, level, currentCond
    lab = (input("Lab: "))
    if lab.isupper():
        lab = lab.lower()
    if(not InputCheck(lab, labList)):
        GetUserInput()
    minggu = int(input("Minggu ke-: "))
    level = input("Jenjang: ")
    currentCond = input("Daring (y/n): ")

if __name__ == "Source":
    GetUserInput()

#region labGroup indexer, level uppercase check, covid_conditional
for group in labList:
    labGroup = labList.index(group)
    for name in group:
        if name == lab:
            break
    else:
        continue
    break

if level.isupper():
    level.lower()

if currentCond == 'y':
    covid_docxHeader = " SELAMA COVID-19"
    covid_docxSubheader = " secara virtual"
else:
    covid_docxHeader = covid_docxSubheader = ""
#endregion

fileDAsLoc = "Data/"
fileBAPLoc = "BAP/Minggu_{0}/".format(minggu)
fileTargetLoc = "Recap/"
fileTempLoc = "Recap/temp/"
dataAssistant = pandas.read_excel(fileDAsLoc + "Data_Assistant.xlsx").to_dict()
fileTXTTarget = "{0}Rekap VLab {1} minggu {2}.txt".format(fileTargetLoc,labList[labGroup][0], minggu)
fileDOCXTarget = "{0}BAP {1} {2} MINGGU {3}.docx".format(fileTargetLoc, labList[labGroup][1], level.upper(), minggu)

#region Load all .docx files
fileList = []
detectedFiles = os.listdir(fileBAPLoc)
for file in detectedFiles:
    fileList.append(fileBAPLoc + file)
if not fileList:
    print("Folder BAP/Minggu_{0} tidak terdeteksi".format(minggu))
    GetUserInput()
#regionend

def GetFullText(fileIndex):
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
