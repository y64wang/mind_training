RHEL7-LINSEE_matlab:
  pkg.installed:
    - pkgs:
      # - LINSEE_matlab_v2014b-2014b-2.x86_64
      # - LINSEE_matlab_v2014b.x86_64
      - LINSEE_matlab_v2011b.x86_64

matlab-icon:
  file.managed:
    - name: /usr/share/icons/matlab.png
    - source: salt://linsee-rhel6/files/matlab.png
    - user: root
    - group: root
    - mode: 755

matlab-desktop:
  file.managed:
    - name: /usr/share/applications/matlab2011b.desktop
    - source: salt://linsee-rhel6/files/matlab2011b.desktop
    - user: root
    - group: root
    - mode: 755
