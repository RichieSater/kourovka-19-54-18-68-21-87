#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

expected="Tectonic 0.17.0"
actual="$(tectonic --version)"
if [[ "$actual" != "$expected" ]]; then
  printf 'Expected %s, found %s\n' "$expected" "$actual" >&2
  exit 1
fi

tectonic --keep-logs --keep-intermediates main.tex

if grep -E 'Warning|Overfull|Underfull|undefined|Error' main.log; then
  echo "LaTeX log contains a review-blocking diagnostic." >&2
  exit 1
fi

pages="$(pdfinfo main.pdf | awk '/^Pages:/ {print $2}')"
if [[ -z "$pages" || "$pages" -lt 1 ]]; then
  echo "Built PDF has no readable page count." >&2
  exit 1
fi

printf 'Manuscript build passed: %s pages with %s.\n' "$pages" "$actual"
