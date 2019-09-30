Name:    sgpio
Version: 1.2.1
Release: 1
Summary: captive backplane LED control utility
License: GPLv2+
URL:     http://sources.redhat.com/lvm2/wiki/DMRAID_Eventing
Source0: %{name}-%{version}.tgz

BuildRequires: gcc, dos2unix

Patch0: sgpio-makefile.patch

%description
Serial General Purpose Input Output (SGPIO) is a communication method used
between a main board and a variety of internal and external hard disk drive
bay enclosures.  This utility can be used to control LEDs in an enclosure.

%prep
%autosetup -p1 -n %{name}
chmod a-x *

%build
make clean
export CFLAGS="%{optflags}"
export LDFLAGS="%{build_ldflags}"
%make_build
dos2unix README LICENSE_GPL

%install
%make_install \
    INSTALL="%{__install} -p -D" \
    SBINDIR="%{buildroot}%{_sbindir}"\
    MANDIR="%{buildroot}%{_mandir}"

%check

%pre

%preun

%post

%postun

%files
%doc README LICENSE_GPL
%{_sbindir}/sgpio
%{_mandir}/man*/*

%changelog
* Sat Aug 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.2.1-1
- Package init

