### How To Configure SSH Key-Based Authentication on a Linux Server
[Detail Info](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)

##### Simple instruction
- create private and public key

      ssh-keygen

- copy your public key to server

      ssh-copy-id username@remote_host
