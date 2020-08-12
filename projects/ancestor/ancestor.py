
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    queue = Queue()
    current_node = starting_node
    cache = {}
    for x in ancestors:
        if x[1] not in cache:
            cache[x[1]] = set()
        cache[x[1]].add(x[0])

    if starting_node in cache:
        queue.enqueue(cache[current_node])
    else:
        return -1

    while True:
        relations = queue.dequeue()
        current_node = min(relations)
        if current_node not in cache:
            return current_node
        else:
            queue.enqueue(cache[current_node])