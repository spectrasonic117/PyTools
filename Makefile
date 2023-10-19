PREFIX ?= /usr/local
OPTDIR ?= /opt

BINDIR = $(PREFIX)/bin
DATDIR = $(OPTDIR)/pytools
# all: build install

# sudo make install
install:
	pip install -r ./requeriments.txt
	mkdir -p $(DATDIR)

	cp ./pytools $(BINDIR)/pytools
	cp ./pytools.py $(DATDIR)/pytools.py

	chmod +x $(BINDIR)/pytools
	chmod +x $(DATDIR)/pytools.py

	echo "Done"

# sudo make uninstall
uninstall:
	rm $(BINDIR)/pytools
	rm -rf $(DATDIR)