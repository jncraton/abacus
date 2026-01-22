all: test

test:
	python3 abacus.py

format:
	uvx black@26.1.0 .

clean:
	rm -rf __pycache__
