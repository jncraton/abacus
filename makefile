all: test

test:
	python3 abacus.py

format:
	uvx black@26.1.0 .
	npx prettier@3.8.1 --write .

clean:
	rm -rf __pycache__
