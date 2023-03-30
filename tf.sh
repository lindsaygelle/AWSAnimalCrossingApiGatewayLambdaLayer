#!/bin/bash

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --bucket)
            bucket=$2
            shift 2
            ;;
        --region)
            region=$2
            shift 2
            ;;
        *)
            echo "Invalid argument: $1"
            exit 1
            ;;
    esac
done

# Generate the Terraform backend file
cat <<EOF >backend.tf
terraform {
  backend "s3" {
    bucket = "$bucket"
    key    = "AnimalCrossing/ApiGatewayLambdaLayer/terraform.tfstate"
    region = "$region"
  }
}
EOF