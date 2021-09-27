def SetupUI():
    import UI

    UI.SetTextColor()
    UI.Header()    

def main():
    SetupUI()

    import Source
    import Recap

    #Recap.RecapTXT()
    Recap.RecapDOCX()

if __name__ == "__main__":
    main()