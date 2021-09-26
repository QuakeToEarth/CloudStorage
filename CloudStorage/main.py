import dropbox

token = "sl.A5MECk15ulV0WUyNcSTWItAWIqX6Ms4n4b73zkOu-9PDQR8Zv7dTCcOBWvv3Z3J-JUQWd0qZAP0_bjnCNY8yJlfiYWPSExZoOxX-d3sns7G6ApE9ag2RPYBTkCHfOowjqRDuIkwozok"
dbx = dropbox.Dropbox(token)

f = open("text.txt", "rb")
dbx.files_upload(f.read(),"/AliciaCloud/text.txt")