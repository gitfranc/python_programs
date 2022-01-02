rd /s/q dist
del *.spec
pyinstaller -D -w  %1  --add-data  "images;images" -n Calculator_%3.exe

7z a -t7z E:\Users\franc\python\project\%2\Calculator_%3.7z .\dist\Calculator_%3.exe\*
