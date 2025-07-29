# Block Preconditioning in 4C Multiphysics

## Context and Content

[4C Multiphysics](https://4c-multiphysics.org) defers the solution of systems of linear equations to [Trilinos](https://trilinos.github.io).
Therefore, this tutorial will

- use 4C Multiphysics to assemble linear systems
- introduce basic preconditioners for iterative solvers in Trilinos
- look into block preconditioning of multiphysics systems

## Prerequesites

This tutorial builds upon 4C Multiphysics. It requires access to a build of 4C Multiphysics (newer than mid of June 2025). The location of the 4C Multiphysics executable will be assumed as `<4Cexe>`.

## Organization of Course Material

The tutorial consists of two parts. First, we look into linear systems arising from 3D elasticity. Then, we switch over to block systems as they occur in monolithic solvers for fluid/solid interaction.

### Part I: Solving linear systems arising from 3D elasticity

Tutorial steps are described in `solid_mechanics/part_I.md`. The tutorial consists of the following steps:

- Step 1: Iterative Solver without Jacobi preconditioner
- Step 2: Iterative Solver without Chebyshev preconditioner
- Step 3: Iterative Solver without ILU preconditioner
- Step 4: Iterative Solver with algebraic multigrid preconditioner
- Step 5: Weak Scaling Study

### Part II: Solving linear systems arising from 3D fluid/solid interaction

Tutorial steps are described in `fsi/part_II.md`. The tutorial consists of the following steps:

- Step 1: Iterative Solver with block-iterative preconditioner and AMG for block inverses
- Step 2: Iterative Solver with fully coupled AMG preconditioners

## Contributors

In alphabetical order:

- Bühler, Regina ([@reginabuehler](https://github.com/reginabuehler))
- Mayr, Matthias ([@mayrmt](https://github.com/mayrmt))
