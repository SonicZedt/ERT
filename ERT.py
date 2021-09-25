def SetupUI():
    import UI

    UI.SetTextColor()
    UI.Header()

def ImportSource():
    import Source

def StartRecap():
    import Recap

    Recap.RecapTXT()

if __name__ == "__main__":
    SetupUI()
    ImportSource()
    StartRecap()