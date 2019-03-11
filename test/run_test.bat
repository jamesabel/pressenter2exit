pushd .
cd ..
set PYTHONPATH=.
venv\Scripts\python.exe test\test_pressenter2exit.py
venv\Scripts\python.exe test\test_pressenter2exitgui.py
popd
set PYTHONPATH=
