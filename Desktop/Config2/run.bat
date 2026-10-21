@echo off
cd /d "%~dp0"
echo Starting demo.py ...
py -3 demo.py
if errorlevel 1 python demo.py
if errorlevel 1 (
  echo.
  echo ERROR: не удалось запустить Python.
  echo Установите Python с python.org и отметьте Add to PATH.
  pause
)
