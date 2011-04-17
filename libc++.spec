%define		revision	129657
Summary:	C++ standard library
Summary(pl.UTF-8):	Biblioteka standardowa C++
Name:		libc++
Version:	0.0.%{revision}
Release:	1
License:	MIT/UIUC
Group:		Development
Source0:	libcxx-%{revision}.tar.xz
# Source0-md5:	53c082f604d3d06c332de5361cbd7933
BuildRequires:	clang
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		__cc	clang
%define		__cxx	clang++
%define		no_install_post_check_so	1

%description
libc++ is a new implementation of the C++ standard library, targeting C++0X.

%package devel
Summary:	libc++ devel
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description devel
libc++ devel.

%prep
%setup -q -n libcxx

%build
install -d build
cd build
%{cmake} ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CREDITS.TXT
%attr(755,root,root) %{_libdir}/libc++.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libc++.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libc++.so
%{_includedir}/c++
