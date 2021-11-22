import os
import docx
import pandas
import requests
import pickle
from Handler import check, ERT, License

dataLoc = "Data/"
urlList = [
    'https://drive.google.com/uc?export=download&id=1VaW-0_6JXbyf8ZreOkgc7t5dHAQZVavB', # class
    'https://drive.google.com/uc?export=download&id=1T7MheGGLmsWOQc981uwfNU7nV_q3u1qv', # lab
    'https://drive.google.com/uc?export=download&id=14rS4B7_UvZCFVnBvNK0dUNQL_EwkydSs', # shift
    'https://drive.google.com/uc?export=download&id=12yIITL_DjUmmYnU6sz8yJFg7bxMP3dIw' # ta
    ]

def ReadData(url, data, message, type = 'ZEDT'):
    if not check.Url(url):
        ERT.Exit()

    print("Membaca data", message)  
    def GetData(url):
        file = requests.get(url, allow_redirects=True)
        fileName = "Data_{0}.{1}".format(data, type)
        open(dataLoc + fileName, 'wb').write(file.content)
        print(fileName)
        return fileName

    if type == 'ZEDT':
        data = dataLoc + GetData(url)
        with open(data, 'rb') as dataFile:
            return pickle.load(dataFile)

    elif type == 'txt':
        with open(dataLoc + GetData(url), 'r') as dataFile:
            return dataFile.readline()

classes = ReadData(urlList[0], "Class", "1/" + str(len(urlList)))
labList = ReadData(urlList[1], "Lab", "2/" + str(len(urlList)))
shift = ReadData(urlList[2], "Shift", "3/" + str(len(urlList)))
year = ReadData(urlList[3], "TA", "4/" + str(len(urlList)), type='txt')
days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

def GetUserInput():
    global lab, minggu, level, currentCond
    License.Read("License.ZEDT")
    lab = (input("Lab: "))
    minggu = int(input("Minggu ke-: "))
    level = input("Jenjang: ")
    if level.islower():
       level = level.upper()
    currentCond = input("Daring (y/n): ")

def InputCheck(): # Redo input if incorrect value given
    def CorrectCheck(inp, src):
        for i in src:
            if isinstance(src[0], list):
                for j in i:
                    if inp == j:
                        return True
            else:
                if inp == i:
                    return True
        print("[Error] Invalid {0} input!".format(inp))
        return False

    if(not CorrectCheck(lab, labList)):
        GetUserInput()

if __name__ == "Source":
    print('\n')
    GetUserInput()
    License.Validation(lab)
    print('\n')

#region labGroup indexer, covid_conditional
for group in labList:
    labGroup = labList.index(group)
    for name in group:
        if name == lab:
            break
    else:
        continue
    break

if currentCond == 'y':
    covid_docxHeader = " SELAMA COVID-19"
    covid_docxSubheader = " secara virtual"
else:
    covid_docxHeader = covid_docxSubheader = ""
#endregion

def GetDataAssistant():
    url = "https://drive.google.com/uc?export=download&id=1gdU4G8a81j-cX7zu9n180zZZFC2MwX3j"
    if check.Url(url):
        return url
    else:
        ERT.Exit()

fileDAsLoc = "Data/"
fileBAPLoc = "BAP/Minggu_{0}/".format(minggu)
fileTargetLoc = "Recap/"
fileTempLoc = "Recap/temp/"
dataAssistant = pandas.read_csv(GetDataAssistant()).to_dict()
fileTXTTarget = "{0}Rekap VLab {1} minggu {2}.txt".format(fileTargetLoc,labList[labGroup][0], minggu)
fileDOCXTarget = "{0}BAP {1} {2} MINGGU {3}.docx".format(fileTargetLoc, labList[labGroup][1], level, minggu)

#region Load all .docx files
fileList = []
detectedFiles = os.listdir(fileBAPLoc)
for file in detectedFiles:
    if file == 'BAP.ZEDT':
        continue
    fileList.append(fileBAPLoc + file)
if not fileList:
    print("Folder BAP/Minggu_{0} kosong".format(minggu))
    GetUserInput()
#endregion

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
