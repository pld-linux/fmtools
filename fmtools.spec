Summary:	Programs for Video for Linux radio cards
Name:		fmtools
Version:	0.99.1
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.exploits.org/v4l/fmtools/%{name}-%{version}.tar.gz
URL:		http://www.exploits.org/v4l/fmtools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avifile-devel
BuildRequires:	libstdc++-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fmtools consists of two "tools" - a tuner called "fm" and a band
scanner called "fmscan".

fm handles basic on/off, tuning, and volume changes for v4l radio
cards. There is also a quiet mode to allow it to run inside IRC
scripts and other programs without disrupting the display.

fmscan will by default scan from 87.9 to 107.9 MHz in 0.2 MHz
increments looking for stations that have an average signal strength
of 50% or greater. VCR is a program which enables you to record a
program using a video

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
