Summary:    A musical instrument tuner
Name:       lingot
Version:    0.8.1
Release:    %mkrel 1
URL:        http://savannah.nongnu.org/projects/%{name}
Source:     http://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Patch0:     lingot-0.8.1-fix-string-format.patch
License:    GPLv2
Group:      Sound
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel libglade2-devel
BuildRequires: intltool
BuildRequires: libalsa-devel libjack-devel

%description
LINGOT is a musical instrument tuner. It's accurate, easy to use, and highly
configurable. Originally conceived to tune electric guitars, it can now be used
to tune other instruments.

It looks like an analogue tuner, with a gauge indicating the relative shift to
a certain note, found automatically as the closest note to the estimated
frequency.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README THANKS
%{_bindir}/%name
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}
%{_datadir}/%{name}
