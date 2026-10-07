# Validation Status Vocabulary (all books)

| Status | Meaning |
|---|---|
| DESIGN VALIDATED | Reviewed against the book and its sources; nothing executed |
| STATICALLY VALIDATED | Files parse and lint; nothing executed |
| LOCALLY VALIDATED | Executed on a local machine with stated versions and synthetic data, and passed |
| CLOUD VALIDATION REQUIRED | Needs a real tenant or cloud service; not yet executed |
| EXECUTION VALIDATION REQUIRED | Not yet executed in the stated environment |

Every lab README ends with a status line that names the date, environment and versions. A status is never raised without a recorded run.
