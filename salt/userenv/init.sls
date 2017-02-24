global-ulphy-env:
  file.managed:
    - name: /etc/default/global_ulphy_env.bashrc
    - source: salt://userenv/files/global_ulphy_env.bashrc
    - mode: 644

vncserver:
  iptables.append:
    - table: filter
    - chain: INPUT
    - jump: ACCEPT
    - match: state
    - connstate: NEW
    - match: tcp
    - proto: tcp
    - match: multiport
    - dport: 5901:5903,6001:6003
    - save: True

xenabts_c_es:
  user.present:
    - fullname: xenabts_c_es
    - shell: /bin/bash
    - password: $1$Wsdpghjo$IqDCGk5Z88lxEeoi3li85/
    - home: /home/xenabts_c_es
    - uid: 500
    - gid: 501
    - groups:
      - wheel
      - dialout

/home/xenabts_c_es/.bashrc:
  file.managed:
    - source: salt://userenv/files/user.bashrc
    - user: xenabts_c_es
    - group: xenabts_c_es
    - mode: 644

/home/xenabts_c_es/.ssh:
  file.recurse:
    - source: salt://userenv/files/_ssh 
    - user: xenabts_c_es
    - group: xenabts_c_es
    - dir_mode: 2700
    - file_mode: 600
