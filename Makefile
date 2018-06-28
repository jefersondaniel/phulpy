release:
	rm -Rf dist
	rm -Rf build
	python setup.py sdist upload
	python setup.py bdist_wheel upload
