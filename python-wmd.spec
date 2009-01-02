%define oname wmd
%define name python-%{oname}
%define version 0.1.2
%define release %mkrel 6

Summary: Driver for the Nintendo Wii Remote
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://forthewiin.org/WMD/%{oname}-%{version}.tar.bz2
Patch0: wmd-0.1.2.2-uinput.patch
Patch1: wmd-0.1.2.2-defaddr.patch
Patch2: wmd-0.1.2.2-compiz.patch
Source1: setup.py
License: GPL
Group: System/Kernel and hardware
Url: http://www.forthewiin.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel
Requires: python-xlib python-pybluez python-osd pygame

%description
WMD is a Linux Driver for the Nintendo Wii Remote.
WMD lets you use the Wiimote as a mouse.
WMD lets you use the Wiimote as a keyboard.

%prep
%setup -q -n %{oname}-%{version}
perl -p -e 's/(^\s+version = \").*(\",$)/${1}%{version}${2}/' %{SOURCE1} > setup.py
%patch0 -p1 -b .uinput
%patch1 -p1 -b .defaddr
%patch2 -p1 -b .compiz

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

install -d %{buildroot}%{_sysconfdir}/modprobe.preload.d
echo uinput > %{buildroot}%{_sysconfdir}/modprobe.preload.d/%{oname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%config(noreplace) %{_sysconfdir}/modprobe.preload.d/%{oname}
%{_bindir}/WMD.py
%{py_puresitedir}/%{oname}
%{py_puresitedir}/*.egg-info


