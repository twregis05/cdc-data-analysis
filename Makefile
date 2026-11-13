PY ?= .venv/bin/python

.PHONY: all base-clean export serve

all: base-clean export  # TODO: add steps as they exist

base-clean:
	$(PY) -m jupyter nbconvert --to notebook --execute --inplace cleaning/base_clean.ipynb

export:
	$(PY) export/export_site.py

serve:
	cd site && python3 -m http.server 8000
