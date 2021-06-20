#####################################################################
#   Project: Cluster Master-Workers                                 #
#   Subject: SD - Distributed Sistems                               #
#   Authors: Younes Kabiri <younes.kabiri@estudiants.urv.cat.>      #
#            Safia Guellil <safia.guellil@urv.cat>                  #
#   Version: 1.0                                                    #
#   Date: 23-04-2021                                                #
#   Title-File: Client Object                                       #
#   Description: defines de Client's class                          #
#                                                                   #
#####################################################################
import grpc
import cluster_pb2_grpc as pb2_grpc

class Client(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50001

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.WorkerStub(self.channel)


    