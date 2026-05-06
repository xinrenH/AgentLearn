$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root

$python = Join-Path $root ".venv\Scripts\python.exe"
if (!(Test-Path -LiteralPath $python)) {
    Write-Host "未找到虚拟环境，请先执行：py -m venv .venv" -ForegroundColor Red
    exit 1
}

$envFile = Join-Path $root ".env"
$devEnvFile = Join-Path $root ".env.dev"
if (!(Test-Path -LiteralPath $envFile) -and (Test-Path -LiteralPath $devEnvFile)) {
    Copy-Item -LiteralPath $devEnvFile -Destination $envFile -Force
}

& $python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
