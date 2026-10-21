#!/bin/bash
set -e
cd "$(dirname "$0")"
export PYTHONPATH="."

CRATES="https://crates.io/api/v1"
PY="python3 -m src.main"

echo "=== ТЕСТ 1: Ошибка — нет --package ==="
set +e
$PY --repo "$CRATES" --output graph.svg
set -e

echo "=== ТЕСТ 2: Ошибка — нет --output ==="
set +e
$PY --package serde --repo "$CRATES"
set -e

echo "=== ТЕСТ 3: Ошибка — плохое расширение ==="
set +e
$PY --package serde --repo "$CRATES" --output x.txt
set -e

echo "=== ТЕСТ 4: Ошибка — путь без --test-mode ==="
set +e
$PY --package serde --repo fixtures/repo_simple.txt \
  --output graph.svg
set -e

echo "=== ТЕСТ 5: Ошибка — нет файла test-mode ==="
set +e
$PY --package A --repo missing.txt \
  --output graph.svg --test-mode
set -e

echo "=== ТЕСТ 6: Успех — crates.io URL ==="
$PY --package serde \
  --repo "$CRATES" \
  --output graph.svg \
  --filter syn

echo "=== ТЕСТ 7: Успех — тестовый репозиторий ==="
$PY --package A \
  --repo fixtures/repo_simple.txt \
  --output out.svg \
  --test-mode

echo "=== Юнит-тесты ==="
python3 -m unittest discover -s tests -v

echo "=== ГОТОВО ==="
echo
echo "Нажмите Enter, чтобы закрыть окно..."
read -r _
