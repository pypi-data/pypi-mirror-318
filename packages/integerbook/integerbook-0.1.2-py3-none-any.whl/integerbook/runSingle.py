from VisualiserScroll import Visualiser
# from Visualiser import Visualiser

dirOutput = "/Users/jvo/Downloads/output"
pathSong = "/Users/jvo/Downloads/All_Of_Me.musicxml"
pathSong = "/Users/jvo/Downloads/Autumn_Leaves_18ae0812-5600-4fcc-8a30-170c9edcd876.musicxml"
# pathSong = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/slash-chords.musicxml"
# pathSong = "/Users/jvo/Downloads/Misty_c0d09bcf-f693-4a6e-b301-6f784a5135ae.musicxml"
# pathSong = "/Users/jvo/Library/Mobile Documents/com~apple~CloudDocs/icloudDocuments/bladmuziek/test-files/chords1.musicxml"
# pathSong = "/Users/jvo/Documents/programming/sheet-music/sheets/DSAll/Misty_57dd99fc-ce06-483a-bfa6-7ffb502d7c7b.musicxml"
# pathSong = "/Users/jvo/Documents/programming/sheet-music/sheets/christmas-selection/Winter_Wonderland_4733ce23-44ff-415e-8946-01da35371e18.musicxml"

settings = {}

settings["dpi"] = 700   # only relevant when outputting png (you can get errors for large dpi)
settings["outputFormat"] = 'pdf'

settings["plotLyrics"] = True
settings["plotMelody"] = True
settings["plotChords"] = True
settings["plotChordNotes"] = False
settings["plotBarlines"] = True

settings["subdivision"] = 1   # 0: measure barlines, 1: quarternote lines, 2: 16th note lines
settings["facecolorMelody"] = (0,0,1)
settings["alphaMelody"] = 0.8
settings["alphaChordNotes"] = 0.2
settings["colorTextMelody"] =  (.95, .95, .95)
settings["colorTextChords"] = (0.8,0.8,0.8)
settings["colorTextChordNotes"] = 'green'
settings["colorLyrics"] = 'yellow'
settings["colorTextKey"] = (.95, .95, .95)


settings["chordVerbosity"] = 2  # 0: triads, 1: 7th, 9th, etc, 2: add9, add11 etc.
settings["numbersRelativeToChord"] = False

settings["romanNumerals"] = True

settings["forceMinor"] = True
settings["minorFromParallelMajorScalePerspective"] = True
settings["minorFromRelativeMajorScalePerspective"] = False
settings["minorFromMinorScalePerspective"] = False

settings['coloringCircleOfFifths'] = True
settings['coloringVoices'] = False




# do not change below settings
settings["plotMetadata"] = False   # keep false (prints title when using the normal a4 format
settings["plotFirstKeyWithinBar"] = True

vis = Visualiser(pathSong, settings)
vis.saveFig(dirName=dirOutput)
