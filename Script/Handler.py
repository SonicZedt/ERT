import requests
import os

class font_color:
    error = '\033[91m'
    success = '\033[92m'
    normal = '\033[93m'

class error_message:
    notFound = "{0}[Error] Data - 404{1}".format(font_color.error, font_color.normal)
    connectionFail = "{0}[Error] Tidak ada koneksi internet{1}".format(font_color.error, font_color.normal)

def UrlCheck(url):
    try:
        requests.get(url, timeout=50)
        if requests.get(url).status_code == 404:
            print(error_message.notFound)
            return False
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        print(error_message.connectionFail)
        return False

def ErrorMessage(source, keyword, extra = ""):
    if extra:
        extra = (", " + extra)
    msg = "{0}[Error] {1} tidak terbaca di {2}{3}{4}".format(font_color.error, keyword, source, extra, font_color.normal)
    print(msg)

def DeleteMultiFiles(location, files, exception = 'exception', log = False):
    for file in files:
        if file == exception:
            continue
        if log == True:
            print("Menghapus", location + file)
        os.remove(location + file)

def Exit():
        input("Tekan Enter untuk keluar")
        exit()