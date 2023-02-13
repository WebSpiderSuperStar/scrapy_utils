all: lint test clean

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

# generate requirements
REQS:
	if [[ ---f requirements.txt ]]; then
		# install pipreqs
		$(PY) -m pip install -U pipreqs
		# use pipreqs generate requirements
		pipreqs --encoding=utf-8 --force
	fi


# build a new VENV env
$(VENV): requirements.txt $(REQS)
	$(PY) -m pip install --upgrade -i $(MIRRORS) pip
	$(PY) -m venv $(VENV);
	$(BIN)/pip install --upgrade -i $(MIRRORS) pip
	[[ -f requirements.txt ]] && $(BIN)/pip install -Ur requirements.txt
	-$(BIN)/pip install -e .
	touch $(VENV)


test: $(VENV)
	$(BIN)/pip install -Ui  $(MIRRORS) pytest
	-$(BIN)/pytest
	rm -rf .pytest_cache


lint:
	$(PY) -m pip install -Ui $(MIRRORS) flake8 autopep8
	# stop the build if there are Python syntax errors or undefined names
	flake8 . --count --select=E9,F63,F7,F82 --show-source --exclude venv --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --exclude venv --statistics
	-find . -path './venv' -a -prune -o -name "*.py" -print | xargs autopep8 --exclude venv  --in-place


clean:
	@rm -rf $(VENV)
	@find . -type f -name *.pyc -delete && find . -type d -name __pycache__ -delete


run:
	python3 -Bu main.py


release: $(VENV)
	-$(BIN)/python setup.py sdist bdist_wheel upload


source_release:
	@git pull && git add -A && git commit -am `date +'%Y%m%d%H%M%S'` && git push -u origin

archive_project:
	@git tag -a `date +'%Y%m%d%H%M%S'` -m "archive `date +'%Y%m%d%H%M%S'`" && git push origin --tags

docker_release: $(clean)
	bash Deploy/dockerRelease
