%define _snap 050303
Summary:	An object oriented wrapper for OpenAL
Summary(pl):	Obiektowy zamiennik dla OpenAL
Name:		OpenAL++
Version:	0.2
Release:	0.20%{_snap}.1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/alpp/openalpp-%{_snap}.tgz
# Source0-md5:	f93325e71675e7e4744cbdb4ca3b9603
URL:		http://alpp.sourceforge.net/
BuildRequires:	OpenAL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenAL++ is an object oriented wrapper for OpenAL. It makes using
spatial sound extremely easy. It has built in functionality for
streaming sound over sockets or from an input device.

%description -l pl
OpenAL++ to zorientowany obiektowo zamiennik OpenAL. Znacznie u³atwia
u¿ywanie d¼wiêku przestrzennego. Posiada wbudowan± funkcionalno¶æ
strumieniowania dziêku po gniazdach lub z urz±dzenia wej¶ciowego.

%package devel
Summary:	Header files for OpenAL++ library
Summary(pl):	Pliki nag³ówkowe biblioteki OpenAL++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenAL-devel
Requires:	libstdc++-devel

%description devel
Header files for OpenAL++ library.

%description devel -l pl
Pliki nag³ówkowe biblioteki OpenAL++.

%prep
%setup -q -n openalpp

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/openalpp
%{_pkgconfigdir}/*.pc
%{_libdir}/lib*.so
%{_libdir}/lib*.la

#%{_libdir}/lib*.a
