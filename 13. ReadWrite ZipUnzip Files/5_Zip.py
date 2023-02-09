
from zipfile import ZipFile

with ZipFile('zip_text_2.zip', 'w') as zip:
    zip.write("zip_text")
