def SetupUI():
    import UI

    UI.SetTextColor()
    UI.Header()    

def TerminateIn(delay):
    import time
    for d in range(delay):
        print("Keluar otomatis dalam", 5-d)
        time.sleep(1)

def main():
    SetupUI()

    import Source
    import Recap

    Recap.RecapTXT()
    Recap.RecapDOCX()
    TerminateIn(5)

if __name__ == "__main__":
    main()