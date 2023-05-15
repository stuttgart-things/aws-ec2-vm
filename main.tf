provider "aws" {
  profile    = "default"
  region     = var.region
  # export AWS_ACCESS_KEY_ID
  # export AWS_SECRET_ACCESS_KEY
}

resource "aws_security_group" "project-iac-sg" {
  name = var.secgroupname
  description = var.secgroupname
  vpc_id = var.vpc

  // To Allow SSH Transport
  ingress {
    from_port = 22
    protocol = "tcp"
    to_port = 22
    cidr_blocks = ["0.0.0.0/0"]
  }

  // To Allow Port 80 Transport
  ingress {
    from_port = 80
    protocol = "tcp"
    to_port = 80
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port       = 0
    to_port         = 0
    protocol        = "-1"
    cidr_blocks     = ["0.0.0.0/0"]
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_key_pair" "my_key_pair" {
  key_name   = var.key_name
  public_key = file(var.ssh_path)
}

resource "aws_instance" "project-iac" {
  ami = var.ami
  instance_type = var.itype
  subnet_id = var.subnet #FFXsubnet2
  associate_public_ip_address = var.publicip
  key_name = var.key_name


  vpc_security_group_ids = [
    aws_security_group.project-iac-sg.id
  ]
  root_block_device {
    delete_on_termination = true
    iops = 150
    volume_size = 50
    volume_type = "gp3"
  }
  tags = {
    Name ="SERVER01"
    Environment = "DEV"
    OS = "UBUNTU"
    Managed = "IAC"
  }

  depends_on = [ aws_security_group.project-iac-sg ]
}


output "ec2instance" {
  value = aws_instance.project-iac.public_ip
}
