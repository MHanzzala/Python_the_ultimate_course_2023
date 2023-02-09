
from zipfile import ZipFile


with ZipFile("zip_text.zip", 'r') as zip:

    zip.extractall()
    print('\n','Your Files extracted!')