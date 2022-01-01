rd /s/q dist
del *.spec
pyinstaller -F -w  %1  --add-data  "images;images" -n Calculator_%2.exe
