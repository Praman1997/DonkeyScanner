all:

clean:

install:
	chmod 755 banner.py
	chmod 755 install.py
	chmod 755 run.sh
	chmod 755 dscan.py
	mkdir -p $(DESTDIR)/opt/dscan/
	mkdir -p $(DESTDIR)/usr/share/doc/dscan/
	mkdir -p $(DESTDIR)/opt/dscan/tools/
	mkdir -p $(DESTDIR)/usr/bin/
	cp banner.py $(DESTDIR)/opt/dscan/
	cp install.py $(DESTDIR)/opt/dscan/
	cp LICENSE $(DESTDIR)/opt/dscan/
	cp Makefile $(DESTDIR)/opt/dscan/
	cp README.md $(DESTDIR)/opt/dscan/
	cp README.md $(DESTDIR)/usr/share/doc/dscan/
	cp run.sh $(DESTDIR)/opt/dscan/
	cp run.sh $(DESTDIR)/usr/bin/
	cp dscan.py $(DESTDIR)/opt/dscan/
	cp -r tools $(DESTDIR)/opt/dscan/
	

