#!/usr/bin/env python3

# Code Create by Spectrasonic

# =============
# =  Imports  =
# =============

from PIL import Image # python3 -m pip install -U Pillow
from colorama import Fore   # python3 -m pip install -U colorama
from PyPDF4 import PdfFileMerger #python3 -m pip install -U PyPDF4
import qrcode # python3 -m pip install -U qrcode
import os

# python3 -m pip install -U Pillow colorama PyPDF4 qrcode

# ===================
# =  FN Variabbles  =
# ===================

cfolder = os.getcwd() + "/"
directory = "Converted"
path = os.path.join(cfolder, directory)

# ======================
# =  FN Create Folder  =
# ======================

def create_folder():
    os.mkdir(path)
    print("")
    print(Fore.GREEN + "Directory '%s' created" %directory)
    print("")

# ===================
# = FN Webp to PNG  =
# ===================

def webp_to_png():
    cfolder = os.getcwd() + "/"
    for filename in os.listdir(cfolder):
        name, extension = os.path.splitext(cfolder + filename)
        if extension in [".webp"]:
            img = Image.open(cfolder + filename).convert("RGB")
            img.save(path + "/" + filename +".png", "png")
            print(Fore.YELLOW + "Converted "+ filename)
        else:
            print(Fore.RED + "Nothing to Convert")
            exit()

# ====================
# =  FN PNG to WebP  =
# ====================

def png_to_webp():
    
    for filename in os.listdir(cfolder):
        name, extension = os.path.splitext(cfolder + filename)
        if extension in [".png"]:
            img = Image.open(cfolder + filename).convert("RGB")
            img.save(path + "/" + filename +".webp", "webp")
            print(Fore.YELLOW + "Converted "+ filename)
        else:
            print(Fore.RED + "Nothing to Convert")
            exit()

# ===================
# =  FN JPG to PNG  =
# ===================

def jpg_to_png():
    for filename in os.listdir(cfolder):
        name, extension = os.path.splitext(cfolder + filename)
        if extension in [".jpg"]:
            img = Image.open(cfolder + filename).convert("RGB")
            img.save(path + "/" + filename +".png", "png")
            print(Fore.YELLOW + "Converted "+ filename)
        else:
            print(Fore.RED + "Nothing to Convert")
            exit()

# ===================
# =  FN IMG to PDF  =
# ===================
def img_to_pdf():
    if not os.path.exists('output'):
        os.makedirs('output')

    images = [file for file in os.listdir('.') if file.endswith(('jpg', 'jpeg', 'png'))]

    for image in images:
        im = Image.open(image)
        filename = os.path.splitext(image)[0]
        im.save(f'output/{filename}.pdf', 'PDF', resolution=100.0)
        print(Fore.YELLOW + f'Converted {image} to pdf')

    print(Fore.GREEN + 'All images converted to pdf')

# ===================
# =  FN PDF Merger  =
# ===================

def pdf_merger():
    merger = PdfFileMerger()

    pdf_file = [file for file in os.listdir('.') if file.endswith(('.pdf'))]

    for pdf in pdf_file:
        merger.append(pdf)
        print(Fore.YELLOW + f'Merge {pdf} to the pdf')

    merger.write('merged.pdf')
    merger.close()

    for filename in os.listdir():
        if filename != ( 'merged.pdf') and filename.endswith('.pdf'):
            os.remove(filename)

# ==========================
# =  FN Compress function  =
# ==========================

def compress_images():
    cfolder = os.getcwd() + "/"
    directory = "Compressed"
    path = os.path.join(cfolder, directory)

    os.mkdir(path)
    print("")
    print("Directory '%s' created" %directory)
    print("")

    for filename in os.listdir(cfolder):
        extension = os.path.splitext(cfolder + filename)

        if extension in [".webp", ".jpg", ".jpeg", ".png"]:
            picture = Image.open(cfolder + filename)
            picture.save(path + "/" + filename, optimize=True, quality=40)
            print(Fore.YELLOW + "compress "+filename)
        else:
            print(Fore.RED + "Nothing to Compress")
            exit()

# =======================
# =  QR Code Generator  =
# =======================

def qrgen():
    workd = os.getcwd() + "/"
    data = input(Fore.GREEN + "Enter Link: " + Fore.RESET)

    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    image = qr.make_image(fill="black", back_color="white")

    image.save(workd +"qr_code.png")

    print("")
    print(Fore.YELLOW + "QR Code Generated")

# ====================
# =  Main Function  =
# ====================

def main():
    print('''
    ██████╗ ██╗   ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██████╔╝ ╚████╔╝    ██║   ██║   ██║██║   ██║██║     ███████╗
    ██╔═══╝   ╚██╔╝     ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║        ██║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝        ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
    
Select an option:

    '''
    )
    print(Fore.GREEN + "1 - Convert WebP to PNG")
    print(Fore.GREEN + "2 - Convert PNG to WebP")
    print(Fore.GREEN + "3 - Convert JPG to PNG")
    print(Fore.GREEN + "4 - Convert IMG to PDF")
    print(Fore.YELLOW + "5 - MERGE PDF")
    print(Fore.GREEN + "QR - GENERATE QR")
    print(Fore.CYAN + "C - Compress Images")
    print(Fore.RED + "Q - Exit")

    print("")
    choice = input(Fore.BLUE + "Enter choice: " + Fore.RESET)

    if choice == "1":
        create_folder()
        webp_to_png()
    elif choice == "2":
        create_folder()
        png_to_webp()
    elif choice == "3":
        create_folder()
        jpg_to_png()
    elif choice == "4":
        img_to_pdf()
    elif choice == "5":
        pdf_merger()
    elif choice == "qr" or choice == "QR":
        qrgen()
    elif choice == "c" or choice == "C":
        compress_images()
    elif choice == "q" or choice == "Q":
        print(Fore.BLUE + "❮❯", Fore.RESET + "With", Fore.RED + "❤️", Fore.RESET + "by Spectrasonic")
        exit()
    else:
        os.system('clear')
        main()

# ===================
# =  Init function  =
# ===================

if __name__ == "__main__":
    main()