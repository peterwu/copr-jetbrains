# disable debuginfo subpackage
%global         debug_package %{nil}
# Disable build-id symlinks to avoid conflicts
%global         _build_id_links none

%global         source_name pycharm-community

Name:           jetbrains-pycharm-ce
Version:        2020.3
Release:        1%{?dist}
Summary:        JetBrain PyCharm Community Edition

License:        ASL2.0
URL:            https://www.jetbrains.com/pycharm
Source0:        https://download.jetbrains.com/python/%{source_name}-%{version}.tar.gz
Source1:        %{name}.desktop

Requires:       python3
Requires:       bash
Requires:       java
Requires:       glibc
Requires:       libgcc

%description
JetBrain PyCharm Community Edition

%prep
%autosetup -n %{source_name}-%{version}

%build
%{__rm} -rf %{_builddir}/%{source_name}-%{version}/jbr
%{__rm} -rf %{_builddir}/%{source_name}-%{version}/bin/fsnotifier

find %{_builddir}/%{source_name}-%{version}/bin -type f -name '*.py' -exec sed -i '1 s/env python/python3/' {} \;

%install
%{__rm} -rf %{buildroot}
%{__mkdir} -p %{buildroot}/opt/jetbrains/pycharm-ce
%{__mkdir} -p %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/applications

%{__ln_s} /opt/jetbrains/pycharm-ce/bin/pycharm.sh %{buildroot}%{_bindir}/pycharm-ce

%{__install} -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications
%{__cp} -r %{_builddir}/%{source_name}-%{version}/* %{buildroot}/opt/jetbrains/pycharm-ce

%files
%{_bindir}/pycharm-ce
%{_datadir}/*
/opt/jetbrains/pycharm-ce/*

%changelog
* Wed Dec  2 17:48:36 EST 2020 Peter Wu <peterwu@hotmail.com>
- PyCharm CE 2020.3
* Fri Nov 27 09:43:05 EST 2020 Peter Wu <peterwu@hotmail.com>
- PyCharm CE 2020.2.4
* Sat Nov 21 13:25:14 EST 2020 Peter Wu <peterwu@hotmail.com>
- PyCharm CE 2020.2.3
