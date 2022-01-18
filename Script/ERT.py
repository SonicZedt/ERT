# Author    : Zulfikar Hidayat
# Project   : ERT

import UI
import datetime
from Handler import ERT


def main():
    UI.SetTextColor()
    UI.Header()  

    import Source
    import Recap
    import Summarize

    startTime = datetime.datetime.now()
    Recap.Start()
    endTime = datetime.datetime.now()

    print("\n\nJumlah laporan direkap:", Summarize.count.SourceFile())
    print("Jumlah error:", Summarize.count.Error())
    print("Waktu yang dibutuhkan:", (endTime - startTime).total_seconds(), "detik\n\n")
    UI.Footer()
    
    ERT.Exit()

if __name__ == "__main__":
    main()