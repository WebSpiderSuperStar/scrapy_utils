all: lint test clean
.PHONY: test lint release clean


# system python interpreter. used only to create virtual environment
PY = python3
VENV = venv
BIN=$(VENV)/bin
MIRRORS="https://pypi.tuna.tsinghua.edu.cn/simple"

# make it work on windows too
ifeq ($(OS), Windows_NT)
    BIN=$(VENV)/Scripts
    PY=python
endif


$(VENV): requirements.txt
	$(PY) -m pip install --upgrade -i $(MIRRORS) pip
	$(PY) -m venv $(VENV);
	$(BIN)/pip install --upgrade -i $(MIRRORS) pip
	if [ -f requirements.txt ]; then $(BIN)/pip install -Ur requirements.txt; fi
	-$(BIN)/pip install -e .
	touch $(VENV)


test:
	$(BIN)/pip install -Ui  $(MIRRORS) pytest
	-$(BIN)/pytest
	rm -rf .pytest_cache


lint:
	python -m pip install -Ui $(MIRRORS) flake8 autopep8
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --exclude venv --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --exclude venv --statistics
	-find . -path './venv' -a -prune -o -name "*.py" -print | xargs autopep8 --exclude venv  --in-place


release: $(VENV)
	-$(BIN)/python setup.py sdist bdist_wheel upload


source_release:
	git add -A
	git commit -m "commit"
	-git push origin master


docker_release:
	make clean
	/usr/bin/env bash Deploy/dockerRelease

clean:
	-rm -rf $(VENV)
	-find . -type f -name *.pyc -delete
	-find . -type d -name __pycache__ -delete
