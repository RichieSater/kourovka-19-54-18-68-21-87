SHELL := /bin/bash

.PHONY: check structure tracker status

check: structure tracker
	git diff --check

structure:
	python3 scripts/check_structure.py

tracker:
	python3 scripts/check_tracker.py

status:
	@sed -n '1,120p' STATUS.md
