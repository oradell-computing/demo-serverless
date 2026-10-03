# CLAUDE.md

AWS CDK app (Python): API Gateway -> Lambda -> RDS. Demonstration only.
Scaffolded with `cdk init app --language python`; never re-run `cdk init`.

## Python Environment

1. Fresh clone only: `python3 -m venv .venv`
2. Activate before running pip, cdk, or mypy: `source .venv/bin/activate`
3. Install: `python -m pip install -r requirements.txt -r requirements-dev.txt`
4. Never `pip install` outside `.venv` or with `sudo`.
5. New package: add it pinned with `==` to `requirements.txt` (app) or `requirements-dev.txt` (tests, tooling). Direct dependencies only; never `pip freeze`.
6. The `cdk` CLI is an npm package installed globally by the user (see README). Never install, upgrade, or `pip install` it.
7. Stable `aws-cdk-lib` modules only. No `*-alpha` packages unless asked.
