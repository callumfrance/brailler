# Adding the following directory as the PYTHONPATH ensures that, among
# other libraries, the LibLouis 'louis' library is used from the device,
# located externally from the venv environment.
#
# 		/usr/lib/python3.8/site-packages
#

cli:
	. venv/bin/activate; \
	pip install -r requirements.txt; \
	export PYTHONPATH="/usr/lib/python3.8/site-packages"; \
	python main.py CLIView

braille:
	. venv/bin/activate; \
	pip install -r requirements.txt; \
	export PYTHONPATH="/usr/lib/python3.8/site-packages"; \
	python main.py BrailleView

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

.PHONY: test cli braille coverage
