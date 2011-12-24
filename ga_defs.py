import random
import time
from celery.task import task

class genome():
 def __init__(self,sz,genes=None):
  self.fitness=0
  if(genes==None):
   self.genes=[random.random() for x in range(sz)]
  else:
   self.genes=genes[:]
 def mutate(self):
  for k in range(len(self.genes)):
   if random.random()<0.05:
    self.genes[k]+=(random.random()*2.0-1.0)*0.1
    self.genes[k]=max((self.genes[k],0.0))
    self.genes[k]=min((self.genes[k],1.0))

class domain():
 def __init(self):
  pass
 def evaluate(self,genome):
  time.sleep(random.random()*5.0)
  fitness = sum(genome.genes)
  return fitness

@task
def evaltask(domain,genome):
 fit=domain.evaluate(genome)
 return fit
