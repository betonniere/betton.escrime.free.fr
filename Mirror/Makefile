.SILENT:

prepare:
	git clean -fdx

collect: prepare
	cd root && httrack -N100 --footer "" http://127.0.0.1:8080/fencing-tournament-software
	cd root && rm -rf *gif hts* index.html; cp ../htaccess .htaccess; cp ../index.html index.html

publish:
	cd root && lftp -u betton.escrime ftp://ftpperso.free.fr -e "mirror -R ./ / ; quit"

publish_version:
	lftp -u betton.escrime ftp://ftpperso.free.fr -e "put -O /documents/BellePoule latest.html ; quit"

open:
	xdg-open http://betton.escrime.free.fr/fencing-tournament-software/
