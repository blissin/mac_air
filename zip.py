import zipfile
archive = zipfile.ZipFile('mail.zip', 'r')
#Let us verify the operation..
txtdata = archive.read('mail.txt')
print(txtdata)
