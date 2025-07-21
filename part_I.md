# Solving linear systems arising from 3D elasticity

The following instructions will guide you through different preconditioner options
to solve a linear system

$$Ax = b$$

arising from the finite element discretization of a cantilever beam using solid elements.

> The exact details of the problem setup are not important for the course of this tutorial
and, thus, are omitted for the sake of brevity.

The simulation model with three possible meshes is defined using the following files:

- `solid.4C.yaml`: simulation parameters and boundary conditions
- `solid_small.exo`: coarse mesh
- `solid_medium.exo`: medium mesh
- `solid_large.exo`: fine mesh

## Preliminary Steps

The default intput file comes with a direct solver, so you can run it right away.
To do so, use the follwoing command:

```bash
<4Cexe> solid.4C.yaml output
```

Please verify, that the simulation has finished successfully.

## Step 0: Iterative Solver without any Preconditioner

In theory, you can run a Krylov solver without any preconditioner and it will converge in N iterations for a system with N equations.
Since performance will be bad, 4C does not offer this option,
and we also do not cover it in this tutorial.

## Step 1: Iterative Solver with Jacobi preconditioner

The `solid.4C.yaml` input file comes with a pre-configured iterative solver (GMRES) with a relaxation preconditioner, namely `Jacobi`.
In the input file, it is defined in `SOLVER 2`.
The preconditioner is configured in the file `prec_solid_Jacobi.xml`.

To switch to this solver, perform the following steps:

1. Open the `solid.4C.yaml` input file.
1. Familiarize yourself with the list `SOLVER 2`
1. To switch to the new solver,
   1. find the list `STRUCTURAL DYNAMIC`,
   1. modify the value of its parameter `LINEAR_SOLVER` to `2`.
1. Save the file `solid.4C.yaml`

Now, run the example and Observe the convergence behavior of the iterative solver.

<details>
<summary>Solution</summary>

```
STRUCTURAL DYNAMIC:
  INT_STRATEGY: "Standard"
  DYNAMICTYPE: "Statics"
  TIMESTEP: 1.0
  NUMSTEP: 1
  MAXTIME: 1
  MAXITER: 1
  DIVERCONT: "continue"
  LINEAR_SOLVER: 2
```

</details>

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
