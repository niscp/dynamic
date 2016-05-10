#!/usr/bin/env python
from app import app
import os
from flask.ext.script import Manager, Server

environment = os.environ.get("HOSTENV")

if not environment:
    environment = 'default'

app = app(environment)
print "Mode: " + environment

manager = Manager(app)
manager.add_command("runserver", Server(host="0.0.0.0"))

@manager.command
def test(coverage=False):
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()