%define		_rc	pre
%define		_rel	3
Summary:	Synchronization mediator for AvantGo and Pocket PC
Summary(pl.UTF-8):	Mediator synchronizacji dla AvantGo i Pocket PC
Name:		agsync
Version:	0.2
Release:	0.%{_rc}.%{_rel}
License:	MPL v1.1
Group:		Applications/Communications
Source0:	http://duskwood.lownewulf.com/%{name}-%{version}-%{_rc}.tgz
Patch0:		%{name}-debian.patch
# Source0-md5:	74de1b1452a718c85364fab5ce3c0c2a
URL:		http://duskwood.lownewulf.com/avantgo.html
BuildRequires:	synce-core-lib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the AvantGo - Pocket PC synchronization mediator
command line application.

%description -l pl.UTF-8
Ten pakiet zawiera aplikację działającego z linii poleceń mediatora
synchronizacji AvantGo - Pocket PC.

%package devel
Summary:	Development files for AvantGo and Pocket PC synchronization
Summary(pl.UTF-8):	Pliki programistyczne do synchronizacji AvantGo i Pocket PC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files to develop applications which
provides AvantGo synchronization from Pocket PC to be mediated by the
connected PC.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe do tworzenia aplikacji
obsługującej synchronizację AvantGo z Pocket PC mediowaną przez
podłączony PC.

%package static
Summary:	Static AvantGo library
Summary(pl.UTF-8):	Statyczna biblioteka AvantGo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static AvantGo library library.

%description static -l pl.UTF-8
Statyczna biblioteka AvantGo.

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
%attr(755,root,root) %{_libdir}/libmal-funcs.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmal-funcs.so.0
%{_mandir}/man1/agsync.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmal-funcs.so
%{_libdir}/libmal-funcs.la
%{_includedir}/AG*.h
%{_includedir}/md5.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libmal-funcs.a
