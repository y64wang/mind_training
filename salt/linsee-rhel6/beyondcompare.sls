RHEL7-LINSEE_beyondcompare:
  pkg.installed:
    - pkgs:
      - LINSEE_beyondcompare_v41921719.x86_64
      - LINSEE_beyondcompare-license_v40.noarch

byc-desktop:
  file.managed:
    - name: /usr/share/applications/beyondcompare.desktop
    - source: salt://linsee-rhel6/files/beyondcompare.desktop
    - user: root
    - group: root
    - mode: 755
