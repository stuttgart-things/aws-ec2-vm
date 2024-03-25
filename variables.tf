variable "region" {
  default     = false
  type        = string
  description = "AWS region"
}

variable "vpc" {
  default     = false
  type        = string
  description = "Virtual Private Cloud id"
}

variable "ami" {
  default     = false
  type        = string
  description = "AWS Machine Image id"
}

variable "itype" {
  default     = false
  type        = string
  description = "Instance Type"
}

variable "subnet" {
  default     = false
  type        = string
  description = "Subnet id"
}

variable "publicip" {
  default     = false
  type        = string
  description = "Use of public ip True/false"
}

variable "secgroupname" {
  default     = false
  type        = string
  description = "Name of Security Group"
}

variable "package_update" {
  type        = bool
  default     = false
  description = "package update during cloud init"
}

variable "package_upgrade" {
  type        = bool
  default     = false
  description = "package upgrade during cloud init"
}

variable "packages" {
  type        = list(string)
  default     = ["git", "vim"]
  description = "packages to be installed during cloud init"
}

variable "instance_tags" {
  type        = map(string)
  default     = {}
  description = "To define the tags for resources"
}

variable "init_username" {
  default     = false
  type        = string
  description = "init ssh user (cloud-init)"
}

variable "init_sudo" {
  default     = "ALL=(ALL) NOPASSWD:ALL"
  type        = string
  description = "init ssh user (cloud-init) sudo command"
}

variable "init_groups" {
  default     = "ubuntu, admin"
  type        = string
  description = "init ssh user (cloud-init) init group"
}

variable "init_pubkey" {
  default     = false
  type        = string
  description = "init ssh user (cloud-init) pub key"
}