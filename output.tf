output "ec2instance" {
  value = aws_instance.project-iac.public_ip
}

data "template_file" "cloudinit" {
  template = templatefile(
    "${path.module}/templates/cloud-init.yaml.tpl",
    {
      "package_update"  = var.package_update
      "package_upgrade" = var.package_upgrade
      "init_username"   = var.init_username
      "init_sudo"       = var.init_sudo
      "init_pubkey"     = var.init_pubkey
      "init_groups"     = var.init_groups
      "packages"        = var.packages
  })
}

output "cloudinit" {
  value = data.template_file.cloudinit.rendered
}