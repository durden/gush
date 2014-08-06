#!/usr/bin/env python

"""
Script to automatically shorten a link with google's url shortening service,
which is actually allowed by Twitter (for now) in Direct Messages.

Shortener API: https://developers.google.com/url-shortener/

Thanks to Dr. Drang (http://www.leancrew.com) for the idea.
    - http://www.leancrew.com/all-this/2014/08/automatic-shortened-urls-via-google/
"""

# Yes, requests is better but having external dependencies for a short script
# sucks.
import urllib2

import argparse
import json


def _parse_args():
    parser = argparse.ArgumentParser(
                prog='gush',
                description='Shorten URLS with Google url shortener web API')

    parser.add_argument('long_url', help='Url to shorten')

    return vars(parser.parse_args())


def sendit(url):
    req = urllib2.Request('https://www.googleapis.com/urlshortener/v1/url')
    req.add_header('Content-Type', 'application/json')
    req.add_data(json.dumps({'longUrl': url}))

    return json.loads(urllib2.urlopen(req).read())['id']

 
def main():
    url = _parse_args()['long_url']
    print sendit(url)


if __name__ == '__main__':
    main()
