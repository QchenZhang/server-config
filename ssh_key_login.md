### How To Configure SSH Key-Based Authentication on a Linux Server
This method allows user to login using private and public based authentication,
therefore, you don't have to enter password every time when you login.   
[Detail Info](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)

##### Simple instruction
- create private and public key on your local machine. 

      ssh-keygen

- copy your public key to server

      ssh-copy-id username@remote_host
