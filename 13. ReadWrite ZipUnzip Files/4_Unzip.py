
from zipfile import ZipFile


with ZipFile("Unzip.zip", 'r') as zip:

    zip.extractall()
    print('Files extracted!')
