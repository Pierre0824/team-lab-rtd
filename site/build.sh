#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"

if [[ -f "$ROOT/.venv/bin/activate" ]]; then
  # shellcheck disable=SC1091
  source "$ROOT/.venv/bin/activate"
fi

sphinx-build -b html "$ROOT/docs" "$ROOT/docs/_build/html"
echo "Built: $ROOT/docs/_build/html/index.html"
