# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os

from flask.ext.script import Manager
from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()