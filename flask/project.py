#!flask/bin/python
from YOURAPP import YOURAPP
#website.run(debug = True) ## This is for debugging use only.

if __name__ == 'main':	## This is for execution via gunicorn.
    YOURAPP.run(debug=True)

# gunicorn command
# gunicorn YOURPROJECT:YOURAPP -b 127.0.0.1:8001
