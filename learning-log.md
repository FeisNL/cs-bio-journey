Learning‑Log Entry — Session Recap ( 5 May 2025 )
Scope: Everything we covered today—every quiz item, its correct answer, and the explanatory notes you asked for, plus the mini‑lesson on Syntax / Static Semantics / Semantics.

1  Algorithms, Programs & Foundations of CS  (Quiz #1)
| Quiz Item                                                                                                            | Correct Answer                                      | Why                                                                                                                                  |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Algorithm vs Program** “An algorithm is a conceptual idea, a program is a concrete instantiation of an algorithm.” | ✅                                                   | Algorithm = abstract, language‑independent procedure. Program = one concrete expression of it in code.                               |
| **Computational mode of thinking** “Everything can be viewed as a math problem involving numbers and formulas.”      | **True**                                            | Computation = formal symbol manipulation; we encode any real‑world problem as data/operations.                                       |
| **“Computer Science studies how to build efficient machines.”**                                                      | **False**                                           | CS studies *computation itself* (what’s computable, how efficiently, theoretical limits). Building hardware is Computer Engineering. |
| **Two things every computer can do**                                                                                 | **Perform calculations** & **Remember the results** | At the lowest level a computer is just processing (ALU) + storage (memory). Display, I/O, etc. are peripherals.                      |


Key Take‑aways

Stored‑program flexibilty is what lets one machine solve many problems.

CS ≠ only hardware; it’s algorithms, theory, representation, limits.

2  Computer Architecture Basics  (Quiz #2)
| Quiz Item                                              | Correct Answer                               | Why                                                                                                                                |
| ------------------------------------------------------ | -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Stored‑program computer does only one computation.** | **False**                                    | Its code lives in RAM, so you can load *any* sequence of instructions.                                                             |
| **Fixed‑program computer can run any computation.**    | **False**                                    | Logic is hard‑wired; you *cannot* feed it arbitrary code. (Example: basic calculator chip.)                                        |
| **Program Counter (PC)**                               | **Points to the next instruction**           | CPU fetches instruction at address = PC; then PC is updated (or overwritten by a branch).                                          |
| **“Walking through the program”**                      | **Mostly linear execution; sometimes jumps** | Default fetch‑decode‑execute moves sequentially; control‑flow ops change the PC.                                                   |
| **Need 16 primitive ops for universality.**            | **False**                                    | Turing‑completeness requires a *functionally complete* set, not a magic number; even one instruction (e.g., *SUBLEQ*) can suffice. |


Key Take‑aways

Von Neumann architecture (instructions + data in same memory) underpins general‑purpose computers.

Control flow = sequential fetch plus jumps (branches, calls, returns).

Universality is about capability, not instruction‑count.

3  Language Layers: Syntax → Static Semantics → Semantics
| Layer                   | Definition                                                                              | Example Error                                                            |
| ----------------------- | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| **Syntax**              | Grammar / legal character sequences.                                                    | `print("hi"` → `SyntaxError: '(' was never closed`                       |
| **Static Semantics**    | Rule‑checks the interpreter/compiler can decide *before* running (scope, arity, types). | `add(2)` when `add(a, b)` expects 2 args → `TypeError` in many languages |
| **(Dynamic) Semantics** | Actual runtime meaning / behavior.                                                      | Fahrenheit conversion bug returns wrong value though code *runs*.        |


Mental Debug Flow
1. Parser blows up? → Syntax.
2. Compiles but fails early? → Static semantics.
3. Runs but wrong output / crash? → Semantic (logic) issue.