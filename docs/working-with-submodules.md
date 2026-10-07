# Working with Book Submodules

Each book folder under `books/` is a separate git repository pinned to a specific commit.

- **Update a book to its latest commit:** `git submodule update --remote books/book-01-microsoft-copilot`, then commit the new pointer in this repository.
- **Change a book's labs:** commit and push inside the book repository first, then update the pointer here. Pushing only the master leaves the book change behind.
- **Relative URLs:** `.gitmodules` uses `../ai-adoption-copilot-playbook`, so the submodule resolves next to this repository on the same GitHub account (or the same local folder). Publish book repositories under the same account as the master.
- **Order when publishing:** publish the book repository first, then this master, so the submodule URL resolves.
