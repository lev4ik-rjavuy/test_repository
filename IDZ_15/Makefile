.PHONY: run test format check-format check-security install

install:
	pip install -r requirements.txt

run:
	python app.py

test:
	python -m doctest app.py -v
	python -m unittest tests.py -v

format:
	black .

check-format:
	black --check .

check-security:
	safety scan -r requirements.txt