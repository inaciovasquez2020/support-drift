# Support Drift Obstruction (Vasquez, 2026)  
**Failure of Uniform Local Fragmentation in Finitary Local Groups**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18434555.svg)](https://doi.org/10.5281/zenodo.18434555)

---

## Scope

This repository is a **Tier A module** in the **Scientific Infrastructure (URF)**.  
It provides a **canonical negative result** in the locality program:
the structural obstruction known as **Support Drift**.

It contains:
- a closed formal lemma,
- deterministic group-theoretic counterexamples,
- a permanent refutation object for ULF-style locality claims.

No simulations or probabilistic arguments are used.  
All results are structural and deterministic.

---

## Institutional Verification

- **Registry ID:** ART-SUPDRIFT-01  
- **Artifact Type:** Formal Lemma Module  
- **Status:** Mathematically Closed / Frozen Result  
- **Framework Alignment:** Unified Rigidity Framework (URF) — Locality Obstructions  

---

## Significance Statement

The **Support Drift Obstruction** establishes that
**Uniform Local Fragmentation (ULF) fails** for the finitary local permutation group:

\[
\Gamma_0(\mathbb{R})
\]

This provides a **structural impossibility result**:
no bounded-radius generating system can yield a uniform presentation
for local permutations on continuous supports.

This refutes an entire class of locality-to-global rigidity arguments
based on fragmentation heuristics.

---

## Core Result

### Support Drift Theorem

ULF fails for \(\Gamma_0(\mathbb{R})\):

- commutator width is infinite,
- local generators exhibit unbounded drift,
- no finite-radius presentation can stabilize supports.

Consequences:

- Non-Abelian Subadditivity (NAS) fails,
- FP-from-BCW is false,
- locality-based normal forms collapse.

---

## Contents

- `support_drift_obstruction.tex` — Formal lemma (LaTeX)  
- `support_drift_obstruction.pdf` — Compiled, citable artifact  
- `support_drift_module.tex` — Drop-in structural module  

These files constitute a permanent scientific object:
- globally addressable,
- versioned,
- cryptographically auditable.

---

## Reproducibility

All results are deterministic.

Verification consists of:

```bash
open support_drift_obstruction.pdf
