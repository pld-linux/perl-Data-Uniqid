#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Data
%define		pnam	Uniqid
Summary:	Data::Uniqid - Perl extension for simple genrating of unique id's
Name:		perl-Data-Uniqid
Version:	0.12
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Data/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6bab3b5da09fedfdf60ce2629a7367db
URL:		https://metacpan.org/release/Data-Uniqid/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data::Uniqid provides three simple routines for generating unique ids.
These ids are coded with a Base62 systen to make them short and handy
(e.g. to use it as part of a URL).

suinqid genrates a very short id valid only for the localhost and with
a liftime of 1 day

uniqid generates a short id valid on the local host

luniqid generates a long id valid everywhere and ever

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Data/Uniqid.pm
%dir %{perl_vendorlib}/auto/Data/Uniqid
%{perl_vendorlib}/auto/Data/Uniqid/autosplit.ix
%{_mandir}/man3/Data::Uniqid.3*
