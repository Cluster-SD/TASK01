######################################################################   
#   Project: Cluster Master-Workers                                  #
#   Subject: SD - Distributed Sistems                                #
#   Authors: Younes Kabiri <younes.kabiri@estudiants.urv.cat.>       #
#            Safia Guellil <safia.guellil@urv.cat>                   #
#   Version: 1.0                                                     #
#   Date: 19-05-2021                                                 #
#   Title-File: Proto File [Protocol Buffer]                         #
#   Description: Class to establish http communicationthrough flask. #
#                                                                    #
######################################################################
from flask import Flask
from pathlib import Path

app = Flask(__name__)

#Method to get files from browser(root method).
@app.route('/<address>')
def getValues(address):
    #We build the root file.
    file = Path("./files/"+address)
    #Check if file exists.
    if file.is_file():
        #Then we read it.
        return readFile(file)
    else:    
        return ""

#Method to read files and returns a string object.
def readFile(file):
    with open(file, 'r') as file:
        data = file.read().replace('\n', '')
    return data

#Main method.
if __name__ == "__main__":
    app.run(debug=True, port=8000)