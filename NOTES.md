# Implementation and Design Notes

- make _no_ assumptions about the code that is running
- ensure there is a way to detect errors or other events within the entire chain at any step in the chain.
- cross-talk (functions executing within the same group of the chain can communicate)?
- super simple api (similar to `canvas.py` in `elnino`, but clearer)
- the parent-child relationship is synchronous, but asynchronous within groups
- implicit definition of chain link size (the output node doesn't need to be told how many inlets to expect).
