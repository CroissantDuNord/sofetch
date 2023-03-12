install: soshell/soshell.py soshell/ascii.py
	pip --use-pep517 -r requirements.txt
	cp soshell/* /usr/bin
	mv /usr/bin/soshell.py /usr/bin/soshell
	chmod +x /usr/bin/soshell
