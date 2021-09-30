from Source import fileList
errorCount = 0

def ErrorCount(e = 0):
    global errorCount
    errorCount = errorCount + e
    return errorCount

def SourceFileCount():
    return len(fileList) 