import os
import json
import sys

LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = 5000
ALCHEMY_URL = os.environ.get('ALCHEMY_URL', '')

SECRET = os.environ.get('APP_SECRET')
if not SECRET:
    print("Specify an app secret in the APP_SECRET env variable")
    sys.exit(3)
TEST_MODE = str(os.environ.get('TEST_MODE', False)).lower() == 'true'
