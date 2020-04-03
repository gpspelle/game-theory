from random import randrange, choice
from uuid import uuid4
from argparse import ArgumentParser
from numpy import random as rd
import sys




def main(fname, size, dist, lam):

    with open(fname, 'w') as fout:
        #Each graph have the same amount of nodes 
        size = int(size) - 1
        #Title of each test file
        fout.write("parity " + str(size+1) + ";\n")
        
        #Loop to create each node
        for i in  range(size+1):
            #node_name
            fout.write(str(i) + ' ')
            #color
            priority = randrange(1, 100)
            fout.write(str(priority) + ' ')
            #player
            owner = randrange(0, 2)
            fout.write(str(owner) + ' ')
            #Neighbours
            #Number of edges of the this node
            if dist == "unif": 
                number_of_edges = randrange(1, size+1)
            elif dist == "poisson":
                number_of_edges = rd.poisson(int(lam)) + 1
                if number_of_edges > size:
                    number_of_edges = size
            elif dist == "heavy":
                number_of_edges = int((rd.pareto(1.0) + 1) * (1 + 0.05 * size))
                if number_of_edges > size:
                    number_of_edges = size
            
            #Defining connected nodes to node i
            sequence = list(range(size+1))
            #No self-loops allowed
            sequence.remove(i)
            for j in range(number_of_edges):
                t = choice(sequence)
                fout.write(str(t))
                sequence.remove(t)
                if j == number_of_edges - 1:
                    fout.write(" ")
                else:
                    fout.write(",")

            #Create a uuid for each node
            uuid = uuid4()
            fout.write("\"" + str(uuid) + "\";\n")

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--fname", help="name of the file to be created", nargs=1, required=True)
    parser.add_argument("--size", help="size of each graph. Default = 30", nargs=1, required=True)
    parser.add_argument("--dist", help="unif/poisson/heavy -> probability distribution of the degree of each node", nargs=1, required=True)
    parser.add_argument("--lam", help="value of lambda for poisson distribuitions", nargs=1, required=True)

    try:
        args = parser.parse_args()
    except:
        parser.print_help(sys.stderr)
        exit(1)

    main(args.fname[0], args.size[0], args.dist[0], args.lam[0])
