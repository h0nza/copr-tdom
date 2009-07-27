%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%(echo 'puts $tcl_version' | tclsh)}

Name:           tdom
Version:        0.8.2
Release:        6%{?dist}
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
Requires:       tcl(abi) = 8.5

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

mkdir -p $RPM_BUILD_ROOT%{tcl_sitearch}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}%{version}/*.so $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}%{version}/*.a $RPM_BUILD_ROOT%{_libdir}
mv $RPM_BUILD_ROOT%{_libdir}/%{name}%{version} $RPM_BUILD_ROOT%{tcl_sitearch}

# Adjust some paths to reflect the new file locations
sed -i -e 's/file join $dir libtdom/file join $dir .. .. libtdom/' $RPM_BUILD_ROOT%{tcl_sitearch}/%{name}%{version}/pkgIndex.tcl

sed -i -e "s#%{_libdir}/%{name}%{version}#%{_libdir}#" $RPM_BUILD_ROOT%{_libdir}/tdomConfig.sh

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE CHANGES ChangeLog doc/*.html NPL-1_1Final.html
%{tcl_sitearch}/%{name}%{version}
%{_libdir}/*.so
%exclude %{_libdir}/*.a
%{_mandir}/mann/*.gz

%files devel
%defattr(-,root,root,-)
%{_libdir}/%{name}Config.sh
# This static library is a 'stub' library that is used to assist with
# shared lib linking across library versions:  http://wiki.tcl.tk/285
%{_libdir}/*.a
%{_includedir}/*.h



%changelog
* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jun 4 2008 Wart <wart at kobold.org> - 0.8.2-4
- Change installation directory for faster loading

* Sat Feb 9 2008 Wart <wart at kobold.org> - 0.8.2-3
- Rebuild for gcc 4.3

* Sun Sep 23 2007 Wart <wart at kobold.org> - 0.8.2-2
- Added missing linkage against -lexpat

* Sun Aug 26 2007 Wart <wart at kobold.org> - 0.8.2-1
- Update to 0.8.2
- Split into base and -devel packages
- License tag clarification

* Tue May 1 2007 Wart <wart at kobold.org> - 0.8.0-2
- Updated patch 1 to add $RPM_OPT_FLAGS to the compiler flags
- Add --enable-threads to match the configuration of the core Tcl package

* Sat Nov 25 2006 Wart <wart at kobold.org> - 0.8.0-1
- Initial package for Fedora
