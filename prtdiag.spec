Summary:	A tool that generates report of the hardware
Summary(pl):	Narzêdzie do generowania raportu na temat urz±dzeñ komputera
Name:		prtdiag
Version:	1.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://people.redhat.com/tcallawa/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	08aa8468294aca3d3d622d8be70177ab
URL:		http://people.redhat.com/tcallawa/prtdiag/
Requires:	bash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Prtdiag is a bash script that generates a report that describes the
state of the hardware on the running machine.

%description -l pl
Prtdiag jest skryptem napisanym w bashu, który generuje raport
dotycz±cy stanu urz±dzeñ znajduj±cych siê w komputerze.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir},%{_mandir}/man8}

install prtdiag $RPM_BUILD_ROOT%{_sbindir}
install prtdiag.cfg $RPM_BUILD_ROOT%{_sysconfdir}
gzip -dc prtdiag.8.gz > $RPM_BUILD_ROOT%{_mandir}/man8/prtdiag.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README AUTHORS
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/prtdiag.cfg
%{_mandir}/man8/*
