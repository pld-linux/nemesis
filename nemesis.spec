Summary:	nemesis packet injection tool-suite
Summary(pl.UTF-8):	Zbiór narzędzi do iniekcji pakietów
Name:		nemesis
Version:	1.4
%define	_beta	beta3
Release:	0.%{_beta}.1
License:	BSD
Group:		Networking
Source0:	http://www.packetfactory.net/Projects/nemesis/%{name}-%{version}%{_beta}.tar.gz
# Source0-md5:	6409bddf2d54cc9400028f491d342aea
Patch0:		%{name}-libnet1.patch
URL:		http://www.packetfactory.net/Projects/nemesis/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:	libpcap-devel
BuildRequires:	libnet1-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nemesis packet injection tool-suite.

%description -l pl.UTF-8
Zbiór narzędzi do iniekcji pakietów.

%prep
%setup -q -n %{name}-%{version}%{_beta}
%patch0 -p1

%build
install /usr/share/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_prefix}/man,%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
