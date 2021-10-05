# Author    : Zulfikar Hidayat
# Project   : ERT
import UI
import datetime

def ConfirmTerminate():
    input("Tekan Enter untuk keluar")

def main():
    UI.SetTextColor()
    UI.Header()  

    import Source
    import Recap
    import Summarize

    startTime = datetime.datetime.now()
    Recap.RecapTXT()
    Recap.RecapDOCX()
    endTime = datetime.datetime.now()

    print("\n\nJumlah laporan direkap:", Summarize.SourceFileCount())
    print("Jumlah error:", Summarize.ErrorCount())
    print("Waktu yang dibutuhkan:", (endTime - startTime).total_seconds(), "detik\n\n")
    UI.Footer()
    
    ConfirmTerminate()

if __name__ == "__main__":
    main()