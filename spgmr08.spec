Summary:	MC68HC908 programmer
Name:		spgmr08
Version:	0.12
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/spgmr08/%{name}-%{version}.tar.gz
# Source0-md5:	da2bcdae8c3cd2c1ce395bc03528452a
URL:		http://spgmr08.sourceforge.net/
BuildRequires:	readline-devel
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-big_endian-fix.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
spgmr08 is a Linux software package for programming devices in the
Motorola MC68HC908 microcontroller family.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPTCFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	LIBDIR="%{_datadir}/%{name}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install spgmr $RPM_BUILD_ROOT%{_bindir}
#%{__sed} 's/Toplevel/tkspgmr/' < tkspgmr.tcl > $RPM_BUILD_ROOT%{_bindir}/tkspgmr
install *.s19 $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES design.txt README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
