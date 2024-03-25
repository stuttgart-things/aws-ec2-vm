# stuttgart-things/aws-ec2-vm

terraform module for creating ec2 vm instances

## EXAMPLE MODULE CALL

```hcl
module "ec2-vm" {
  source        = "github.com/stuttgart-things/aws-ec2-vm"
  region        = "eu-central-1"
  vpc           = "vpc-ec6e8e86"
  ami           = "ami-023adaba598e661ac"
  itype         = "t2.micro"
  subnet        = "subnet-19213454"
  publicip      = true
  key_name      = "~/.ssh/id_rsa.pub"
  secgroupname  = "IAC-Sec-Group"
  ssh_path      = "pub.key"
ssh_path        = "/home/shq1kor/.ssh/id_rsa.pub"
  package_upgrade = "true"
  package_update  = "true"
  packages        = ["wget", "whoami", "chmod", "mv", "update-ca-certificates"]
  users           = [{ name = "patrick", gecos = "patrick user", groups = "admin, ubuntu", lock_passwd = "true", sudo = "ALL=(ALL) NOPASSWD:ALL", ssh_authorized_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCfYG248QubjU8EQN0tjIwq5CSJn2kMvGa/2IbPtXqR3UeDNdZ6QDaaXk7IyGeTAcNH5JnAO7gVBIrH5UEFBUWGQ84JbiDoDfLNNV9IXDagXHfv41wFP8Bhd026LoQqUEBU5/Uc+N+myq29pRpH0v+ko55cmxAq3JEvIJ6FqCIi4NQNT4zi2V0CAbWsHMbx9+bLAqQhyHtx+vBxncEtfuS7H6qjipDmXsnCJPVlnh2RjhPKCivQTBLozQm8xT0isFiSuRXsKg3fPz6s14YrAR7pA3oeRmHF4o0OVHN2XCY+zp8+E+nPeZ7j8eoL+iZuQgVxk5ISVpT1iMpDBLRyGdqHD02BlkqAKVhLHUoeWFbjLw1ge7QYz63BwYOxEme+9VHImT3f+nRzCUUiiwgzyCURcUKraD3CTSJXmy3rA2ADrUuswIsoNm0E3JnDqsRP8NMcZR22R1NkEXuMhiPGeY6FbqSAPOoOir9KZBS3ZUFq37pyHq0Fqbp/PAQq1BONBr0= shq1kor@BMH2-C-00134" }]

}

output "ec2-vm" {
  value       = [module.ec2-vm.ec2instance]           ### referencing output value from child module ###
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
