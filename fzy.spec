Summary:	A simple, fast fuzzy finder for the terminal
Name:		fzy
Version:	1.0
Release:	1
License:	MIT
Group:		Applications/Shells
Source0:	https://github.com/jhawthorn/fzy/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2d63086ddf03ccfb3f18f9a8af08203a
URL:		https://github.com/jhawthorn/fzy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fzy is a fast, simple fuzzy text selector for the terminal with an
advanced scoring algorithm.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -MD -std=c99 -Ideps"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	MANDIR=%{_mandir} \
	BINDIR=%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ALGORITHM.md CHANGELOG.md README.md
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
