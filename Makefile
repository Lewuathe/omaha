.PHONY: package clean test

PACKAGE_TYPES:=sdist bdist_wheel

package:
	python setup.py $(PACKAGE_TYPES)

clean:
	rm -rf dist build

test:
	python setup.py test
