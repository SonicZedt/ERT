from Source import *
from Summarize import count
from Handler import error_message

class date:
    global dates
    dates = []
    for fileIndex in range(len(fileList)):
        date = GetParagraph("Hari", fileIndex)
        try:
            dates.append(date[date.find(",") + 2:])
        except:
            error_message.Generate(fileList[fileIndex], "Tanggal", "perbaikan manual diperlukan untuk {0}".format(fileDOCXTarget))
    print("Praktikum pertama pada:", dates[0], "dari", fileList[0])
    print("Praktikum terakhir pada:", dates[-1], "dari", fileList[-1], '\n')

    def Start():
        return dates[0]

    def End():
        return dates[-1]

class content:
    def Date_Shift(fileIndex): # Return date | shift
        date = GetParagraph("Hari", fileIndex)
        class_shift = GetParagraph("Kelas", fileIndex)

        def ObjectNotFound(obj):
            if obj is None:
                return True
            return False

        def NotFoundLog(source, message, error = 1):
            errorMsg = error_message.Generate(source, message)
            count.Error(error)
            return errorMsg

        if ObjectNotFound(date):
            return NotFoundLog(fileList[fileIndex], "Hari")

        elif ObjectNotFound(class_shift):
            return NotFoundLog(fileList[fileIndex], "Kelas")

        def NewDate():
            val = ""

            def Value(day, lower = False):
                if lower:
                    day = day.lower()
                newdate = date[date.find(day):]
                if day in date:
                    return newdate
                else:
                    return None

            for day in days:
                val = Value(day)
                if val is not None:
                    break

            if val is None:    
                for day in days:
                    val = Value(day, True)
                    if val is not None:
                        break

            return val

        def NewClass():
            val = ""

            def Value(c, lower = False):
                if lower:
                    c = c.lower()
                classIndex = class_shift.find(c)
                for s in shift:
                    shiftIndex = class_shift.find(s) + len(s) + s.count(" ")
                    if s in class_shift:
                        break
                newclass = class_shift[classIndex:shiftIndex]
                if c in class_shift:
                    return newclass
                else:
                    return None

            for c in classes:
                val = Value(c)
                if val is not None:
                    break

            if val is None:
                for c in classes:
                    val = Value(c, True)
                    if val is not None:
                        break
            return val

        newdate = NewDate()
        newclass = NewClass()

        subheader = "\n{nd} | {nc}".format(nd = newdate, nc = newclass)
        return subheader

    def ListAssistant(fileIndex): # Return listed assistant name in loaded file
        presentAssistant = []

        def GetList(key):
            dataset = dataAssistant[key]

            def AttempAppend(var):
                if var != None:
                    presentAssistant.append(" - " + var)

            for data in dataset:
                d = dataset.get(data)
                if type(d) is not str:
                    continue
                
                dlow = d.lower()
                name = GetParagraph(d, fileIndex)
                namelow = GetParagraph(dlow, fileIndex)
                AttempAppend(name)
                AttempAppend(namelow)

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

class format:
    def DOCXHeader(fileIndex): # Remove PJS report header and save in temp folder
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