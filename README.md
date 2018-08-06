### Menu
- [Python](#python)
- [SSH Key-Based Authentication](ssh_key_login.md)


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

          virtualenv <name>
    - activate virtual environment

          source <name>/bin/activate
    - deactivate

          deactivate

    - remove virtual environment

          rm -r <name>
  - other virtual environment tools (e.g. venv)  
    [( ͡° ͜ʖ ͡°)](https://www.google.com)
