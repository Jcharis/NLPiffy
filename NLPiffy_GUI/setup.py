import cx_Freeze
import textblob
import spacy
import sys


base = None 

if sys.platform=='win32':
    base = "Win32GUI"


executables = [cx_Freeze.Executable("nlpiffy_gui.py")]    

cx_Freeze.setup(
        name = "NLPiffy GUI",
        options = {"build_exe":{"packages":["tkinter","textblob","spacy"]}},
        version="0.01",
        executables=executables) 
