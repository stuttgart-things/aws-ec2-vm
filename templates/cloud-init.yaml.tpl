#cloud-config

${yamlencode({
  users = [
    for user in users : {
      name = user.name
      gecos = user.gecos
      groups = user.groups
      sudo = user.sudo
      lock_passwd = user.lock_passwd
      ssh_authorized_keys = user.ssh_authorized_keys
    }
  ]
})}


# user management
#users:
#  - name: sthings
#    gecos: sthings user
#    sudo: ALL=(ALL) NOPASSWD:ALL
#    groups: ubuntu, admin
#    lock_passwd: true
#    ssh_authorized_keys:
#      - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCsHiyet7tO+qXYKEy6XBiHNICRfGsBZYIo/JBQ2i16WgkC7rq6bkGwBYtni2j0X2pp0JVtcMO+hthqj37LcGH02hKa24eAoj2UdnFU+bhYxA6Mau1B/5MCkvs8VvBjxtM3FVJE7mY5bZ19YrKJ9ZIosAQaVHiGUu1kk49rzQqMrwT/1PNbUYW19P8J2LsfnaYJIl4Ljbxr0k52MGdbKwgxdph3UKciQz2DhutrmO0gf3Ncn4zpdClldaBtDB0EMMqD3BAtEVsucttzqdeYQwixMTtyuGpAKAJNUqhpleeVhShPZLke0vXxlA6/fyfkSM78gN2FQcRGVPN6hOMkns/b

# package installation
package_update: ${package_update}
package_upgrade: ${package_upgrade}

%{ for package in packages ~}
packages:
  - ${package}
%{ endfor ~}
