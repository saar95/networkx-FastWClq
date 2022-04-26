"""Doc tests for the :mod:`networkx.algorithms.approximation.FastWClq_Algorithm` module."""
import networkx as nx
import doctest
import random
from networkx.algorithms.approximation import maximum_independent_set
from networkx.algorithms.approximation.FastWClq_Algorithm import FastWClq_Algorithm


"""

"""
def build_test_graph_1():
    g = nx.Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_edge(0, 2)
    g.add_edge(1, 0)
    g.add_edge(0, 3)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    return g


def build_test_graph_2():
    g = nx.Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
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
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
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
    clique_list = [8, 25, 48, 55, 128, 546, 7850, 45123, 85147, 97852]
    g = nx.Graph()
    for key in range(100000):
        g.add_node(key)
    for i in range(len(clique_list)):
        for j in range(len(clique_list)):
            if i != j:
                g.add_edge(clique_list[j], clique_list[i], weight=random.randint(0, 10000))
    return g


def build_test_graph_5():
    g = nx.Graph()
    for key in range(1000):
        g.add_node(key)
        g.add_edge(key, key, weight=key)
    return g


def test_Example_1():
    """
    Example 1: A small graph (with 4 vertices) that is neither weighted nor directed. In addition, all the sides of the graph are connected to each other.
    >>> solution_g = nx.Graph()
    >>> solution_g.add_node(0)
    >>> solution_g.add_node(1)
    >>> solution_g.add_node(2)
    >>> solution_g.add_node(3)
    >>> solution_g.add_edge(0,2)
    >>> solution_g.add_edge(1,0)
    >>> solution_g.add_edge(0,3)
    >>> solution_g.add_edge(2,3)
    >>> solution_g.add_edge(1,2)
    >>> solution_g.add_edge(1,3)
    >>> g = build_test_graph_1()
    >>> clique = FastWClq_Algorithm(g,100)
    >>> nx.is_isomorphic(solution_g,clique)
    False
    """

def test_Example_2():
    """
    Example 2: A medium graph (with two components) is weighted and unadjusted.
    In addition, all the sides of the graph are connected to each other in each component, so there are 2 clique in the graph
    >>> solution_g = nx.Graph()
    >>> solution_g.add_node(4)
    >>> solution_g.add_node(5)
    >>> solution_g.add_node(6)
    >>> solution_g.add_edge(4,5,weight=15)
    >>> solution_g.add_edge(5,6,weight=32)
    >>> solution_g.add_edge(6,4,weight=27)
    >>> g = build_test_graph_2()
    >>> clique = FastWClq_Algorithm(g,100)
    >>> nx.is_isomorphic(solution_g,clique)
    False
    """
def test_Example_3():
        """
    Example 3: A large graph (with one component which divides into 2 components) is weighted and unadjusted.
    In this graph there are 2 clique after removing "bad" vertices
    >>> solution_g = nx.Graph()
    >>> solution_g.add_node(4)
    >>> solution_g.add_node(5)
    >>> solution_g.add_node(6)
    >>> solution_g.add_edge(4,5,weight=15)
    >>> solution_g.add_edge(5,6,weight=32)
    >>> solution_g.add_edge(6,4,weight=27)
    >>> g = build_test_graph_3()
    >>> clique = FastWClq_Algorithm(g,100)
    >>> nx.is_isomorphic(solution_g,clique)
    False
    """
def test_Example_4():
    """
    Example 4: A huge graph with 100,000 nodes (2^n while n>=17)
    In most cases on heavy graphs, the algorithm will not find the final solution but will find a better solution than the other algorithms
    (If given enough time the algorithm will find the best clique)
    >>> clique_list = [8,25,48,55,128,546,7850,45123,85147,97852]
    >>> solution_g = nx.Graph()
    >>> for key in clique_list:
    ...     solution_g.add_node(key)
    >>> for i in range(len(clique_list)):
    ...    for j in range(len(clique_list)):
    ...         if i!=j:
    ...            solution_g.add_edge(clique_list[j],clique_list[i],weight=random.randint(0,10000))
    >>> g = build_test_graph_4()
    >>> clique = FastWClq_Algorithm(g,100)
    >>> nx.is_isomorphic(solution_g,clique)
    False
    """

def test_Example_5():
    """
    Example 5: A graph with 1000 individual vertices without sides (the weight is on the vertices).
    In this example we assume that the vertex number also constitutes its weight
    >>> solution_g = nx.Graph()
    >>> for key in range(1000):
    ...     solution_g.add_node(key)
    ...     solution_g.add_edge(key,key,weight = key)
    >>> g = build_test_graph_5()
    >>> clique = FastWClq_Algorithm(g,100)
    >>> nx.is_isomorphic(solution_g,clique)
    False
    """


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
