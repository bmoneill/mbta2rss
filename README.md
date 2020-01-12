# MBTA Schedule and Alerts RSS Feed

This software will generate an RSS feed using the [MBTA
API](https://www.mbta.com/developers/v3-api) and Python 3. The
feed will show current schedule and alerts for different routes. This
is very helpful if you want to send notifications to your phone as an
email or via SMS.

## Features

- [X] Generate an RSS feed containing alerts, neatly formatted.
- [X] Filters for certain routes in RSS feed using command-line options.
- [X] Allow the user to use an API key.
- [X] Export to Markdown instead of RSS.
- [ ] Only include alerts published after a certain time.
- [ ] Convert route schedules to Markdown format.

## Usage

### Basics

Run `python mbta2rss.py >out.xml`. Then you can open the XML file in your
favorite RSS feed reader.

### Options

* `-k key`: Use an API key
* `-o fmt`: Set output format (rss or md, default set to rss)
* `-r route`: Set route to look for

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

	mbta2rss -o md -k "$MYAPIKEY" | md2mail "$FROM" "$TO" | msmtp -a \
	"$MSMTPACCOUNT" -t "$TO"

If you wanted to convert it to HTML first, a Markdown to HTML filter must be
used:

	mbta2rss -o md -k "$MYAPIKEY" | smu | md2mail "$FROM" "$TO" \
	| msmtp -a "$MSMTPACCOUNT" -t "$TO"

### Publishing Alerts
	
It is possible to make a HTML webpage (no CSS included by default) for the web
using the Markdown output format and piping it into a Markdown to HTML filter
like `smu`.

	mbta2rss -o md -k "$MYAPIKEY" | smu >out.html

## Important Notes

1. Don't run too frequently without an API key. There are heavy rate limits. If
   you run this too many times, your IP could be banned from the service.
2. If you publish anything containing content related to this, make sure it is
   clear this is unofficial and not officially affiliated with the MBTA. They
   have a [license agreement](https://www.mass.gov/files/documents/2017/10/27/develop_license_agree_0.pdf).

## Bugs

I don't know of any bugs but I know there are bound to be some so submit an
issue or email me.

## Contributing

Please feel free to contribute. Email me patch files or submit a pull request.
Also, the license is GNU GPL v3 so you can fork this and use it for any purpose.
