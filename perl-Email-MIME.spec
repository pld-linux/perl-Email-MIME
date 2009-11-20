#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME
Summary:	Email::MIME - easy MIME message parsing
Summary(pl.UTF-8):	Email::MIME - łatwe analizowanie wiadomości w formacie MIME
Name:		perl-Email-MIME
Version:	1.902
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b60af53f995c8cdbbe2f23518fafd8b0
URL:		http://search.cpan.org/dist/Email-MIME/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-MIME-ContentType >= 1.011
BuildRequires:	perl-Email-MIME-Encodings >= 1.3
BuildRequires:	perl-Email-Simple >= 1:2.004
BuildRequires:	perl-MIME-Types >= 1.13
%endif
Requires:	perl-Email-Simple >= 1:2.004
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
%{_mandir}/man3/*
