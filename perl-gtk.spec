#
# Conditional build:
# _without_gnome
#
%define		_noautoreq "perl(Gtk::TypesLazy)" "perl(Gnome::TypesLazy)"
%include	/usr/lib/rpm/macros.perl
Summary:	Perl extensions for Gtk+ (the Gimp ToolKit)
Summary(es):	Extensiones Perl para GTK+
Summary(pl):	Rozszerzenie Perl dla Gtk
Summary(pt_BR):	Extensões Perl para o GTK+
Name:		perl-gtk
Version:	0.7008
Release:	7
License:	LGPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Gtk/Gtk-Perl-%{version}.tar.gz
Patch0:		%{name}-fix.patch
URL:		http://www.gtkperl.org/
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	gtk+-devel
%{!?_without_gnome:BuildRequires: gnome-libs-devel}
BuildRequires:	imlib-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Writer
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Gtk-perl

%description
This package includes Perl extensions for Gtk+ (the Gimp ToolKit), a
library used for creating graphical user interfaces for the X Window
System. The extensions provided in this package allow you to write
graphical interfaces using Perl and Gtk+. If you install this package,
you'll need to also have Perl and Gtk+ installed.

%description -l es
Este paquete contiene extensiones Perl para GTK+.

%description -l pl
Gtk+-perl pozwoli ci na pisanie interfejsu graficznego przy u¿yciu
perl'a i gtk.

%description -l pt_BR
Este pacote contém extensões Perl para o GTK+.

%package -n perl-gnome
Summary:	Perl extensions for Gnome
Summary(pl):	Rozszerzenie Perl dla Gnome
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Requires:	%{name} = %{version}

%description -n perl-gnome
This package includes Perl extensions for Gnome.

%prep
%setup -q -n Gtk-Perl-%{version}
%patch0 -p1

%build
perl Makefile.PL \
	--without-guessing \
	--with-gdkimlib \
	%{?_without_gnome:--without-gnome}%{!?_without_gnome:--with-gnome}

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT 

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Gtk
%{perl_sitearch}/Gtk.pm
%dir %{perl_sitearch}/auto/Gtk
%dir %{perl_sitearch}/auto/Gtk/Gdk
%dir %{perl_sitearch}/auto/Gtk/Gdk/ImlibImage
%{perl_sitearch}/auto/Gtk/Gtk.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gtk.so
%{perl_sitearch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.so
%{_mandir}/man3/Gtk*

%if %{?_without_gnome:0}%{!?_without_gnome:1}
%files -n perl-gnome
%defattr(644,root,root,755)
%{perl_sitearch}/Gnome
%{perl_sitearch}/Gnome.pm
%dir %{perl_sitearch}/auto/Gnome
%{perl_sitearch}/auto/Gnome/Gnome.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gnome/Gnome.so
%{_mandir}/man3/Gnome*
%endif
