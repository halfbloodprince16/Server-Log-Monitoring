from flask import Flask, render_template
import time, math, flask

import subprocess
def tail(f, n, offset=0):
    proc = subprocess.Popen(['tail', '-n', n + str(offset), f], stdout=subprocess.PIPE)
    lines = proc.stdout.readlines()
    #print(len(lines))
    return lines[-10:]

app = flask.Flask(__name__)

@app.route('/content') # render the content a url differnt from index
def content():
    def inner():
    	while(1):
    		con = str(tail("/var/log/syslog","1")) + '<br/>\n'
    		yield con
    		time.sleep(3)
    		del con
    return app.response_class(inner(), mimetype='text/html')

@app.route('/')
def index():
    return render_template('index.html.jinja') # render a template at the index. The content will be embedded in this template

app.run(debug=True)