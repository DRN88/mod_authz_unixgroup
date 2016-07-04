# Building mod_authz_unixgroup on CentOS 7

https://code.google.com/archive/p/mod-auth-external/wikis/ModAuthzUnixGroup.wiki  
https://code.google.com/archive/p/mod-auth-external/downloads  

Use 1.1.0 for Apache 2.3/2.4 (tested, works)  
Use 1.0.x for Apache 2.2 (not tested)  

## Artifacts
These are ready to be installed. Built on:
```
Linux box 3.10.0-327.22.2.el7.x86_64 #1 SMP Thu Jun 23 17:05:11 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```
https://github.com/DRN88/mod_authz_unixgroup/raw/master/mod_authz_unixgroup-1.1.0/artifacts/mod_authz_unixgroup-1.1.0-7.el7.centos.x86_64.rpm  
https://github.com/DRN88/mod_authz_unixgroup/raw/master/mod_authz_unixgroup-1.1.0/artifacts/mod_authz_unixgroup-debuginfo-1.1.0-7.el7.centos.x86_64.rpm  

## Quick Build

```bash
sudo -i

yum -y install rpmdevtools rpm-build httpd-devel gcc unzip wget

cd /root/

# git clone git@github.com:DRN88/mod_authz_unixgroup.git
wget "https://github.com/DRN88/mod_authz_unixgroup/archive/master.zip" -O "/root/mod_authz_unixgroup.zip"
unzip /root/mod_authz_unixgroup.zip

cp -ra /root/mod_authz_unixgroup-master/mod_authz_unixgroup-1.1.0/rpmbuild/ /root/rpmbuild

spectool -g -R /root/rpmbuild/SPECS/mod_authz_unixgroup.spec
rpmbuild -ba /root/rpmbuild/SPECS/mod_authz_unixgroup.spec
```

## Built Artifacts
```bash
[root@box ~]# tree rpmbuild/RPMS/
rpmbuild/RPMS/
└── x86_64
    ├── mod_authz_unixgroup-1.1.0-7.el7.centos.x86_64.rpm
    └── mod_authz_unixgroup-debuginfo-1.1.0-7.el7.centos.x86_64.rpm

1 directory, 2 files

[root@box ~]# cd /root/rpmbuild/RPMS/x86_64/
[root@box x86_64]# sha1sum *
beed29cbfb144bd8bed476ea91dd0659137ce2ae  mod_authz_unixgroup-1.1.0-7.el7.centos.x86_64.rpm
05f4d824f8ea57f6a2bb1afe10d7bfc459d95b9b  mod_authz_unixgroup-debuginfo-1.1.0-7.el7.centos.x86_64.rpm

```
