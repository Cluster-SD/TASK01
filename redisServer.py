######################################################################   
#   Project: Cluster Master-Workers                                 #
#   Subject: SD - Distributed Sistems                               #
#   Authors: Younes Kabiri <younes.kabiri@estudiants.urv.cat.>      #
#            Safia Guellil <safia.guellil@urv.cat>                  #
#   Version: 1.0                                                    #
#   Date: 23-05-2021                                                #
#   Title-File: redisServer                                         #
#   Description: In this class, we established connection with      #
#                 redis serves, after that, we can get and delete   #
#                 item.                                             #
#                                                                   #
######################################################################   


# Import the redis-py client package
import time
import json
import redis
from types import SimpleNamespace

#Redis connection values.
redis = redis.Redis(
     host= 'localhost',
     port= '6379')

#Or redis queues.
redis_bd_tasks = 'queue:tasks'
redis_bd_intermediate = 'queue:intermediate'
redis_bd_results = 'hash_results'

#Method to test the redis connectivity
def test_redis():
    redis.set("msg:hello", "Hello Redis!!!")
    msg = redis.get("msg:hello")
    print(msg)  

#Metgod to empty lists of Redis.
def empty():
    redis.flushall()
    redis.flushdb()

#We will have two type of functions, wordcount and countwords.  
        # type_of_function --> [wordcount]
        # type_of_function --> [countwords]


# Master sends to redis the tasks:
def send_task_queue(job_ID, function, address,state):
    
    #We create the body of the object(json) to save in redis.
    data = {
        'job_ID': job_ID,
        'type_of_function': function,
        'address': address,
        'state': state,
        'time': time.time()
    }
    redis.rpush(redis_bd_tasks, json.dumps(data))

# Worker sends to redis the intermediate result from job:
def send_intermediate_queue(job_ID, function,state,result):
    
    data = {
        'job_ID': job_ID,
        'type_of_function': function,
        'state': state,
        'result': result,
        'time': time.time()
    }
    redis.rpush(redis_bd_intermediate, json.dumps(data))

# Method to get all items of the list.
def get_task_queue(queue_name):
    return redis.lrange(queue_name,-100,100)

#Method to add hash item.
def add_hash(hash_list,job_ID,result):
    redis.hset(hash_list,job_ID,result)

#Method to get values of hash item.
def get_value_hash(hash_list, job_ID):
    return redis.hget(hash_list,job_ID)

#Method to delete item of hash table.
def delete_value_hash(hash_list,job_ID):
    return redis.hdel(hash_list,job_ID)

#Method to get items of intermediate table by key.
    #--> This table is where each process saves the result of task.
def getTaskIntermediate(key):  
    
    task = list()
    all = get_task_queue(redis_bd_intermediate)
    
    for i in all:
        t = json.loads(i, object_hook=lambda d: SimpleNamespace(**d))
        if(t.job_ID == key):
            task.append(t)
                   
    return task

# Method that removes gets and the first element in a list (FIFO).
def getFirstElement(queue_name):
    task = redis.lpop(queue_name)
    return task
     
#Main method.
if __name__ == '__main__': 
    pass
   



