# Lab Standard (all books)

Every lab README uses these sections in this order:

Lab X.X Name; What You Will Build; Why This Matters; Enterprise Scenario; Learning Objectives; Prerequisites; Architecture;
Repository Structure; Step 1 Environment Setup; Step 2 Configure; Step 3 Build; Step 4 Test; Step 5 Secure; Step 6 Break It Safely;
Step 7 Observe; Step 8 Remediate; Step 9 Validate; Expected Results; Evidence; Common Problems; Security Considerations;
Enterprise Application; Production Considerations; Cleanup; Further Challenge; Validation status.

Every lab folder contains `lab.json`, `starter/` (with `run.py`), `solution/`, `lab-changes/` and, where the fix differs from the
solution, `solution-after-break/`. A `REMOVE.txt` in an overlay lists files to delete.

## Proof sequence (enforced by each book's tests)
1. Starter runs and returns the status declared in `lab.json` (PASS for a compliant baseline, FAIL when the starter is the finding).
2. Solution overlay returns PASS.
3. `lab-changes/` overlay (break it safely) returns FAIL with a named blocking rule.
4. Fix overlay (`solution-after-break/` if present, otherwise `solution/`) returns PASS.
5. `evidence/manifest.json` lists a SHA-256 hash for each evidence file.

## Difficulty levels
1 Explore, 2 Build, 3 Integrate, 4 Secure, 5 Evaluate, 6 Govern, 7 Deploy, 8 Scale.

## Rules
- Offline first; no API keys. Tenant or cloud steps are optional, isolated, and marked CLOUD VALIDATION REQUIRED until executed.
- No console screenshots; evidence is files.
- No empty folders.
