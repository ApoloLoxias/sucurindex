# Lessons Learnt from MVP phase

## 1. Python decorator behaviour:
```
@decorator
def func():
    ( . . .)
```
VS
```
@decorator()
def func():
    ( . . .)
```

## 2. Simple Logging:
Using a single, simple, copypasted logging apparatus and decorating mostly every
function with it works kinda ok/well enough for initial project phases, by
providing pretty good info for a really small effort

## 3. MVP pattern:
Move fast, write ugly code. Be inconsistent and try different patterns. See
how various ways of doing things fit into an integrated project. Make a proof
of concept before setting architecture in stone.

## 4. Landmarks and phases:
Spliting development of complex programs with phases with clear goals helps
to control scope and organize ideas. Furthermore, it creates a balanced cycle
of alternating high-level, abstract, strategical and architectural design and
concrete, tactical, low-level implementation, providing breathing room for
reflection, refactoring and knowledge consolidation in between intensive
building stretches.

## 4. Documentation:
Comit tests to git repo. Periodically asses project state, document assessment
and comit it to git repo. Comit ideas/thoughts to git repo. Git is not only for
core functional code. Future me will thank past me

## 5. Cool python libraries:
- os and pathlib
- argparse
- datetime
- uuid
- logging
- functools

## 6. Basic cli design:
- With argparse parsers and subparsers
- With Python's native input() function


## 7. Pure Python is not good for a search engine:
- Thinking about programming search logic with Python alone made my head hurt
- Deffer real searching functionality for after DB implementation and use SQL

## 8. Not polishing temporary code:
MVP's codebase has several isues and is pretty ugly, and yet:
1. It works
2. It successfully acts as a proof of concept
3. It let's me see how the core logical operations will get integrated in a
cohesive project, and plan better for longterm architecture
4. It demonstrates metadata file can be collected, stored and parsed in human-
readable and human-editable formats using relatively simple Python code with
acceptable performance for personal use cases

It will get documented, discarded and rebuilt with judicious copying of
chosen snippets, rather than laboriously iterated upon before getting
refactored due to big architectural shifts

## 9. Personal Projects Benefict from Personality:
Very dry and technical code can get boring. Injecting some creativity into the
project can keep it fun to work on and enjoyable to use.

---

*"Skin sheds. Venom linger"*