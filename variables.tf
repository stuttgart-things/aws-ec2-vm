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

variable "user_data" {
  type = string
  default = false
  description = "Path for user-data script"
}
