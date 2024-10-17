%define		_class		HTML
%define		_subclass	Crypt
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.4
Release:	5
Summary:	Encrypts text which is later decoded using javascript on the client side
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/HTML_Crypt/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
The PEAR::HTML_Crypt provides methods to encrypt text, which can be
later be decrypted using JavaScript on the client side. This is very
useful to prevent spam robots collecting email addresses from your
site, included is a method to add mailto links to the text being
generated.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-3mdv2012.0
+ Revision: 741992
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2
+ Revision: 679343
- mass rebuild

* Sun Nov 07 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 594487
- update to new version 1.3.4

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-4mdv2010.1
+ Revision: 477862
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.3.3-3mdv2010.0
+ Revision: 441113
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.3-2mdv2009.1
+ Revision: 322111
- rebuild

* Sun Oct 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.3-1mdv2009.1
+ Revision: 292880
- update to new version 1.3.3

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-3mdv2009.0
+ Revision: 236864
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-2mdv2008.1
+ Revision: 171038
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-1mdv2008.0
+ Revision: 15748
- fix build
- 1.3.2


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-7mdv2007.0
+ Revision: 81611
- Import php-pear-HTML_Crypt

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- initial Mandriva package (PLD import)

