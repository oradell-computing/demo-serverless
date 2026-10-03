# CLAUDE.md

AWS CDK app (Python): API Gateway -> Lambda -> RDS. Demonstration only.

## Python Environment

1. Fresh clone only: `python3 -m venv .venv` (`cdk init` creates it for new projects).
2. Activate before running pip, cdk, or mypy: `source .venv/bin/activate`
3. Install: `python -m pip install -r requirements.txt`
4. Never `pip install` outside `.venv` or with `sudo`.
5. New package: add it to `requirements.txt` pinned with `==`. Direct dependencies only; never `pip freeze`.
6. The `cdk` CLI is an npm package installed globally by the user (see README). Never install, upgrade, or `pip install` it.
7. Stable `aws-cdk-lib` modules only. No `*-alpha` packages unless asked.
