- Add new group

      # sudo groupadd <group>
      sudo groupadd phd

- Add new user  
      # -m: create home directory  
      # -g: assign to group

      # sudo useradd -m -g <group> <user>
      sudo useradd -m -g phd mark

- change password

      # passwd <user>
      passwd mark

- change user default login shell

      # usermod --shell <path> <user>
      usermod --shell /bin/bash mark

- enforce user change password at the first time

      # chage -d 0 <user>
      chage -d 0 mark

- allow user to  use docker

      # sudo usermod -aG docker <user>
      sudo usermod -aG docker mark

- firewall rule

  Please enable the firewall on the GPU server before it goes online using
these commands:

      ufw logging on
      ufw default deny incoming
      ufw default allow outgoing
      ufw allow from 170.140.150.0/23 to any port 22
      ufw allow from 170.140.147.0/24 to any port 22
      ufw allow from 10.40.0.0/16 to any port 22
      ufw allow from 10.110.0.0/16 to any port 22
      ufw enable
      ufw status`
