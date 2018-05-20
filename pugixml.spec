%define major 1
%define libname	%mklibname pugixml %{major}
%define devname	%mklibname pugixml -d

Summary:	A light-weight C++ XML processing library
Name:		pugixml
Version:	1.9
Release:	1
Group:		System/Libraries
License:	MIT
Url:		http://pugixml.org
Source0:	http://github.com/zeux/pugixml/releases/download/v%{version}/pugixml-%{version}.tar.gz
Source100:	pugixml.rpmlintrc
BuildRequires:	cmake ninja

%description
pugixml is a light-weight C++ XML processing library.
It features:
- DOM-like interface with rich traversal/modification capabilities
- Extremely fast non-validating XML parser which constructs the DOM tree from
  an XML file/buffer
- XPath 1.0 implementation for complex data-driven tree queries
- Full Unicode support with Unicode interface variants and automatic encoding
  conversions

%package -n %{libname}
Summary:	A light-weight C++ XML processing library
Group:		System/Libraries

%description -n %{libname}
pugixml is a light-weight C++ XML processing library.
It features:
- DOM-like interface with rich traversal/modification capabilities
- Extremely fast non-validating XML parser which constructs the DOM tree from
  an XML file/buffer
- XPath 1.0 implementation for complex data-driven tree queries
- Full Unicode support with Unicode interface variants and automatic encoding
  conversions

%package -n %{devname}
Summary:	Development files for %{name} library
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for package %{name} library

%prep
%setup -q

%build
%cmake -G Ninja
%ninja_build

%install
%ninja_install -C build

mkdir -p %{buildroot}%{_datadir}/%{name}/contrib
install -p -m 0644 contrib/* %{buildroot}%{_datadir}/%{name}/contrib/

%files -n %{libname}
%{_libdir}/libpugixml.so.%{major}*

%files -n %{devname}
%doc docs/*
%doc readme.txt
%{_libdir}/*.so
%{_datadir}/%{name}
%{_includedir}/*.hpp
%{_libdir}/cmake/pugixml
