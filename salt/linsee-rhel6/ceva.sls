RHEL7-LINSEE_ceva:
  pkg.installed:
    - pkgs:
      # - LINSEE_ceva-toolbox_v1610-16.1.0-1.x86_64
      - LINSEE_ceva-toolbox_v1610.x86_64

ceva-desktop:
  file.managed:
    - name: /usr/share/applications/ceva_ide.desktop
    - source: salt://linsee-rhel6/files/ceva_ide.desktop
    - user: root
    - group: root
    - mode: 755
