import networkx as nx

file_name = "input.txt"

G = nx.DiGraph()

sum = 0
section2 = False

with open(file_name, 'r') as file:
    for line in file:

        if line == "\n":
            section2 = True
            continue

        if not section2:
            rule = line.strip().split("|")
            G.add_nodes_from(rule)
            G.add_edge(rule[0], rule[1])
        else:
            update = line.strip().split(",")

            valid = True
            for i in range(len(update)-1):
                if not G.has_edge(update[i], update[i+1]):
                    valid = False
        
            if valid:
                sum += int(update[int(len(update)/2)])

print(sum)