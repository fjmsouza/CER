SHELL := /bin/zsh
.PHONY: venv

venv:
	poetry run poetry install

start:
	poetry run python cft_model/main.py

test_all:
	@poetry run task test_all

commit:
	@echo "Revisar mudanças para este commit: "
	@echo "------------------------------------- "
	@git status -s 
	@echo "------------------------------------- "
	@read "?Commit note: " msg ; \
	git add . ;\
	git commit -m "$$msg" ;\

build:
	@python setup.py build_ext --build-lib dist

compile:
	@files=$$(find model_xpto/ -name '*.cpp') ; \
	gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
    -I/usr/include/python3.12 -o dist/model_xpto.so $$files

clean:
	@setopt NONOMATCH; \
	rm -rf dist/ \
			build/ \
			model_xpto/__pycache__ \
			model_xpto/*.so \
			model_xpto/*.cpp

release: clean build compile