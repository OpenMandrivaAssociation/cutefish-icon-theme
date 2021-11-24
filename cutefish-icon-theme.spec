%define  _name  Crule
Name:           cutefish-icon-theme
Version:        @SERVICE@
Release:        0
Summary:        Cutefish Desktop Icon Theme
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/cutefishos/icons
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       gtk3-tools
Conflicts:      cyber-icon-theme
BuildArch:      noarch

%description
Dark and light icons for Cutefish Desktop

%prep
%autosetup
rm -fv %{_name}*/icon-theme.cache

%build

%install
install -dm 0755 %{buildroot}%{_datadir}/icons/
cp -a %{_name} %{buildroot}%{_datadir}/icons/
cp -a %{_name}-dark %{buildroot}%{_datadir}/icons/
find %{buildroot}%{_datadir}/icons -type f -exec chmod 0644 {} \;
find -L %{buildroot}%{_datadir}/icons -type l -delete -print

%fdupes -s %{buildroot}%{_datadir}/icons/

%icon_theme_cache_create_ghost %{_name}
%icon_theme_cache_create_ghost %{_name}-dark

%files
%doc README.md
%{_datadir}/icons/%{_name}*/
%ghost %{_datadir}/icons/%{_name}*/icon-theme.cache
%license LICENSE
