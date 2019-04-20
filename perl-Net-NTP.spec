#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-NTP
Version  : 1.5
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/A/AB/ABH/Net-NTP-1.5.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AB/ABH/Net-NTP-1.5.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-ntp-perl/libnet-ntp-perl_1.5-1.debian.tar.xz
Summary  : 'Perl extension for decoding NTP server responses'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Net-NTP-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Net::NTP
========
This module will allow you to send a packet to an NTP server, get
a response back, and then parse out the results according to RFC1305
and RFC2030.

%package dev
Summary: dev components for the perl-Net-NTP package.
Group: Development
Provides: perl-Net-NTP-devel = %{version}-%{release}

%description dev
dev components for the perl-Net-NTP package.


%package license
Summary: license components for the perl-Net-NTP package.
Group: Default

%description license
license components for the perl-Net-NTP package.


%prep
%setup -q -n Net-NTP-1.5
cd ..
%setup -q -T -D -n Net-NTP-1.5 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Net-NTP-1.5/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-NTP
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Net-NTP/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Net/NTP.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::NTP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-NTP/deblicense_copyright
