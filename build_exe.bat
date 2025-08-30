@echo off
echo Создание исполняемых файлов для игры "Крестики-нолики"
echo.

echo Установка PyInstaller...
pip install pyinstaller
echo.

echo Создание .exe для консольной версии...
pyinstaller --onefile --console tic_tac_toe.py
echo.

echo Создание .exe для графической версии...
pyinstaller --onefile --windowed tic_tac_toe_gui.py
echo.

echo Готово! Исполняемые файлы находятся в папке dist:
echo - tic_tac_toe.exe (консольная версия)
echo - tic_tac_toe_gui.exe (графическая версия)
echo.

pause