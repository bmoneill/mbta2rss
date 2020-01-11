all: install

install:
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp -f mbta2rss md2mail ${DESTDIR}${PREFIX}/bin
	chmod 755 ${DESTDIR}${PREFIX}/bin/mbta2rss ${DESTDIR}${PREFIX}/bin/md2mail

uninstall:
	rm -f ${DESTDIR}${PREFIX}/bin/mbta2rss ${DESTDIR}${PREFIX}/bin/md2mail

.PHONY: all install uninstall
