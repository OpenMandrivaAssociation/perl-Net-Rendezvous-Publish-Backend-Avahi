%define upstream_name    Net-Rendezvous-Publish-Backend-Avahi
%define upstream_version 0.04
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.04
Release:	1

Summary:	Publish zeroconf data with the Avahi library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Net/Net-Rendezvous-Publish-Backend-Avahi-0.04.tar.gz

BuildRequires:	perl-devel
Provides:	perl-Net-Rendezvous-Publish-Backend
BuildArch:	noarch

%description
This module publishes zeroconf data with the Avahi library
It is a backend for the Net::Rendezvous::Publish module.

%prep
%setup -q -n Net-Rendezvous-Publish-Backend-Avahi-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 406175
- rebuild using %%perl_convert_version

* Thu Jul 03 2008 Michael Scherer <misc@mandriva.org> 0.03-3mdv2009.0
+ Revision: 230902
- rebuild
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 20 2007 Michael Scherer <misc@mandriva.org> 0.03-1mdv2008.0
+ Revision: 28773
- new version 0.03


* Thu Nov 02 2006 Michael Scherer <misc@mandriva.org> 0.02-2mdv2007.0
+ Revision: 75748
- Bump release
- provides perl-Net-Rendezvous-Publish-Backend, like howl backend
- Do not ship empty directory
- Import perl-Net-Rendezvous-Publish-Backend-Avahi


