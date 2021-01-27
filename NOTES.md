# Implementation and Design Notes

- Make _no_ assumptions about the code that is running.
- Ensure there is a way to detect errors or other events within the entire chain at any step in the chain.
- Cross-talk (functions executing within the same group of the chain can communicate)?
- Super simple api (similar to `canvas.py` in `elnino`, but clearer).
- The parent-child relationship is synchronous, but parallel between branches.
- Implicit definition of chain link size (the output node doesn't need to be told how many inlets to expect)
- Storages for processors in the chain (like `ctx_mappings`) with:
  - private, dependant, and shared contexts: private contexts are only accessible to the current processor. dependant contexts are accesible to the current processor and can be modified by upstream processors. shared contexts can be accessed by the whole stream.
  - private and dependant contexts are unique to every processor.
  - shared contexts must be atomic (thread-safe) as they can be written/read by parallel processors.
  