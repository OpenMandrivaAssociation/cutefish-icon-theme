%define oname icons
%define  _name  Crule
Name:           cutefish-icon-theme
Version:        0.8
Release:        1
Summary:        Cutefish Desktop Icon Theme
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/cutefishos/icons
Source:         https://github.com/cutefishos/icons/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       gtk-update-icon-cache

BuildArch:      noarch

%description
Dark and light icons for Cutefish Desktop

%prep
%autosetup -n %{oname}-%{version} -p1
rm -fv %{_name}*/icon-theme.cache

%build

%install
install -dm 0755 %{buildroot}%{_datadir}/icons/
cp -a %{_name} %{buildroot}%{_datadir}/icons/
cp -a %{_name}-dark %{buildroot}%{_datadir}/icons/
find %{buildroot}%{_datadir}/icons -type f -exec chmod 0644 {} \;
find -L %{buildroot}%{_datadir}/icons -type l -delete -print

%fdupes -s %{buildroot}%{_datadir}/icons/

#icon_theme_cache_create_ghost %{_name}
#icon_theme_cache_create_ghost %{_name}-dark

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/%{_name}*/
%ghost %{_datadir}/icons/%{_name}*/icon-theme.cache
