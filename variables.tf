variable "region" {
  default     = false
  description = "AWS region"
}

variable "vpc" {
  default     = false
  description = "Virtual Private Cloud id"
}

variable "ami" {
  default     = false
  description = "AWS Machine Image id"
}

variable "itype" {
  default     = false
  description = "Instance Type"
}

variable "subnet" {
  default     = false
  description = "Subnet id"
}

variable "publicip" {
  default     = false
  description = "Use of public ip True/false"
}

variable "key_name" {
  default     = false
  description = "Key name for ssh key"
}

variable "secgroupname" {
  default     = false
  description = "Name of Security Group"
}

variable "ssh_path" {
  default     = false
  description = "Path for ssh public key"
}
