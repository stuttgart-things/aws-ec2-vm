terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.42.0"
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
