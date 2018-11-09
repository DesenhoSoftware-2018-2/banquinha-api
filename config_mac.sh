echo " " >> ~/.bash_profile

echo '# set where virtual environments will live' >> ~/.bash_profile
echo 'export WORKON_HOME=$HOME/code/.virtualenvs' >> ~/.bash_profile
echo '# ensure all new environments are isolated from the site-packages directory' >> ~/.bash_profile
echo "export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'" >> ~/.bash_profile
echo '#' >> ~/.bash_profile
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3" >> ~/.bash_profile
echo '# use the same directory for virtualenvs as virtualenvwrapper' >> ~/.bash_profile
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> ~/.bash_profile
echo '# makes pip detect an active virtualenv and install to it' >> ~/.bash_profile
echo 'export PIP_RESPECT_VIRTUALENV=true' >> ~/.bash_profile
echo 'if [[ -r /usr/local/bin/virtualenvwrapper.sh ]]; then' >> ~/.bash_profile
echo '    source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bash_profile
echo 'else' >> ~/.bash_profile
echo '    echo "WARNING: Cant find virtualenvwrapper.sh"' >> ~/.bash_profile
echo 'fi' >> ~/.bash_profile
