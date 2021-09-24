import os
import docx
import pandas
import UI

UI.SetTextColor()
UI.Header()

lab = input("Lab: ")
minggu = int(input("Minggu ke-: "))

#region Data
days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
classes = ["2KB", "3KB", "2DC", "3DC"]
shift = ["Shift 1", "Shift 2", "Shift 3", "Shift 4"]
year = "PTA 2021/2022"

fileDAsLoc = "Data/"
fileBAPLoc = "BAP/Minggu_{n}/".format(n = minggu)
fileTXTLoc = "Recap/"
dataAssistant = pandas.read_excel(fileDAsLoc + "Data_Assistant.xlsx").to_dict()
fileTarget = "{TXTLoc}Rekap VLab {labName} minggu {n}{type}".format(TXTLoc = fileTXTLoc, labName = lab, n = minggu, type = ".txt")
#endregion

def LoadFile():
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

# Return paragraph that contains str
def GetParagraph(str, fileIndex):
    paragraph = GetFullText(fileIndex)
    for i, j in enumerate(paragraph):
        if str in j:
            return(paragraph[i])

def CreateTXT():
    with open(fileTarget, 'w') as file:
        file.write("Rekapan PJ Shift {labName} {ta} \n".format(labName = lab, ta = year))

#region Paragraph formatting
def Date_Shift(fileIndex):
    date = GetParagraph("Hari", fileIndex)
    class_shift = GetParagraph("Kelas", fileIndex)

    for day in days:            
        newdate = date[date.find(day):]
        if day in date:
            break

    for c in classes:
        classIndex = class_shift.find(c)
        for s in shift:
            shiftIndex = class_shift.find(s) + len(s) + s.count(" ")
            if s in class_shift:
                break
        newclass = class_shift[classIndex:shiftIndex]
        if c in class_shift:
            break

    subheader = "\n{nd} | {nc}".format(nd = newdate, nc = newclass)
    return subheader

def ListAssistant(fileIndex):
    presentAssistant = []

    def GetList(key):
        for data in dataAssistant[key]:
            name = GetParagraph(dataAssistant[key].get(data), fileIndex)
            if name != None:
                if '*' in name:
                    presentAssistant.insert(0,"- " + name)
                else:
                    presentAssistant.append(" - " + name)

    GetList('Assistant')
    GetList('Coass')
    presentAssistant[1:] = sorted(set(presentAssistant[1:]))

    return '\n'.join(presentAssistant)
#endregion

# Weekly PJS recap into txt
def RecapTXT():
    CreateTXT()

    fileList = LoadFile()
    for fileIndex in range(len(fileList)):
        print("Merekap", fileList[fileIndex], ".......")

        formattedParagraph = "{DS} \n {LA} \n\n".format(DS = Date_Shift(fileIndex), LA = ListAssistant(fileIndex))
        with open(fileTarget, 'a') as fileTXT:
            fileTXT.write(formattedParagraph)
    
    print("Rekapan Lab {labName} minggu {n} selesai dibuat!".format(labName = lab, n = minggu))

RecapTXT()