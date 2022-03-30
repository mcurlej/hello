Name: hello
Version: 0.1.0
Release: 1%{?dist}
Summary: Hello Pyvo!
License: MIT
BuildArch: noarch

URL: https://github.com/mcurlej/module-build
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: python3-pytest

%description
Prints "Hello Pyvo!" to the command line.


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%check
%pytest


%files
%doc README.md
%license LICENSE
%{python3_sitelib}/hello/
%{python3_sitelib}/hello-*.egg-info/
%{_bindir}/hello


%changelog
* Wed Mar 30 2022 Martin Čurlej <mcurlej@redhat.com> - 0.1.0-1
- Hello Pyvo! (martin.curlej@gmail.com)
