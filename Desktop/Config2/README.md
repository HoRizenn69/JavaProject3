# Визуализация графа зависимостей Cargo — этап 1

## 1. Общее описание

Минимальный CLI-прототип практической работы №2
(вариант №16). На этапе 1 приложение читает параметры
командной строки, проверяет их и выводит в формате
ключ-значение. Сбор зависимостей Cargo и визуализация —
на следующих этапах.

## 2. Описание функций и настроек

| Параметр | Назначение |
| --- | --- |
| `--package` | Имя анализируемого пакета |
| `--repo` | URL репозитория или путь к тестовому файлу |
| `--test-mode` | Режим тестового репозитория |
| `--output` | Имя файла изображения графа (`.svg`/`.png`) |
| `--filter` | Подстрока для фильтрации пакетов |

## 3. Сборка и запуск (Windows)

Требования: Python 3.8+ (с галкой **Add to PATH** при установке).

### Способ 1 — демо всех проверок

Двойной клик по `run.bat` **или** в `cmd.exe`:

```bat
cd /d путь\к\этап 1
run.bat
```

Либо напрямую:

```bat
cd /d путь\к\этап 1
py -3 demo.py
```

Если `py` не найден:

```bat
python demo.py
```

### Способ 2 — один запуск вручную

В `cmd.exe` из папки проекта:

```bat
cd /d путь\к\этап 1
set PYTHONPATH=.
py -3 -m src.main --package serde --repo "https://crates.io/api/v1" --output graph.svg --filter syn
```

### Юнит-тесты

```bat
cd /d путь\к\этап 1
set PYTHONPATH=.
py -3 -m unittest discover -s tests -v
```

### Запуск из PyCharm

1. Открыть папку `этап 1` как проект.
2. Interpreter: установленный Python 3.
3. ПКМ по `demo.py` → **Run**,  
   либо ПКМ по `src/main.py` → **Run** с Parameters, например:

```text
--package serde --repo https://crates.io/api/v1 --output graph.svg --filter syn
```

Environment: `PYTHONPATH=.`  
Working directory: папка `этап 1`.

## 4. Примеры использования

Успешный вывод параметров:

```text
=== Параметры конфигурации ===
package=serde
repo=https://crates.io/api/v1
test_mode=False
output=graph.svg
filter=syn
================================
```

Ошибка без `--package`:

```text
Ошибка: не задан параметр --package
```
