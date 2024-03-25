# stuttgart-things/aws-ec2-vm

terraform module for creating ec2 vm instances

## EXAMPLE MODULE CALL

```hcl
module "ec2-vm" {
  source          = "github.com/stuttgart-things/aws-ec2-vm" # /home/sthings/projects/tf/aws-ec2-vm
  region          = "eu-west-1"
  vpc             = "vpc-08520570421e6f9f4"
  ami             = "ami-0cccdaf0d83701c22"
  itype           = "t3.micro"
  publicip        = true
  secgroupname    = "terraform-20240325102244051600000002"
  ssh_path        = "~/.ssh/id_rsa.pub"
  key_name        = "id_rsa.pub"
  packages        = ["wget", "whoami", "chmod", "mv", "update-ca-certificates"]
  package_upgrade = true
  subnet          = "subnet-09dd9c1f37ae08fb3"
  package_update  = true
  init_username   = "sthings"
  init_pubkey     = "ssh-rsa AAAAB3Nz #..."
}

output "ec2-vm" {
  value = [module.ec2-vm.ec2instance] ### referencing output value from child module ###
}

output "cloudinit" {
  value = [module.ec2-vm.cloudinit] ### referencing output value from child module ###
}
```

## PREREQUISITES

Add access key and secret key to environment variables:

```
export AWS_ACCESS_KEY_ID=<insert access key>
export AWS_SECRET_ACCESS_KEY=<insert secret id>
```

Or install [aws-cli](https://github.com/aws/aws-cli) and run the configure command.

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
