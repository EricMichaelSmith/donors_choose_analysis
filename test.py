# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 17:16:19 2015

@author: Eric

For now, primarily tests out the DonorsChoose.org API

Suffixes at the end of variable names:
a: numpy array
b: boolean
d: dictionary
df: pandas DataFrame
l: list
s: string
t: tuple
Underscores indicate chaining: for instance, "foo_t_t" is a tuple of tuples
"""

import json
import requests



def main():
    """ Run test script. """
    
    
    # Create URL string
    query_d = {'APIKey': 'DONORSCHOOSE',
               'subject1': '-1'}
    url = 'http://api.donorschoose.org/common/json_feed.html?'
    for key, val in query_d.iteritems():
        url += key + '=' + val + '&'
    url = url[:-1]
    
    
    # Get query results
    resp = requests.get(url=url, params={})
    data = json.loads(resp.text)
    print(len(data[u'proposals']))