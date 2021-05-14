# mbta2rss

This software utilizes the [MBTA API](https://www.mbta.com/developers/v3-api)
to grab alerts and stop lists for public transit routes in Greater Boston.

## Features (check means implemented)

- [X] Generate an RSS feed containing alerts, neatly formatted.
- [X] Only include certain routes.
- [X] Allow the user to use an API key.
- [X] Export to Markdown instead of RSS.
- [X] Only include alerts active at a certain time.
- [X] Convert stop lists to Markdown format.
- [ ] Convert route schedules to CSV and Markdown format.

## Dependencies

* requests (`pip install requests`)

## Installation

Run the following as root:

	make install

## Usage

### Basics

Run `mbta2rss >out.xml`. Then you can open the XML file in your
favorite RSS feed reader.

### Options

* `-d datatype`: choose type of data to grab (alerts or stops, default is alerts)
* `-k key`: Use an API key.
* `-o fmt`: Set output format (rss or md, default is rss).
* `-r routes`: Set route(s) to look for (comma separated)
* `-t time`: Set time filter to show alerts active at that time
  (default shows all times, "NOW" for alerts in effect now, must be in
  ISO 8601 time format).
* `-T title`: document/feed title
* `-D description`: document/feed description
* `-U url`: upstream URL for RSS feed

### Use Cases

* Set up a cron job to update alerts feed every hour or so.
* Email alerts to you (for the route(s) you take or all routes).
* Post alerts on a webpage.
* View alerts in a RSS feed reader.

### Cron-based Alert Updater

Add the following to your crontab:

	0 * * * * /usr/bin/mbta2rss -k "$MYAPIKEY" >$HOSTDIR/rss.xml

### Emailing Digests

An example of emailing a Markdown-formatted digest using the `headmail` filter
script and `sendmail`:

	mbta2rss -o md -k "$MYAPIKEY" -r "Orange,36" -t "NOW" | headmail "$FROM" "$TO" | sendmail -a \
	"$ACCOUNT" -t "$TO"

If you wanted to convert it to HTML first, a Markdown to HTML filter must be
used (like [smu](https://github.com/Gottox/smu):

	mbta2rss -o md -k "$MYAPIKEY" -r "Orange,36" -t "NOW" | smu | headmail "$FROM" "$TO" \
	| msmtp -a "$MSMTPACCOUNT" -t "$TO"

### Publishing Alerts
	
It is possible to make a HTML webpage (no CSS included by default) for the web
using the Markdown output format and piping it into a Markdown to HTML filter.

	mbta2rss -o md -k "$MYAPIKEY" | smu >out.html

## Important Notes

1. Without an API key, you are limited to 20 calls per minute.
2. If you publish anything containing content related to this, make sure it is
   clear this is unofficial and not officially affiliated with the MBTA. They
   have a [license agreement](https://www.mass.gov/files/documents/2017/10/27/develop_license_agree_0.pdf).
3. Green Line routes are differenciated like so: "Green-B", "Green-C", "Green-D", "Green-E"

## Bugs

No known bugs. If one is found, submit an issue, PR, or email me with
a description and/or patch.

## Contributing

Please feel free to contribute. Send patches via email or submit a pull request.

## License

Copyright (C) 2019-2021 Ben O'Neill <ben@benoneill.xyz>. License: GNU
GPL Version 3 <https://gnu.org/licenses/gpl.html>. This is free
software: you are free to change and redistribute it. There is NO
WARRANTY, to the extent permitted by law.
