module "ec2-vm" {
  source = "/home/sthings/projects/bosch/ankit/aws-ec2-vm"
  region = "eu-west-1"
  vpc = "vpc-08520570421e6f9f4"
  ami = "ami-0cccdaf0d83701c22"
  itype = "t3.micro"
  publicip = true
  secgroupname = "terraform-20240325102244051600000002"
  ssh_path = "~/.ssh/id_rsa.pub"
  key_name = "id_rsa.pub"
  packages = ["wget", "whoami", "chmod", "mv", "update-ca-certificates"]
  package_upgrade = true
  subnet = "subnet-09dd9c1f37ae08fb3"
  package_update = true
  users           = [{ name = "sthings", gecos = "sthings user", groups = "admin, ubuntu", lock_passwd = "true", sudo = "ALL=(ALL) NOPASSWD:ALL", ssh_authorized_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsHiyet7tO+qXYKEy6XBiHNICRfGsBZYIo/JBQ2i16WgkC7rq6bkGwBYtni2j0X2pp0JVtcMO+hthqj37LcGH02hKa24eAoj2UdnFU+bhYxA6Mau1B/5MCkvs8VvBjxtM3FVJE7mY5bZ19YrKJ9ZIosAQaVHiGUu1kk49rzQqMrwT/1PNbUYW19P8J2LsfnaYJIl4Ljbxr0k52MGdbKwgxdph3UKciQz2DhutrmO0gf3Ncn4zpdClldaBtDB0EMMqD3BAtEVsucttzqdeYQwixMTtyuGpAKAJNUqhpleeVhShPZLke0vXxlA6/fyfkSM78gN2FQcRGVPN6hOMkns/b" }]
}

output "ec2-vm" {
  value       = [module.ec2-vm.ec2instance]           ### referencing output value from child module ###
}

output "cloudinit" {
  value       = [module.ec2-vm.cloudinit]           ### referencing output value from child module ###
}