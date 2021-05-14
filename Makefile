PREFIX := /usr/local
MANPREFIX := ${PREFIX}/share/man

all: install

install:
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp -f mbta2rss headmail ${DESTDIR}${PREFIX}/bin
	cp -f mbta2rss.1 ${DESTDIR}${MANPREFIX}/man1
	chmod 755 ${DESTDIR}${PREFIX}/bin/mbta2rss ${DESTDIR}${PREFIX}/bin/headmail
	chmod 644 ${DESTDIR}${MANPREFIX}/man1/mbta2rss.1

uninstall:
	rm -f ${DESTDIR}${PREFIX}/bin/mbta2rss ${DESTDIR}${PREFIX}/bin/headmail ${DESTDIR}${MANPREFIX}/man1/mbta2rss.1

.PHONY: all install uninstall
