Internal-CentOS-6-Mirror:
  pkgrepo.managed:
    - name: centos6
    - humanname: CentOS 6
    - baseurl: http://linux.int.net.nokia.com/ftp/mirror/CentOS/6.8/os/x86_64/
    - gpgcheck: 0

Internal-CentOS-6-Mirror-Updates:
  pkgrepo.managed:
    - name: centos6-updates
    - humanname: CentOS 6 Updates
    - baseurl: http://linux.int.net.nokia.com/ftp/mirror/CentOS/6.8/updates/x86_64/
    - gpgcheck: 0

Internal-CentOS-6-Mirror-Extras:
  pkgrepo.managed:
    - name: centos6-extras
    - humanname: CentOS 6 Extras
    - baseurl: http://linux.int.net.nokia.com/ftp/mirror/CentOS/6.8/extras/x86_64/
    - gpgcheck: 0

Internal-CentOS-6-Mirror-Plus:
  pkgrepo.managed:
    - name: centos6-plus
    - humanname: CentOS 6 Plus
    - baseurl: http://linux.int.net.nokia.com/ftp/mirror/CentOS/6.8/centosplus/x86_64/
    - gpgcheck: 0

Internal-RHEL6-Mirror-EPEL:
  pkgrepo.managed:
    - name: epel
    - humanname: RHEL6 EPEL
    - baseurl: http://linux.int.net.nokia.com/ftp/rhel/epel/6/x86_64/
    - gpgcheck: 0

SEE-RPMs-RHEL6-repo:
  pkgrepo.managed:
    - name: see-rpms
    - humanname: SEE RPMs
    - baseurl: http://eslina60.emea.nsn-net.net/repository/SEE/rpms/rhel6/$basearch
    - gpgcheck: 0
