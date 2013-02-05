# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       sdk-setup

# >> macros
# << macros

Summary:    SDK setup packages for Mer SDK
Version:    0.21
Release:    1
Group:      System/Base
License:    GPL
BuildArch:  noarch
URL:        https://github.com/mer-tools/sdk-setup
Source0:    sdk-setup.tgz
Source100:  sdk-setup.yaml

%description
Scripts, configurations and utilities to build Mer SDK and variants

%package -n sdk-chroot
Summary:    Mer SDK files for the chroot variant
Group:      System/Base
Requires(pre): rpm
Requires(pre): /bin/rm
Conflicts:   sdk-vm

%description -n sdk-chroot
Contains the mer_sdk_chroot script and supporting configs

%package -n sdk-vm
Summary:    Mer SDK files for the VM variant
Group:      System/Base
Requires(post): /bin/ln
Conflicts:   sdk-chroot

%description -n sdk-vm
Contains the supporting configs for VMs

%package -n sdk-sb2-config
Summary:    Mer SDK files to configure sb2
Group:      System/Base
Requires:   scratchbox2

%description -n sdk-sb2-config
Contains the sdk build and install modes used by scratchbox2 in the SDK

%package -n sdk-utils
Summary:    Mer SDK utility scripts
Group:      System/Base
Requires:   rpm-build

%description -n sdk-utils
Contains some utility scripts to support Mer SDK development


%prep
%setup -q -n src

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre

# all sdks
mkdir -p %{buildroot}%{_bindir}/
cp src/sdk-version %{buildroot}%{_bindir}/

# sdk-chroot
cp src/mer-sdk-chroot %{buildroot}/
cp src/mer-bash-setup %{buildroot}/

# sdk-vm
mkdir -p %{buildroot}/%{_sysconfdir}/systemd/system
cp --no-dereference systemd/* %{buildroot}/%{_sysconfdir}/systemd/system/
cp src/sdk-info %{buildroot}%{_bindir}/

# sdk-sb2-config
mkdir -p %{buildroot}/usr/share/scratchbox2/modes/
cp -ar modes/* %{buildroot}/usr/share/scratchbox2/modes/

# sdk-utils
cp src/mb %{buildroot}%{_bindir}/
cp src/qb %{buildroot}%{_bindir}/
cp src/sdk-manage %{buildroot}%{_bindir}/

# << install pre

# >> install post
# << install post


%pre
# >> pre
%pre -n sdk-chroot
if ! rpm --quiet -q ca-certificates && [ -d /etc/ssl/certs ] ; then echo "Cleaning up copied ssl certs. ca-certificates should now install"; rm -rf /etc/ssl/certs ;fi

# << pre

%post
# >> post
%post -n sdk-vm
# Enable the information.service
/bin/ln -s %{_sysconfdir}/systemd/system/information.service %{_sysconfdir}/systemd/system/multi-user.target.wants/
# << post

%files -n sdk-chroot
%defattr(-,root,root,-)
/mer-sdk-chroot
/mer-bash-setup
%{_bindir}/sdk-version
# >> files sdk-chroot
# << files sdk-chroot

%files -n sdk-vm
%defattr(-,root,root,-)
%{_bindir}/sdk-version
%{_bindir}/sdk-info
%{_sysconfdir}/systemd/system/information.service
%{_sysconfdir}/systemd/system/default.target
# >> files sdk-vm
# << files sdk-vm

%files -n sdk-sb2-config
%defattr(-,root,root,-)
%{_datadir}/scratchbox2/modes/*
# >> files sdk-sb2-config
# << files sdk-sb2-config

%files -n sdk-utils
%defattr(-,root,root,-)
%{_bindir}/mb
%{_bindir}/qb
%{_bindir}/sdk-manage
# >> files sdk-utils
# << files sdk-utils
