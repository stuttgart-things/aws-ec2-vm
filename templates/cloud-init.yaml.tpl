#cloud-config

# PACKAGE INSTALLATION
package_update: ${package_update}
package_upgrade: ${package_upgrade}
packages:
%{ for package in packages ~}
  - ${package}
%{ endfor ~}

# CREATE INIT SSH USER
users:
 - name: ${init_username}
   gecos: ${init_username} user
   sudo: ${init_sudo}
   groups: ${init_groups}
   lock_passwd: true
   ssh_authorized_keys:
     - ${init_pubkey}