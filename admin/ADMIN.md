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
      pass mark

- change user default login shell

      # usermod --shell <path> <user>
      usermod --shell /bin/shell mark

- enforce user change password at the first time

      # chage -d 0 <user>
      chage -d 0 mark
