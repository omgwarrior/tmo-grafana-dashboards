#!/bin/bash
set -e

# Initialize Terraform
terraform init

# Apply Terraform configuration
terraform apply -auto-approve

# Install Python dependencies
pip install -r requirements.txt
