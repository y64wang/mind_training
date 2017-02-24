# Matlab shortcut
#ln -sf /usr/share/applications/matlab2011b.desktop $HOME/Desktop/matlab2011b.desktop
# Ceva shortcut
#ln -sf /usr/share/applications/ceva_ide.desktop $HOME/Desktop/ceva_ide.desktop
# Beynd compare shortcut
#ln -sf /usr/share/applications/beyondcompare.desktop $HOME/Desktop/beyondcompare.desktop

# Subversion PATH
source /opt/subversion/x86_64/1.9.2/interface/startup/linsee.env
# Valgrind paths
# unset VALGRIND_VERSION
# unset VALGRIND_HOME
# source /opt/valgrind/x86_64/3.11.0/interface/startup/valgrind-3.11.0-2.env
# git paths
source /opt/git/x86_64/2.6.2/interface/startup/linsee.env
# python path
source /opt/python/x86_64/2.7.3/interface/startup/linsee.env

# Matlab paths
#export MATLAB_EXE=matlab
#source /opt/matlab/x86_64/2011b/interface/startup/matlab-2011b-1.env
# Ceva toolbox
#export CEVAXC_ROOT=/opt/ceva-toolbox/x86_64/16.1.0/
#export CEVAXCTOOLS=/opt/ceva-toolbox/x86_64/16.1.0/CEVA-XC/
#source /opt/ceva-toolbox/x86_64/16.1.0/interface/startup/ceva-toolbox-16.1.0-1.env
#export PATH=$PATH:/opt/ceva-toolbox/x86_64/16.1.0/CEVA-XC/
#export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/ceva-toolbox/x86_64/16.1.0/CEVA-XC/
# Gcovr
source /opt/gcovr/noarch/3.3/interface/startup/linsee.env

# Python libs path
source /opt/python-pip/noarch/6.0.6.p273/interface/startup/linsee.env
source /opt/python-numpy/x86_64/1.9.3.p273/interface/startup/linsee.env
source /opt/python-paramiko/noarch/1.15.2.p273/interface/startup/linsee.env
source /opt/python-ply/noarch/3.8.p274/interface/startup/linsee.env
source /opt/python-pycrypto/x86_64/2.6.1.p273/interface/startup/linsee.env
source /opt/python-prophy/noarch/0.7.7.p274/interface/startup/linsee.env
source /opt/python-psutil/x86_64/2.1.3.p2711/interface/startup/linsee.env
source /opt/python-mysql/x86_64/1.2.3/interface/startup/linsee.env
source /opt/pysvn/x86_64/1.7.8.p274s189/interface/startup/linsee.env
source /opt/robotframework/x86_64/3.0/interface/startup/linsee.env

# Beyond Compare, git mergetool, git difftool
export PATH=$PATH:/opt/EE_LinSEE/bin
source seesetenv beyondcompare=4.1.9.21719
