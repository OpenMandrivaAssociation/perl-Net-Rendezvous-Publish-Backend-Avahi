%define upstream_name    Net-Rendezvous-Publish-Backend-Avahi
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Publish zeroconf data with the Avahi library
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Rendezvous-Publish-Backend-Avahi-%{upstream_version}.tar.bz2

Provides:  perl-Net-Rendezvous-Publish-Backend
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module publishes zeroconf data with the Avahi library
It is a backend for the Net::Rendezvous::Publish module.

%prep
%setup -q -n Net-Rendezvous-Publish-Backend-Avahi-%{upstream_version}

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
