# Game theory project - CentraleSupélec
 
Author - Gabriel Pellegrino da Silva

Contributor - Guilherme Lubk do Prado
	      Lucas Akira Morishita

## Graph Creation

### create\_graphs.py

Run this script to create n random graphs and save it on a specific folder. You'll need to specify how many graphs do you intend to create (num\_graphs), how many nodes each graph will have (size), and how many connexions each node will have with its neighbours. The number of connexions per node is a random variable with probability distribution function: Uniform (unif), Poisson (poisson), and Heravy-Tail (heavy). Set this p. function by altering the "dist" parameter in the code. If you choose the Poisson p. function, specify the desired rate "lambda". The graphs will be store in a folder with the following name "test\_n\_num\_graphs\_dist\_chosenDist". If Poisson p. function has been choosen, the folder will be named "test\_n\_num\_graphs\_dist\_chosenDist\_lam\_chosenLambda".

The Heavy-Tail distribution chosen was the Pareto p. distribution with alpha and X\_m equals to one multiplied by a correction factor equal to 5% the number of nodes. That means that, on average, 80% of the nodes will have less than 0.05*size connections and the remaining 20% of the nodes will have more connections than that (some being fully connected with the other nodes).

### generate\_graph.py

This script is called multiple times by create\_graphs.py to really create the graph and save it
in a file.

### tools.py

This file contains classes to create a Graph and a Node

## Result Analysis

### test.py

Run this script to call two solvers: the one developped by https://github.com/tcsprojects/pgsolver
Note that you need to follow the instructions present there to be able to use it.
The second solver is ours, fait maison.


## Solvers

### zielonka.py

This is our solver for a parity game, based on https://arxiv.org/abs/1904.12446 

### pawel\_parys.py

Pawel Parys improvements over the zielonka's algorithm, a Quasi-polynomial approach.
https://www.mimuw.edu.pl/~parys/publications/2018-parity-algorithm.pdf

## Solvers improvements

On the conclusion of his paper, https://www.mimuw.edu.pl/~parys/publications/2018-parity-algorithm.pdf, Pawel Parys commented
another five possible optimization. Some of them are implemented below, note that they are incremental, that said, op4 contain
the improvements 1, 2, 3 and 4 and the pawel\_parys.py initial improvement described on his paper.

### op1\_pawel.py
Over the years, some optimizations to Zielonka’s algorithm were proposed. Replace the loopguard WO=∅ by WO=AtrO(G,WO) (which ensures that WO will be empty in the next iteration of the loop). 

### op2\_pawel.py
check whether AtrE(G,Nh) contains all nodes of priority h−1, and if so, to extend Nh by nodes of the next highest Even priority (i.e., h−2).
It seems that these optimizations can be applied to our algorithm as well.

### op3\_pawel.py
A straightforward optimization is to decrease pO and pE to |G| at the beginning of every recursive call.

### op4\_pawel.py
One can also observe that the call to SolveO in line 13 (with the full precision) gets the same subgame H as the last call to SolveO in line 8 (with decreased precision). 
A very rough idea is to make someuse of the computations performed by the decreased-precision call during the full-precision call.
