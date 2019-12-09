# MBTA Schedule and Alerts RSS Feed

This software will generate an RSS feed using the [MBTA
API](https://www.mbta.com/developers/v3-api) and Python 3. The
feed will show current schedule and alerts for different routes.

## Features

- [X] Generate an RSS feed containing alerts, neatly formatted.
- [ ] Filters for certain routes in RSS feed using command-line options.
- [ ] Allow the user to use an API key.

## Usage

### Unix-like Systems (macOS, GNU/Linux, \*BSD, WSL...)

Run `python mbta2rss.py > out.xml`

## Important Notes

Don't abuse this: I'm not using an API key so there are heavy rate limits. If
you run this too many times, your IP will probably be banned from the service.
