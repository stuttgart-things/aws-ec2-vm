# stuttgart-things/aws-ec2-vm

terraform module for creating ec2 vm instances

## EXAMPLE MODULE CALL

```hcl
module "ec2-vm" {
  source          = "github.com/stuttgart-things/aws-ec2-vm"
  #source          = "/home/sthings/projects/bosch/pat/aws-ec2-vm"
  region          = "eu-west-1"
  vpc             = "vpc-08520570421e6f9f4"
  ami             = "ami-0cccdaf0d83701c22"
  itype           = "t3.micro"
  publicip        = true
  secgroupname    = "terraform-20240325102244051600000002"
  subnet          = "subnet-09dd9c1f37ae08fb3"
  packages        = ["vim", "git"]
  package_upgrade = false
  package_update  = true
  init_username   = "sthings"
  instance_tags   = { Name = "test", Environment = "dev" }
  init_pubkey     = "ssh-rsa AAAAB3Nz.."
}

output "ec2-vm" {
  value = [module.ec2-vm.ec2instance]
}

output "cloudinit" {
  value = [module.ec2-vm.cloudinit]
}

terraform {
  backend "s3" {
    bucket = "pat-tf1"
    key    = "terraform.tfstate"
    region = "eu-west-1"
  }
}
```

## PREREQUISITES

Add access key and secret key to environment variables:

```
export AWS_ACCESS_KEY_ID=<insert access key>
export AWS_SECRET_ACCESS_KEY=<insert secret id>
```

Or install [aws-cli](https://github.com/aws/aws-cli) and run the configure command.

## CREATE (LOCAL) TEST CONFIGURATION

```bash
# EXAMPLE CALL
python3 tests/create-module-test.py \
--values tests/values.yaml \
--path /tmp/terraform/ \
--overwrites publicip=true; bucket=bossalex \
--state s3
```

## CONNECT TO MACHINE(S)

```bash
ssh <${USERNAME}>@${PUBLIC-IP}
# CHECK CLOUD-INIT LOGS
cat /var/log/cloud-init-output.log
```

## Author Information

```bash
Ankit Sharma, stuttgart-things 03/2024
Patrick Hermann, stuttgart-things 03/2024
Ana Cakva, stuttgart-things 04/2023
```

## License

Licensed under the Apache License, Version 2.0 (the "License").

You may obtain a copy of the License at [apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0).

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an _"AS IS"_ basis, without WARRANTIES or conditions of any kind, either express or implied.

See the License for the specific language governing permissions and limitations under the License.
