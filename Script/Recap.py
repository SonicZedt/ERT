from Handler import files, font_color
from Source import *
from Formatting import date, content, format
from docxcompose.composer import Composer

class create:
    def CreateTXT():
        with open(fileTXTTarget, 'w') as file:
            file.write("Rekapan PJ Shift {0} {1} \n".format(labList[labGroup][0], year))

    def CreateDOCX():
        doc = docx.Document()
        #region Long header and subheader text
        header = "BERITA ACARA PRAKTIKUM DAN REKAPAN NILAI \nMINGGU KE - {0}{1} \nLABORATORIUM {2} \n".format(minggu, covid_docxHeader, labList[labGroup][1])
        subheader = "Praktikum {0} diadakan satu minggu sekali{1}. Berikut berita acara praktikum di minggu ke-{2} ({3} - {4})".format(labList[labGroup][2], covid_docxSubheader, minggu, date.Start(), date.End())
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
    
class recap:
    def RecapTXT():
        create.CreateTXT()

        for fileIndex in range(len(fileList)):
            print("Merekap", fileList[fileIndex], "ke TXT")

            formattedParagraph = "{0} \n {1} \n\n".format(content.Date_Shift(fileIndex), content.ListAssistant(fileIndex))
            with open(fileTXTTarget, 'a') as fileTXT:
                fileTXT.write(formattedParagraph)

        print("{0}Rekapan Lab {1} minggu {2} (TXT) selesai dibuat!{3}\n".format(font_color.success, labList[labGroup][2], minggu, font_color.normal))


    def RecapDOCX():
        create.CreateDOCX()
        docTempList = []

        for fileIndex in range(len(fileList)):
            format.DOCXHeader(fileIndex)

        tempFiles = os.listdir(fileTempLoc)

        def AppendDocTemp():
            for file in tempFiles:
                if file == 'Recap.ZEDT':
                    continue
                docTempList.append(fileTempLoc + file)
            MergeDOCX()

        mainFile = docx.Document(fileDOCXTarget)
        composer = Composer(mainFile)

        def MergeDOCX():
            for fileIndex in range(len(docTempList)):
                print("Menggabungkan", docTempList[fileIndex], "ke dokumen utama")
                nextFile = docx.Document(docTempList[fileIndex])
                composer.append(nextFile)

        AppendDocTemp()
        composer.save(fileDOCXTarget)
        print("{0}Rekapan Lab {1} minggu {2} (DOCX) selesai dibuat!{3}\n".format(font_color.success, labList[labGroup][2], minggu, font_color.normal))

        files.DeleteMulti(fileTempLoc, tempFiles, exception='Recap.ZEDT', log=True)
        #files.DeleteMulti(dataLoc, os.listdir(dataLoc))

def Start():
    recap.RecapTXT()
    recap.RecapDOCX()