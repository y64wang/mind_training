salt-master:
  pkg:
    - installed

remove-down-minions:
  cron.present:
    - name: /usr/bin/salt-run manage.down removekeys=True

weekly-salt-master-termination:
  cron.present:
    - minute: 0
    - hour: 0
    - dayweek: 0
    - name: /usr/sbin/shutdown -P now
