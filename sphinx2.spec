Summary:	Speech recognitnion engine
Name:		sphinx2
Version:	0.6
Release:	3
License:	BSD-like
Group:		Sound
Source0:	http://dl.sourceforge.net/cmusphinx/%{name}-%{version}.tar.gz
Patch0:		%{name}-wid.patch
URL:		https://www.speech.cs.cmu.edu/sphinx/

Requires: sphinxbase
BuildRequires: sphinxbase sphinxbase-devel

%define Werror_cflags %nil
%define _disable_ld_no_undefined 1

%description
One of Carnegie Mellon University's open source large vocabulary,
speaker-independent continuous speech recognition engine.

Plug your microphone, launch sphinx2-simple, and test it!

%package devel
Summary:	%{name} header files
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
%{name} header files.

%package static
Summary:	Static sphinx2 libraries
Group:		System/Libraries 
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of sphinx2 libraries.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cp configure.ac configure.in
%configure
%{__make}

%install
%makeinstall_std

# hmm, name may conflict
rm -f %{buildroot}%{_bindir}/batch.csh

%files
%defattr(644,root,root,755)
%doc README doc
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*
%ghost %{_libdir}/*.so.0
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
