pushd .
cd ..
call venv\Scripts\activate.bat
set PYTHONPATH=%CD%
python examples\example_runtime.py
call deactivate
popd
set PYTHONPATH=
