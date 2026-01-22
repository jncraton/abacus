all: test

test:
	python3 abacus.py

clean:
	rm -rf __pycache__
