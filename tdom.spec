Name:           tdom
Version:        0.8.0
Release:        2%{?dist}
Summary:        DOM parser for Tcl

Group:          Development/Libraries
License:        MPL
URL:            http://www.tdom.org
Source0:        http://www.tdom.org/files/tDOM-0.8.0.tar.gz
Patch0:         tdom-0.8.0-tclconfig.patch
Patch1:         tdom-0.8.0-sourcelist.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  tcl-devel expat-devel

%description
tDOM combines high performance XML data processing with easy and powerful Tcl
scripting functionality. tDOM should be one of the fastest ways to manipulate
XML with a scripting language and uses very little memory.

%prep
%setup -q -n tDOM-%{version}
%patch0
%patch1


%build
%configure --enable-threads
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT/%{_libdir}/%{name}%{version}/*.a


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README LICENSE CHANGES ChangeLog doc/*.html NPL-1_1Final.html
%{_libdir}/%{name}%{version}
%{_libdir}/%{name}Config.sh
%{_mandir}/mann/*.gz



%changelog
* Tue May 1 2007 Wart <wart at kobold.org> - 0.8.0-2
- Updated patch 1 to add $RPM_OPT_FLAGS to the compiler flags
- Add --enable-threads to match the configuration of the core Tcl package

* Sat Nov 25 2006 Wart <wart at kobold.org> - 0.8.0-1
- Initial package for Fedora
