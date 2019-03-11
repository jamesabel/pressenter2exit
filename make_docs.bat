REM rmdir /S /Q build
REM remember to run activate.bat before running this
venv\Scripts\sphinx-apidoc.exe -f -o source pressenter2exit
call make.bat html

