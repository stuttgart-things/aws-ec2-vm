resource "aws_instance" "project-iac" {
  ami                         = var.ami
  instance_type               = var.itype
  subnet_id                   = var.subnet #FFXsubnet2
  associate_public_ip_address = var.publicip
  key_name                    = var.key_name
  user_data = templatefile(
    "${path.module}/templates/cloud-init.yaml.tpl",
    {
      "package_update"  = var.package_update
      "package_upgrade" = var.package_upgrade
      "init_username"   = var.init_username
      "init_sudo"       = var.init_sudo
      "init_pubkey"     = var.init_pubkey
      "init_groups"     = var.init_groups
      "packages"        = var.packages
    }
  )

  vpc_security_group_ids = [
    aws_security_group.project-iac-sg.id
  ]

  root_block_device {
    delete_on_termination = true
    iops                  = 150
    volume_size           = 50
    volume_type           = "gp3"
  }

  tags = var.instance_tags

  depends_on = [aws_security_group.project-iac-sg]
}
