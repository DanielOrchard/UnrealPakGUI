# DanO tool for easy packaging and unpackaging uassets to upack files with UnrealPak

import Tkinter as tkinter
from tkFileDialog import askopenfilename
from tkFileDialog import askdirectory
import ttk
import subprocess
import os

unrealPakDIR = r'"' + "C:\Program Files\Epic Games\UE_4.20\Engine\Binaries\Win64\UnrealPak.exe" + '"'
Path_PackInputDir = r"Choose your input directory"
Path_PackOutputDIR = r"Alternatively, choose a text doc defining all assets"
Path_UnpackInputDir = r"Choose your output directory"
Path_UnpackOutputDir = r"D:\Temp"
Path_PackNotepad = r"D:\Temp"
Pack_Filename = "Filename"

# Base UI window
window = tkinter.Tk()
window.title("Unreal Pack Toolkit")
window.geometry("560x420")
#window.wm_iconbitmap('filename.ico')
window.configure(background="#222222")
window.grid

subwindow = tkinter.Frame(window)
subwindow.configure(bg="#222222", pady="10")
subwindow.grid(row=8, column=0, columnspan=3)

subwindow2 = tkinter.Frame(window)
subwindow2.configure(bg="#222222", pady="10")
subwindow2.grid(row=18, column=0, columnspan=3)
window.columnconfigure(0, minsize=20)
window.columnconfigure(1, minsize=300)
window.columnconfigure(2, minsize=1)

# LinkChecker tests if the directory is OS valid and if so, sets the variable and label.
def LinkChecker(chosenDir, labelToCheck):
	if os.path.isdir(chosenDir):

		labelToCheck.configure(text=chosenDir)
	else:
		labelToCheck.configure(text="INVALID DIRECTORY")

## to do tomorrow
## check if in && out are valid, if not, grey out the process buttons. 
## add the link valid check to the rest of the buttons ( os.path.isfile(path))
## bonus - convert a bunch to functions or classes.

def packInDirectoryBtn():
	global Path_PackInputDir
	Path_PackInputDir = askdirectory()
	LinkChecker(Path_PackInputDir, lbl_pack_inDirDisplay)
	
def packInNotepadBtn():
	global Path_PackNotepad
	Path_PackNotepad = askopenfilename(filetypes = [("Text Files","*.txt")])
	lbl_pack_notepadDisplay.configure(text=Path_PackNotepad)

def packOutputBtn():
	global Path_PackOutputDIR
	Path_PackOutputDIR = askdirectory()
	lbl_pack_outDirDisplay.configure(text=Path_PackOutputDIR)
	
def PackBtn():
	filename = "/" + txt_pack_name.get() + ".upack"
	x = unrealPakDIR + " " + Path_PackOutputDIR + filename + " -create=" + Path_PackInputDir
	subprocess.call(x, shell=True)
	print x

def PackNotepadBtn():
	filename = txt_pack_name.get() + ".upack"
	X = unrealPakDIR + " " + Path_PackOutputDIR + filename + " -create=" + Path_PackNotepad
	subprocess.call(X, shell=False)
	
def unpackFromBtn():
	global Path_UnpackInputDir
	Path_UnpackInputDir = askopenfilename(filetypes = [("PAK Files","*.upack")])
	lbl_unpack_fromDirDisplay.configure(text=Path_UnpackInputDir)

def unpackToBtn():
	global Path_UnpackOutputDir
	Path_UnpackOutputDir = askdirectory()
	lbl_unpack_toDirDisplay.configure(text=Path_UnpackOutputDir)

def unpackBtn():
	x = unrealPakDIR + " " + Path_UnpackInputDir + " -Extract " + Path_UnpackOutputDir
	subprocess.call(x, shell=False)
	print x
	

def toolPathBtn():
	global unrealPakDIR 
	x = askopenfilename(filetypes = [("exe files","*.exe")])
	unrealPakDIR = '"' + x + '"'
	lbl_tool.configure(text=unrealPakDIR)

# Packaging Parts
lbl_pack = tkinter.Label(window, text="Packaging", bg="#222222", fg="#FFFFFF", font=(None, 18, "bold"))
btn_pack_inDir = tkinter.Button(window, text="Input Directory", command=packInDirectoryBtn, width=14)
lbl_pack_inDirDisplay = tkinter.Label(window, text=Path_PackInputDir, bg="#222222", fg="#FFFFFF")

btn_pack_notepad = tkinter.Button(window, text="Input Notepad", command=packInNotepadBtn, width=14)
lbl_pack_notepadDisplay = tkinter.Label(window, text=Path_PackNotepad, bg="#222222", fg="#FFFFFF")

btn_pack_outDir = tkinter.Button(window, text="Output Directory", command=packOutputBtn, width=14)
lbl_pack_outDirDisplay = tkinter.Label(window, text=Path_PackOutputDIR, bg="#222222", fg="#FFFFFF")

txt_pack_name = tkinter.Entry(subwindow)
txt_pack_name.insert(0, Pack_Filename)

btn_pack_pack = tkinter.Button(subwindow, text="Package (Directory)", command = PackBtn, bg="green", width=14)
btn_pack_notepack = tkinter.Button(subwindow, text="Package (Notepad)", command = PackNotepadBtn, bg="green", width=14)

# Unpackaging
lbl_unpack = tkinter.Label(window, text="Unpacking", bg="#222222", fg="#FFFFFF", font=(None, 18, "bold"))
btn_unpack_fromDir = tkinter.Button(window, text="Pak File", command=unpackFromBtn, width=14)
lbl_unpack_fromDirDisplay = tkinter.Label(window, text=Path_UnpackInputDir, bg="#222222", fg="#FFFFFF")

btn_unpack_toDir = tkinter.Button(window, text="Output Directory", command=unpackToBtn, width=14)
lbl_unpack_toDirDisplay = tkinter.Label(window, text=Path_UnpackOutputDir, bg="#222222", fg="#FFFFFF")

btn_pack_unpack = tkinter.Button(subwindow2, text="Unpack", command = unpackBtn, bg="green", width=14)

# pak tool
lbl_OptionsHeader = tkinter.Label(window, text="Options", bg="#222222", fg="#FFFFFF", font=(None, 18, "bold"))
btn_toolDir = tkinter.Button(window, text="UnrealPak.exe", command=toolPathBtn, width=14)
lbl_tool = tkinter.Label(window, text=unrealPakDIR, bg="#222222", fg="#FFFFFF")

spacer = ttk.Separator().grid(row=10,columnspan=6, sticky='EW', pady=5, padx = 10)


#Batch add all widgets
	# packaging
lbl_pack.grid(row=0, column=0, columnspan=3, pady=6) # Header
btn_pack_inDir.grid(row=5, column=0, sticky='W', padx = 5)
lbl_pack_inDirDisplay.grid(row=5, column=1, sticky='W', columnspan=2)
btn_pack_notepad.grid(row=6, column=0, sticky='W', padx = 5)
lbl_pack_notepadDisplay.grid(row=6, column=1, sticky='W', columnspan=2)
btn_pack_outDir.grid(row=7, column=0, sticky='W', padx = 5)
lbl_pack_outDirDisplay.grid(row=7, column=1, sticky='W', columnspan=2)
txt_pack_name.grid(row=0, column=0, sticky='w', padx = 5) # Inside subwindow
btn_pack_pack.grid(row=0, column=1, sticky='W', padx = 5) # Inside subwindow
btn_pack_notepack.grid(row=0, column=2, sticky='W', padx = 5) # Inside subwindow
	# unpackaging
lbl_unpack.grid(row=15, column=0, columnspan=3, pady=6) # HEADER
btn_unpack_fromDir.grid(row=16, column=0, sticky='W', padx = 5)
lbl_unpack_fromDirDisplay.grid(row=16, column=1, sticky='W', columnspan=2)
btn_unpack_toDir.grid(row=17, column=0, sticky='W', padx = 5)
lbl_unpack_toDirDisplay.grid(row=17, column=1, sticky='W', columnspan=2)
btn_pack_unpack.grid(row=0, column=0) # Inside subwindow2

spacer = ttk.Separator().grid(row=20,columnspan=6, sticky='EW', pady=5, padx = 5)

	#tool path
lbl_OptionsHeader.grid(row=98, column=0, columnspan=3) # HEADER
btn_toolDir.grid(row=99, column=0, sticky='w', padx = 5)
lbl_tool.grid(row=99, column=1, sticky='w')


window.mainloop()
