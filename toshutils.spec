Summary:	Toshiba Linux Utilities
Summary(es):	Herramientas para Toshibas para Linux
Summary(pl):	Programy dla notebooków firmy Toshiba
Name:		toshutils
Version:	2.0.1
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://www.buzzard.org.uk/toshiba/%{name}-%{version}.tar.gz
# Source0-md5:	807589cf1e209eb0a39e1ede427140d5
Source1:	%{name}-fan.init
Patch0:		%{name}-include.patch
Patch1:		%{name}-gtk+2.patch
URL:		http://www.buzzard.org.uk/toshiba/
BuildRequires:	XFree86-tools
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk+2-devel
BuildRequires:	pkgconfig
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
ExclusiveArch:	%{ix86}
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

%description -l es
Ésta es una serie pequeña de programas para controlar las idiosincracias
de portátiles de Toshiba. Entre otros habilitan ajustar muchos de los
parametros normalmente ajustados por MaxTime o Power Saver.

Como estas herramientas usan código específico para Toshiba, no
funcionarán con otros portátiles. Además, tampoco servirán para
Toshiba Satellite 15xx, 16xx, 17xx y 35DVD. Esos modelos contienen BIOS
de Phoenix y están producidas en aquella parte de China que no es parte
de China. O sea que no son verdaderos portátiles de Toshiba y es dudoso
que jamás sean soportados por estas herramientas.

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
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__aclocal}
%{__autoconf}
%configure
%{__make} depend
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir}/man{1,8},/etc/rc.d/init.d}

install src/{alarm,dispswitch,fan,fnfind} $RPM_BUILD_ROOT%{_bindir}
install src/{ownerstring,svpw} $RPM_BUILD_ROOT%{_bindir}
install src/t{backlight,docked,passwd} $RPM_BUILD_ROOT%{_bindir}
install src/thotswap $RPM_BUILD_ROOT%{_sbindir}
install src/{tuxtime-conf,wmtuxtime,hotkey} $RPM_BUILD_ROOT%{_bindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.1x $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.8 $RPM_BUILD_ROOT%{_mandir}/man8
install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/fan

%post
/sbin/chkconfig --add fan
%service fan restart

%preun
if [ "$1" = "0" ]; then
	%service fan stop
	/sbin/chkconfig --del fan
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog CONTRIBUTE FAQ README README.hotkey TODO
%attr(754,root,root) /etc/rc.d/init.d/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man*/*
