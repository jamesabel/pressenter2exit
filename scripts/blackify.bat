pushd .
cd ..
call venv\Scripts\activate.bat
python -m black -l 192 pressenter2exit setup.py
call deactivate
popd
