Summary:	nemesis packet injection tool-suite
Summary(pl):	Zbiór narzêdzi do injekcji pakietów
Name:		nemesis
Version:	1.32
Release:	1
License:	BSD
Group:		Networking
Source0:	http://jeff.wwti.com/nemesis/%{name}-%{version}.tar.gz
# Source0-md5:	19e3e8eb6ff86c35580adf630e6df398
URL:		http://www.packetfactory.net/Projects/nemesis/
BuildRequires:	libpcap-devel
BuildRequires:	libnet-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nemesis packet injection tool-suite.

%description -l pl
Zbiór narzêdzi do injekcji pakietów.

%prep
%setup -q

%build
install %{_datadir}/automake/config.* .
%{__aclocal}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_prefix}/man,%{_sbindir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install *.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
