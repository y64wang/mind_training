#!/bin/sh

krb5_url="https://es-si-s3-z4.eecloud.nsn-net.net/eecloud-baseimage-config/krb5.conf"
sssd_url="https://es-si-s3-z4.eecloud.nsn-net.net/eecloud-baseimage-config/sssd.conf"

getent group everybody >/dev/null 2>&1 || groupadd -g 55555 everybody >/dev/null 2>&1
perl -pi -e 's?^PasswordAuthentication no?PasswordAuthentication yes?' /etc/ssh/sshd_config;service sshd restart

for pkg in oddjob sssd krb5-workstation
do
    rpm -qi $pkg >/dev/null 2>&1 && continue
    yum install -y $pkg
done

wget -q -O /etc/krb5.conf $krb5_url
wget -q -O /etc/sssd/sssd.conf $sssd_url
chmod 0600 /etc/sssd/sssd.conf

authconfig --passalgo=sha512 --enableshadow --enablesssd --enablesssdauth --enablepamaccess --enablemkhomedir --enablefingerprint --kickstart

for f in /etc/pam.d/sudo /etc/pam.d/sudo-i
do
  test -f $f || continue
  grep -q pma_mkhomedir.so $f && continue
  echo "session     required      pam_mkhomedir.so umask=0022 skel=/etc/skel/" >> $f
done

service sssd restart

# For some reason we need to restart this after a while to actually get
# authentication working as well. Feel free to fix.
sleep 60; service sssd restart


authconfig --passalgo=sha512 --enableshadow --enablesssd --enablesssdauth --enablepamaccess --enablemkhomedir --enablefingerprint --kickstart
service sssd restart
sleep 60; service sssd restart
