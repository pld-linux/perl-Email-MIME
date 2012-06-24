#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	MIME
Summary:	Email::MIME - easy MIME message parsing
Summary(pl):	Email::MIME - �atwe analizowanie wiadomo�ci w formacie MIME
Name:		perl-Email-MIME
Version:	1.85
Release:	0.1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	161ca345509281b706ad7e7fbab3d530
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-MIME-ContentType >= 1
BuildRequires:	perl-Email-MIME-Encodings >= 1.3
BuildRequires:	perl-Email-Simple >= 1:1.91
BuildRequires:	perl-MIME-Types >= 1.13
%endif
# not autodetected
Requires:	perl-Email-Simple >= 1:1.91
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension of the Email::Simple module, to handle MIME
encoded messages. It takes a message as a string, splits it up into
its constituent parts, and allows you access to various parts of the
message. Headers are decoded from MIME encoding.

%description -l pl
Jest to rozszerzenie modu�u Email::Simple s�u��ce do obs�ugi
wiadomo�ci w formacie MIME. Pobiera ono wiadomo�� jako �a�cuch
tekstowy, dzieli go na cz�ci sk�adowe i umo�liwia dost�p do
poszczeg�lnych cz�ci wiadomo�ci. Nag��wki r�wnie� s� dekodowane.

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
%doc Changes
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
