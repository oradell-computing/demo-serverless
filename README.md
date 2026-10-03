# demo-serverless
API Gateway -> Lambda -> RDS (demonstration only)

## CDK CLI

This demo uses a **global** install of the CDK CLI, for simplicity. Before installing, note whether you already have one (`cdk --version`), so teardown doesn't remove a CLI other projects need.

```
npm install -g aws-cdk
cdk --version   # record this version
```

If you get a permission error, the AWS fix is `sudo npm install -g aws-cdk`.

## AWS Credentials

You supply your own; this repo stores none. You need:

- **An AWS account you can be billed for.** RDS is not free; run Teardown when done.
- **The AWS CLI v2**, with a profile that has a default region. CDK deploys to that profile's account and region.
- **Admin-level permissions** for that profile. `cdk bootstrap` creates IAM roles, so use a sandbox account if you can.

Configure a profile with one of:

| You sign in with | Run | Notes |
| --- | --- | --- |
| IAM Identity Center (SSO), recommended | `aws configure sso` | Re-run `aws sso login --profile <name>` when the session expires. |
| IAM user access keys | `aws configure` | Long-lived keys. Never commit them. |

Then check it, and point the CDK at it if it isn't `default`:

```
aws sts get-caller-identity --profile <name>   # shows the account you'll deploy to
export AWS_PROFILE=<name>                      # or add --profile <name> to each cdk command
```

## Setup

Prerequisites: Node.js, Python 3.11+, the CDK CLI (above), and AWS credentials (above).

```
git clone <repo-url> && cd demo-serverless
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r requirements-dev.txt
cdk synth                # check: builds the template, no AWS changes
cdk bootstrap            # once per account and region
cdk deploy
```

## Teardown

When the demo is over, remove it in this order. Run steps 1-2 while the CLI is still installed.

1. **Stacks:** `cdk destroy --all`
2. **Leftover AWS resources:**
   - **RDS snapshots:** by default, RDS takes a final snapshot on delete, and snapshots keep costing money. Delete them in the RDS console.
   - **Bootstrap stack:** do this only if nothing else in this account and region uses CDK. Empty and delete the `cdk-*-assets-<account>-<region>` S3 bucket and `cdk-*-container-assets-<account>-<region>` ECR repository; deleting the stack leaves them behind. Then run `aws cloudformation delete-stack --stack-name CDKToolkit`.
3. **CLI:** `npm uninstall -g aws-cdk` (use `sudo` if you installed with it). Confirm with `command -v cdk`, which should print nothing. Skip this step if the CLI was already installed before the demo.
4. **Local files:** `rm -rf .venv cdk.out`
