salt-minion:
  pkg:
    - installed

salt-minion-keepalive:
  file.managed:
    - name: /etc/salt/minion.d/keepalive.conf
    - source: salt://salt/files/keepalive.conf

salt-minion-service:
  service.running:
    - name: salt-minion
    - enable: True
    - full_restart: True
    - watch:
      - file: /etc/salt/minion.d/keepalive.conf
