def SetupUI():
    import UI

    UI.SetTextColor()
    UI.Header()

def ImportSource():
    import Source

def StartRecap():
    import Recap

    Recap.RecapTXT()

def main():
    SetupUI()
    ImportSource()
    StartRecap()   

if __name__ == "__main__":
    main()