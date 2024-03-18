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

variable "key_name" {
  default     = false
  type        = string
  description = "Key name for ssh key"
}

variable "secgroupname" {
  default     = false
  type        = string
  description = "Name of Security Group"
}

variable "ssh_path" {
  default     = false
  type        = string
  description = "Path for ssh public key"
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

variable "users" {
  type = list(object({
    name               = string
    gecos              = string
    sudo               = string
    groups             = string
    lock_passwd        = bool
    ssh_authorized_key = string
  }))
  default     = []
  description = "A list of users created during cloud-init"
}

variable "instance_tags" {
  type = map(string)
  default = {
    Name = "SERVER01"
    Environment = "DEV"
    OS = "UBUNTU"
    Managed = "IAC"
  }
}