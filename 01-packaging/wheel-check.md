# Проверка wheel в отдельном окружении

Следующие команды — macOS/Linux, из `demo-project`. Они создают новую
временную папку и не меняют окружение разработки:

```bash
project_dir="$PWD"
check_dir="$(mktemp -d)"
uv venv --python 3.14 "$check_dir/venv"
uv pip install --python "$check_dir/venv/bin/python" "$project_dir/dist/seminar_text_tools-0.1.0-py3-none-any.whl"
cd "$check_dir"
"$check_dir/venv/bin/python" -I -c "import text_tools; print(text_tools.__file__); print(text_tools.count_words('hello world'))"
"$check_dir/venv/bin/text-tools" "hello world" --count
"$check_dir/venv/bin/python" -I -m text_tools "  hello   world  "
cd "$project_dir"
```

Ожидается путь внутри нового `site-packages`, затем `2`, `2`, `hello world`.
`-I` исключает влияние пользовательского `PYTHONPATH` и текущей папки
на импорт в проверочных вызовах Python.

В PowerShell можно выполнить эквивалент:

```powershell
$projectDir = (Get-Location).Path
$checkDir = Join-Path ([System.IO.Path]::GetTempPath()) ([guid]::NewGuid().ToString())
uv venv --python 3.14 "$checkDir/venv"
uv pip install --python "$checkDir/venv/Scripts/python.exe" "$projectDir/dist/seminar_text_tools-0.1.0-py3-none-any.whl"
Set-Location $checkDir
& "$checkDir/venv/Scripts/python.exe" -I -c "import text_tools; print(text_tools.__file__); print(text_tools.count_words('hello world'))"
& "$checkDir/venv/Scripts/text-tools.exe" "hello world" --count
& "$checkDir/venv/Scripts/python.exe" -I -m text_tools "  hello   world  "
Set-Location $projectDir
```


Для собственного проекта замените имя wheel, имя импортируемого пакета и команду
на свои. Перед проверкой выполните `uv build` в корне проекта.
