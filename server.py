######################################################################   
#   Project: Cluster Master-Workers                                  #
#   Subject: SD - Distributed Sistems                                #
#   Authors: Younes Kabiri <younes.kabiri@estudiants.urv.cat.>       #
#            Safia Guellil <safia.guellil@urv.cat>                   #
#   Version: 1.0                                                     #
#   Date: 19-05-2021                                                 #
#   Title-File: Server                                               #
#   Description: defines Server Comunication                         #
#                                                                    #
######################################################################
from time import sleep
from typing import Counter
import grpc
import cluster_pb2 as pb2
import cluster_pb2_grpc as pb2_grpc
from concurrent import futures
from multiprocessing import Process
import redisServer as redis
import commonMethod as common
from types import SimpleNamespace
import json
import appflask as flask
import ast
import time

# Global variables:
WORKERS = {}
WORKER_ID = 0
JOB_ID = 0

   
def startWorker(id):
    print("Worker Created")
    result = 0
    while True:
        
        # Getting a task from redis: 
        task = redis.getFirstElement(redis.redis_bd_tasks)
        
        if(task != None):
            
            t = json.loads(task, object_hook=lambda d: SimpleNamespace(**d))
            if (t.type_of_function == 'countwords') :
                result = common.run_counterWord(t.address)
                redis.send_intermediate_queue(t.job_ID,'countwords','Ok',result)

            elif (t.type_of_function == 'wordcount') :
                result = common.run_wordcount(t.address)
                redis.send_intermediate_queue(t.job_ID,'wordcount','Ok',result)

            elif (t.type_of_function == 'unify') :
                
                num_of_tasks = int(t.address)
                working = True
                tasks = list()
                while(working):
                    tasks=redis.getTaskIntermediate(t.job_ID)
                    if(len(tasks) == num_of_tasks):
                        working = False
                    else:
                        sleep(1)

                
                if(t.state == 'countwords'):
                    total = 0
                    for x in tasks:
                        total += int(x.result)
                    redis.add_hash(redis.redis_bd_results,t.job_ID,total)
                
                elif (t.state == 'wordcount'):
                    
                    tmp = None
                    for x in tasks:    
                        convert = vars(x.result)
                        if (tmp == None):
                            tmp = Counter(convert)
                        else:
                            tmp = tmp + Counter(convert) 
                    
                    result = dict(tmp)
                    redis.add_hash(redis.redis_bd_results,t.job_ID,str(result))
            else :
                sleep(1)
        




            



class WorkerService(pb2_grpc.WorkerServicer):

    def CreateWorkers(self, request, context):
        global WORKERS
        global WORKER_ID
        inicio = time.time()
        num = int(request.workers)
        for _ in range(num):
            proc = Process(target=startWorker, args=(WORKER_ID,))
            proc.start()
            WORKERS[WORKER_ID] = proc
            WORKER_ID += 1
        fin = time.time()
        print("--> [Time Creating Workers]: ",fin-inicio) 
        return pb2.Response(message='{}{}'.format("Workers created: ", num))


    def DeleteWorkers(self, request, context):
        global WORKERS
        global WORKER_ID

        inicio = time.time()
        num = int(request.workers) 
        delete = num
        
        if (WORKER_ID < num):
            delete = WORKER_ID 
        
        for _ in range(delete): 
            WORKER_ID -= 1
            proc = WORKERS[WORKER_ID]
            proc.terminate()

        response = '{}{}'.format("Workers deleted: ", delete)
        fin = time.time()
        print("--> [Time Deleting Workers]: ",fin-inicio) 
        return pb2.Response(message=response)


    def List(self, request, context):
        global WORKERS
        global WORKER_ID
        inicio = time.time()
        for x in range(WORKER_ID):
            yield pb2.Response(message=str(WORKERS[x]))
        fin = time.time()
        print("--> [Time Listing Workers]: ",fin-inicio) 


    def CoutingWords(self, request_iterator, context):
        global JOB_ID
        
        inicio = time.time()
        
        JOB_ID += 1
        nTasks = 0 # Count the number of files 'Tasks'
        tasks = False
        # Creating Tasks:
        for file in request_iterator:
            nTasks += 1
            tasks=True
            redis.send_task_queue(JOB_ID,'countwords',file.files,'processing')

        # Send task for unifying the job's result:
        redis.send_task_queue(JOB_ID,'unify',nTasks,'countwords')
        
        result = pb2.Words(totalWords=0)

        # Waiting to get the final result:
        while tasks:
            value = redis.get_value_hash(redis.redis_bd_results,JOB_ID)
            if(value != None):
                result = pb2.Words(totalWords=int(value))
                tasks=False
                redis.delete_value_hash(redis.redis_bd_results,JOB_ID)

        fin = time.time()
        print("--> [Time Counting Words]: ",fin-inicio) 
        return result
    
    


    def WordCounts(self, request_iterator, context):
        global JOB_ID
        
        inicio = time.time()
        JOB_ID += 1
        nTasks = 0 # Count the number of files 'Tasks'
        tasks = False
        # Creating Tasks:
        for file in request_iterator:
            nTasks += 1
            tasks=True
            redis.send_task_queue(JOB_ID,'wordcount',file.files,'processing')

        # Send task for unifying the job's result:
        redis.send_task_queue(JOB_ID,'unify',nTasks,'wordcount')
        
       
        # Waiting to get the final result:
        while tasks:
            dic = redis.get_value_hash(redis.redis_bd_results,JOB_ID)
            
            if(dic != None):
                list=ast.literal_eval(dic.decode('utf-8'))
                for x,y in list.items():
                    tasks=False
                    redis.delete_value_hash(redis.redis_bd_results,JOB_ID)
                    yield pb2.WordCount(word=x,num=int(y))
        fin = time.time()
        print("--> [Time Word Count]: ",fin-inicio) 
            

            

    


def serve():
    redis.empty()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_WorkerServicer_to_server(WorkerService(), server)
    server.add_insecure_port('[::]:50001')
    server.start()
    print("-- Server are listening on port [50001]. --")
    flask.app.run(debug=True, port=8000)
    
    
   
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
