# Adding a Book's Lab Repository

1. Create the book repository from `templates/book-lab-repo/` and name it `ai-adoption-<platform>-playbook`.
2. Build and test the labs in that repository; publish it.
3. In this repository: `git submodule add ../ai-adoption-<platform>-playbook books/book-NN-<platform>`.
4. In `series/books.yaml`, set the book's status to `labs-active` and set `submodule_path`.
5. Run `python scripts/check_series.py --run-tests` and commit.
