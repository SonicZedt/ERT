import requests
import os
import pickle

class font_color:
    error = '\033[91m'
    success = '\033[92m'
    normal = '\033[93m'

class error_message:
    notFound = "{0}[Error] Data - 404{1}".format(font_color.error, font_color.normal)
    connectionFail = "{0}[Error] Tidak ada koneksi internet{1}".format(font_color.error, font_color.normal)
    badLicense = "{0}[Error] Lisensi tidak valid!{1}".format(font_color.error, font_color.normal)
    unlicensedLab = "{0}[Error] Lisensi tidak sesuai atau Lab ini belum terlisensi{1}".format(font_color.error, font_color.normal)

    def Generate(source, keyword, extra = ""):
        if extra:
            extra = (", " + extra)
        msg = "{0}[Error] {1} tidak terbaca di {2}{3}{4}".format(font_color.error, keyword, source, extra, font_color.normal)
        print(msg)
        return msg

class check:
    def Url(url):
        try:
            requests.get(url, timeout=50)
            if requests.get(url).status_code == 404:
                print(error_message.notFound)
                return False
            return True
        except (requests.ConnectionError, requests.Timeout) as exception:
            print(error_message.connectionFail)
            return False

class files:
    def DeleteMulti(location, files, exception = 'exception', log = False):
        for file in files:
            if file == exception:
                continue
            if log == True:
                print("Menghapus", location + file)
            os.remove(location + file)

class ERT:
    def Exit():
            input("Tekan Enter untuk keluar")
            exit()

class License:
    licensedLab = ""
    def Read(license):
        global licensedLab

        labList = pickle.load(open("Data/Data_Lab.ZEDT", 'rb'))
        with open(license, 'rb') as file:
            licensedLab = pickle.load(file)
        
        for lab in labList:
            if isinstance(labList[0], list):
                for name in lab:
                    if licensedLab == name:
                        print("{0}ERT terlisensi untuk {1}{2}\n".format(font_color.success, lab[2], font_color.normal))
                        return
        else:
            print(error_message.badLicense)
            ERT.Exit()
    
    def Validation(lab):
        if lab == licensedLab:
            return
        else:
            print(error_message.unlicensedLab)
            ERT.Exit()
