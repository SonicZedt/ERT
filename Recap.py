from Source import *
from Formatting import Date_Shift, ListAssistant

def CreateTXT():
    with open(fileTarget, 'w') as file:
        file.write("Rekapan PJ Shift {labName} {ta} \n".format(labName = lab, ta = year))

def RecapTXT():
    CreateTXT()

    fileList = LoadFile()
    for fileIndex in range(len(fileList)):
        print("Merekap", fileList[fileIndex], ".......")

        formattedParagraph = "{DS} \n {LA} \n\n".format(DS = Date_Shift(fileIndex), LA = ListAssistant(fileIndex))
        with open(fileTarget, 'a') as fileTXT:
            fileTXT.write(formattedParagraph)
    
    print("Rekapan Lab {labName} minggu {n} selesai dibuat!".format(labName = lab, n = minggu))