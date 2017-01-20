
%define		oname	wxWidgets
%define		api	3.0
%define		major	0

Summary:	GTK+ port of the wxWidgets library
Name:		wxgtk%{api}-gtk2
Version:	3.0.2
Release:	9
License:	wxWidgets Library Licence
Group:		System/Libraries
Url:		http://www.wxwidgets.org/
Source0:	http://prdownloads.sourceforge.net/wxwindows/%{oname}-%{version}.tar.bz2
Patch1:		gst1.0.patch
# abi check is useless as it reports different abi used between clang and gcc
# however clang just hard codes a def to an old abi version, its not actually
# a different abi
Patch2:		wxWidgets-3.0.2-disable_abi_check.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	pkgconfig(zlib)

%global wxversion %{version}-gtk2
%global wxrelease %(echo %{wxversion} |sed 's/\\([0-9]*\\.[0-9]*\\)\\.[0-9]*/\\1/')
%global wxrelease_nodot %(echo %{wxrelease} |sed 's/\\.//g')
%global wxsubversion %{version}.${wx_subrelease_number}-gtk2
%global mfl WX_RELEASE=%{wxrelease} WX_RELEASE_NODOT=%{wxrelease_nodot} WX_VERSION=%{wxversion}


%description
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

%files -f wxstd%{wxrelease_nodot}.lang
%doc *.txt

#----------------------------------------------------------------------------

%define libwx_baseu %mklibname wx_baseu %{wxrelease} %{major}

%package -n	%{libwx_baseu}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu}
%{_libdir}/libwx_baseu-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_baseu_net %mklibname wx_baseu_net %{wxrelease} %{major}

%package -n	%{libwx_baseu_net}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu_net}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu_net}
%{_libdir}/libwx_baseu_net-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_baseu_xml %mklibname wx_baseu_xml %{wxrelease} %{major}

%package -n	%{libwx_baseu_xml}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_baseu_xml}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_baseu_xml}
%{_libdir}/libwx_baseu_xml-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_adv %mklibname wx_gtk2u_adv %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_adv}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_adv}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_adv}
%{_libdir}/libwx_gtk2u_adv-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_aui %mklibname wx_gtk2u_aui %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_aui}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_aui}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_aui}
%{_libdir}/libwx_gtk2u_aui-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_core %mklibname wx_gtk2u_core %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_core}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_core}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_core}
%{_libdir}/libwx_gtk2u_core-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_gl %mklibname wx_gtk2u_gl %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_gl}
Summary:	OpenGL shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_gl}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_gl}
%{_libdir}/libwx_gtk2u_gl-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_html %mklibname wx_gtk2u_html %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_html}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_html}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_html}
%{_libdir}/libwx_gtk2u_html-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_media %mklibname wx_gtk2u_media %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_media}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_media}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_media}
%{_libdir}/libwx_gtk2u_media-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_propgrid %mklibname wx_gtk2u_propgrid %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_propgrid}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_propgrid}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_propgrid}
%{_libdir}/libwx_gtk2u_propgrid-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_qa %mklibname wx_gtk2u_qa %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_qa}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_qa}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_qa}
%{_libdir}/libwx_gtk2u_qa-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_ribbon %mklibname wx_gtk2u_ribbon %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_ribbon}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_ribbon}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_ribbon}
%{_libdir}/libwx_gtk2u_ribbon-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_richtext %mklibname wx_gtk2u_richtext %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_richtext}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_richtext}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_richtext}
%{_libdir}/libwx_gtk2u_richtext-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_stc %mklibname wx_gtk2u_stc %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_stc}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_stc}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_stc}
%{_libdir}/libwx_gtk2u_stc-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libwx_gtk2u_xrc %mklibname wx_gtk2u_xrc %{wxrelease} %{major}

%package -n	%{libwx_gtk2u_xrc}
Summary:	Shared library of wxGTK - Unicode enabled
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libwx_gtk2u_xrc}
wxWidgets is a free C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif/LessTif, MS Windows, Mac) from the same source code.

This package contains the library needed to run programs dynamically
linked with the unicode enabled version of %{name}.

%files -n %{libwx_gtk2u_xrc}
%{_libdir}/libwx_gtk2u_xrc-%{wxrelease}.so.%{major}*

#----------------------------------------------------------------------------

%define libnameudev %mklibname -d wxgtku %{api}-gtk2

%package -n	%{libnameudev}
Summary:	Header files and development documentation for wxGTK - unicode
Group:		Development/C++
Requires:	%{libwx_baseu} = %{EVRD}
Requires:	%{libwx_baseu_net} = %{EVRD}
Requires:	%{libwx_baseu_xml} = %{EVRD}
Requires:	%{libwx_gtk2u_adv} = %{EVRD}
Requires:	%{libwx_gtk2u_aui} = %{EVRD}
Requires:	%{libwx_gtk2u_core} = %{EVRD}
Requires:	%{libwx_gtk2u_gl} = %{EVRD}
Requires:	%{libwx_gtk2u_html} = %{EVRD}
Requires:	%{libwx_gtk2u_media} = %{EVRD}
Requires:	%{libwx_gtk2u_propgrid} = %{EVRD}
Requires:	%{libwx_gtk2u_qa} = %{EVRD}
Requires:	%{libwx_gtk2u_ribbon} = %{EVRD}
Requires:	%{libwx_gtk2u_richtext} = %{EVRD}
Requires:	%{libwx_gtk2u_stc} = %{EVRD}
Requires:	%{libwx_gtk2u_xrc} = %{EVRD}
Provides:	wxgtku%{api}-gtk2-devel = %{EVRD}
# At this time 2.8 and 3.0 cannot co-exist because of file conflicts
Conflicts:	%{_lib}wxgtku2.8-devel

%description -n %{libnameudev}
Header files for the unicode enabled version of wxGTK, the GTK+ port of
the wxWidgets library.

%files -n %{libnameudev}
%doc samples/
%doc docs/
%doc demos/
%{_bindir}/wx-config-%{wxrelease}
%{_bindir}/wxrc-%{wxrelease}
%{_includedir}/wx-%{wxrelease}/
%{_datadir}/aclocal/*
%{_datadir}/bakefile/
%{_libdir}/wx/config/gtk2-unicode-%{wxrelease}
%{_libdir}/wx/include/gtk2-unicode-%{wxrelease}/wx/setup.h
%{_libdir}/libwx_baseu-%{wxrelease}.so
%{_libdir}/libwx_baseu_net-%{wxrelease}.so
%{_libdir}/libwx_baseu_xml-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_adv-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_aui-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_core-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_gl-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_html-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_media-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_propgrid-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_qa-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_ribbon-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_richtext-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_stc-%{wxrelease}.so
%{_libdir}/libwx_gtk2u_xrc-%{wxrelease}.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%apply_patches

sh autogen.sh
#autoreconf -fiv -I `pwd`/build/aclocal
# fix plugin dir for 64-bit
sed -i -e 's|/lib|/%{_lib}|' src/unix/stdpaths.cpp

# patch some installed files to avoid conflicts with 2.8.*/3.0 gtk3
sed -i -e 's|aclocal)|aclocal/wxwin%{wxrelease_nodot}.m4)|' Makefile.in
sed -i -e 's|wxstd.mo|wxstd%{wxrelease_nodot}.mo|' Makefile.in
sed -i -e 's|wxmsw.mo|wxmsw%{wxrelease_nodot}.mo|' Makefile.in


sed 's/WX_RELEASE=.*/WX_RELEASE=%{wxrelease}/' -i configure
sed 's/WX_VERSION=.*/WX_VERSION=%{wxversion}/' -i configure
sed 's/WX_SUBVERSION=.*/WX_SUBVERSION=%{wxsubversion}/' -i configure
sed "s/WX_VERSION_TAG=.*/WX_VERSION_TAG=`echo WX\${lib_unicode_suffix}\${WX_LIB_FLAVOUR}_%(echo %{wxrelease} |sed 's/-.*//') | tr '[[a-z]]' '[[A-Z]]'`/" -i configure

%build
#gw 2.8.11 doesn't build otherwise:
%define _disable_ld_no_undefined 1
%define _disable_rebuild_configure 1
%define Werror_cflags %nil
# --disable-optimise prevents our $RPM_OPT_FLAGS being overridden
# (see OPTIMISE in configure).
# this code dereferences type-punned pointers like there's no tomorrow.
CFLAGS="%{optflags} -fno-strict-aliasing"
CXXFLAGS="%{optflags} -fno-strict-aliasing"

%configure --enable-unicode \
	--enable-compat28 \
	--without-odbc \
	--with-opengl \
	--with-gtk=2  \
	--without-debug_flag \
	--without-debug_info \
	--with-sdl \
	--with-libpng=sys \
	--with-libjpeg=sys \
	--with-libtiff=sys \
	--with-zlib=sys \
	--disable-optimise \
	--enable-calendar \
	--enable-intl \
	--enable-wave \
	--enable-fraction \
	--enable-wxprintfv \
	--enable-xresources \
	--enable-controls \
	--enable-tabdialog \
	--enable-msgdlg \
	--enable-dirdlg \
	--enable-numberdlg \
	--enable-splash \
	--enable-textdlg \
	--enable-graphics_ctx \
	--enable-grid \
	--disable-catch_segvs \
	--enable-mediactrl \
	--disable-webview \
	--enable-dataviewctrl

%make %mfl

%install
%makeinstall_std %mfl
%find_lang wxstd%{wxrelease_nodot}
%find_lang wxmsw%{wxrelease_nodot}

cat wxmsw%{wxrelease_nodot}.lang >> wxstd%{wxrelease_nodot}.lang

##Remove installed
mv %{buildroot}%{_bindir}/wx-config %{buildroot}/%{_bindir}/wx-config-%wxrelease
rm %{buildroot}%{_bindir}/wxrc
