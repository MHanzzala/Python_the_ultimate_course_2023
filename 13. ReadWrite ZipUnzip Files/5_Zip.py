
from zipfile import ZipFile

with ZipFile('ZippedFiles.zip', 'w') as zip:
    zip.write("New Folder")
