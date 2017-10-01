rmdir /S /Q build
venv\Scripts\sphinx-apidoc.exe -f -o source pressenter2exit
call make.bat html
copy /Y source\index.rst .
