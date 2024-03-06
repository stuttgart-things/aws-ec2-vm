resource "aws_instance" "project-iac" {
  ami                         = var.ami
  instance_type               = var.itype
  subnet_id                   = var.subnet #FFXsubnet2
  associate_public_ip_address = var.publicip
  key_name                    = var.key_name
  user_data                   = data.template_file.user_data.rendered


  vpc_security_group_ids = [
    aws_security_group.project-iac-sg.id
  ]
  root_block_device {
    delete_on_termination = true
    iops                  = 150
    volume_size           = 50
    volume_type           = "gp3"
  }
  tags = {
    Name        = "SERVER01"
    Environment = "DEV"
    OS          = "UBUNTU"
    Managed     = "IAC"
  }

  depends_on = [aws_security_group.project-iac-sg]
}

data "template_file" "user_data" {
  template = file(var.user_data)
}