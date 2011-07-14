#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
import os
import hashlib
import anydbm
from cStringIO import StringIO
import config
application = Flask(__name__)

@application.route('/')
def index():
    return 'Gyazo Flask'

@application.route('/upload', methods=['POST'])
def upload():
    id = request.values['id']
    image = request.files['imagedata']

    imagedata = image.stream.read()
    hash = hashlib.md5(imagedata).hexdigest()

    dbm = anydbm.open(config.app['dbm_path'], 'c')
    dbm[hash] = str(id)
    dbm.close()

    filename = '%s.png' % hash
    image.stream = StringIO(imagedata)
    image.save(os.path.join(config.app['image_dir'], filename))
    return os.path.join(config.app['image_url'], filename)

if __name__ == '__main__':
    application.run(**config.server)

