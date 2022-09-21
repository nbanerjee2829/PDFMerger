import os.path
import tkinter as tk
from tkinter import ttk
import glob

import self as self
from PyPDF2 import PdfFileMerger
from tkinter import filedialog
import subprocess
import queue


FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
pdfs_to_convert = []
offset = 20
files_selected = queue.LifoQueue()
# Function for opening the
# file explorer window
def explore(path):
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        print("heheh")
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        print("ASD")
        subprocess.run([FILEBROWSER_PATH, '/select,', os.path.normpath(path)])
# done = False

def browseFiles():
    global offset
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("PDF",
                                                      "*.pdf*"),
                                                     ("all files",
                                                      "*.*")))

    pdfs_to_convert.append(filename)
    print(pdfs_to_convert)
    baseName = os.path.basename(filename)
    # lastpos = -1;
    # pos = 0;
    # if(lastpos == pos):
    #     pos +=1;
    # Change label contents
    label_file_explorer.configure(text="File Opened: " + baseName)
    # text.delete('1.0', 'end')
    files_selected.put(baseName)
    # text.insert(1, f'Got {files_selected.get()}\n')
    b1_text = tk.StringVar()
    b1 = tk.Button(root, textvariable=b1_text,
                                  bg="#579DF2", width=30,
                                  height=2, relief="flat",
                                  borderwidth=0, fg="white")
    b1_text.set(baseName)

    b1.place(x=320, y=100 + offset)
    offset +=50;
    # lastpos = pos;

        # position = f'{i}.0'
        # text.insert(position, f'Got {files_selected.get()}\n')

def merger():
    pdf_merger = PdfFileMerger()
    print(pdfs_to_convert)
    for path in pdfs_to_convert:
        print(path)
        pdf_merger.append(path)

    with open( 'MergedOutputs/pdf_merger2.pdf', 'wb') as fileobj:
        pdf_merger.write(fileobj)

    os.system(os.path.realpath('MergedOutputs/pdf_merger2.pdf'))




root = tk.Tk()
root.resizable(False, False)
canvas = tk.Canvas(root, width= 600, height=500,bg="#000000")
canvas.grid(columnspan=4, rowspan=3)
# text = tk.Text(root, height=10,width=30)
# text.grid(row=0, column=2, sticky=tk.EW)
# text.place(x=300, y=50)
instructions = tk.Label(root, text="MERGE PDFs",font=("Arial", 20, "bold"),
                        bg="#555E5A",fg="white")

instructions.place( x=33.5, y=100)
info_text = tk.Label(root, text="Because looking \nfor a free one sucks!!",font=("Arial", 15),
                        bg="#555E5A",fg="white")
info_text.place(x=33.5,y=250)
canvas.create_rectangle(0, 600, 250, 0, fill="#555E5A")
browse_text = tk.StringVar()
select_pdf_button = tk.Button(root, textvariable=browse_text,
                              bg="#579DF2",width=30,
                              height=2, relief="flat",
                              borderwidth=0,fg="white",
                              command = browseFiles)
browse_text.set("Select PDFs")
select_pdf_button.place(x=320,y=350)
browse_text = tk.StringVar()
merge_button = tk.Button(root, textvariable=browse_text,
                         bg="#579DF2",width=30,height=2,
                         relief="flat",borderwidth=0,fg="white",
                         command= merger)
browse_text.set("Merge")
merge_button.place(x=320, y=420)
label_file_explorer = tk.Label(root,
                            text = "File Explorer using Tkinter",
                            width = 20, height = 2,
                            fg = "white", bg="#000000")
label_file_explorer.place(x=330, y=10)
# create the text widget


# scrollbar = ttk.Scrollbar(root, orient='vertical', command=text.yview)
# scrollbar.grid(row=0, column=3, sticky=tk.NS)
# scrollbar.place(x=530, y=50)
# text['yscrollcommand'] = scrollbar.set

root.mainloop()