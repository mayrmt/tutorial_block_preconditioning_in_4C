#!/bin/python3

print("ID\tn_x\tn_y\tn_z\tn_nodes\tn_dofs\tn_procs")

for n_nodes_short in range(1,30):
    n_nodes = 5 * (n_nodes_short ** 3)
    n_dofs = n_nodes * 3
    n_procs = n_dofs / 30000

    print(f"{n_nodes_short}\t{n_nodes_short}\t{n_nodes_short}\t{n_nodes_short * 5}\t{n_nodes}\t{n_nodes * 3}\t{n_procs}")
