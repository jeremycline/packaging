%global srcname twine

Name:           python-%{srcname}
Version:        1.6.5
Release:        1%{?dist}
Summary:        Collection of utilities for interacting with PyPI

License:        ASL 2.0
URL:            https://github.com/pypa/%{srcname}
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz
# There's a shebang in twine/__main__.py which generates rpmlint warnings.
Patch0:         0001-Remove-shebang-from-__main__.py.patch
BuildArch:      noarch

%description
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.


%package -n python2-%{srcname}
Summary:        %{summary}
Requires:       python-pkginfo >= 1.0
Requires:       python-requests >= 2.3.0
Requires:       python-requests-toolbelt >= 0.5.1
Requires:       python-setuptools >= 0.7.0
# Test requirements
BuildRequires:  python2-devel
BuildRequires:  python-pkginfo >= 1.0
BuildRequires:  python-requests >= 2.3.0
BuildRequires:  python-requests-toolbelt >= 0.5.1
BuildRequires:  python-setuptools >= 0.7.0
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.


%package doc
Summary: Documentation for the python2-twine package
BuildRequires:  python-sphinx10
BuildRequires:  python-releases

%description doc
Documentation for the python2-twine package.
Twine is a utility for interacting with PyPI.
Currently it only supports registering projects and uploading distributions.


%prep
%autosetup -p1 -n %{srcname}-%{version}


%build
%py2_build

make %{?_smp_mflags} -C docs SPHINXBUILD=sphinx-build html PYTHONPATH=$(pwd)
make %{?_smp_mflags} -C docs SPHINXBUILD=sphinx-build man PYTHONPATH=$(pwd)
rm docs/_build/html/.buildinfo


%install
%py2_install
ln -s %{_bindir}/twine %{buildroot}%{_bindir}/twine-%{python2_version}
ln -s %{_bindir}/twine-%{python2_version} %{buildroot}%{_bindir}/twine-2

install -p -D -T -m 0644 docs/_build/man/%{srcname}.1 %{buildroot}%{_mandir}/man1/%{srcname}.1


%check
%{__python2} setup.py test


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst AUTHORS
%doc %{_mandir}/man1/%{srcname}.1*
%{python2_sitelib}/*
%{_bindir}/twine
%{_bindir}/twine-2
%{_bindir}/twine-%{python2_version}


%files doc
%license LICENSE
%doc README.rst AUTHORS docs/_build/html


%changelog
* Thu Jun 09 2016 Jeremy Cline <jeremy@jcline.org> - 1.6.5-1
- Initial commit
