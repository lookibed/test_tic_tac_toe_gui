# Скрипт для публикации проекта на GitHub
# Использование: .\publish_to_github.ps1 -Token "ваш_токен" -RepoName "название_репозитория"

param(
    [Parameter(Mandatory=$true)]
    [string]$Token,
    
    [Parameter(Mandatory=$true)]
    [string]$RepoName,
    
    [string]$Description = "Крестики-нолики на Python с ИИ",
    [string]$UserName = "Andry"  # Замените на ваше имя пользователя GitHub
)

# Заголовки для авторизации
$headers = @{
    "Authorization" = "Bearer $Token"
    "Accept" = "application/vnd.github.v3+json"
    "X-GitHub-Api-Version" = "2022-11-28"
}

# Создание репозитория
$body = @{
    name = $RepoName
    description = $Description
    private = $false
} | ConvertTo-Json

try {
    Write-Host "Создание репозитория $RepoName..."
    $response = Invoke-RestMethod -Uri "https://api.github.com/user/repos" -Method Post -Headers $headers -Body $body
    Write-Host "Репозиторий успешно создан: $($response.html_url)"
} catch {
    if ($_.Exception.Response.StatusCode -eq 422) {
        Write-Host "Репозиторий уже существует, продолжаем..."
    } else {
        Write-Error "Ошибка создания репозитория: $($_.Exception.Message)"
        exit 1
    }
}

# Инициализация Git репозитория
Write-Host "Инициализация Git репозитория..."
git init
git add .
git commit -m "Initial commit"

# Добавление удаленного репозитория
$remoteUrl = "https://$Token@github.com/$UserName/$RepoName.git"
git remote add origin $remoteUrl

# Отправка изменений
Write-Host "Отправка изменений на GitHub..."
git push -u origin main

Write-Host "Проект успешно опубликован!"
Write-Host "Не забудьте удалить токен после завершения работы!"