Summary:	Toshiba Linux Utilities
Summary(pl):	Programy dla notebooków firmy Toshiba
Name:		toshutils
Version:	2.0.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://www.buzzard.org.uk/toshiba/%{name}-%{version}.tar.gz
# Source0-md5:	807589cf1e209eb0a39e1ede427140d5
Source1:	%{name}-fan.init
Patch0:		%{name}-include.patch
URL:		http://www.buzzard.org.uk/toshiba/
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk+-devel
BuildRequires:	XFree86-tools
Requires(post,preun):	chkconfig
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_xmandir	/usr/X11R6/man
%define		_xbindir	/usr/X11R6/bin

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
%setup -q
%patch0 -p1

%build
%configure2_13
%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_xbindir}}
install -d $RPM_BUILD_ROOT{%{_mandir}/man{1,8},%{_xmandir}/man1}
install -d $RPM_BUILD_ROOT/etc/rc.d/init.d

install src/{alarm,dispswitch,fan,fnfind} $RPM_BUILD_ROOT%{_bindir}
install src/{ownerstring,svpw} $RPM_BUILD_ROOT%{_bindir}
install src/t{backlight,docked,passwd} $RPM_BUILD_ROOT%{_bindir}
install src/thotswap $RPM_BUILD_ROOT%{_sbindir}
install src/{tuxtime-conf,wmtuxtime,hotkey} $RPM_BUILD_ROOT%{_xbindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.1x $RPM_BUILD_ROOT%{_xmandir}/man1
install doc/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/fan

%post
/sbin/chkconfig --add fan
if [ -f /var/lock/subsys/fan ]; then
	/etc/rc.d/init.d/fan restart >&2
else
	echo "Run \"/etc/rc.d/init.d/fan start\" to start Toshiba fan daemon."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/fan ]; then
		/etc/rc.d/init.d/fan stop >&2
	fi
	/sbin/chkconfig --del fan
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CONTRIBUTE FAQ README README.hotkey TODO
%attr(755,root,root) /etc/rc.d/init.d/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_xbindir}/*
%{_mandir}/man*/*
%{_xmandir}/man*/*
