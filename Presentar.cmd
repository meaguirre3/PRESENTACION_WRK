@echo off
cd /d "%~dp0"
call quarto render presentacion.qmd
if errorlevel 1 goto fallo
py -3.14 sesion.py
if not errorlevel 1 exit /b 0
:fallo
pause
exit /b 1
