import tkinter as tk
from os.path import join as pjoin
from tkinter import filedialog
from pikepdf import Pdf


def get_name():
    """
    Collects the name of the file required.
    :return: List of file names.
    """
    file = tk.Tk()
    file.withdraw()
    path = filedialog.askopenfilename()
    return path


def get_names():
    """
    Collects the names of the files required.
    :return: List of file names.
    """
    files = tk.Tk()
    files.withdraw()
    paths = filedialog.askopenfilenames()
    return paths


def get_folder():
    direc = filedialog.askdirectory()
    return direc


def set_text(widget,text):
    widget.set(text)


def split(source, destination):
    """

    :param source: path for source file
    :param destination: Path for destination file
    :return: number of files, list of files created
    """

    count = 0
    output_filename = ""
    pdf = Pdf.open(source)
    
    for n, page in enumerate(pdf.pages):
        new_pdf = Pdf.new()
        new_pdf.pages.append(page)

        output_filename = 'Doc_page_{}.pdf'.format(count + 1)
        path_to_file = pjoin(destination, output_filename)
        new_pdf.save(path_to_file)
        count += 1

    return count


def merge(source, destination):
    """

    :param source:
    :return:
    """
    
    pdf = Pdf.new()

    for file in source:
        src =Pdf.open(file)
        pdf.pages.extend(src.pages)
    
    output_filename = 'Merge_Doc.pdf'
    path_to_file = pjoin(destination, output_filename)
    pdf.save(path_to_file)


def export(file):
    """

    :param file:
    :return:
    """
    pass
