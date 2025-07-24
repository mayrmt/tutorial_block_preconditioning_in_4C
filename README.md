# Block Preconditioning in 4C Multiphysics

## Context and Content

[4C Multiphysics](https://4c-multiphysics.org) defers the solution of systems of linear equations to [Trilinos](https://trilinos.github.io).
Therefore, this tutorial will

- use 4C Multiphysics to assemble linear systems
- introduce basic preconditioners for iterative solvers in Trilinos
- look into block preconditioning of multiphysics systems

## Prerequesites

This tutorial builds upon 4C Multiphysics. It requires access to a build of 4C Multiphysics (newer than mid of June 2025). The location of the 4C Multiphysics executable will be assumed as `<4Cexe>`

## Organization of Course Material

### Part I: Solving linear systems arising in 3D elasticity

- Step 1: Iterative Solver without Jacobi preconditioner
- Step 2: Iterative Solver without Chebyshev preconditioner
- Step 3: Iterative Solver without ILU preconditioner
- Step 4: Iterative Solver with algebraic multigrid preconditioner
- Step 5: Weak Scaling Study

### Part II: Solving linear systems arising in 3D fluid/solid interaction

- Step 1: Iterative Solver with block-iterative preconditioner and AMG for block inverses
- Step 2: Iterative Solver with fully coupled AMG preconditioners
