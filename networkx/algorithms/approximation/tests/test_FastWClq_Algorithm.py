"""Unit tests for :mod:`networkx.algorithms.approximation.FastWClq_Algorithm` module."""
import networkx as nx
from networkx.algorithms.approximation.FastWClq_Algorithm import FastWClq_Algorithm
import unittest


class test_FastWClq_Algorithm(unittest.TestCase):
    def test_null_graph(self):
        g = build_null_graph()
        self.assertFalse(FastWClq_Algorithm(g, 100), False)
        self.assertFalse(FastWClq_Algorithm(g, 1000), False)
        self.assertFalse(FastWClq_Algorithm(g, 1), False)

    def test_small_clique(self):
        g = build_small_clique()
        self.assertFalse(FastWClq_Algorithm(g, 100), False)
        self.assertFalse(FastWClq_Algorithm(g, 1000), False)
        self.assertFalse(FastWClq_Algorithm(g, 1), False)

    def test_single_node_clique(self):
        g = build_single_node_clique()
        self.assertFalse(FastWClq_Algorithm(g, 0), False)
        self.assertFalse(FastWClq_Algorithm(g, 1000), False)
        self.assertFalse(FastWClq_Algorithm(g, 100), False)

    def test_mid_clique(self):
        g = build_mid_clique()
        self.assertFalse(FastWClq_Algorithm(g, 0), False)
        self.assertFalse(FastWClq_Algorithm(g, 1000), False)
        self.assertFalse(FastWClq_Algorithm(g, 100), False)

    def test_big_clique(self):
        g = build_mid_clique()
        self.assertFalse(FastWClq_Algorithm(g, 0), False)
        self.assertFalse(FastWClq_Algorithm(g, 1000), False)
        self.assertFalse(FastWClq_Algorithm(g, 100), False)


def build_small_clique():
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


def build_single_node_clique():
    g = nx.Graph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    return g


def build_null_graph():
    return None


def build_mid_clique():
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


def build_big_clique():
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


if __name__ == '__main__':
    unittest.main()
