# Main window for app
import util
import tkinter as tk
from tkinter import font
from tkinter import messagebox


def run(option, source, dest):

    try:
        if option == 'split':
            count = util.split(source[0], dest)
            messagebox.showinfo(message=f'Complete!, Created {count} files')
        elif option == 'merge':
            util.merge(source, dest)
            messagebox.showinfo(message='Merge Complete!')
    except FileNotFoundError:
        messagebox.showinfo(message='Sorry, File not found!')

# ----------------------------------------------------------


# Main Window
mainWindow = tk.Tk()
mainWindow.title('pdfMods')
mainWindow.geometry('700x300')
mainWindow.configure(background='#fff')

# Title
title_font = font.Font(family='Helvetica', name='appHighlightFont', size=14, weight='bold')
title_label = tk.Label(mainWindow, text='pdfMODS', font=title_font, background='#fff', fg='#db3a34').grid(column=0, row=0, columnspan=4)

# Main
# Source file(s)
source = tk.Variable()
source_label = tk.Label(mainWindow, text='Source File', pady=20, padx=10, font='TkHeadingFont 10 bold italic', bg='#FFFFFF', fg='#4C5454')
source_label.grid(column=0, row=1, sticky='w')
source_entry = tk.Entry(mainWindow,textvariable=source, width=80, fg='#001f3f', bg='#e9ecef')
source_entry.grid(column=1, row=1, columnspan=2, ipady=8)
 # button
btn_browse_1 = tk.Button(mainWindow, text='Browse', command=lambda:util.set_text(source, util.get_names()), bg='#d3d3d3', fg='#202020', font='TkIconFont 10 bold italic', width=10, border=1)
btn_browse_1.grid(column=3, row=1, ipady=5, padx=20)

# Destination path
folder = tk.StringVar()
destination_label = tk.Label(mainWindow, text='Destination Path', padx=10, font='TkHeadingFont 10 bold italic', bg='#FFFFFF', fg='#4C5454')
destination_label.grid(column=0, row=2, sticky='w')
destination_entry = tk.Entry(mainWindow, textvariable=folder, width=80, fg='#001f3f', bg='#e9ecef')
destination_entry.grid(column=1, row=2, columnspan=2, ipady=8, pady=15)
# button
btn_browse_2 = tk.Button(mainWindow, text='Browse', command=lambda:util.set_text(folder, util.get_folder()), bg='#d3d3d3', fg='#202020', font='TkIconFont 10 bold italic', width=10, border=1)
btn_browse_2.grid(column=3, row=2, ipady=5, padx=20)

# Label Frame
l_frame = tk.LabelFrame(mainWindow, text='Options', bg='#FFF')
l_frame.grid(column=1, row=4, columnspan=2, sticky='E')
option = tk.StringVar(None, 'split')
split = tk.Radiobutton(l_frame, text='Split', variable=option, value='split', bg='#FFFFFF', font='TkHeadingFont 10 bold italic', fg='#4C5454')
merge = tk.Radiobutton(l_frame, text='Merge', variable=option, value='merge', bg='#FFFFFF', font='TkHeadingFont 10 bold italic', fg='#4C5454')
split.grid(column=1, row=1)
merge.grid(column=1, row=2)
# button
btn_run = tk.Button(mainWindow, text='Run', command=lambda:run(option.get(), source.get(), folder.get()), bg='#f94144', fg='white', font='TkIconFont 10 bold italic', width=10, border=1)
btn_run.grid(column=2, row=4, columnspan=2, ipady=5, padx=20)

# Column/Row Configs
mainWindow.columnconfigure(0, weight=0)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=0)
mainWindow.columnconfigure(3, weight=0)
mainWindow.rowconfigure(0, weight=0)
mainWindow.rowconfigure(1, weight=0)
mainWindow.rowconfigure(2, weight=0)
mainWindow.rowconfigure(3, weight=0)
mainWindow.rowconfigure(4, weight=0)

# ------------------------------------------------------------------------
mainWindow.mainloop()
