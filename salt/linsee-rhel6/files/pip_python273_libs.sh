#!/bin/bash
# install modules to /opt/python/x86_64/2.7.3 by pip

. /opt/python/x86_64/2.7.3/interface/startup/linsee.env
. /opt/python-pip/noarch/6.0.6.p273/interface/startup/linsee.env

pip install future --proxy=http://10.144.1.10:8080
