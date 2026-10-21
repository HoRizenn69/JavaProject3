"""Тесты разбора и валидации конфигурации."""

import os
import sys
import tempfile
import unittest
from unittest import mock

ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)
sys.path.insert(0, ROOT)

from src.config import (  # noqa: E402
    build_parser,
    print_config,
    validate_config,
)


class TestConfig(unittest.TestCase):
    """Проверка параметров CLI этапа 1."""

    def test_parser_defaults(self):
        """Флаг test-mode по умолчанию выключен."""
        parser = build_parser()
        args = parser.parse_args(
            [
                "--package",
                "serde",
                "--repo",
                "https://crates.io/api/v1",
                "--output",
                "graph.svg",
            ]
        )
        self.assertFalse(args.test_mode)
        self.assertEqual(args.filter, "")

    def test_missing_package_exits(self):
        """Ошибка при отсутствии --package."""
        parser = build_parser()
        args = parser.parse_args(
            [
                "--repo",
                "https://crates.io/api/v1",
                "--output",
                "graph.svg",
            ]
        )
        with self.assertRaises(SystemExit):
            validate_config(args)

    def test_missing_output_exits(self):
        """Ошибка при отсутствии --output."""
        parser = build_parser()
        args = parser.parse_args(
            [
                "--package",
                "serde",
                "--repo",
                "https://crates.io/api/v1",
            ]
        )
        with self.assertRaises(SystemExit):
            validate_config(args)

    def test_bad_output_extension(self):
        """Ошибка при неверном расширении --output."""
        parser = build_parser()
        args = parser.parse_args(
            [
                "--package",
                "serde",
                "--repo",
                "https://crates.io/api/v1",
                "--output",
                "graph.txt",
            ]
        )
        with self.assertRaises(SystemExit):
            validate_config(args)

    def test_invalid_url_exits(self):
        """Ошибка при пути без --test-mode."""
        parser = build_parser()
        args = parser.parse_args(
            [
                "--package",
                "serde",
                "--repo",
                "not-a-url",
                "--output",
                "graph.svg",
            ]
        )
        with self.assertRaises(SystemExit):
            validate_config(args)

    def test_test_mode_ok(self):
        """Успешная валидация test-mode."""
        with tempfile.NamedTemporaryFile(
            mode="w",
            suffix=".txt",
            delete=False,
        ) as handle:
            handle.write("A: B\nB:\n")
            path = handle.name
        try:
            parser = build_parser()
            args = parser.parse_args(
                [
                    "--package",
                    "A",
                    "--repo",
                    path,
                    "--output",
                    "out.svg",
                    "--test-mode",
                    "--filter",
                    "XX",
                ]
            )
            validate_config(args)
            self.assertEqual(args.filter, "XX")
        finally:
            os.unlink(path)

    def test_print_config(self):
        """Печать ключ-значение не падает."""
        parser = build_parser()
        args = parser.parse_args(
            [
                "--package",
                "serde",
                "--repo",
                "https://crates.io/api/v1",
                "--output",
                "graph.svg",
            ]
        )
        validate_config(args)
        with mock.patch("builtins.print") as mocked:
            print_config(args)
            self.assertTrue(mocked.called)


if __name__ == "__main__":
    unittest.main()
