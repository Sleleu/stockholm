VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
NAME = stockholm.py

all:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
	chmod +x venv/bin/activate
	$(VENV)/bin/activate
	bash infection.sh

run:
	$(PYTHON) $(NAME)

clean:
	bash infection.sh delete
	rm -rf venv
