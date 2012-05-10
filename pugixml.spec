%define		major 1
%define		libname		%mklibname pugixml %{major}
%define		develname	%mklibname pugixml -d

Name:		pugixml
Version:	1.2
Release:	1
Summary:	A light-weight C++ XML processing library
Group:		System/Libraries
License:	MIT
URL:		http://pugixml.org
Source0:	http://pugixml.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:	cmake

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

%package -n %{develname}
Summary:	Development files for %{name} library
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for package %{name} library

%prep
%setup -q -c %{name}-%{version}
#%patch0 -p0

%build
%cmake ../scripts
%make

%install
mkdir -p %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_datadir}/%{name}/contrib
mkdir -p %{buildroot}%{_libdir}

install -p -m 0644 contrib/* %{buildroot}%{_datadir}/%{name}/contrib/
install -p -m 0644 src/*.hpp %{buildroot}%{_includedir}/
install -p -m 0755  build/*.so.* %{buildroot}%{_libdir}/
mv build/*.so %{buildroot}%{_libdir}/

%files -n %{libname}
%doc readme.txt
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%doc docs/*
%{_libdir}/*.so
%{_datadir}/%{name}
%{_includedir}/*.hpp
