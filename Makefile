all: install

install:
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp -f mbta2rss headmail ${DESTDIR}${PREFIX}/bin
	chmod 755 ${DESTDIR}${PREFIX}/bin/mbta2rss ${DESTDIR}${PREFIX}/bin/headmail

uninstall:
	rm -f ${DESTDIR}${PREFIX}/bin/mbta2rss ${DESTDIR}${PREFIX}/bin/headmail

.PHONY: all install uninstall
