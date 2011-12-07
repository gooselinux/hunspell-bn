%define upstreamver 0.04

Name: hunspell-bn
Summary: Bengali hunspell dictionaries
Version: %{upstreamver}
Release: 2%{?dist}
Epoch: 1
Group:          Applications/Text
Source: http://sourceforge.net/projects/bengalinux/files/bengali-spellcheck/%{name}-%{version}.tar.bz2
URL: http://ankur.org.bd/wiki
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv2+
BuildArch: noarch

Requires: hunspell

%description
Bengali hunspell dictionaries.

%prep
%setup -q -n %{name}-%{upstreamver}
chmod -x bn.aff  bn.dic  COPYING  Copyright README
chmod -x doc/README
mv bn.aff bn_BD.aff
mv bn.dic bn_BD.dic

# Convert to utf-8
for file in Copyright doc/README; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
bn_BD_aliases="bn_IN"
for lang in $bn_BD_aliases; do
        ln -s bn_BD.aff $lang.aff
        ln -s bn_BD.dic $lang.dic
done
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc doc/README COPYING Copyright
%{_datadir}/myspell/*

%changelog
* Thu Mar 25 2010 Parag <pnemade AT redhat.com> - 1:0.04-2
- Resolves:rh#576773  - newer release 0.04 made symlink to bn_BD nonexistent 

* Fri Feb 26 2010 Parag <pnemade AT redhat.com> - 1:0.04-1
- Resolves:rh#568644 - Should use correct version what upstream provides by adding epoch

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 20080201-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 08 2008 Parag <pnemade@redhat.com> - 20080201-1
- update to latest release.

* Tue Sep 02 2008 Caolán McNamara <caolanm@redhat.com> - 20050726-3
- add bn_BD alias

* Sun Jan 06 2008 Parag <pnemade@redhat.com> - 20050726-2
- Added Copyright and corrected changelog version.

* Thu Jan 03 2008 Parag <pnemade@redhat.com> - 20050726-1
- Initial Fedora release
