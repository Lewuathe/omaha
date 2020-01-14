.PHONY: package clean test docs

PACKAGE_TYPES:=sdist bdist_wheel

package:
	python setup.py $(PACKAGE_TYPES)

clean:
	rm -rf dist build site

test:
	python setup.py test

docs:
	sphinx-apidoc -F -o docs omaha
	sphinx-build -b html docs site