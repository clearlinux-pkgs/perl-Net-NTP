#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Net-NTP
Version  : 1.5
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/A/AB/ABH/Net-NTP-1.5.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AB/ABH/Net-NTP-1.5.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libn/libnet-ntp-perl/libnet-ntp-perl_1.5-1.debian.tar.xz
Summary  : 'Perl extension for decoding NTP server responses'
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Net-NTP-license = %{version}-%{release}
Requires: perl-Net-NTP-perl = %{version}-%{release}
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
Requires: perl-Net-NTP = %{version}-%{release}

%description dev
dev components for the perl-Net-NTP package.


%package license
Summary: license components for the perl-Net-NTP package.
Group: Default

%description license
license components for the perl-Net-NTP package.


%package perl
Summary: perl components for the perl-Net-NTP package.
Group: Default
Requires: perl-Net-NTP = %{version}-%{release}

%description perl
perl components for the perl-Net-NTP package.


%prep
%setup -q -n Net-NTP-1.5
cd %{_builddir}
tar xf %{_sourcedir}/libnet-ntp-perl_1.5-1.debian.tar.xz
cd %{_builddir}/Net-NTP-1.5
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Net-NTP-1.5/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Net-NTP
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Net-NTP/4305dcc1b68ae3beee4147db0b9510139ea3096f
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Net::NTP.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Net-NTP/4305dcc1b68ae3beee4147db0b9510139ea3096f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Net/NTP.pm
