#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x70FE17F8A643E15B (lukasa@keybase.io)
#
Name     : brotlipy
Version  : 0.7.0
Release  : 18
URL      : https://files.pythonhosted.org/packages/d9/91/bc79b88590e4f662bd40a55a2b6beb0f15da4726732efec5aa5a3763d856/brotlipy-0.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/d9/91/bc79b88590e4f662bd40a55a2b6beb0f15da4726732efec5aa5a3763d856/brotlipy-0.7.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/d9/91/bc79b88590e4f662bd40a55a2b6beb0f15da4726732efec5aa5a3763d856/brotlipy-0.7.0.tar.gz.asc
Summary  : Python binding to the Brotli library
Group    : Development/Tools
License  : MIT
Requires: brotlipy-license = %{version}-%{release}
Requires: brotlipy-python = %{version}-%{release}
Requires: brotlipy-python3 = %{version}-%{release}
Requires: cffi
BuildRequires : buildreq-distutils3
BuildRequires : cffi

%description
========
        
        This library contains Python bindings for the reference Brotli encoder/decoder,
        `available here`_. This allows Python software to use the Brotli compression
        algorithm directly from Python code.

%package license
Summary: license components for the brotlipy package.
Group: Default

%description license
license components for the brotlipy package.


%package python
Summary: python components for the brotlipy package.
Group: Default
Requires: brotlipy-python3 = %{version}-%{release}

%description python
python components for the brotlipy package.


%package python3
Summary: python3 components for the brotlipy package.
Group: Default
Requires: python3-core
Provides: pypi(brotlipy)
Requires: pypi(cffi)

%description python3
python3 components for the brotlipy package.


%prep
%setup -q -n brotlipy-0.7.0
cd %{_builddir}/brotlipy-0.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603334872
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/brotlipy
cp %{_builddir}/brotlipy-0.7.0/LICENSE %{buildroot}/usr/share/package-licenses/brotlipy/bae61d713726c8dbf4b43a6bf0ddeb04e1f927cd
cp %{_builddir}/brotlipy-0.7.0/libbrotli/LICENSE %{buildroot}/usr/share/package-licenses/brotlipy/c045813a6c514f2d30d60a07c6aaf3603850e608
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/brotlipy/bae61d713726c8dbf4b43a6bf0ddeb04e1f927cd
/usr/share/package-licenses/brotlipy/c045813a6c514f2d30d60a07c6aaf3603850e608

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
