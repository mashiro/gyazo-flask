#!/usr/bin/env python
# -*- coding: utf-8 -*-

def current_dir(path):
    import os
    return os.path.join(os.path.dirname(__file__), path)

server = {
    'host': '127.0.0.1',
    'port': 15001,
    'debug': False,
}

app = {
    'dbm_path': current_dir('db/id'),
    'image_url': 'http://mashiro.org:15001',
    'image_dir': current_dir('public/images')
}

