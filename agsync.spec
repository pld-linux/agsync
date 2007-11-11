%define		_rc	pre
%define		_rel	0.1
Summary:	Synchronization mediator for AvantGo and Pocket PC
Name:		agsync
Version:	0.2
Release:	0.%{_rc}.%{_rel}
License:	MPL v1.1
Group:		Applications
URL:		http://duskwood.lownewulf.com/avantgo.html
Source0:	http://ftp.debian.org/debian/pool/main/a/agsync/%{name}_%{version}-%{_rc}.orig.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the AvantGo - Pocket PC synchronization mediator
command line application.

%prep
%setup -q -n %{name}-%{version}-%{_rc}.orig

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install agsync $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
