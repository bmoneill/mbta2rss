import html

DEFAULT_TITLE = 'Unofficial MBTA Alert Feed'
DEFAULT_DESC = 'An unofficial feed for public transit alerts in the Boston area.'
DEFAULT_LANG = 'en_us'
DEFAULT_URL = 'https://github.com/boneill02/mbta-rss'
DEFAULT_DATATYPE = 'alerts'

class OutputDriver:
    """
    Base output driver class
    """
    def __init__(self, title=DEFAULT_TITLE, desc=DEFAULT_DESC,
            lang=DEFAULT_LANG, url=DEFAULT_URL):
        self.title = title
        self.desc = desc
        self.lang = lang
        self.url = url
    
    def print_start(self):
        pass

    def print_item(self, header, long_header='', desc='', effect='', date='', categories=['default'], guid='')
        pass

    def print_end(self):
        pass

class MarkdownOutputDriver(OutputDriver):
    """
    Driver for printing Markdown output. This formats the data from the API
    to be semi-neatly displayed in basic Markdown.
    """
    def __init__(self, title=DEFAULT_TITLE, desc=DEFAULT_DESC,
            lang=DEFAULT_LANG, url=DEFAULT_URL):
        self.title = title
        self.desc = desc
        self.lang = lang
        self.url = url
    
    def print_start(self):
        """ Stuff to print before the main content """
        print('# ' + title)
        print(desc)

    def print_item(self, header, long_header='', desc='', effect='', date='',categories=['default'], guid=''):
        """ Format and print alert """
        print('## ' + header + ' (added ' + date + ')')
        print(long_header + '\n\n' + desc.replace('\n', '\n\n') + '\n\n')

class RSSOutputDriver:
    """
    Driver for printing RSS output. This formats the data from the API
    to be semi-neatly displayed as an RSS feed.
    """
    def __init__(self, title=DEFAULT_TITLE, desc=DEFAULT_DESC,
            lang=DEFAULT_LANG, url=DEFAULT_URL):
        self.title = title
        self.desc = desc
        self.lang = lang
        self.url = url
    
    """ Stuff to print before the main content """
    def print_start(self):
        print('<?xml version="1.0" encoding="utf-8"?>')
        print('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">')
        print('<channel>')
        print('<title>' + self.title + '</title>')
        print('<description>' + self.desc + '</description>')
        print('<language>' + self.lang + '</language>')
        print('<link>' + self.url + '</link>')

    """ Format and print alert """
    def print_item(self, header, long_header='', desc='', effect='', date='',
            categories=[], guid=''):
        content = "<pre>" + html.escape(long_header) + "\n\n" + html.escape(desc) + "</pre>"

        print('<item>')
        print('<title>' + html.escape(header) + '</title>')
        print('<description>' + content + '</description>')
        print('<pubDate>' + date + '</pubDate>')
        print('<guid>' + guid + '</guid>')
        for category in categories:
            print('<category>' + category + '</category>')
        print('</item>')

    """ Stuff to print after the main content """
    def print_end(self):
        print('</channel>')
        print('</rss>')