.PHONY: package clean test docs

PACKAGE_TYPES:=sdist bdist_wheel

package:
	python setup.py $(PACKAGE_TYPES)

clean:
	rm -rf dist build docs/_build

test:
	python setup.py test

docs:
	sphinx-apidoc -F -o source omaha
	sphinx-build -b html source docs
