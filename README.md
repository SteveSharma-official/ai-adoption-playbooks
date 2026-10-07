# AI Adoption Playbooks

The master repository for the **AI Adoption Playbooks** series by Steve Sharma: practical enterprise guides to adopting, governing, securing and scaling the AI platforms organisations already own.

Each book has its own hands-on lab repository. This repository links them together as git submodules and holds what every book shares: the lab standard, the validation vocabulary, the writing standard, series terminology, schemas, templates and a series-wide check.

> Status: working repository, prepared October 2026. Repository addresses are planned and will be confirmed at publication.

## Books

| Book | Title | Platform | Lab repository | Status |
|---|---|---|---|---|
| 0 | Implementing Agentic AI: Building Your Organizational Playbook | Series methodology | Not applicable | Methodology |
| 1 | The Microsoft Copilot Enterprise Playbook | Microsoft 365 Copilot, Copilot Studio, Agent 365, Microsoft Foundry | [`books/book-01-microsoft-copilot`](books/book-01-microsoft-copilot/) (submodule of `ai-adoption-copilot-playbook`) | Labs active |
| 2 | The Google Gemini Enterprise Playbook | Google Gemini for Workspace and Google Cloud | `ai-adoption-gemini-playbook` (planned) | Planned |
| 3 | The OpenAI Enterprise Playbook | ChatGPT Enterprise and the OpenAI platform | `ai-adoption-openai-playbook` (planned) | Planned |
| 4 | The Claude Enterprise Playbook | Claude for enterprise | `ai-adoption-claude-playbook` (planned) | Planned |
| 5 | The Open-Weight and Sovereign AI Playbook | Open-weight and sovereign models | `ai-adoption-open-weight-playbook` (planned) | Planned |
| 6 | The AWS Enterprise AI Playbook | AWS AI services | `ai-adoption-aws-playbook` (planned) | Planned |
| 7 | The Salesforce Agentforce Enterprise Playbook | Salesforce Agentforce | `ai-adoption-agentforce-playbook` (planned) | Planned |

Book 0 is the vendor-neutral methodology; it has no lab repository. Planned books have no folder here until their labs start (see `series/books.yaml`).

## Clone the series with its book repositories

```
git clone --recurse-submodules https://github.com/SteveSharma-official/ai-adoption-playbooks.git
cd ai-adoption-playbooks
python -m pip install -r requirements.txt
python scripts/check_series.py --run-tests
```

Already cloned without submodules? Run `git submodule update --init --recursive`.

## What every book's labs share

- **One journey:** Read, Understand, Design, Build, Test, Secure, Govern, Validate, Apply, Scale.
- **One proof sequence:** build it, break it safely, observe, remediate, prove the fix, clean up.
- **One naming scheme:** `chapter-NN/lab-NN-slug`, referred to in the book as Lab N.N.
- **One evidence pack:** `result.json`, `report.md`, `manifest.json` (SHA-256).
- **One validation vocabulary:** DESIGN VALIDATED, STATICALLY VALIDATED, LOCALLY VALIDATED, CLOUD VALIDATION REQUIRED, EXECUTION VALIDATION REQUIRED.
- **Synthetic data only**, with a fictional organisation per book.

See [standards/](standards/).

## Repository structure

```
ai-adoption-playbooks/
  README.md  LICENSE  SECURITY.md  CONTRIBUTING.md  CHANGELOG.md  requirements.txt
  series/books.yaml                 registry of books, status and lab repositories
  books/book-01-microsoft-copilot/  Book 1 lab repository (git submodule)
  standards/                        lab, validation, naming, writing and terminology standards
  schemas/lab.schema.json           the lab.json contract every lab folder must meet
  templates/book-lab-repo/          starting files for a new book's lab repository
  scripts/check_series.py           series-wide consistency check
  docs/                             getting started, adding a book, working with submodules
```

## Licence
Code and templates: MIT (see LICENSE). Book text, figures and frameworks are not licensed by this repository.
