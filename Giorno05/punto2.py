import networkx as nx

file_name = "input.txt"

G = nx.DiGraph()

def validification(G, update):
    pred = {v: sum(1 for u in update if u != v and G.has_edge(u,v)) for v in update}
    for v in pred:
        update[pred[v]] = v
    
    
somma = 0
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

            if not valid:
                validification(G, update)
                somma += int(update[int(len(update)/2)])

print(somma)