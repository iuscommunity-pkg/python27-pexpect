%global pymajor 2
%global pyminor 7
%global pyver %{pymajor}.%{pyminor}
%global iusver %{pymajor}%{pyminor}
%global __python27 %{_bindir}/python%{pyver}
%global python27_sitelib  %(%{__python27} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")
%global python27_sitearch %(%{__python27} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")
%global __os_install_post %{__python27_os_install_post}
%global with_check 0

Summary: Unicode-aware Pure Python Expect-like module
Name: python%{iusver}-pexpect
Version: 3.3
Release: 1.ius%{?dist}
License: MIT
Group: Development/Languages
URL: https://github.com/pexpect/pexpect
Source0: https://pypi.python.org/packages/source/p/pexpect/pexpect-%{version}.tar.gz
%{?el5:BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}

BuildArch: noarch
%if 0%{?with_tests}
BuildRequires: python-nose
%endif
BuildRequires: python%{iusver}-devel ed


%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

Pexpect can be used for automating interactive applications such as ssh, ftp,
passwd, telnet, etc. It can be used to automate setup scripts for duplicating
software package installations on different servers. And it can be used for
automated software testing. Pexpect is in the spirit of Don Libes' Expect, but
Pexpect is pure Python. Unlike other Expect-like modules for Python, Pexpect
does not require TCL or Expect nor does it require C extensions to be
compiled.  It should work on any platform that supports the standard Python
pty module.


%prep
%setup -q -n pexpect-%{version}
find -name '*.py' -type f -print0 | xargs -0 sed -i '1s|^#!/usr/bin/env .*|#!/usr/bin/env python%{pyver}|'


%build
%{__python27} setup.py build


%check
%if 0%{?with_tests}
. ./test.env
./tools/testall.py
%endif


%install
%{?el5:%{__rm} -rf %{buildroot}}

%{__python27} setup.py install \
    --root %{buildroot} \
    --install-lib %{python27_sitelib} \
    --optimize 1 \
    --skip-build

# Correct some permissions
find examples -type f -exec chmod a-x \{\} \;


%{?el5:%clean}
%{?el5:%{__rm} -rf %{buildroot}}


%files
%doc doc examples LICENSE
%{python27_sitelib}/*.py*
%{python27_sitelib}/pexpect/
%{python27_sitelib}/pexpect-%{version}-py?.?.egg-info


%changelog
* Fri Feb 06 2015 Carl George <carl.george@rackspace.com> - 3.3
- Port from Fedora to IUS
- Latest upstream

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Tue Apr 08 2014 Fabian Deutsch <fabiand@fedoraproject.org> - 3.1-1
- Update to 3.1

* Tue Nov 12 2013 Thomas Spura <tomspur@fedoraproject.org> - 3.0-1
- update to 3.0

* Wed Oct 30 2013 Thomas Spura <tomspur@fedoraproject.org> - 3.0-0.1
- new upstream is github/pexpect/pexpect
- update to rc3
- build on noarch again
- consistently use %%{buildroot} everywhere
- be more explicit in %%files
- remove CFLAGS

* Thu Sep 05 2013 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-11
- Fix the name of the arm architecture in ExcludeArch

* Thu Sep 05 2013 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-10
- Remove noarch because of arm build problems (bug #999174)

* Tue Aug 20 2013 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-9
- Exclude the arm architecture (bug #999174)

* Tue Aug 20 2013 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-8
- Bump the obsoletes version

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-5
- Exclude test scripts from the files list

* Tue Nov 20 2012 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-4
- Moved unit tests to a check section

* Tue Nov 20 2012 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-3
- Added unit tests and fixed metadata fields

* Tue Nov 20 2012 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-2
- Added versions to the obsoletes and provides fields

* Tue Nov 20 2012 Andrew McNabb <amcnabb@mcnabbs.org> - 2.5.1-1
- Updated to version 2.5.1 (pexpect-u fork) and added support for Python 3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 2.3-3
- Rebuild for gcc 4.4 and rpm 4.6

* Fri Dec  5 2008 Jeremy Katz <katzj@redhat.com> - 2.3-2
- Rebuild for python 2.6

* Tue Jan 08 2008 Robert Scheck <robert@fedoraproject.org> 2.3-1
- Upgrade to 2.3
- Updated the source URL to match with the guidelines

* Wed Aug 29 2007 Robert Scheck <robert@fedoraproject.org> 2.1-5
- Rebuilt (and some minor spec file tweaks)

* Sat Dec 09 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.1-4
- Bump and rebuild because I forgot to cvs up before the last build.

* Sat Dec 09 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.1-3
- Bump and rebuild for python 2.5 on devel.
- Add BR: python-devel as it provides a header necessary for python modules
  on python 2.5.

* Fri Sep 01 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.1-2
- Remove pyver define as it's not needed with the automatic python(abi).
- Stop ghosting .pyos.
- Let automatic python compilation take care of creating pyos.
- Rebuild for FC6.

* Mon Jul 17 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.1-1
- Update to 2.1.

* Thu Feb 16 2006 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.0-2
- Bump and rebuild for FC5.
- Convert from python-abi to python(abi) requires.

* Thu Nov 17 2005 Toshio Kuratomi <toshio@tiki-lounge.com> - 2.0-1
- Update to 2.0.

* Sat Sep 3 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0.99999b-2
- Add LICENSE File.
- Make noarch.
- Remove executable permissions from the modules copied to examples.

* Fri Sep  2 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0.99999b
- Update to version 0.99999b.
- Add dist tag.

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu Feb 03 2005 Toshio Kuratomi <toshio@tiki-lounge.com> 0.999-2
- Use python_sitelib macro to resolve build issues on x86_64.
- %%ghost *.pyo
- Install ANSI.py, screen.py, and FSM.py into the examples.  These are intended
  to suplement pexpect eventually but they are currently much less robust and
  not installed to by default.  But they are needed by some examples.
- Use __python macro in build/install for consistency.
- Add --skip-build to the invocation of setup.py in install.

* Mon May 31 2004 Panu Matilainen <pmatilai@welho.com> 0.999-0.fdr.1
- get rid of distrel munging, buildsys does that...
- update to 0.999
- update doc and example tarballs
- fix build on python <> 2.2
- use -O1 in install to generate .pyo files instead of manually creating the files
- require python-abi = pyver to get dependencies right

* Sun Jul 27 2003 Panu Matilainen <pmatilai@welho.com> 0.98-0.fdr.3
- own .pyo files too as suggested by Ville (#517)

* Sat Jul 26 2003 Panu Matilainen <pmatilai@welho.com> 0.98-0.fdr.2
- fixes by Ville (bug #517) applied

* Sat Jul 26 2003 Panu Matilainen <pmatilai@welho.com>
- Initial Fedora packaging

