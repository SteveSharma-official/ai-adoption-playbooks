# Book Lab Repository Template

Starting files for a new book's lab repository. Copy this folder into a new repository named `ai-adoption-<platform>-playbook`, then:

1. Rename `README.template.md` to `README.md` and fill in the book details.
2. Keep `tests/test_lab_sequences.py` and `shared/scripts/start-lab.py` unchanged so every book behaves the same way.
3. Write the shared engines for the book under `shared/<package>/` and synthetic data under `shared/datasets/<organisation>/`.
4. Add labs as `chapter-NN/lab-NN-slug/` with `lab.json`, `starter/run.py`, `solution/` and `lab-changes/`.
5. Add the repository to this master as a submodule (see docs/adding-a-book.md).

These files are copied from Book 1, which is the reference implementation.
