%define major 2
%define libname %mklibname cds
%define devname %mklibname cds -d
%define staticname %mklibname cds-s -d -s

Name: libcds
Version: 2.3.3
Release: 1
Source0: https://github.com/khizmax/libcds/archive/refs/tags/v%{version}.tar.gz
Summary: Concurrent Data Structures library for C++
URL: https://github.com/khizmax/libcds
License: BSL-1.0
Group: System/Libraries
BuildRequires: cmake

%description
Concurrent Data Structures library for C++

%package -n %{libname}
Summary: Concurrent Data Structures library for C++
Group: System/Libraries

%description -n %{libname}
Concurrent Data Structures library for C++

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}, a
Concurrent Data Structures library for C++.

%package -n %{staticname}
Summary: Static library files for %{name}
Group: Development/C
Requires: %{devname} = %{EVRD}

%description -n %{staticname}
Static library files (Headers etc.) for %{name}, a
Concurrent Data Structures library for C++.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_prefix}/lib/cmake/*

%files -n %{staticname}
%{_libdir}/*.a
