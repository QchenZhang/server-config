### Menu
- [Server Spec](#server-Specifications)
- [Login Policy](#Login-Policy)
- [Python](#python)
- [Linux Commands](#Linux-Commands)
- [SSH Key-Based Authentication](ssh_key_login.md)

#### Server Specifications
|Server IP| CPU   | RAM |  SSD/HDD* | GPU | System | Ports** |Admin |
| :---: | :---: | :---: | :---: | :---: | :---: | :---:|
|170.140.150.87|i7 6700k|64GB|512GB/1TB|-|Ubuntu 18.04| 22 | Qiuchen, Mark |
|170.140.150.240|i7 6700k|64GB|512GB/1TB|-|Ubuntu 16.04| 22 | Qiuchen, Mark |
|170.140.150.91|i7 8700k|32GB|256GB/6TB|GTX 1080Ti x 2|Ubuntu 16.04| 22 | Qiuchen, Mark |

__*__ Storage: The SSD is for OS and system wide software. All users
data is stored in HDD.  
__**__ Ports: Ask admin if you need other ports to be open.



#### Login Policy
At the request of department, for the security reason, we can only access
the servers form Emory network. (e.g. Lab WIFI, Ethernet, VPN)  
- [Emory VPN](http://it.emory.edu/security/vpn.html)
- [Account sign up](https://goo.gl/forms/J11mLy2AhOegSkkg2)

#### Python
- Python version management   
By default _3.6.5_ and _2.7.15_ are installed.  
If you want other version of python or you want to mange your own python version,
I recommend [pyenv](https://github.com/pyenv/pyenv). You can simply download the
[script](https://github.com/pyenv/pyenv-installer) and install your own python
in your user-local directory.

- Python package management
  - _pip_  
    - Download script  

          curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    - Install _pip_  

          python get-pip.py --user
    - Add _pip_ to your PATH  

          export PATH="$PATH:/home/$USER/.local/bin"
    - Using _pip_ to install package  

          pip install <package> --user

    __Note:__ If you are using _pyenv_, you don't need to specify _--user_

  - Other package management tools (e.g. anaconda)  
    [( ͡° ͜ʖ ͡°)](https://www.google.com)

- Virtual environment  
When you need  mange different versions of packages, this is the recommend
method
  - _virtualenv_
    - install _virtualenv_  

          pip install virtualenv --user
    - create virtual environment  
    `-p PYTHON_EXE` The Python interpreter to use

          virtualenv -p `which python` <name>
    - activate virtual environment

          source <name>/bin/activate
    - deactivate

          deactivate

    - remove virtual environment

          rm -r <name>
  - other virtual environment tools (e.g. venv)  
    [( ͡° ͜ʖ ͡°)](https://www.google.com)

#### Linux Commands
- Check GPU usage

      nvidia-smi

- Display Linux processes

      top
      # enter q to quit

- Copy a file from local to remote

      scp <local path> <user>@<remove ip>:<remote path>
