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

Summary:        The MHAL library for REDHAWK
Name:           mhalInterfaces
Version:        3.0
Release:        1%{?dist}

Group:          REDHAWK/Interfaces
License:        None
Source:         %{name}-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  redhawk-devel >= 2.1
Requires:       redhawk >= 2.1


%description
Libraries and interface definitions for MHAL.


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
%{_datadir}/idl/redhawk/MHAL
%{_includedir}/redhawk/MHAL
%{_libdir}/libmhalInterfaces.*
%{_libdir}/pkgconfig/MHALInterfaces.pc
%{_prefix}/lib/python/redhawk/mhalInterfaces
%if 0%{?rhel} >= 6
%{_prefix}/lib/python/mhalInterfaces-%{version}-py%{python_version}.egg-info
%endif
%if %{with java}
%{_prefix}/lib/MHALInterfaces.jar
%{_prefix}/lib/MHALInterfaces.src.jar
%endif


%post
/sbin/ldconfig


%postun
/sbin/ldconfig
