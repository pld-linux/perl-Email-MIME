#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Email
%define	pnam	MIME
Summary:	Email::MIME - easy MIME message parsing
Summary(pl.UTF-8):	Email::MIME - łatwe analizowanie wiadomości w formacie MIME
Name:		perl-Email-MIME
Version:	1.946
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
#Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31e3aca6bee28cd29c351b65fe89bc6a
URL:		http://search.cpan.org/dist/Email-MIME/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Date-Format
BuildRequires:	perl-Email-MIME-ContentType >= 1.016
BuildRequires:	perl-Email-MIME-Encodings >= 1.314
BuildRequires:	perl-Email-MessageID
BuildRequires:	perl-Email-Simple >= 1:2.211
BuildRequires:	perl-Encode
BuildRequires:	perl-MIME-Types >= 1.13
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
%endif
Requires:	perl-Email-Simple >= 1:2.004
Provides:	perl-Email-MIME-Creator
Provides:	perl-Email-MIME-Modifier
Obsoletes:	perl-Email-MIME-Creator
Obsoletes:	perl-Email-MIME-Modifier
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension of the Email::Simple module, to handle MIME
encoded messages. It takes a message as a string, splits it up into
its constituent parts, and allows you access to various parts of the
message. Headers are decoded from MIME encoding.

%description -l pl.UTF-8
Jest to rozszerzenie modułu Email::Simple służące do obsługi
wiadomości w formacie MIME. Pobiera ono wiadomość jako łańcuch
tekstowy, dzieli go na części składowe i umożliwia dostęp do
poszczególnych części wiadomości. Nagłówki również są dekodowane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/*.pm
%{perl_vendorlib}/Email/MIME/*.pm
%{perl_vendorlib}/Email/MIME/Header
%{_mandir}/man3/*
