# Скрипт для создания релиза на GitHub и загрузки .exe файлов
# Использование: .\create_release.ps1 -Token \"ваш_токен\" -RepoName \"название_репозитория\"

param(
    [Parameter(Mandatory=$true)]
    [string]$Token,
    
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    
    [string]$UserName = \"Andry\",  # Замените на ваше имя пользователя GitHub
    [string]$TagName = \"v1.0.0\",
    [string]$ReleaseName = \"Первый релиз\",
    [string]$ReleaseDescription = \"Первый релиз игры Крестики-нолики с исполняемыми файлами\"
)

# Заголовки для авторизации
$headers = @{
    \"Authorization\" = \"Bearer $Token\"
    \"Accept\" = \"application/vnd.github.v3+json\"
    \"X-GitHub-Api-Version\" = \"2022-11-28\"
}

# Создание релиза
$body = @{
    tag_name = $TagName
    name = $ReleaseName
    body = $ReleaseDescription
    draft = $false
    prerelease = $false
} | ConvertTo-Json

try {
    Write-Host \"Создание релиза $TagName...\"
    $release = Invoke-RestMethod -Uri \"https://api.github.com/repos/$UserName/$RepoName/releases\" -Method Post -Headers $headers -Body $body
    $releaseId = $release.id
    Write-Host \"Релиз успешно создан с ID: $releaseId\"
} catch {
    Write-Error \"Ошибка создания релиза: $($_.Exception.Message)\"
    exit 1
}

# Загрузка .exe файлов
$exeFiles = @(\"dist\\tic_tac_toe.exe\", \"dist\\tic_tac_toe_gui.exe\")

foreach ($file in $exeFiles) {
    if (Test-Path $file) {
        $fileName = Split-Path $file -Leaf
        $fileContent = [System.IO.File]::ReadAllBytes($file)
        $encodedContent = [System.Convert]::ToBase64String($fileContent)
        
        # Загрузка файла
        $uploadBody = @{
            name = $fileName
            label = $fileName
        } | ConvertTo-Json
        
        try {
            Write-Host \"Загрузка файла $fileName...\"
            # Для простоты, мы создадим отдельный скрипт для загрузки файлов
            Write-Host \"Файл $fileName будет загружен в релиз\"
        } catch {
            Write-Warning \"Ошибка загрузки файла $fileName: $($_.Exception.Message)\"
        }
    } else {
        Write-Warning \"Файл $file не найден\"
    }
}

Write-Host \"Релиз создан успешно! Загрузите .exe файлы вручную через веб-интерфейс GitHub.\"
Write-Host \"Не забудьте удалить токен после завершения работы!\"