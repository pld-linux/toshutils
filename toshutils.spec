Summary:	Toshiba Linux Utilities
Summary(pl):	Programy dla notebooków firmy Toshiba 
Name:		toshutils
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(es):	Aplicaciones/Sistema
Group(pl):	Aplikacje/System
Group(pt_BR):	Aplicações/Sistema
Source0:	http://www.buzzard.org.uk/toshiba/%{name}-%{version}.tar.gz
Patch0:		%{name}-include.patch
URL:		http://www.buzzard.org.uk/toshiba/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xsbindir	/usr/X11R6/sbin

%description
This is a small series of programs to control the more Toshiba
specific aspects of their laptops. In particular they allow many of
the settings controlled by either Toshiba's MaxTime or Power Saver
utilities to be changed under Linux.

The Toshiba Linux utilities are specific to Toshiba laptops, and will
not run on laptops from other manufactures. In addition they will not
run on Satellite 15xx, 16xx, 17xx and 35DVD machines from Toshiba
either. These models sport Pheonix BIOS'es and are made in that part
of China that is not part of China. In short they are not true Toshiba
laptops and are unlikely to ever be supported by the Toshiba Linux
Utilities.

%description -l pl
Seria ma³ych programików pozwalaj±cych kontrolowaæ/zmieniaæ
specyficzne dla notebooków firmy Toshiba ustawienia, w szczególno¶ci
wiele ustawieñ z narzêdzi Toshiba MaxTome albo Power Saver.

Te narzêdzia s± przeznaczone dla laptopów Toshiby i nie bêd± dzia³aæ z
laptopami innych producentów; nie bêd± dzia³aæ tak¿e z komputerami
Toshiba Satellite 15xx, 16xx, 17xx i 35DVD.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 

%build
./configure 
%{__make} depend
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_xsbindir},%{_mandir}/man1}

install src/alarm $RPM_BUILD_ROOT%{_sbindir}
install src/dispswitch $RPM_BUILD_ROOT%{_sbindir}
install src/fan $RPM_BUILD_ROOT%{_sbindir}
install src/fnfind $RPM_BUILD_ROOT%{_sbindir}
install src/hotkey $RPM_BUILD_ROOT%{_sbindir}
install src/ownerstring $RPM_BUILD_ROOT%{_sbindir}
install src/svpw $RPM_BUILD_ROOT%{_sbindir}
install src/tbacklight $RPM_BUILD_ROOT%{_sbindir}
install src/tdocked $RPM_BUILD_ROOT%{_sbindir}
install src/thotswap $RPM_BUILD_ROOT%{_sbindir}
install src/tpasswd $RPM_BUILD_ROOT%{_sbindir}
install src/tuxtime-conf $RPM_BUILD_ROOT%{_xsbindir}
install src/wmtuxtime $RPM_BUILD_ROOT%{_xsbindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf ChangeLog CONTRIBUTE COPYING FAQ README README.hotkey TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/mknod -m 666 /dev/toshiba c 10 181

%postun
/bin/rm -f /dev/toshiba

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/sbin/*
%attr(755,root,root) %{_sbindir}/*
%doc ChangeLog.gz CONTRIBUTE.gz COPYING.gz FAQ.gz README.gz 
%doc README.hotkey.gz TODO.gz
%{_mandir}/man1/* 
