%define oname wmd
%define name python-%{oname}
%define version 0.1.2
%define release 8

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
Url: https://www.forthewiin.org/
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




%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.1.2-7mdv2010.0
+ Revision: 442544
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.1.2-6mdv2009.1
+ Revision: 323408
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-5mdv2009.0
+ Revision: 259861
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.1.2-4mdv2009.0
+ Revision: 247709
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1.2-2mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Dec 30 2006 Olivier Blin <oblin@mandriva.com> 0.1.2-2mdv2007.0
+ Revision: 102790
- preload uinput module at boot

* Fri Dec 29 2006 Olivier Blin <oblin@mandriva.com> 0.1.2-1mdv2007.1
+ Revision: 102622
- make left and right directionnal keys act as Ctrl+Alt+<key> to get compiz cube rotation
- do not hardcode default Wiimote address
- use /dev/uinput as uinput device
- create setup.py file to build/install
- initial WMD release
- use lowercase name
- Create python-WMD

