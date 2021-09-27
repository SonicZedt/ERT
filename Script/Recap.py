from Source import *
from Formatting import Date_Shift, ListAssistant
from docxcompose.composer import Composer

def CreateTXT():
    with open(fileTXTTarget, 'w') as file:
        file.write("Rekapan PJ Shift {0} {1} \n".format(labList[labGroup][0], year))

def RecapTXT():
    CreateTXT()

    for fileIndex in range(len(fileList)):
        print("Merekap", fileList[fileIndex], "ke TXT.......")

        formattedParagraph = "{0} \n {1} \n\n".format(Date_Shift(fileIndex), ListAssistant(fileIndex))
        with open(fileTXTTarget, 'a') as fileTXT:
            fileTXT.write(formattedParagraph)
    
    print("Rekapan Lab {0} minggu {1} selesai dibuat!".format(labList[labGroup][2], minggu))

def CreateDOCX():
    doc = docx.Document()
    #region Long header and subheader text
    header = "BERITA ACARA PRAKTIKUM DAN REKAPAN NILAI \nMINGGU KE - {0}{1} \nLABORATORIUM {2} \n\n".format(minggu, covid_docxHeader, labList[labGroup][1])
    subheader = "Praktikum {0} diadakan satu minggu sekali{1}. Berikut berita acara praktikum di minggu ke-{2} (PH_TANGGAL)\n\n".format(labList[labGroup][2], covid_docxSubheader, minggu)
    #endregion

    def WriteParagraph(paragraph, styleBbold = False):
        rawParagraph = doc.add_paragraph()
        rawParagraph.paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
        
        paragraphRunner = rawParagraph.add_run(paragraph)
        paragraphRunner.bold = styleBbold
        paragraphRunner.font.name = 'Times New Roman'
        paragraphRunner.font.size = docx.shared.Pt(12)

    WriteParagraph(header, True)
    WriteParagraph(subheader)

    doc.save(fileDOCXTarget)

def RecapDOCX():
    CreateDOCX()
    mainFile = docx.Document(fileDOCXTarget)

    composer = Composer(mainFile)
    for fileIndex in range(len(fileList)):
        print("Merekap", fileList[fileIndex], "ke DOCX.......")
        nextFile = docx.Document(fileList[fileIndex])
        composer.append(nextFile)
    
    composer.save(fileDOCXTarget)