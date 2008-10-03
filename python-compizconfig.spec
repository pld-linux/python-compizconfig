Summary:	Python bindings for the compizconfig library
Summary(pl.UTF-8):	Pythonowe dowiązania do biblioteki compizconfig
Name:		python-compizconfig
Version:	0.7.8
Release:	2
License:	LGPL v2+
Group:		Libraries/Python
Source0:	http://releases.compiz-fusion.org/%{version}/compizconfig-python-%{version}.tar.bz2
# Source0-md5:	f75c3a5a3ef770280e46c3a762d456e3
URL:		http://forum.compiz-fusion.org/
BuildRequires:	glib2-devel >= 1:2.6
BuildRequires:	libcompizconfig-devel >= 0.6.0
BuildRequires:	pkgconfig
BuildRequires:	python-Pyrex
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
Requires:	glib2 >= 1:2.6
Obsoletes:	compizconfig-python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for the compizconfig library.

%description -l pl.UTF-8
Pythonowe dowiązania do biblioteki compizconfig.

%prep
%setup -q -n compizconfig-python-%{version}

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/compizconfig.so
%{_pkgconfigdir}/compizconfig-python.pc
