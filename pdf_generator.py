# Import the required module and sub-modules
from PyPDF2 import PdfFileWriter, PdfFileReader
import os, csv
import random
import string


# генерация рандомных паролей
def generate_random_password(length):
    letters = string.ascii_lowercase
    rand_password = ''.join(random.choice(letters) for i in range(length))
    return rand_password



items = {}



# Create a PdfFileWriter object
result = PdfFileWriter()

# Перебирает папку
dr_name = "D:\ИБ\proj\pdf_encrypt\pdf"

def lst_dir(dir_name=dr_name):
    pt = os.listdir(dir_name)
    return pt


# сохранение файла
def save_info(items, file_name="log.csv"):
    with open(file_name, "a") as file:
        writer = csv.writer(file, delimiter=",")
        for k, v in items.items():
            writer.writerow([k, v])




def crypt():
    for dr in lst_dir():
        # Open the pdf file to encrypt
        file = PdfFileReader(f"pdf\{dr}")
        # Retrieve the number of pages to iterate in the original document
        length = file.numPages

        # Iterates through every page and adds it to the new file (a copy of the original)
        for i in range(length):
            pages = file.getPage(i)
            result.addPage(pages)

        # Creates a variable password.
        password = generate_random_password(8)

        # Encrypt the file using the created password 
        result.encrypt(password)

        # Open a new file 'Magazines.pdf' and write the encrypted pdf file
        with open(f'pdf_with_password\{dr}','wb') as f:
            result.write(f)

        items[dr] = password

def main():
    crypt()
    save_info(items)

if __name__ == '__main__':
    main()





