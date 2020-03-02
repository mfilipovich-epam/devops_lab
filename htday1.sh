#!/bin/bash

# install dependencies
sudo yum install  -y  git gcc zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel

#needed for installation python version 2.* 
sudo yum install -y  patch 

curl -L  https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

# add PATH
echo 'export PATH="/home/student/.pyenv/bin:$PATH"' >> /home/student/.zshrc
echo 'eval "$(pyenv init -)"' >> /home/student/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/student/.zshrc

source ~/.zshrc

# install python:
pyenv install 2.7.7

pyenv virtualenv 2.7.7 my_py_2_7_7

pyenv install 3.7.5

pyenv virtualenv  3.7.5 my_py_3_7_5

pyenv global my_py_3_7_5
