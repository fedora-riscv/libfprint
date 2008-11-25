Name:           libfprint
Version:        0.1.0
Release:        3.pre1%{?dist}
Summary:        Tool kit for fingerprint scanner

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.reactivated.net/fprint/wiki/Main_Page 
Source0:        http://downloads.sourceforge.net/fprint/%{name}-0.1.0-pre1.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0:         0002-Fix-fp_get_pollfds.patch

# FIXME remove the ImageMagick dependency when we either have the
# gdk-pixbuf support merged, or disable the driver that requires it (F10)
BuildRequires:  libusb1-devel ImageMagick-devel glib2-devel openssl-devel 
BuildRequires:  doxygen
Requires:       ConsoleKit

%description
libfprint offers support for consumer fingerprint reader devices.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-0.1.0-pre1
%patch0 -p1

%build
%configure --disable-static 
make %{?_smp_mflags}
pushd doc
make docs
popd

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%clean
rm -rf $RPM_BUILD_ROOT


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc COPYING INSTALL NEWS TODO THANKS AUTHORS
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc HACKING doc/html
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/hal/fdi/information/20thirdparty/10-fingerprint-reader-fprint.fdi

%changelog
* Tue Nov 25 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-3.pre1
- Fix possible crasher in libfprint when setting up the fds for polling

* Mon Nov 24 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-2.pre1
- And add some API docs

* Tue Nov 18 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-1.pre1
- Fix build

* Tue Nov 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1.0-0.pre1
- Update to 0.1.0-pre1

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-6
- Correction on the Build Requires

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-5
- Correction on the Build Requires

* Tue May 13 2008  Pingou <pingoufc4@yahoo.fr> 0.0.5-4
- Update the Build Requires due to the change on ImageMagick

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.0.5-3
- Autorebuild for GCC 4.3

* Sat Jan 05 2008 Pingou <pingoufc4@yahoo.fr> 0.0.5-2
- Change on the BuildRequires

* Sat Jan 05 2008 Pingou <pingoufc4@yahoo.fr> 0.0.5-1
- Update to version 0.0.5

* Sat Dec 01 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-3
- Changes on the Requires

* Sun Nov 25 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-2
- Changes on the Requires

* Sat Nov 24 2007 Pingou <pingoufc4@yahoo.fr> 0.0.4-1
- First release
