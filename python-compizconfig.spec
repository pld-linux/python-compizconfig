Summary:	Python bindings for the compizconfig library
Summary(pl.UTF-8):	Pythonowe dowiązania do biblioteki compizconfig
Name:		python-compizconfig
Version:	0.5.2
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://releases.compiz-fusion.org/%{version}/compizconfig-python-%{version}.tar.bz2
# Source0-md5:	d3bb6415a3f0adc626e2f5e2bdef4495
URL:		http://forum.compiz-fusion.org/
BuildRequires:	glib2-devel
BuildRequires:	libcompizconfig-devel >= %{version}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-Pyrex
BuildRequires:	rpm-pythonprov
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/*.so
%{_pkgconfigdir}/*.pc
