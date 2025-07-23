# Solving linear systems arising from 3D elasticity

The following instructions will guide you through different preconditioner options
to solve a linear system

$$Ax = b$$

arising from the finite element discretization of a cantilever beam using solid elements.

> The exact details of the problem setup are not important for the course of this tutorial
and, thus, are omitted for the sake of brevity.

The simulation model with three possible meshes is defined using the following files:

- `solid.4C.yaml`: simulation parameters and boundary conditions
- `gmres_solid.xml`: definition of a GMRES solver from Belos
- `solid_small.exo`: coarse mesh
- `solid_medium.exo`: medium mesh
- `solid_large.exo`: fine mesh

Meshing details:

| Mesh file | n_nodes_x | n_nodes_y | n_nodes_z |
|-----------|---------|---------|---------|
| `solid_small.exo` | 3 | 3 | 11 |
| `solid_medium.exo` | 6 | 6 | 26 |
| `solid_large.exo` |

Different preconditioners are predefined in the following files:

- `prec_solid_ifpack_Jacobi.xml`
- `prec_solid_ifpack_ILU.xml`
- `prec_solid_ifpack_GaussSeidel.xml`
- `prec_solid_muelu_sa_amg.xml`

They will be used and modified throughout this tutorial.

## Preliminary Steps

The default intput file comes with a direct solver, so you can run it right away.
To run it on `<numProc> MPI ranks, use the following command:

```bash
mpirun -np <numProcs> <4Cexe> solid.4C.yaml output
```

Please verify, that the simulation has finished successfully.

## Step 0: Iterative Solver without any Preconditioner

In theory, you can run a Krylov solver without any preconditioner and it will converge in $N$ iterations for a system with $N$ equations.
Since unpreconditioned Krylov solvers are know to deliver bad performance [^1], 4C does not offer this option,
and we also do not cover it in this tutorial.

## Step 1: Iterative Solver with Jacobi preconditioner

The `solid.4C.yaml` input file comes with a pre-configured iterative solver (GMRES) with a relaxation preconditioner, namely `Jacobi`.
In the input file, it is defined in `SOLVER 2`.
The preconditioner is configured in the file `prec_solid_Jacobi.xml`.

To switch to this solver, perform the following steps:

1. Open the `solid.4C.yaml` input file.
1. Familiarize yourself with the list `SOLVER 2` and the file `prec_solid_Jacobi.xml`.
1. To switch to the new solver,
   1. find the list `STRUCTURAL DYNAMIC`,
   1. modify the value of its parameter `LINEAR_SOLVER` to `2`.
1. Save the file `solid.4C.yaml`

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

Now, run the example and watch the convergence behavior of the iterative solver.
Study the influence of the following parameters:

- Configuration of the preconditioner:

  - Number of sweeps: `"relaxation: sweeps"`
  - Number of sweeps: `"relaxation: damping factor"`

- Mesh (to be set in `solid.4C.yaml`)

  - `solid_small.exo`
  - `solid_medium.exo`
  - `solid_large.exo`

Discuss the observations with your colleagues.

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

[^1]: Y. Saad. Iterative Methods for Sparse Linear Systems. SIAM, Philadelphia, PA, USA, 2003
