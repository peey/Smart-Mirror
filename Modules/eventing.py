from queue import PriorityQueue
import datetime

jobs = PriorityQueue()

def send(delay, what):
	when = datetime.datetime.now() + datetime.timedelta(seconds=delay)
	jobs.put((when, what))