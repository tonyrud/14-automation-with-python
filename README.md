# module-14-automation-with-python

## Init

### Terraform

Use [terraform repo](https://github.com/tonyrud/terraform-learn) for resource creation

### Deps

```bash
pip install boto3 schedule
```

## List VPCs

```bash
python vpcs/main.py
```

## EC2 Health Checks

```bash
python ec2_healthcheck/main.py
```

## EC2 Add Tags

```bash
python ec2_add_tags/main.py
```

## EKS Check Cluster

```bash
python eks_status/main.py
```

## ECS Volume Backup

```bash
python ec2_backup_volumes/main.py
```

## Monitor Web App

Use terraform repo to create a single ec2 instance. The script will start a simple nginx app on port 8080

`direnv` is used for ENV vars. Copy `.envrc.example` to `.envrc`, and add email and password values. Run `direnv allow`

```bash
python monitor_website/main.py
```
