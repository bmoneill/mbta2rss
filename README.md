# MBTA Alerts RSS Feed

This software will generate an RSS feed using the [MBTA
API](https://www.mbta.com/developers/v3-api) and Python 3. The
feed will show alerts for different routes. This is very helpful if
you want to send notifications to your phone as an email or via SMS,
or check them on a desktop or laptop via a feed reader or web page.

## Features (check means implemented)

- [X] Generate an RSS feed containing alerts, neatly formatted.
- [X] Only include certain routes.
- [X] Allow the user to use an API key.
- [X] Export to Markdown instead of RSS.
- [X] Only include alerts active at a certain time.
- [ ] Convert route schedules to Markdown format.

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

* `-k key`: Use an API key.
* `-o fmt`: Set output format (rss or md, default set to rss).
* `-r route`: Set route to look for (or comma separated list of
  routes).
* `-t time`: Set time filter to show alerts active at that time
  (default shows all times, "NOW" for effective now, ISO 8601 time
  format).

### Use Cases

* Set up a cron job to update alerts feed every hour or so.
* Email alerts to you (for the route(s) you take or all routes).
* Post alerts on a webpage.
* View alerts in a RSS feed reader.
* Send alerts via text (not described here).

### Cron-based Alert Updater

Add the following to your crontab:

	0 * * * * /usr/bin/mbta2rss -k "$MYAPIKEY" >$HOSTDIR/rss.xml

### Emailing Digests

An example of emailing a Markdown-formatted digest using the `headmail` filter
script and `msmtp` (a `sendmail`-like program):

	mbta2rss -o md -k "$MYAPIKEY" -r "Orange,36" -t "NOW" | headmail "$FROM" "$TO" | msmtp -a \
	"$MSMTPACCOUNT" -t "$TO"

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

## Bugs

I don't know of any bugs but I know there are bound to be some so submit an
issue or email me.

## Contributing

Please feel free to contribute. Email me patch files or submit a pull request.
Also, the license is GNU GPL v3 so you can fork this and use it for any purpose.
