# module-14-automation-with-python

## Init

### Terraform

copy `terraform/terraform.tfvars.example` to `terraform/terraform.tfvars`

- change `instances_count` to the number of EC2s to create. Default: 1
- add your public ip address

```bash
terraform init && terraform apply
```

### Deps

```bash
pip install boto3 schedule
```

## List VPCs

`cd vpcs`

```bash
python main.py
```

## EC2 Health Checks

`cd ec2_healthcheck`

```bash
python main.py
```
