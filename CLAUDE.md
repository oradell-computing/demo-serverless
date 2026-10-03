# CLAUDE.md

AWS CDK app (Python): API Gateway -> Lambda -> RDS. Demonstration only.

## Python Environment

1. Create once: `python3 -m venv .venv`
2. Activate before running pip, cdk, or mypy: `source .venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. New package: add it to `requirements.txt` pinned with `==`. Direct dependencies only; never `pip freeze`.
5. Stable `aws-cdk-lib` modules only. No `*-alpha` packages unless asked.
