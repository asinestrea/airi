compile:
	rm -rf dist
	python3 setup.py bdist_wheel

install:
	python3 -m pip install --force-reinstall dist/*

upload-pip:
	python3 -m twine upload -r pypi dist/*
