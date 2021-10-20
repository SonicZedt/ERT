from Source import fileList

class count:
    global errorCount
    errorCount = 0

    def Error(e = 0):
        global errorCount
        errorCount = errorCount + e
        return errorCount

    def SourceFile():
        return len(fileList) 