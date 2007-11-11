%define		_rc	pre
%define		_rel	0.1
Summary:	Synchronization mediator for AvantGo and Pocket PC
Name:		agsync
Version:	0.2
Release:	0.%{_rc}.%{_rel}
License:	MPL v1.1
Group:		Applications
URL:		http://duskwood.lownewulf.com/avantgo.html
Source0:	http://duskwood.lownewulf.com/%{name}-%{version}-%{_rc}.tgz
# Source0-md5:	74de1b1452a718c85364fab5ce3c0c2a
BUildRequires:	synce-librapi2-devel
Patch0:		%{name}-debian.patch
BUildRequires:	synce-libsynce-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the AvantGo - Pocket PC synchronization mediator
command line application.

%package devel
Summary:	Development files for AvantGo and Pocket PC synchronization
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the library to develop applications which
provides AvantGo synchronization fro Pocket PC to be mediated by the
connected PC

%package static
Summary:	Static AvantGo library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AvantGo library library.

%prep
%setup -q -n %{name}-%{version}-%{_rc}
%patch0 -p1
chmod +x configure

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -a agsync.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/agsync
%{_mandir}/man1/agsync.1*
%attr(755,root,root) %{_libdir}/libmal-funcs.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmal-funcs.la
%{_libdir}/libmal-funcs.so
%{_includedir}/AG*.h
%{_includedir}/md5.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmal-funcs.a
