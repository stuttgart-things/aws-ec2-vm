terraform {
  required_version = ">= 1.5.5"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.34.0"
    }
    template = {
      source  = "hashicorp/template"
      version = "~> 2"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = var.region
}