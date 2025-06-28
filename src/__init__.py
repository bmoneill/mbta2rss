import argparse
import mbta2rss
from alerts import RSSOutputDriver, MarkdownOutputDriver

if __name__ == '__main__':
    # Set defaults
    title = DEFAULT_TITLE
    desc = DEFAULT_DESC
    url = DEFAULT_URL
    datatype = DEFAULT_DATATYPE
    driver = None

    # Add potential arguments to parser
    parser = argparse.ArgumentParser(description='Pull down MBTA alerts and print them out')
    parser.add_argument('-d', '--datatype', help="data to grab", metavar='DATATYPE')
    parser.add_argument('-o', '--output', help='set output format', metavar='OUTFMT')
    parser.add_argument('-r', '--routes', help='set route list', metavar='ROUTELIST')
    parser.add_argument('-t', '--time', help='set time to check alerts for', metavar='TIME')
    parser.add_argument('-T', '--title', help='set output title', metavar='TITLE')
    parser.add_argument('-D', '--description', help='set output description', metavar='DESC')
    parser.add_argument('-U', '--url', help='set upstream URL', metavar='URL')

    # Parse arguments
    args = parser.parse_args()
    outfmt = args.output
    routes = args.routes
    time = args.time
    if args.title != None:
        title = args.title
    if args.description != None:
        desc = args.description
    if args.url != None:
        url = args.url
    if args.datatype != None:
        datatype = args.datatype

    # Get the API key. We are using an environment variable for better
    # security. It's fine if this is empty/undefined as long as API
    # calls are limited in frequency.
    API_KEY = os.getenv("API_KEY")

    # Check for output driver
    if outfmt == None or outfmt == 'rss':
        driver = RSSOutputDriver(title, desc, DEFAULT_LANG, url)
    elif outfmt == 'md':
        driver = MarkdownOutputDriver(title, desc, DEFAULT_LANG, url)
    else:
        print("No such output driver.")
        exit(1)

    # Execute desired tool/function
    if datatype == 'alerts':
        get_alerts(driver, routes, time)
    elif datatype == 'stops':
        get_stoplist(routes)
    else:
        print("No such data type.")
        exit(1)