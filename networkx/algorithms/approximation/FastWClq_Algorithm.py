"""
Article details:A Semi-Exact Algorithm for Quickly Computing a Maximum Weight Clique in Large Sparse Graphs.
    written by Shaowei Cai, Jinkun Lin Yiyuan Wang, Darren Strash
    Submitted 08/2020; published 09/2021
    Link: https://www.jair.org/index.php/jair/article/view/12327
    Saar Barel : 316524370
    Almog Reuveny : 205883580
"""
import queue
import random

import matplotlib.pyplot as plt
import networkx as nx
import doctest
from datetime import datetime
from networkx import Graph
from networkx.algorithms.clique import max_weight_clique
import time

upper_bound0 = 0
upper_bound1 = 0
upper_bound2 = 3


def graph_builder(weight_dict, neighbors_dict):
    g = nx.Graph()
    for i in weight_dict:
        g.add_node(i, weight=weight_dict[i])
    for i in neighbors_dict:
        for j in neighbors_dict[i]:
            for k in j:
                if (int(k) in g.nodes):
                    g.add_edge(i, int(k))
                else:
                    g.add_node(int(k), weight=0)
                    g.add_edge(i, int(k))

    return FastWClq_Algorithm(g, 10)


'''
build_test_graph() - Constructs different types of graphs (in different scenarios)
'''


def build_test_graph_1():
    g = nx.Graph()
    g.add_node(0, weight=1)
    g.add_node(1, weight=2)
    g.add_node(2, weight=3)
    g.add_node(3, weight=4)
    g.add_edge(0, 2)
    g.add_edge(1, 0)
    g.add_edge(0, 3)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    return g


def build_test_graph_2():
    g = nx.Graph()
    g.add_node(0, weight=4)
    g.add_node(1, weight=12)
    g.add_node(2, weight=22)
    g.add_node(3, weight=6)
    g.add_node(4, weight=2)
    g.add_node(5, weight=13)
    g.add_node(6, weight=9)
    g.add_edge(0, 2, weight=4)
    g.add_edge(1, 0, weight=8)
    g.add_edge(0, 3, weight=12)
    g.add_edge(2, 3, weight=1)
    g.add_edge(1, 2, weight=5)
    g.add_edge(1, 3, weight=19)
    g.add_edge(4, 5, weight=15)
    g.add_edge(5, 6, weight=32)
    g.add_edge(6, 4, weight=27)
    return g


def build_test_graph_3():
    g = nx.Graph()
    g.add_node(0, weight=14)
    g.add_node(1, weight=12)
    g.add_node(2, weight=6)
    g.add_node(3, weight=5)
    g.add_node(4, weight=11)
    g.add_node(5, weight=9)
    g.add_node(6, weight=2)
    g.add_node(7, weight=3)
    g.add_node(8, weight=4)
    g.add_edge(0, 2, weight=4)
    g.add_edge(1, 0, weight=8)
    g.add_edge(0, 3, weight=12)
    g.add_edge(2, 3, weight=1)
    g.add_edge(1, 2, weight=5)
    g.add_edge(1, 3, weight=19)
    g.add_edge(4, 5, weight=15)
    g.add_edge(5, 6, weight=32)
    g.add_edge(6, 4, weight=27)
    g.add_edge(1, 7, weight=44)
    g.add_edge(8, 3, weight=99)
    g.add_edge(6, 8, weight=7)
    return g


def build_test_graph_4():
    clique_list = [8, 25, 48, 55, 128, 546, 768, 454, 985, 234]
    g = nx.Graph()
    for key in range(1,1000):
        g.add_node(key, weight=key)
    for i in range(len(clique_list)):
        for j in range(len(clique_list)):
            if i != j:
                g.add_edge(clique_list[j], clique_list[i])
    return g


def build_test_graph_5():
    g = nx.Graph()
    for key in range(1000):
        g.add_node(key, weight=key)
        g.add_edge(key, key, weight=key)
    return g


def get_weight_clique(g):
    """
    :param g: Given clique
    :return: Weight - The sum of the weights of all the vertices of the clique
    """
    weight = 0
    for node in g:
        weight += g.nodes[node]["weight"]
    return weight


def list_subtraction(x, y):
    return [item for item in x if item not in y]


def get_weight_clique_list(g, l):
    """
    :param g: Graph
    :param l: Clique List
    :return: Weight - The sum of the weights of all the vertices of the Clique List
    """
    weight = 0
    for node in l:
        weight += g.nodes[node]["weight"]
    return weight


def choose_solution_vertex(g, cand_set, t):
    """
    :param cand_set:
    :param t:
    In each iteration we will check whether the neighbor "contributes to the clique" with the help
    of Heuristic function b^.
    b^ - A heuristic function Which returns the value of a vertex, which is calculated by the average of the
    upper and lower limit that found so far and his weight
    :return: Returns the best vertex that can contribute to the current clique
    """
    max_weight = 0
    # if len(cand_set) < t:
    # upper/lower bound is missing, need to understand the if statement
    # for node in cand_set:
    if len(cand_set) != 0  :
        v_best = random.randint(0, len(cand_set) - 1)
        v_best_key = list(cand_set)[v_best]
    for i in range(t):
        v_temp = random.randint(0, len(cand_set) - 1)
        v_temp_key = list(cand_set)[v_temp]
        if g.nodes[v_temp_key]["weight"] > g.nodes[v_best_key]["weight"]:  # need to implement b^ , t is missing
            v_best_key = v_temp_key
    return v_best_key


def best_clique_weight(g):
    return g[1]


def BMS(g, node_set):
    """
    Parameters g ,node_set
    ----------
    g = graph
    node_set = candidates
    Heuristic function.
    The function searches for the node with the highest potential. (the potential is calculated according to the number of neighbors of each node)
    Return value: The node with the highest number of neighbors
    -------
    """
    rand = random.randint(0, len(node_set) - 1)
    best = list(node_set)[rand]
    for i in range(rand):
        temp = random.randint(0, len(node_set) - 1)
        temp_node = list(node_set)[temp]
        best_neighbors = len([n for n in g.neighbors(best)])
        temp_neighbors = len([n for n in g.neighbors(temp_node)])
        if temp_neighbors > best_neighbors:
            best = temp_node
    return best


def intersection(lst1, lst2):
    """
    In mathematics, the intersection of two sets A and B, is the set containing all elements of A that also belong to B
     or equivalently, all elements of B that also belong to A.
    Parameters
    ----------
    lst1 = list
    lst2 = list

    Returns the intersection of lst1 and lst2
    -------
    >>> lst1 = [0,1,2,3]
    >>> lst2 = [2,3,4,5]
    >>> lst3 = [0,1,4,5,6]
    >>> intersection(lst1,lst2)
    [2, 3]
    >>> intersection(lst1,lst3)
    [0, 1]
    >>> intersection(lst2,lst3)
    [4, 5]
    >>> lst3 = [10,20,30,40]
    >>> intersection(lst1,lst3)
    []
    """
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def FindClique(g, best_c):
    """

    :param g: Graph
    :param best_c: The best clique found so far
    :return: Returns a clique that in any iteration can be improved with the help of a
            heuristic functions: improveclique() & BMS().
    BMS() - Returns the best node key by heuristic function
    improveclique() -
    """
    start_set = None
    c = nx.Graph()
    global upper_bound0
    if start_set is None:
        start_set = g.nodes
        t = BMS(g, start_set)
    rand = random.randint(0, len(start_set) - 1)
    u_node_key = list(start_set)[rand]
    c.add_node(u_node_key, weight=g.nodes[u_node_key]["weight"])
    cand_set = [n for n in g.neighbors(u_node_key)]
    while len(cand_set) != 0 :
        v = choose_solution_vertex(g, cand_set, t)
        a = get_weight_clique(c)
        b = g.nodes[v]["weight"]
        d = get_weight_clique_list(g, intersection(list(cand_set), [n for n in g.neighbors(v)]))
        e = get_weight_clique(best_c)
        if get_weight_clique(c) + g.nodes[v]["weight"] + get_weight_clique_list(g, intersection(list(cand_set),
                                                                                                [n for n in g.neighbors(
                                                                                                        v)])) <= get_weight_clique(
                best_c):
            c = best_c
            upper_bound0 = get_weight_clique(c)
            break
        c.add_node(v, weight=g.nodes[v]["weight"])
        cand_set.remove(v)
        cand_set = intersection(list(cand_set), [n for n in g.neighbors(v)])
    if get_weight_clique(c) >= get_weight_clique(best_c):
        # c = improveclique(c) ??????????
        a = 0
    return c


def ReduceGraph(g, c0):
    """

    :param g: Graph
    :param c0: A clique
    The function goes through all the vertices of the graph and checks if the weight of the click is greater than the
    upper bound of the vertex, if so - The algorithm adds the "bad" vertex to the queue that holds all the bad vertices.
    :return: New graph - from which the "bad" vertices were removed.
    """
    q = queue.Queue()
    removed_nodes = []
    for node in g.nodes.keys():
        if upper_bound0 < get_weight_clique(c0) or upper_bound0 < get_weight_clique(
                c0) or upper_bound0 < get_weight_clique(c0):
            q.put(node)
    while not q.empty():
        u = q.get()
        u_neighbors = list([n for n in g.neighbors(u)])
        g.remove_node(u)
        removed_nodes.append(u)
        Nr = list_subtraction(u_neighbors, removed_nodes)
        for v in Nr:
            if upper_bound0 <= get_weight_clique(c0) or upper_bound0 <= get_weight_clique(
                    c0) or upper_bound0 <= get_weight_clique(c0):
                q.put(v)
    return g


def improveClique(best_c):
    c = nx.max_weight_clique(best_c)
    if get_weight_clique(best_c) < best_clique_weight(c):
        return best_c
    else:
        return c


def FastWClq_Algorithm(g: nx.Graph, cutoff: float) -> nx.Graph:
    """

    :param g: Input graph
    :param cutoff: Limiting the algorithm to a set runtime
    :return: The best clique found up to the cutoff time


    Article details:A Semi-Exact Algorithm for Quickly Computing a Maximum Weight Clique in Large Sparse Graphs.
    written by Shaowei Cai, Jinkun Lin Yiyuan Wang, Darren Strash
    Submitted 08/2020; published 09/2021
    Link: https://www.jair.org/index.php/jair/article/view/12327
    This algorithm solves 2 main problems: the first is finding the maximum clique through MCP (subgroup with the largest number of vertices)
    while the second is finding the maximum clique through weighted MWCP (each vertex has a weight).
    FastWClq_Algorithm: accepts Graph and cutoff - running time


    Example 1: A small graph (with 4 vertices) that is neither weighted nor directed. In addition, all the sides of the graph are connected to each other.
    >>> g = build_test_graph_1()
    >>> clique = FastWClq_Algorithm(g,10)
    >>> print(clique)
    ([3, 2, 1, 0], 10)

    Example 2: A medium graph (with two components) is weighted and unadjusted.
    In addition, all the sides of the graph are connected to each other in each component, so there are 2 clique in the graph
    >>> g = build_test_graph_2()
    >>> clique = FastWClq_Algorithm(g,10)
    >>> print(clique)
    ([3, 2, 1, 0], 44)

    Example 3: A large graph (with one component which divides into 2 components) is weighted and unadjusted.
    In this graph there are 2 clique after removing "bad" vertices
    >>> g = build_test_graph_3()
    >>> clique = FastWClq_Algorithm(g,10)
    >>> print(clique)
    ([2, 0, 3, 1], 37)

    Example 4: A huge graph with 100,000 nodes (2^n while n>=17)
    In most cases on heavy graphs, the algorithm will not find the final solution but will find a better solution than the other algorithms
    (If given enough time the algorithm will find the best clique)
    g = build_test_graph_4()
    clique = FastWClq_Algorithm(g,10)
    print(clique)


    Example 5: A graph with 1000 individual vertices without sides (the weight is on the vertices).
    In this example we assume that the vertex number also constitutes its weight
    >>> g = nx.Graph()
    >>> for key in range(1000):
    ...     g.add_node(key,weight = key)
    ...     g.add_edge(key,key)
    >>> g = build_test_graph_5()
    >>> clique = FastWClq_Algorithm(g,10)
    >>> print(clique)
    ([999], 999)
    """
    start = time.time()
    c = nx.Graph()
    best_c = g
    while time.time() - start < cutoff:
        while get_weight_clique(c) < get_weight_clique(best_c):
            c = FindClique(g, best_c)
        best_c = c
        g = ReduceGraph(g, best_c)
        if g is None:
            return best_c
    best_c = improveClique(best_c)
    return best_c


def toString(t):
    g = nx.Graph()
    for n in t[0]:
        g.add_node(n, weight=100)
    for i in t[0]:
        for j in t[0]:
            if i != j:
                g.add_edge(i, j)
    print("Nodes: " + str(t[0]))
    print("Weight: " + str(t[1]))
    val_map = {'A': 1.0,
               'D': 0.5714285714285714,
               'H': 0.0}

    values = [val_map.get(node, 0.25) for node in g.nodes()]

    black_edges = [edge for edge in g.edges()]

    # Need to create a layout when doing
    # separate calls to draw nodes and edges
    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g, pos, cmap=plt.get_cmap('jet'),
                           node_color="red", node_size=500)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos, edgelist=black_edges, arrows=False)
    plt.title("Best Weight Clique - FastWClq_Algorithm")
    plt.show()


if __name__ == '__main__':


    s = build_test_graph_4()
    toString(FastWClq_Algorithm(s,1))
    """
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    """
