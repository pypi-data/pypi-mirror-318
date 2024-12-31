# from VisualiserScroll import Visualiser
from Visualiser import Visualiser

dirOutput = "/Users/jvo/Downloads/output"
pathSong = "/Users/jvo/Downloads/All_Of_Me.musicxml"
pathSong = "/Users/jvo/Downloads/Autumn_Leaves_18ae0812-5600-4fcc-8a30-170c9edcd876.musicxml"
# pathSong = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/slash-chords.musicxml"
pathSong = "/Users/jvo/Downloads/Misty_c0d09bcf-f693-4a6e-b301-6f784a5135ae.musicxml"
# pathSong = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/chords1.musicxml"
pathSong = "/Users/jvo/Documents/programming/sheet-music/sheets/DSAll/Misty_57dd99fc-ce06-483a-bfa6-7ffb502d7c7b.musicxml"

settings = {}
settings["measuresPerLine"] = 4   # when using a4 format
settings["subdivision"] = 1   # 0, 1, 2
settings["facecolorMelody"] = (0,0,1)
settings["alphaMelody"] = 0.8
settings["alphaChordNotes"] = 0.2
settings["colorTextMelody"] = 'red'
settings["colorTextChords"] = 'purple'
settings["colorTextChordNotes"] = 'green'
settings["colorLyrics"] = 'yellow'

settings["plotLyrics"] = False
settings["plotMelody"] = False
settings["plotMetadata"] = False
settings["plotChords"] = True
settings["plotChordNotes"] = False
settings["plotBarlines"] = True

settings["extendBarlineTop"] = False

settings["chordVerbosity"] = 2  # 0, 1 or 2
settings["numbersRelativeToChord"] = False

settings["romanNumerals"] = True

settings["setInMajorKey"] = False
settings["minorFromMajorScalePerspective"] = False

settings["dpi"] = 700
settings["outputFormat"] = 'pdf'

vis = Visualiser(pathSong, settings)
vis.saveFig(dirName=dirOutput)
