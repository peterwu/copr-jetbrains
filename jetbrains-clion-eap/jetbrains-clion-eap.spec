# disable debuginfo subpackage
%global         debug_package %{nil}
# Disable build-id symlinks to avoid conflicts
%global         _build_id_links none

%global         source_name clion
%global         build_version 203.5981.106

Name:           jetbrains-clion-eap
Version:        2020.3
#Version:        %{build_version}
Release:        1%{?dist}
Summary:        JetBrains C/C++ IDE. 30-day evaluation.

License:        Custom. Refer to /opt/jetbrains/clion-eap/license for details.
URL:            https://www.jetbrains.com/clion
Source0:        https://download.jetbrains.com/cpp/CLion-%{build_version}.tar.gz
Source1:        %{name}.desktop

Requires:       python3
Requires:       bash
Requires:       java
Requires:       glibc
Requires:       libgcc
Recommends:     cmake
Recommends:     gdb
Recommends:     lldb

%description
JetBrains cross platform C/C++ IDE.
30-day evaluation.

%prep
%autosetup -n %{source_name}-%{version}

%build
%{__rm} -rf %{_builddir}/%{source_name}-%{version}/jbr
%{__rm} -rf %{_builddir}/%{source_name}-%{version}/bin/cmake
%{__rm} -rf %{_builddir}/%{source_name}-%{version}/bin/gdb
%{__rm} -rf %{_builddir}/%{source_name}-%{version}/bin/lldb
%{__rm} -rf %{_builddir}/%{source_name}-%{version}/bin/fsnotifier

find %{_builddir}/%{source_name}-%{version}/bin -type f -name '*.py' -exec sed -i '1 s/env python/python3/' {} \;

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/opt/jetbrains/clion-eap
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%{__ln_s} /opt/jetbrains/clion-eap/bin/clion.sh %{buildroot}%{_bindir}/clion-eap

%{__install} -D -m 0644 %SOURCE1 -t %{buildroot}%{_datadir}/applications
%{__cp} -r %{_builddir}/%{source_name}-%{version}/* %{buildroot}/opt/jetbrains/clion-eap

%files
%{_bindir}/clion-eap
%{_datadir}/*
/opt/jetbrains/clion-eap/*

%changelog
* Fri Nov 27 09:43:05 EST 2020 Peter Wu <peterwu@hotmail.com>
- CLion-203.5981.106
* Sat Nov 21 13:25:14 EST 2020 Peter Wu <peterwu@hotmail.com>
- CLion-203.5981.40
