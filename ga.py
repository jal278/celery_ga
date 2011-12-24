import random

from ga_defs import *
from celery.task.sets import TaskSet

pop_size=50
genome_size=10
threshold=0.5
population=[genome(genome_size) for k in range(pop_size)]

dom=domain()
eval_concurrent=True
generations=5
generation=0

while generation<generations:
 generation+=1

 #evaluate sequential 
 if(not eval_concurrent):
  for k in population:
   k.fitness = dom.evaluate(k)
 else:
 #evaluate concurrent
  tasks=[]
  for ind in population:
   tasks.append(evaltask.subtask((dom,ind)))

  job = TaskSet(tasks=tasks)
 
  result=job.apply_async()
  fits=result.join()

  for k in range(len(population)):
   population[k].fitness=fits[k]
 
 population.sort(key=lambda k:k.fitness)
 
 #print best fitness
 print "generation: %d, best fitness %0.3f" % (generation,population[-1].fitness)
 
 #reproduce
 newpop = []
 cutoff = int(len(population)*threshold)
 cutoff_pop = population[cutoff:]
 for k in range(len(population)):
  new=genome(0,random.choice(cutoff_pop).genes)
  new.mutate()
  newpop.append(new)
 population=newpop
 
