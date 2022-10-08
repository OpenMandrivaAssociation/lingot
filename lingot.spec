%define major 0
%define libname	%mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Summary:	A musical instrument tuner
Name:		lingot
Version:	1.1.1
Release:	1
License:	GPLv2
URL:		https://www.nongnu.org/%{name}/
Group:		Sound
Source0:	https://github.com/ibancg/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	intltool >= 0.23
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libpulse-simple)

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, it can now be used
to tune other instruments.

It looks like an analogue tuner, with a gauge indicating the relative shift to
a certain note, found automatically as the closest note to the estimated
frequency.

%files -f %{name}.lang
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.nongnu.%{name}.desktop
%{_datadir}/metainfo/org.nongnu.%{name}.appdata.xml
%{_iconsdir}/hicolor/scalable/apps/org.nongnu.%{name}.svg
%{_mandir}/man1/%{name}.1*

#---------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library used by %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the main library used by %{name}.

%files -n %{libname}
%license COPYING
%{_libdir}/lib%{name}.so.%{major}*

#---------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{libname}
Group:		Development/C

%description -n %{devname}
This package contains the files needed to build against %{libname}.

%files -n %{devname}
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.config THANKS
%{_includedir}/%{name}/%{name}-*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

# remove unwanted docs
rm -rf %{buildroot}%{_docdir}/%{name}/{AUTHORS,ChangeLog,COPYING,NEWS,README,README.config,THANKS}

# locales
%find_lang %{name}

