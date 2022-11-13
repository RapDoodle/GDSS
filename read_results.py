import pickle
import matplotlib.pyplot as plt
import networkx as nx

fr=open('samples/pkl/amazon/test/Nov13-08:01:41-sample.pkl','rb')

graphs = pickle.load(fr)
i = 1
for G in graphs:
    print("This is graph No. " + str(i))
    i += 1
    print(list(G.nodes.data()))
    print(list(G.edges))
