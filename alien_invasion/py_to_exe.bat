rd /s/q dist
del *.spec

set outpath=E:\Users\franc\python\project\%2\%2_%3.7z

pyinstaller -D -w  %1  --add-data  "images;images" -n %2_%3.exe

del  /s/q  E:\Users\franc\pythonProject\%2\*.7z
7z a -t7z %outpath% .\dist\%2_%3.exe\*
