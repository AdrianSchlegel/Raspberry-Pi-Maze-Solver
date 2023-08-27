from algs4 import index_min_pq
import sys

# A*
def calc_neighbours(v, cell_array):
    print(v)
    neighbours = []
    if not cell_array[v].left_wall:
        neighbours.append(v.index-1)
    if not cell_array[v].right_wall:
        neighbours.append(v.index+1)
    if not cell_array[v].top_wall:
        neighbours.append(v.index-12)
    if not cell_array[v].bot_wall:
        neighbours.append(v.index+12)

    return neighbours


def relax_astar(v, w, dist, h, indexpq):
    if dist[w] > dist[v]:
        w.referrer = v
        dist[w] = dist[v]
        if indexpq.contains(w):
            indexpq.decrease_key(w, dist[w] + h[w])
        else:
            indexpq.insert(dist[w] + h[w], w)


def astar_algo(cell_array):
    indexpq = index_min_pq.IndexMinPQ(96)
    t = cell_array[-1]
    s = cell_array[0]
    h = []
    dist = []

    for i in cell_array:
        dist.append(sys.maxsize)
        h.append(abs(i.pos[0] - cell_array[-1].pos[0]) + abs(i.pos[1] - cell_array[-1].pos[1]))

    dist[s.index] = s.index
    indexpq.insert(h[s.index], s.index)
    while not indexpq.is_empty():
        print(1)
        v = indexpq.min()
        if v == t:
            return dist[t]
        neighbours = calc_neighbours(v, cell_array)
        for w in neighbours:
            relax_astar(v, w, dist, h, indexpq)

    return sys.maxsize
