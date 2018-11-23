echo " " >> ~/.bashrc

echo '# set where virtual environments will live' >> ~/.bashrc
echo 'export WORKON_HOME=$HOME/.virtualenvs' >> ~/.bashrc
echo '# ensure all new environments are isolated from the site-packages directory' >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'" >> ~/.bashrc
echo '#' >> ~/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
echo '# use the same directory for virtualenvs as virtualenvwrapper' >> ~/.bashrc
echo 'export PIP_VIRTUALENV_BASE=$WORKON_HOME' >> ~/.bashrc
echo '# makes pip detect an active virtualenv and install to it' >> ~/.bashrc
echo 'export PIP_RESPECT_VIRTUALENV=true' >> ~/.bashrc
echo 'if [[ -r /usr/local/bin/virtualenvwrapper.sh ]]; then' >> ~/.bashrc
echo '    source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc
echo 'else' >> ~/.bashrc
echo '    echo "WARNING: Cant find virtualenvwrapper.sh"' >> ~/.bashrc
echo 'fi' >> ~/.bashrc
