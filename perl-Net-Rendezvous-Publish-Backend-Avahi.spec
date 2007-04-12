%define realname   Net-Rendezvous-Publish-Backend-Avahi

Name:		perl-%{realname}
Version:    0.02
Release:    %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Publish zeroconf data with the Avahi library
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Rendezvous-Publish-Backend-Avahi-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
Provides:   perl-Net-Rendezvous-Publish-Backend
BuildArch: noarch

%description
This module publishes zeroconf data with the Avahi library
It is a backend for the Net::Rendezvous::Publish module.

%prep
%setup -q -n Net-Rendezvous-Publish-Backend-Avahi-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/Net/*
%{_mandir}/man3/*


