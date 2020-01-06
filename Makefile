.PHONY: package clean

PACKAGE_TYPES:=sdist bdist_wheel

package:
	python setup.py $(PACKAGE_TYPES)

clean:
	rm -rf dist build
