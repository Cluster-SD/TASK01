#####################################################################
#   Project: Cluster Master-Workers                                 #
#   Subject: SD - Distributed Sistems                               #
#   Authors: Younes Kabiri <younes.kabiri@estudiants.urv.cat.>      #
#            Safia Guellil <safia.guellil@urv.cat>                  #
#   Version: 1.0                                                    #
#   Date: 27-04-2021                                                #
#   Title-File: Client Comunication                                 #
#   Description: Client class, in this class we get all             #
#                client petitions.                                  #
#                                                                   #
#####################################################################

import click
import cluster_pb2 as pb2
from clientObject import Client
import urllib.request
import sys

# Global Object Client:
client = Client()

# Groups of Commands:
@click.group()
def CLI():
    pass

#worker group command.
@click.group(help="Some commands for administrate workers.")
def worker():
    pass

@click.group(help="Some commands for administrate worker's tasks.")
#job group command.
def job():
    pass

@click.command(help="Create especified workers.")
@click.argument('num')
# Method to create a Worker.
def create(num):
    if  num.isnumeric():
        message = pb2.Workers(workers=int(num))
        print(f'{message}')
        response = client.stub.CreateWorkers(message)
        print(f'{response}')
    else:
        click.echo("num must be integer!")
    
    
@click.command(help="Delete especified workers.")
@click.argument('num')
#Method to delete a process.
def delete(num):
    if  num.isnumeric():
        message = pb2.Workers(workers=int(num))
        print(f'{message}')
        response = client.stub.DeleteWorkers(message)
        print(f'{response}')
    else:
        click.echo("num must be integer!")


@click.command(help="List information related with activated workers.")
#Method to list all proces.
def list():
    responses = client.stub.List(pb2.Workers(workers=int(0)))
    for response in responses:
        print(f'{response.message}')



# Job Commands:
#Method to send files to server one by one.
def generator (args):
    for file in args:
        filesToSend = pb2.File(files=file)
        yield filesToSend


@click.command(help="Count the number of words that there are in the files sent.")
@click.argument('args', nargs=-1)
#run_countwords method, method to send countWords task to server.
def run_countwords(args):
    print("--->Run countwords")
    if(checkFile(args)):
        response = client.stub.CoutingWords(generator(args))
        print(f'{response}')


@click.command(help="Count the number of occurrencies of each word from+ files.")
@click.argument('args', nargs=-1)
#run_wordcount method, method to send wordCount task to server.
def run_wordcount(args):
    print("--->Run wordcount")
    if(checkFile(args)):
        responses = client.stub.WordCounts(generator(args))
        for response in responses:
            print(f'{response}')


#Method to check files: After send file to serve, we shoud check if exists.
def checkFile(args):
    correct = False
    #Iterate args one by one
    for x in args:
       #Connect with server. 
        response = urllib.request.urlopen(x)
        #Get status code.
        status_code = response.getcode()
        #If we got a right comunication
        if(status_code == 200):
            with urllib.request.urlopen(x) as url: 
                s = url.read().decode('utf-8')
                if(s):
                    correct = True
                else:
                    print("Warnig...Empty address: ",x)
                    sys.exit(0)
       #If not, we will abort process. 
        else:
            print("ERROR...Bad request: ",x)
            sys.exit(0)
    return correct

#Group commands.
CLI.add_command(worker)
CLI.add_command(job)
worker.add_command(create)
worker.add_command(delete)
worker.add_command(list)
job.add_command(run_countwords)
job.add_command(run_wordcount)

if __name__ == '__main__':
    CLI()