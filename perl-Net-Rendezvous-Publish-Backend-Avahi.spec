%define upstream_name    Net-Rendezvous-Publish-Backend-Avahi
Name:		perl-%{upstream_name}
Version:	0.04
Release:	5

Summary:	Publish zeroconf data with the Avahi library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/ioanrogers/Net-Rendezvous-Publish-Backend-Avahi
Source0:	https://cpan.metacpan.org/authors/id/I/IO/IOANR/Net-Rendezvous-Publish-Backend-Avahi-%{version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Module::Build)
BuildRequires: perl(Net::DBus)
BuildRequires: perl(Net::Rendezvous::Publish)
Provides:	perl-Net-Rendezvous-Publish-Backend
BuildArch:	noarch

%description
This module publishes zeroconf data with the Avahi library
It is a backend for the Net::Rendezvous::Publish module.

%prep
%setup -q -n Net-Rendezvous-Publish-Backend-Avahi-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%{perl_vendorlib}/Net/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 406175
- rebuild using %0.04 Thu Jul 03 2008 Michael Scherer <misc@mandriva.org> 0.03-3mdv2009.0
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


