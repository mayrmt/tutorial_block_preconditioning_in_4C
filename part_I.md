# Solving linear systems arising from 3D elasticity

The following instructions will guide you through different preconditioner options
to solve a linear system

Ax = b

arising from the finite element discretization of a cantilever beam using solid elements.

> The exact details of the problem setup are not important for the course of this tutorial
and, thus, are omitted for the sake of brevity.

The simulation model is defined using the following files:

- `solid.4C.yaml`
- `solid_small.exo`
- `solid_medium.exo`
- `solid_large.exo`

## Preliminary Steps

The default intput file comes with a direct solver, so you can run it right away.
To do so, use the follwoing command:

```bash
<4Cexe> solid.4C.yaml output
```

Please verify, that the simulation has finished successfully.

## Step 1: Iterative Solver without any Preconditioner

1. Open the `solid.4C.yaml` input file.
1. In the list `SOLVER 1`,
   1. modify value of the parameter `SOLVER` to `Belos`.
   1. verify that the parameter `AZPREC` is set to `None`.
1. Run the example.
1. Observe the convergence behavior of the iterative solver.

## Step 2: Iterative Solver with relaxation-based Preconditioner

1. Open the `solid.4C.yaml` input file.
1. In the list `SOLVER 1`,
   1. change the parameter `AZPREC` to `Ifpack`.
   1. verify that
1. Run the example.
1. Observe the convergence behavior of the iterative solver.

## Step 3: Iterative Solver with Incompluete-LU Factorization Preconditioner

1. Open the `solid.4C.yaml` input file.
1. In the list `SOLVER 1`,
   1. change the parameter `AZPREC` to `Ifpack`.
   1. change the parameter `IFPACK_XML_FILE` to `solid_ifpack_ILU.xml`.
1. Run the example.
1. Observe the convergence behavior of the iterative solver.

You can modify the settings of the ILU preconditioner by changing the file `solid_ifpack_ILU.xml`.
In particular,

- `Overlap` defines the overlap at processor boundaries (`0` = no overlap, larger values results in larger overlap)
- `fact: level-of-fill` defines the allowed fill-in (larger values result in a better approximation, however a more expensice setup procedure)

1. Change the ILU settings and explore their impact on runtime and iteration numbers.
