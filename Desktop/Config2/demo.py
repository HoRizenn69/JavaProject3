"""Демонстрация этапа 1: ошибки и вывод параметров."""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
CRATES = "https://crates.io/api/v1"


def run_case(title, args):
    """Запускает один сценарий и печатает его вывод."""
    print(f"=== {title} ===")
    env = os.environ.copy()
    env["PYTHONPATH"] = ROOT
    cmd = [sys.executable, "-m", "src.main", *args]
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    if not result.stdout and not result.stderr:
        print("(нет вывода)")
    print()


def run_unit_tests():
    """Запускает unittest и печатает результат."""
    print("=== unit tests ===")
    env = os.environ.copy()
    env["PYTHONPATH"] = ROOT
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    print()


def main():
    """Точка входа демо этапа 1."""
    print(f"Working dir: {ROOT}")
    print(f"Python: {sys.executable}")
    print(f"Version: {sys.version}")
    print()

    main_py = os.path.join(ROOT, "src", "main.py")
    if not os.path.isfile(main_py):
        print(f"ERROR: нет файла {main_py}")
        print("Скопируйте всю папку этапа 1 целиком.")
        input("Enter...")
        return 1

    run_case(
        "TEST 1: no --package",
        ["--repo", CRATES, "--output", "graph.svg"],
    )
    run_case(
        "TEST 2: no --output",
        ["--package", "serde", "--repo", CRATES],
    )
    run_case(
        "TEST 3: bad extension",
        [
            "--package",
            "serde",
            "--repo",
            CRATES,
            "--output",
            "x.txt",
        ],
    )
    run_case(
        "TEST 4: path without --test-mode",
        [
            "--package",
            "serde",
            "--repo",
            "fixtures/repo_simple.txt",
            "--output",
            "graph.svg",
        ],
    )
    run_case(
        "TEST 5: missing test file",
        [
            "--package",
            "A",
            "--repo",
            "missing.txt",
            "--output",
            "graph.svg",
            "--test-mode",
        ],
    )
    run_case(
        "TEST 6: success crates.io",
        [
            "--package",
            "serde",
            "--repo",
            CRATES,
            "--output",
            "graph.svg",
            "--filter",
            "syn",
        ],
    )
    run_case(
        "TEST 7: success test-mode",
        [
            "--package",
            "A",
            "--repo",
            "fixtures/repo_simple.txt",
            "--output",
            "out.svg",
            "--test-mode",
        ],
    )
    run_unit_tests()
    print("=== DONE ===")
    input("Нажмите Enter, чтобы закрыть...")
    return 0


if __name__ == "__main__":
    sys.exit(main())
