@echo off
setlocal

echo Публикация проекта "Крестики-нолики" на GitHub
echo.

REM Установка параметров
set REPO_NAME=tic-tac-toe-py
set USER_NAME=Andry

REM Проверка наличия токена
if "%GITHUB_TOKEN%"=="" (
    echo ОШИБКА: Токен GitHub не найден!
    echo Установите переменную окружения GITHUB_TOKEN
    echo Пример: set GITHUB_TOKEN=ваш_токен
    pause
    exit /b 1
)

echo Создание репозитория и публикация кода...
powershell -ExecutionPolicy Bypass -File "publish_to_github.ps1" -Token "%GITHUB_TOKEN%" -RepoName "%REPO_NAME%" -UserName "%USER_NAME%"

if %ERRORLEVEL% NEQ 0 (
    echo ОШИБКА: Не удалось опубликовать проект
    pause
    exit /b 1
)

echo.
echo Создание релиза...
powershell -ExecutionPolicy Bypass -File "create_release.ps1" -Token "%GITHUB_TOKEN%" -RepoName "%REPO_NAME%" -UserName "%USER_NAME%"

echo.
echo Проект успешно опубликован на GitHub!
echo.
echo Следующие шаги:
echo 1. Перейдите в раздел Releases вашего репозитория
echo 2. Загрузите файлы tic_tac_toe.exe и tic_tac_toe_gui.exe в релиз
echo 3. Удалите токен GitHub после завершения работы
echo.

pause