
project_dir := justfile_directory()

@help:
  just --list

@setup:
  uv sync

@test *params:
  uv run pytest -vv -x -o log_cli=true {{ params }}

@test-all:
  uv run pytest --capture=no -o log_cli=false tests/

@lint:
  uv run ruff check

@fix:
  uv run ruff check --fix

@format:
  uv run ruff format

@check-format:
  uv run ruff format --check

@check-mypy:
  uv run mypy .
