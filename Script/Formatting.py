from Source import *

dates = []
for fileIndex in range(len(fileList)):
    date = GetParagraph("Hari", fileIndex)
    dates.append(date[date.find(",") + 2:])

def Date_Shift(fileIndex): # Return date | shift
    date = GetParagraph("Hari", fileIndex)
    class_shift = GetParagraph("Kelas", fileIndex)
    
    def ObjectNotFound(obj):
        if obj is None:
            return True
        return False
    
    if ObjectNotFound(date):
        errorMsg = ("[Error] Hari tidak terbaca di {0}".format(fileList[fileIndex]))
        print(errorMsg)
        return errorMsg
    
    elif ObjectNotFound(class_shift):
        errorMsg = ("[Error] Kelas tidak terbaca di {0}".format(fileList[fileIndex]))
        print(errorMsg)
        return errorMsg

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

def ListAssistant(fileIndex): # Return listed assistant name in loaded file
    presentAssistant = []

    def GetList(key):
        dataset = dataAssistant[key]

        for data in dataset:
            d = dataset.get(data)
            if type(d) is not str:
                continue
            name = GetParagraph(d, fileIndex)
            if name != None:
                presentAssistant.append(" - " + name)
    
    GetList('Assistant')
    GetList('Coass')
    GetList('Alt')

    presentAssistant = sorted(set(presentAssistant))
    #region Star sorting
    for starCount in range(1, 3):
        for name in presentAssistant:
            if name.count('*') == starCount:
                presentAssistant.insert(0, presentAssistant.pop(presentAssistant.index(name)))
    #endregion
    
    return '\n'.join(presentAssistant)

def GetStartDate():
    return dates[0]

def GetEndDate():
    return dates[-1]

def RemoveDOCXHeader(fileIndex): # Remove PJS report header and save in temp folder
    print("Menghapus header dokumen " + fileList[fileIndex])
    doc = docx.Document(fileList[fileIndex])

    for paragraph in doc.paragraphs:
        if paragraph.text == GetParagraph("Hari", fileIndex):
            paragraph.insert_paragraph_before('')
            break
        p = paragraph._element
        p.getparent().remove(p)
        paragraph._p = paragraph._element = None

    doc.save("{0}{1}doctemp_{2}_{3}.docx".format(fileTempLoc, labList[labGroup][0], fileIndex, minggu))