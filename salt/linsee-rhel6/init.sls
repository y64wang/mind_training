LinSEE-RHEL6-ephemeral-opt:
  file.directory:
    - name: /ephemeral/opt
    - makedirs: True
    - dir_mode: 755

LinSEE-RHEL6-opt-symlink:
  file.symlink:
    - name: /opt
    - target: /ephemeral/opt
    - force: True
    - makedirs: True
    - mode: 755

LinSEE-RHEL6-repo:
  pkgrepo.managed:
    - name: ee-rpm-linsee-pilot
    - humanname: EE RPM-LinSEE pilot
    - baseurl: http://eslina60.emea.nsn-net.net/repository/SEE/linsee/pilot/rhel6/$basearch
    - gpgcheck: 0

LinSEE-RHEL6-core:
  pkg.installed:
    - pkgs:
      - LINSEE_Core.noarch
      - redhat-lsb-core.x86_64
      - symlinks.x86_64

LinSEE-RHEL6-env:
  file.managed:
    - name: /etc/profile.d/linsee.sh
    - source: salt://linsee-rhel6/files/linsee.sh
    - mode: 644
