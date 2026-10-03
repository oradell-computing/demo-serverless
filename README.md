# demo-serverless
API Gateway -> Lambda -> RDS (demonstration only)

## CDK CLI

This demo uses a **global** install of the CDK CLI, for simplicity. Before installing, note whether you already have one (`cdk --version`), so teardown doesn't remove a CLI other projects need.

```
npm install -g aws-cdk
cdk --version   # record this version
```

If you get a permission error, the AWS fix is `sudo npm install -g aws-cdk`.

## Teardown

When the demo is over, remove it in this order. Run steps 1-2 while the CLI is still installed.

1. **Stacks:** `cdk destroy --all`
2. **Leftover AWS resources:**
   - **RDS snapshots:** by default, RDS takes a final snapshot on delete, and snapshots keep costing money. Delete them in the RDS console.
   - **Bootstrap stack:** do this only if nothing else in this account and region uses CDK. Empty and delete the `cdk-*-assets-<account>-<region>` S3 bucket and `cdk-*-container-assets-<account>-<region>` ECR repository; deleting the stack leaves them behind. Then run `aws cloudformation delete-stack --stack-name CDKToolkit`.
3. **CLI:** `npm uninstall -g aws-cdk` (use `sudo` if you installed with it). Confirm with `command -v cdk`, which should print nothing. Skip this step if the CLI was already installed before the demo.
4. **Local files:** `rm -rf .venv cdk.out`
