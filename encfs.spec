%define major 1
%define libname %mklibname %{name} %{major}

Summary: 	Encrypted pass-through filesystem for Linux
Name:		encfs
Version:	1.9.5
Release:	2
License:	GPLv3+
Group:		File tools
URL: 		https://github.com/vgough/encfs
Source0:	https://github.com/vgough/encfs/releases/download/v%{version}/%{name}-%{version}.tar.gz
Requires:	fuse2
Requires:	openssl >= 0.9.7
BuildRequires:	cmake
BuildRequires:	pkgconfig(librlog)
BuildRequires:	pkgconfig(fuse)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(tinyxml2)
BuildRequires:	chrpath
BuildRequires:	boost-devel >= 1.34
BuildRequires:	autoconf-archive

%description
EncFS implements an encrypted pass-through filesystem in userspace using
FUSE. File names and contents are encrypted using OpenSSL.

%package -n %{libname}
Summary:	Libraries for encfs
Group:		System/Libraries

%description -n %{libname}
Libraries for encfs.

%prep
%autosetup -p1

%cmake -DUSE_INTERNAL_TINYXML=OFF \
      -DINSTALL_LIBENCFS=ON \
      -DBUILD_SHARED_LIBS=ON

%build
%make_build -C build

%install
%make_install -C build

%find_lang %{name}

chrpath -d %{buildroot}%{_bindir}/{encfs,encfsctl}

# unneeded files
rm -f %{buildroot}%{_libdir}/libencfs.la
rm -f %{buildroot}%{_libdir}/libencfs.so

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%{_bindir}/*
%{_mandir}/man?/*

%files -n %{libname}
%{_libdir}/libencfs.so.%{major}*
