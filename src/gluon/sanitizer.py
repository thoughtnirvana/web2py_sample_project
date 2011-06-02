#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
::

    # from http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/496942
    # Title: Cross-site scripting (XSS) defense
    # Submitter: Josh Goldfoot (other recipes)
    # Last Updated: 2006/08/05
    # Version no: 1.0

"""


from htmllib import HTMLParser
from cgi import escape
from urlparse import urlparse
from formatter import AbstractFormatter
from htmlentitydefs import entitydefs
from xml.sax.saxutils import quoteattr

__all__ = ['sanitize']


def xssescape(text):
    """Gets rid of < and > and & and, for good measure, :"""

    return escape(text, quote=True).replace(':', '&#58;')


class XssCleaner(HTMLParser):

    def __init__(
        self,
        permitted_tags=[
            'a',
            'b',
            'blockquote',
            'br/',
            'i',
            'li',
            'ol',
            'ul',
            'p',
            'cite',
            'code',
            'pre',
            'img/',
            ],
        allowed_attributes={'a': ['href', 'title'], 'img': ['src', 'alt'
                            ], 'blockquote': ['type']},
        fmt=AbstractFormatter,
        ):

        HTMLParser.__init__(self, fmt)
        self.result = ''
        self.open_tags = []
        self.permitted_tags = [i for i in permitted_tags if i[-1] != '/']
        self.requires_no_close = [i[:-1] for i in permitted_tags
                                  if i[-1] == '/']
        self.permitted_tags += self.requires_no_close
        self.allowed_attributes = allowed_attributes

        # The only schemes allowed in URLs (for href and src attributes).
        # Adding "javascript" or "vbscript" to this list would not be smart.

        self.allowed_schemes = ['http', 'https', 'ftp']

    def handle_data(self, data):
        if data:
            self.result += xssescape(data)

    def handle_charref(self, ref):
        if len(ref) < 7 and ref.isdigit():
            self.result += '&#%s;' % ref
        else:
            self.result += xssescape('&#%s' % ref)

    def handle_entityref(self, ref):
        if ref in entitydefs:
            self.result += '&%s;' % ref
        else:
            self.result += xssescape('&%s' % ref)

    def handle_comment(self, comment):
        if comment:
            self.result += xssescape('<!--%s-->' % comment)

    def handle_starttag(
        self,
        tag,
        method,
        attrs,
        ):
        if tag not in self.permitted_tags:
            self.result += xssescape('<%s>' % tag)
        else:
            bt = '<' + tag
            if tag in self.allowed_attributes:
                attrs = dict(attrs)
                self.allowed_attributes_here = [x for x in
                        self.allowed_attributes[tag] if x in attrs
                         and len(attrs[x]) > 0]
                for attribute in self.allowed_attributes_here:
                    if attribute in ['href', 'src', 'background']:
                        if self.url_is_acceptable(attrs[attribute]):
                            bt += ' %s="%s"' % (attribute,
                                    attrs[attribute])
                    else:
                        bt += ' %s=%s' % (xssescape(attribute),
                                quoteattr(attrs[attribute]))
            if bt == '<a' or bt == '<img':
                return
            if tag in self.requires_no_close:
                bt += ' /'
            bt += '>'
            self.result += bt
            self.open_tags.insert(0, tag)

    def handle_endtag(self, tag, attrs):
        bracketed = '</%s>' % tag
        if tag not in self.permitted_tags:
            self.result += xssescape(bracketed)
        elif tag in self.open_tags:
            self.result += bracketed
            self.open_tags.remove(tag)

    def unknown_starttag(self, tag, attributes):
        self.handle_starttag(tag, None, attributes)

    def unknown_endtag(self, tag):
        self.handle_endtag(tag, None)

    def url_is_acceptable(self, url):
        """
        Requires all URLs to be \"absolute.\"
        """

        parsed = urlparse(url)
        return parsed[0] in self.allowed_schemes and '.' in parsed[1]

    def strip(self, rawstring):
        """
        Returns the argument stripped of potentially harmful
        HTML or Javascript code
        """

        for tag in self.requires_no_close:
            rawstring = rawstring.replace("<%s/>" % tag, "<%s />" % tag)
        self.result = ''
        self.feed(rawstring)
        for endtag in self.open_tags:
            if endtag not in self.requires_no_close:
                self.result += '</%s>' % endtag
        return self.result

    def xtags(self):
        """
        Returns a printable string informing the user which tags are allowed
        """

        tg = ''
        for x in sorted(self.permitted_tags):
            tg += '<' + x
            if x in self.allowed_attributes:
                for y in self.allowed_attributes[x]:
                    tg += ' %s=""' % y
            tg += '> '
        return xssescape(tg.strip())


def sanitize(text, permitted_tags=[
    'a',
    'b',
    'blockquote',
    'br/',
    'i',
    'li',
    'ol',
    'ul',
    'p',
    'cite',
    'code',
    'pre',
    'img/',
    ], allowed_attributes={'a': ['href', 'title'], 'img': ['src', 'alt'
                           ], 'blockquote': ['type']}):
    return XssCleaner(permitted_tags=permitted_tags,
                      allowed_attributes=allowed_attributes).strip(text)
