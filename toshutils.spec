Summary:	Toshiba Linux Utilities
Summary(pl):	Programy dla notebookow firmy Toshiba 
Name:		toshutils
Version:	2.0
Release:	1
License:	GPL
Group:		Applications/System
Group(pl):	Aplikacje/System
URL:		http://www.buzzard.org.uk/toshiba/
Source0:	http://www.buzzard.org.uk/toshiba/%{name}-%{version}.tar.gz
Patch0:		%{name}-include.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 

%build
./configure 
%{__make} depend
%{__make} -j 8 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install -d $RPM_BUILD_ROOT%{_prefix}/X11R6/sbin
install -d $RPM_BUILD_ROOT%{_mandir}/man1

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
install src/tuxtime-conf $RPM_BUILD_ROOT%{_prefix}/X11R6/sbin
install src/wmtuxtime $RPM_BUILD_ROOT%{_prefix}/X11R6/sbin
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf ChangeLog CONTRIBUTE COPYING FAQ README README.hotkey TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/sbin/*
%attr(755,root,root) %{_sbindir}/*
%doc ChangeLog.gz CONTRIBUTE.gz COPYING.gz FAQ.gz README.gz 
%doc README.hotkey.gz TODO.gz
%{_mandir}/man1/* 
