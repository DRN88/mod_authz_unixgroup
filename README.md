# Building mod_authz_unixgroup on CentOS 7

https://code.google.com/archive/p/mod-auth-external/downloads

# Build

```bash
yum -y install rpmdevtools rpm-build httpd-devel gcc unzip wget

cd /root/

# git clone git@github.com:DRN88/mod_authz_unixgroup.git
wget "https://github.com/DRN88/mod_authz_unixgroup/archive/master.zip" -O "/root/mod_authz_unixgroup.zip"
unzip /root/mod_authz_unixgroup.zip

spectool -g -R /root/rpmbuild/SPECS/mod_authz_unixgroup.spec
rpmbuild -ba /root/rpmbuild/SPECS/mod_authz_unixgroup.spec

[root@ftp2 ~]# tree rpmbuild/RPMS/
rpmbuild/RPMS/
└── x86_64
    ├── mod_authz_unixgroup-1.1.0-7.el7.centos.x86_64.rpm
    └── mod_authz_unixgroup-debuginfo-1.1.0-7.el7.centos.x86_64.rpm

1 directory, 2 files
```
