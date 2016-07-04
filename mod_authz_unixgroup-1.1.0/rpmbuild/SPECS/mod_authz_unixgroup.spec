%global modsuffix authz_unixgroup
%global conffile %{modsuffix}.conf

Summary: An Apache module used for group membership checking
Name: mod_%{modsuffix}
Version: 1.1.0
Release: 7%{?dist}
License: ASL 1.0
Group: System Environment/Libraries
URL: http://code.google.com/p/mod-auth-external/
Source: http://mod-auth-external.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: %{conffile}
Requires: pwauth, httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing)
BuildRequires: httpd-devel

%description
Mod_Authz_Unixgroup can be used to filter users during authentication.

%global modulesdir %{_libdir}/httpd/modules
%global confdir %{_sysconfdir}/httpd/conf


%prep
%setup -q

%build
apxs -c -I . %{name}.c


%install
mkdir -p %{buildroot}%{modulesdir} %{buildroot}%{confdir}.d
apxs -i -S LIBEXECDIR=%{buildroot}%{modulesdir} -n %{name} %{name}.la
install -p -m 644 -t %{buildroot}%{confdir}.d/ %{SOURCE1}

# in case we're on a 64-bit machine, otherwise a no-op
sed -i \
	-e 's@/usr/lib/@%{_libdir}/@' \
	%{buildroot}%{confdir}.d/%{conffile}


%files
%{modulesdir}/%{name}.so
%config(noreplace) %lang(en) %{confdir}.d/%{conffile}
%doc CHANGES INSTALL LICENSE NOTICE README


%changelog
