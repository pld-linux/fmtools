Summary:	Programs for Video for Linux radio cards
Summary(pl):	Programy do kart radiowych zgodnych z Video for Linux
Name:		fmtools
Version:	0.99.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.exploits.org/v4l/fmtools/%{name}-%{version}.tar.gz
# Source0-md5:	6093f8a69ab51a056e3e1ae9ee6d6b0f
URL:		http://www.exploits.org/v4l/fmtools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fmtools consists of two "tools" - a tuner called "fm" and a band
scanner called "fmscan".

fm handles basic on/off, tuning, and volume changes for v4l radio
cards. There is also a quiet mode to allow it to run inside IRC
scripts and other programs without disrupting the display.

fmscan will by default scan from 87.9 to 107.9 MHz in 0.2 MHz
increments looking for stations that have an average signal strength
of 50% or greater.

%description -l pl
fmtools sk�ada si� z dw�ch narz�dzi - tunera o nazwie "fm" oraz
skanera pasma o nazwie "fmscan".

fm obs�uguje podstawowe funkcje kart radiowych v4l: w��czanie,
wy��czanie, strojenie i zmian� g�o�no�ci. Jest tak�e tryb cichy, kt�ry
pozwala na uruchamianie ze skrypt�w IRC i innych program�w bez
zak��cania obrazu.

fmscan domy�lnie przeszukuje zakres cz�stotliwo�ci 87.9 do 107.9 MHz w
krokach co 0.2 MHz w poszukiwaniu stacji o �redniej mocy sygna�u 50%
lub wi�cej.

%prep
%setup -q

%build
%{__make} CC=%{__cc} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install fm fmscan $RPM_BUILD_ROOT%{_bindir}
install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
