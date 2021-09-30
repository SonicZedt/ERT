def SetupUI():
    import UI

    UI.SetTextColor()
    UI.Header()    

def ConfirmTerminate():
    input("Tekan Enter untuk keluar")

def main():
    SetupUI()

    import Source
    import Recap
    import Summarize

    Recap.RecapTXT()
    Recap.RecapDOCX()

    print("\n\nJumlah laporan direkap:", Summarize.SourceFileCount())
    print("Jumlah error:", Summarize.ErrorCount(), "\n")
    
    ConfirmTerminate()

if __name__ == "__main__":
    main()