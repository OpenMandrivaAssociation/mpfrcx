%define libmajor	1
%define libname		%mklibname %{name} %{libmajor}
%define libname_devel	%mklibname %{name} -d

Summary:	Arithmetic of univariate polynomials
Name:		mpfrcx
Version:	0.6.3
Release:	1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.multiprecision.org/%{name}
Source0:	http://www.multiprecision.org/downloads/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gmp)
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	libmpc-devel

%description
Mpfrcx is a library for the arithmetic of univariate polynomials over
arbitrary precision real (Mpfr) or complex (Mpc) numbers, without control
on the rounding. For the time being, only the few functions needed to
implement the floating point approach to complex multiplication are
implemented. On the other hand, these comprise asymptotically fast
multiplication routines such as Toom-Cook and the FFT.

%package	-n %{libname}
Summary:	Arithmetic of univariate polynomials
Group:		System/Libraries

%description	-n %{libname}
Mpfrcx is a library for the arithmetic of univariate polynomials over
arbitrary precision real (Mpfr) or complex (Mpc) numbers, without control
on the rounding. For the time being, only the few functions needed to
implement the floating point approach to complex multiplication are
implemented. On the other hand, these comprise asymptotically fast
multiplication routines such as Toom-Cook and the FFT.

%package	-n %{libname_devel}
Summary:	Development headers and libraries for MPFRCX
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{libname_devel}
Development headers and libraries for MPFRCX.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%check
make check

%files -n %{libname}
%{_libdir}/libmpfrcx.so.%{libmajor}*

%files -n %{libname_devel}
%doc AUTHORS NEWS README
%{_includedir}/mpfrcx.h
%{_infodir}/mpfrcx.info*
%{_libdir}/libmpfrcx.so

