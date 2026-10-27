from main import *

# 7 pts
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

# 7 pts
def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    # parent of 'b' depends on whether 'a' or 'b' is visited first
    # work it on paper to see
    assert parents['b'] == 's' or parents['b'] == 'a'
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'

# 7 pts
def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    # two possible paths depending on whether 'a' or 'b' is visited first
    assert get_path(parents, 'd') == 'sbc' or get_path(parents, 'd') == 'sabc'
