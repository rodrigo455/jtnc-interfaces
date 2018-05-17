# By default, the RPM will install to the standard REDHAWK OSSIE root location (/usr/local/redhawk/core)
%{!?_ossiehome: %global _ossiehome /usr/local/redhawk/core}
%define _prefix %{_ossiehome}
Prefix:         %{_prefix}

# Point install paths to locations within our target OSSIE root
%define _sysconfdir    %{_prefix}/etc
%define _localstatedir %{_prefix}/var
%define _mandir        %{_prefix}/man
%define _infodir       %{_prefix}/info

# Assume Java support by default. Use "rpmbuild --without java" to disable
%bcond_without java

Summary:        The Ethernet library for REDHAWK
Name:           ethernetInterfaces
Version:        1.2.2
Release:        1%{?dist}

Group:          REDHAWK/Interfaces
License:        None
Source:         %{name}-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  redhawk-devel >= 2.1
Requires:       redhawk >= 2.1


%description
Libraries and interface definitions for Ethernet.


%prep
%setup


%build
./reconf
%configure %{?_without_java: --disable-java}
make


%install
rm -rf --preserve-root $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf --preserve-root $RPM_BUILD_ROOT


%files
%defattr(-,redhawk,redhawk,-)
%{_datadir}/idl/redhawk/ETHERNET
%{_includedir}/redhawk/ETHERNET
%{_libdir}/libethernetInterfaces.*
%{_libdir}/pkgconfig/EthernetInterfaces.pc
%{_prefix}/lib/python/redhawk/ethernetInterfaces
%if 0%{?rhel} >= 6
%{_prefix}/lib/python/ethernetInterfaces-%{version}-py%{python_version}.egg-info
%endif
%if %{with java}
%{_prefix}/lib/ETHERNETInterfaces.jar
%{_prefix}/lib/ETHERNETInterfaces.src.jar
%endif


%post
/sbin/ldconfig


%postun
/sbin/ldconfig
