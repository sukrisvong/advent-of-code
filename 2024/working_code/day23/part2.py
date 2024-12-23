import re
from itertools import combinations

NODE_STARTS_WITH_T_REGEX = "t."

class Links:
    def __init__(self):
        self.links = {}

    def add(self, node1, node2):
        if node1 in self.links:
            self.links[node1].add(node2)
        else:
            self.links[node1] = { node2 }
        if node2 in self.links:
            self.links[node2].add(node1)
        else:
            self.links[node2] = { node1 }

    def remove(self, node1, node2):
        if node1 in self.links:
            self.links[node1].remove(node2)
        if node2 in self.links:
            self.links[node2].remove(node1)
    
    def __str__(self):
        s = ''
        for key, value in self.links.items():
            s += f'{key}: {value}\n'
        return s

def get_links():
    ACTUAL_FILE = "input.txt"
    TEST_FILE = "input_test.txt"
    links = Links()
    with open(ACTUAL_FILE, "r") as input_file:
        for line in input_file.readlines():
            nodes = line.strip().split('-')
            links.add(*nodes)

    return links

def is_chief_computer(node):
    matches = re.findall(NODE_STARTS_WITH_T_REGEX, node)
    return len(matches) > 0

def are_all_connected(links, nodes):
    for n in range(len(nodes)):
        for m in range(n+1, len(nodes)):
            if nodes[m] not in links[nodes[n]]:
                return False
    return True

def find_all_connected(links, connection_size):
    for node in links:
        next_nodes = links[node]
        groups = list(combinations(next_nodes, connection_size - 1))
        for group in groups:
            if are_all_connected(links, group):
                return [node] + [n for n in group]
    return []

links = get_links()
# print(links)
max_output = []
for n in range(len(links.links)):
    output = find_all_connected(links.links, n+1)
    if len(output) > len(max_output):
        max_output = output
max_output.sort()
print(','.join(max_output))
