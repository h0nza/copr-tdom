Name:           tdom
Version:        0.8.2
Release:        1%{?dist}
Summary:        DOM parser for Tcl

Group:          Development/Libraries
# Most files MPL except for ./generic/xmlsimple.c and ./generic/domhtml.c
# which are LGPLV2+.
License:        LGPLv2+
URL:            http://www.tdom.org
Source0:        http://www.tdom.org/files/tDOM-%{version}.tgz
Patch0:         tdom-0.8.2-noexpat.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  tcl-devel expat-devel

%description
tDOM combines high performance XML data processing with easy and powerful Tcl
scripting functionality. tDOM should be one of the fastest ways to manipulate
XML with a scripting language and uses very little memory.

%package devel
Summary: Development files for compiling against tdom
Group: Development/Libraries
Requires:       %{name} = %{version}-%{release} expat-devel
%description devel
Development header files for compiling against tdom.

%prep
%setup -q -n tDOM-%{version}
%patch0 -p1


%build
%configure --enable-threads
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE CHANGES ChangeLog doc/*.html NPL-1_1Final.html
%{_libdir}/%{name}%{version}
%exclude %{_libdir}/%{name}%{version}/*.a
%{_mandir}/mann/*.gz

%files devel
%defattr(-,root,root,-)
%{_libdir}/%{name}Config.sh
# This static library is a 'stub' library that is used to assist with
# shared lib linking across library versions:  http://wiki.tcl.tk/285
%{_libdir}/%{name}%{version}/*.a
%{_includedir}/*.h



%changelog
* Sun Aug 26 2007 Wart <wart at kobold.org> - 0.8.2-1
- Update to 0.8.2
- Split into base and -devel packages
- License tag clarification

* Tue May 1 2007 Wart <wart at kobold.org> - 0.8.0-2
- Updated patch 1 to add $RPM_OPT_FLAGS to the compiler flags
- Add --enable-threads to match the configuration of the core Tcl package

* Sat Nov 25 2006 Wart <wart at kobold.org> - 0.8.0-1
- Initial package for Fedora
