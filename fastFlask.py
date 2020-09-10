'''
Author: Jake Wachs

Automates Flask directory structure setup

Flask app directory is created in your current directory
'''

'''
Additions:
- Parse command line args for options
- Option for enabling CORS
- add ability to specify where the flask app is setup
'''

import sys
import subprocess

def createDir(dirName):
    '''
    Creates the directory structure

    Keyword Arguments:
    dirName - name of the directory to be created
    '''
    subprocess.call(['mkdir', dirName])
    subprocess.call(['mkdir', dirName + '/static'])
    subprocess.call(['mkdir', dirName + '/templates'])
    subprocess.call(['mkdir', dirName + '/templates/js'])


def createApp(appName):
    '''
    Creates a Python file for Flask with appName as filename

    Keyword Arguments:
    appName - Name of the app
    '''
    filename = appName + '/' + appName + '.py'

    code = 'from flask import Flask, render_template\n\napp = Flask(\'' + \
        appName + '\')\n\n' 
    code = code + '''
@app.route('/', methods=['GET', 'POST'])
def home():
    render_template(\'''' + appName + '.html\')'
    code = code + '\n\nif __name__ == \'__main__\':\n\tapp.run(host=\'0.0.0.0\', debug=True, threaded=True)\n'
    
    args = 'echo ' + code + ' > ' + filename
    subprocess.call(args)


def addHTML(appName):
    '''
    Adds a template HTML page to templates/

    Keyword Arguments:
    appName - Name of the app
    '''
    filename = appName + '/templates/' + appName + '.html'

    code = '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>' + appName + \
        '</title>\n\t</head>\n\t<body>\n\t\tHello, world!\n\t</body>\n</html>'

    args = 'echo ' + code + ' > ' + filename
    subprocess.call(args)


def runApp(appName):
    '''
    Starts the new Flask web app on port 5000 in debug mode
    '''
    subprocess.call(['python3', appName])



if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('*** Usage: python3 fastFlask <project_name>')
        print('No project name supplied. Exiting...')
        exit(-1)

    projectName = sys.argv[1]

    createDir(projectName)
    createApp(projectName)
    addHTML(projectName)
    runApp(projectName)
