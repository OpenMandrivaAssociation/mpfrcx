%define libmajor	1
%define libname		%mklibname %{name} %{libmajor}
%define libname_devel	%mklibname %{name} -d

Summary:	Arithmetic of univariate polynomials over arbitrary precision real (Mpfr) or complex (Mpc) numbers
Name:		mpfrcx
Version:	0.3.1
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.http://www.multiprecision.org/%{name}
Source0:	http://www.multiprecision.org/mpfrcx/download/%{name}-%{version}.tar.gz
BuildRequires:	libgmp-devel
BuildRequires:	libmpfr-devel
BuildRequires:	libmpc-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Mpfrcx is a library for the arithmetic of univariate polynomials over
arbitrary precision real (Mpfr) or complex (Mpc) numbers, without control
on the rounding. For the time being, only the few functions needed to
implement the floating point approach to complex multiplication are implemented.
On the other hand, these comprise asymptotically fast multiplication routines
such as Toom-Cook and the FFT.

%package	-n %{libname}
Summary:	Arithmetic of complex numbers with arbitrarily high precision and correct rounding
Group:		System/Libraries

%description	-n %{libname}
Mpfrcx is a library for the arithmetic of univariate polynomials over
arbitrary precision real (Mpfr) or complex (Mpc) numbers, without control
on the rounding. For the time being, only the few functions needed to
implement the floating point approach to complex multiplication are implemented.
On the other hand, these comprise asymptotically fast multiplication routines
such as Toom-Cook and the FFT.

%package	-n %{libname_devel}
Summary:	Development headers and libraries for MPFRCX
Group:		Development/C
Requires(post):	info-install
Requires(preun):info-install
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description	-n %{libname_devel}
Development headers and libraries for MPFRCX.

%prep
%setup -q

%build
%configure2_5x			\
	--enable-shared		\
	--disable-static

%make

%install
rm -fr %buildroot
%makeinstall_std
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 0644 AUTHORS NEWS README TODO %{buildroot}%{_docdir}/%{name}

%check
make check

%clean
%{__rm} -rf %{buildroot}

%files		-n %{libname}
%defattr(-,root,root)
%doc %dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*
%{_libdir}/libmpfrcx.so.%{libmajor}*

%files		-n %{libname_devel}
%defattr(-,root,root)
%{_includedir}/mpfrcx.h
%{_infodir}/mpfrcx.info*
%{_libdir}/libmpfrcx.la 
%{_libdir}/libmpfrcx.so
