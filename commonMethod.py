######################################################################
#  Project: Cluster Master-Workers                                   #
#  Subject: SD - Distributed Sistems                                 #
#  Authors: Younes Kabiri <younes.kabiri@estudiants.urv.cat.>        #
#           Safia Guellil <safia.guellil@urv.cat>                    #
#  Version: 1.0                                                      #
#  Date: 19-05-2021                                                  #
#  Title-File: commonMethod                                          #
#  Description: In this class, we will process files.                #
#                                                                    #
######################################################################

import urllib.request


#run_wordcount: Method which counts and shows the number of times when each word appears.
def run_wordcount(file):
    
    #consume the file using the http protocol.
    with urllib.request.urlopen(file) as url:  
        #To avoid ascii transformations
        s = url.read().decode('utf-8')
        chain = s
        #Splitting and cleaning chain.
        listWords = chain.replace(',', ' ').replace('.', ' ').split()
        frequencyWords = []
        #Counting the word's frequency
        for w in listWords:
            frequencyWords.append(listWords.count(w))

        #we will return map obbject.
        return dict(zip(listWords, frequencyWords))


#run_counterWord: Method which counts the total number of words that appears in the file.
def run_counterWord(file):
    #consume the file using the http protocol.
    with urllib.request.urlopen(file) as url:
        s = url.read()
        res = len(s.split())
        #If the result is empty, we will return zero number.
        if (s == '') :
            res = 0
    return res


#Main method.
if __name__ == "__main__":
    pass
    
    