.PHONY: test lint run clean

run:
    python -m src.main

test:
    python -m unittest discover -s tests

lint:
	flake8 --max-line-length=80 --max-complexity=10 src tests

clean:
    del /s /q __pycache__ 2>nul
    del /s /q *.pyc 2>nul
