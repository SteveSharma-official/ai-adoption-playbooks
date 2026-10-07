# Naming and Structure (all books)

| Item | Convention | Example |
|---|---|---|
| Series master repository | `ai-adoption-playbooks` | |
| Book lab repository | `ai-adoption-<platform>-playbook` | `ai-adoption-copilot-playbook` |
| Submodule path in this repository | `books/book-NN-<platform>` | `books/book-01-microsoft-copilot` |
| Lab folder | `chapter-NN/lab-NN-slug` | `chapter-06/lab-01-oversharing-exposure-report` |
| Lab ID in the book | `Lab N.N` | Lab 6.1 |
| Capstone | `capstone/<slug>` | `capstone/enterprise-ai-adoption` |

Book lab repository top level: README, LICENSE, SECURITY, CONTRIBUTING, CHANGELOG, requirements.txt, chapter folders, capstone, shared, architecture, governance, evaluations, sector-labs, docs, tests. A folder is created only when it has content.
