import re


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


def find_loop(links):
    loops = []
    for node in links.links:
        if not is_chief_computer(node):
            continue

        for next_node_1 in links.links[node].copy():
            if next_node_1 not in links.links[node]:
                continue
            for next_node_2 in links.links[next_node_1].copy():
                if next_node_1 not in links.links[node]:
                    continue
                if node in links.links[next_node_2]:
                    loop = {node, next_node_1, next_node_2}
                    if loop not in loops:
                        loops.append(loop)

    return loops
         


links = get_links()
loops = find_loop(links)
print(len(loops))
