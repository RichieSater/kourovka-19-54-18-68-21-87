SHELL := /bin/bash

.PHONY: check structure status

check: structure
	git diff --check

structure:
	python3 scripts/check_structure.py

status:
	@sed -n '1,120p' STATUS.md
