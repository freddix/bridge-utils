Summary:	Utilities for configuring the Linux ethernet bridge
Name:		bridge-utils
Version:	1.5
Release:	2
License:	GPL
Group:		Networking/Admin
Source0:	http://downloads.sourceforge.net/sourceforge/bridge/%{name}-%{version}.tar.gz
# Source0-md5:	ec7b381160b340648dede58c31bb2238
Patch0:		%{name}-linux3.8.patch
URL:		http://linux-net.osdl.org/index.php/Bridge
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	linux-libc-headers
BuildRequires:	sed
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
This package contains utilities for configuring the Linux ethernet
bridge. The Linux ethernet bridge can be used for connecting multiple
ethernet devices together. The connecting is fully transparent: hosts
connected to one ethernet device see hosts connected to the other
ethernet devices directly.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
export CFLAGS="%{rpmcflags}"
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
%doc AUTHORS ChangeLog THANKS TODO doc/{FAQ,FIREWALL,HOWTO,SMPNOTES,WISHLIST}
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*

