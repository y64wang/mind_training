RHEL7-LINSEE_python:
  pkg.installed:
    - pkgs:
      - LINSEE_python_v274.x86_64
      - LINSEE_python_v273.x86_64
      - LINSEE_python_v2710.x86_64
      - LINSEE_python_v335.x86_64
      - LINSEE_python_v341.x86_64
      - LINSEE_python_v351.x86_64

RHEL7-LINSEE_python273-libs:
  pkg.installed:
    - pkgs:
      - LINSEE_python-pip_v606p273.noarch
      - LINSEE_python-matplotlib_v150p273.x86_64
      - LINSEE_python-numpy_v193p273.x86_64
      - LINSEE_python-pandas_v0170p273.x86_64
      - LINSEE_python-paramiko_v1152p273.noarch
      - LINSEE_python-pycrypto_v261p273.x86_64
      - LINSEE_python-matplotlib_v150p273.x86_64
      - LINSEE_python-prophy_v077p274.noarch
      - LINSEE_python-psutil_v213p2711.x86_64
      - LINSEE_python-mysql_v123.x86_64
      - LINSEE_pysvn_v178p274s189.x86_64      
      - python-devel.x86_64
      - libffi-devel.x86_64
      - freetype-devel.x86_64
      - libpng-devel.x86_64
      - tkinter.x86_64
      - python2-future.noarch

salt://linsee-rhel6/files/pip_python273_libs.sh: 
  cmd:
    - script

RHEL7-LINSEE_python2710-libs:
  pkg.installed:
    - pkgs:
      - LINSEE_python-virtualenv_v1312p2710.x86_64

RHEL7-LINSEE_python341-libs:
  pkg.installed:
    - pkgs:
      - LINSEE_python-virtualenv_v1502p341.x86_64
      - LINSEE_python-pip_v802p341.noarch
      - LINSEE_python-django_v18p341.noarch
      - LINSEE_python-mock_v200p341.noarch
      # - LINSEE_python-numpy_v1100p341.x86_64
      - LINSEE_python-coverage_v403p341.x86_64
      - LINSEE_python-pytest_v292p341.noarch
