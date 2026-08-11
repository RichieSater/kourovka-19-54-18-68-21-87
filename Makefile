SHELL := /bin/bash

.PHONY: check structure tracker notation proof-21-87 status

check: structure tracker notation proof-21-87
	git diff --check

structure:
	python3 scripts/check_structure.py

tracker:
	python3 scripts/check_tracker.py

notation:
	python3 scripts/check_finite_group_notation.py

proof-21-87:
	python3 problem-21-87/tests/check-manuscript.py --self-test

status:
	@sed -n '1,120p' STATUS.md
