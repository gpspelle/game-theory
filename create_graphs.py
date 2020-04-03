import os
import math

#Parameters to be defined for each test
#For comparison, the number of graphs shold be high and constant
num_graphs = 1
size = 30
# Distributions availlable:
#   unif - poisson - heavy
dist = "heavy"
lam = 15

folder = "tests_n_" + str(size) + "_dist_" + dist
if dist == "poisson":
    folder = folder + "_lam_" + str(lam) + "/"
else:
    folder = folder + "/"

base_name = "test"
#defining number of digits for name encoding
nDigits = math.trunc(math.log10(num_graphs)) + 1


if not os.path.exists(folder):
    os.makedirs(folder)


print("Creating graphs\n")
for i in range(num_graphs):
    print("Created", str(i+1).zfill(nDigits), "of", num_graphs)
    os.system("python3 generate_graph.py --fname " + folder + 
        base_name + str(i).zfill(nDigits) + ".gm --size " + str(size) + " --dist " + dist
        + " --lam " + str(lam))

#File Structure
print("\nFile Structure:")
print("Header: purpose number_of_nodes")
print("Body: node_name color player neighbours id_code")
