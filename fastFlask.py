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
- Do a system check to see if flask, pip installed. If not, install them after asking user for permission
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
    return render_template(\'''' + appName + '.html\')'
    code = code + '\n\nif __name__ == \'__main__\':\n    app.run(host=\'0.0.0.0\', debug=True, threaded=True)\n'
    
    subprocess.call(['touch', appName + '/' + appName + '.py'])
    
    args = 'echo ' + '\"' + code +'\"' + ' > ' + filename
    subprocess.call(args, shell=True)


def addHTML(appName):
    '''
    Adds a template HTML page to templates/

    Keyword Arguments:
    appName - Name of the app
    '''
    filename = appName + '/templates/' + appName + '.html'

    code = '<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>' + appName + \
        '</title>\n\t</head>\n\t<body>\n\t\t<h1>Hello, world!</h1>\n\t</body>\n</html>'

    subprocess.call(['touch', filename])
    
    args = 'echo ' + code + ' > ' + filename
    subprocess.call(args, shell=True)


def runApp(appName):
    '''
    Starts the new Flask web app on port 5000 in debug mode
    '''
    subprocess.call(['python3', appName + '/' + appName + '.py'])



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
