#!/bin/bash

# Ceva paths
export CEVAXC_ROOT=/opt/ceva-toolbox/x86_64/16.1.0/
export CEVAXCTOOLS=/opt/ceva-toolbox/x86_64/16.1.0/CEVA-XC/
export PATH=$PATH:/opt/ceva-toolbox/x86_64/16.1.0/CEVA-XC/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/ceva-toolbox/x86_64/16.1.0/CEVA-XC/

# Matlab paths
export MATLAB_EXE=matlab
export PATH=$PATH:/opt/matlab/x86_64/2014b/bin

# Matlab shortcut
sudo cp matlab.png /usr/share/icons
sudo cp matlab2014b.desktop /usr/share/applications
sudo chmod 755 /usr/share/applications/matlab2014b.desktop
ln -sf /usr/share/applications/matlab2014b.desktop $HOME/Desktop

# Ceva shortcut
sudo cp ceva_ide.desktop /usr/share/applications
sudo chmod 755 /usr/share/applications/ceva_ide.desktop
ln -sf /usr/share/applications/ceva_ide.desktop $HOME/Desktop
