Name:           spotifyd
Version:        0.2.23
Release:        1%{?dist}
Summary:        An open source Spotify client running as a UNIX daemon.

License:        GPL3
URL:            https://github.com/Spotifyd/spotifyd
Source0:        https://github.com/Spotifyd/spotifyd/archive/v%{version}.zip

BuildRequires:  cargo openssl-devel rust-libdbus-sys-devel alsa-lib-devel pulseaudio-libs-devel systemd-rpm-macros
Requires:       openssl pulseaudio-libs alsa-lib

%description


%prep
%autosetup


%build
export RUSTFLAGS=-g
cargo build --release --features "pulseaudio_backend,dbus_keyring,dbus_mpris"

%install
mkdir -p %{buildroot}/%{_bindir} %{buildroot}/%{_userunitdir}

cp target/release/spotifyd %{buildroot}/%{_bindir}/spotifyd
cp contrib/spotifyd.service %{buildroot}/%{_userunitdir}/%{name}.service

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%{_bindir}/spotifyd
%{_userunitdir}/%{name}.service
%license LICENCE



%changelog
* Fri Jan 24 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl>
- 