VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
NAME = stockholm.py

all:
	python3 -m venv venv
	venv/bin/pip3 install -r requirements.txt --use-pep517
	chmod +x venv/bin/activate
	$(VENV)/bin/activate
	bash infection.sh

run:
	-bash infection.sh
	$(PYTHON) $(NAME)

clean:
	bash infection.sh delete
	rm -rf master.key 

fclean: clean
	rm -rfd venv
	rm -rfd __pycache__

re: clean all

.PHONY: all clean fclean re run