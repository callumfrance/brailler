# Adding the following directory as the PYTHONPATH ensures that, among
# other libraries, the LibLouis 'louis' library is used from the device,
# located externally from the venv environment.
#
# 		/usr/lib/python3.8/site-packages
#

all:
	. venv/bin/activate; \
	export PYTHONPATH="/usr/lib/python3.8/site-packages"; \
	python main.py

test:
	. venv/bin/activate; \
	export PYTHONPATH="/usr/lib/python3.8/site-packages"; \
	python -m pytest

coverage:
	. venv/bin/activate; \
	export PYTHONPATH="/usr/lib/python3.8/site-packages"; \
	coverage run -m pytest; \
	coverage html; \
	xdg-open htmlcov/index.html

.PHONY: test all coverage
