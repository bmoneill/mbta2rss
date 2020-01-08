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

## Usage

### Unix-like Systems (macOS, GNU/Linux, \*BSD, WSL...)

Run `python mbta2rss.py >out.xml`. Then you can open the XML file in your
favorite RSS feed reader. It is also possible to set up a cron job to update it
every few hours on a server by adding the command to your crontab (with proper
paths of course). For a specific route, run `python mbta2rss.py -r Red >out.xml`
for the Red Line, as an example. To use an API key, run `python mbta2rss.py -k
KEY`. These options can be combined.

## Important Notes

Don't run too frequently without an API key. There are heavy rate limits. If you
run this too many times, your IP could be banned from the service.

## Bugs

I don't know of any bugs but I know there are bound to be some so submit an
issue or email me.

## Contributing

Please feel free to contribute. Email me patch files or submit a pull request.
Also, the license is GNU GPL v3 so you can fork this and use it for any purpose.
