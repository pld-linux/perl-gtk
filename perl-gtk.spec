%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk
%define		pnam	Perl
#
# Conditional build:
# _with_gtkhtml
# _without_gdkimlib
# _without_gdkpixbuf
# _without_glade
# _without_gnome
# _without_gnomeprint
# _without_gtkglarea
# _without_gtkhtml
#
%{?_without_gnome:%define	_without_gnomeprint	1}
Summary:	Perl extensions for Gtk+ (the Gimp ToolKit)
Summary(cs):	Roz¹íøení Perlu pro Gtk+ (Gimp ToolKit)
Summary(da):	Perl udvidelser for Gtk+
Summary(de):	Perl-Erweiterungen für Gtk+ (das Gimp ToolKit)
Summary(es):	Extensiones Perl para Gtk+
Summary(fr):	Extensions Perl pour Gtk+ (l'ensemble d'outils GIMP)
Summary(it):	Estensioni Perl per Gtk+ (Gimp Toolkit)
Summary(ja):	Gtk+ (the Gimp ToolKit) ÍÑ¤Î Perl ³ÈÄ¥
Summary(no):	Perlmodul for Gtk+
Summary(pl):	Rozszerzenie Perl dla Gtk+
Summary(pt):	Uma extensão de Perl para o Gtk+ (Gimp Toolkit)
Summary(pt_BR):	Extensões Perl para o Gtk+
Summary(ru):	òÁÓÛÉÒÅÎÎÁÑ ×ÅÒÓÉÑ Perl ÄÌÑ Gtk+ (Gimp Toolkit)
Summary(sl):	Perlovske raz¹iritve za Gtk+ (Gimp ToolKit)
Summary(sv):	Perl-utvidgning för Gtk+ (the Gimp ToolKit)
Name:		perl-gtk
Version:	0.7008
Release:	10.3
License:	LGPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fix.patch
URL:		http://www.gtkperl.org/
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	gtk+-devel
%{!?_without_gnome:BuildRequires: gnome-libs-devel}
BuildRequires:	imlib-devel
%{!?_without_gdkimlib:BuildRequires: imlib-devel}
%{!?_without_gtkglarea:BuildRequires: gtkglarea-devel}
%{!?_without_gdkpixbuf:BuildRequires: gdk-pixbuf-devel}
%{?_with_gtkhtml:BuildRequires: gtkhtml-devel}
%{!?_without_gnomeprint:BuildRequires: gnome-print-devel}
%{!?_without_glade:BuildRequires: libglade-devel}
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Writer
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Gtk-perl

%define		_noautoreq "perl(Gtk::TypesLazy)" "perl(Gnome::TypesLazy)" "perl(Gtk::GLArea::Types)" "perl(Gtk::Gdk::Pixbuf::Types)" "perl(Gtk::GladeXML::Types)"

%description
This package includes Perl extensions for Gtk+ (the Gimp ToolKit), a
library used for creating graphical user interfaces for the X Window
System. The extensions provided in this package allow you to write
graphical interfaces using Perl and Gtk+. If you install this package,
you'll need to also have Perl and Gtk+ installed.

%description -l cs
Balíèek obsahuje roz¹íøení Perlu o Gtk+ (Gimp ToolKit), které umo¾òuje
vytváøet grafická u¾ivatelská rozhraní pro prostøedí X Window System.
Balíèek potøebuje pro svou funkci Perl a Gtk+.

%description -l da
Denne pakke indeholder perl-moduler for Gtk+, et bibliotek som bruges
for at lave grafiske grænseflade for X. Modulerne i denne pakke gør
det mulig at lave grafiske programmer ved hjælp af perl og Gtk+. For
at kunne installere denne pakke skal både perl og Gtk+ være
installeret.

%description -l de
Dieses Paket enthält Perl-Erweiterungen für Gtk+ (das Gimp-ToolKit),
eine Bibliothek, die für die Erzeugung von grafischen
Benutzeroberflächen für das X Window-System verwendet wird. Die in
diesem Paket enthaltenen Erweiterungen ermöglichen es Ihnen, grafische
Schnittstellen mithilfe von Perl und Gtk+ zu schreiben. Wenn Sie
dieses Paket installieren, müssen auch Perl und Gtk+ installiert sein.

%description -l es
Este paquete incluye las extensiones de Perl para Gtk+ (El Kit de
herramientas de Gimp), una biblioteca usada para crear interfaces
gráficos de usuario para el Sistema X Window. Las extensiones
proporcionadas en este paquete le permiten escribir interfaces
gráficos usando Perl y Gtk+. Si instala este paquete, necesitará tener
instalados también Perl y Gtk+.

%description -l fr
Ce paquetage contient des extensions Perl pour Gtk+ (ensemble d'outils
GIMP), une bibliothèque utilisée pour créer des interfaces utilisateur
graphiques pour le système X Window. Les extensions fournies dans ce
paquetage vous permettent de créer des interfaces graphiques à l'aide
de Perl et Gtk+. Si vous installez ce paquetage, vous devrez aussi
installer Perl et Gtk+.

%description -l it
Questo pacchetto include le estensioni Perl per Gtk+ (Gimp Toolkit);
una libreria utilizzata per creare interfaccia utente grafiche per il
Sistema X Window. L'estensione fornita in questo pacchetto vi consente
di creare interfacce grafiche usando Perl e Gtk+. Con questo
pacchetto; sara necessario installare anche Perl e Gtk+.

%description -l ja
¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤Ë¤Ï¡¢Gtk+ (Gimp ToolKit) ÍÑ¤Î Perl ¥¨¥¯¥¹¥Æ¥ó¥·¥ç¥ó¡¢ X
Window System ÍÑ¤Î¥°¥é¥Õ¥£¥«¥ë¥æ¡¼¥¶¡¼¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹¤òºîÀ®¤¹¤ë¤¿¤á¤Ë
»ÈÍÑ¤µ¤ì¤ë¥é¥¤¥Ö¥é¥ê¤¬´Þ¤Þ¤ì¤Æ¤¤¤Þ¤¹¡£¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ËÆþ¤Ã¤Æ¤¤¤ë
¥¨¥¯¥¹¥Æ¥ó¥·¥ç¥ó¤Ë¤è¤Ã¤Æ¡¢Perl ¤È Gtk+
¤ò»È¤Ã¤Æ¥°¥é¥Õ¥£¥«¥ë¥¤¥ó¥¿¡¼¥Õ¥§¥¤¥¹
¤òºîÀ®¤¹¤ë¤³¤È¤¬¤Ç¤­¤Þ¤¹¡£¤³¤Î¥Ñ¥Ã¥±¡¼¥¸¤ò¥¤¥ó¥¹¥È¡¼¥ë¤¹¤ë¾ì¹ç¤Ï¡¢
Perl ¤È Gtk+ ¤â¥¤¥ó¥¹¥È¡¼¥ë¤·¤Ê¤±¤ì¤Ð¤Ê¤ê¤Þ¤»¤ó¡£

%description -l no
Denne pakken inneholder perl-moduler for Gtk+, et bibliotek som brukes
for å lage grafiske grensesnitt for X. Modulene i denne pakken gjør
det mulig å lage grafiske programmer ved hjelp av perl og Gtk+. For å
kunne installere denne pakken må både perl og Gtk+ være installert.

%description -l pl
Gtk+-perl pozwoli ci na pisanie interfejsu graficznego przy u¿yciu
perl'a i gtk.

%description -l pt_BR
Este pacote contém extensões Perl para o Gtk+.

%description -l sv
Detta paket innehåller Perlutvidgningar för Gtk+ (verktygslådan Gimp),
ett bibliotek använt för att skapa grafiska användargränssnitt för X.
Utvidgningen som tillhandahålls i detta paket låter dig skapa grafiska
gränssnitt med Perl och Gtk+. Om du installerar detta paket behöver du
även ha Perl och Gtk+ installerade.

%package -n perl-gnome
Summary:	Perl extensions for Gnome
Summary(cs):	Roz¹íøení Perlu pro Gnome
Summary(da):	Perl udvidelser for Gnome
Summary(de):	Perl-Erweiterungen für Gnome
Summary(es):	Extensiones Perl para Gnome
Summary(fr):	Extensions Perl pour Gnome
Summary(it):	Estensioni Perl per Gnome
Summary(ja):	Gnome ÍÑ¤Î Perl ³ÈÄ¥
Summary(no):	Perlmodul for Gnome
Summary(pl):	Rozszerzenie Perl dla Gnome
Summary(pt):	Uma extensão de Perl para o Gnome
Summary(pt_BR):	Extensões Perl para o Gnome
Summary(ru):	òÁÓÛÉÒÅÎÎÁÑ ×ÅÒÓÉÑ Perl ÄÌÑ Gnome
Summary(sl):	Perlovske raz¹iritve za Gnome
Summary(sv):	Perl-utvidgning för Gnome
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
%{!?_without_gnomeprint:Provides:	perl(Gnome::Print::Types)}
%{!?_without_gnomeprint:Provides:	perl(Gnome::Print::TypesLazy)}

%description -n perl-gnome
This package includes Perl extensions for Gnome.

%description -n perl-gnome -l pl
Ten pakiet zawiera rozszerzenia perla dla Gnome.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
perl Makefile.PL \
	--without-guessing \
	%{?_without_gnome:--without-gnome}%{!?_without_gnome:--with-gnome-force} \
	%{?_without_gdkimlib:--without-gdkimlib}%{!?_without_gdkimlib:--with-gdkimlib-force} \
	%{?_without_gtkglarea:--without-gtkglarea}%{!?_without_gtkglarea:--with-gtkglarea-force} \
	%{?_without_gdkpixbuf:--without-gdkpixbuf}%{!?_without_gdkpixbuf:--with-gdkpixbuf-force} \
	%{?!_with_gtkhtml:--without-gtkhtml}%{?_with_gtkhtml:--with-gtkhtml-force} \
	%{?_without_gnomeprint:--without-gnomeprint}%{!?_without_gnomeprint:--with-gnomeprint-force} \
	%{?_without_glade:--without-glade}%{!?_without_glade:--with-glade-force}
	#%{?_without_gnome:--without-applets}%{!?_without_gnome:--with-applets-force} \

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_archlib}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitearch}/Gtk
%{perl_sitearch}/Gtk.pm
%dir %{perl_sitearch}/auto/Gtk
%dir %{perl_sitearch}/auto/Gtk/Gdk
%dir %{perl_sitearch}/auto/Gtk/Gdk/ImlibImage
%{perl_sitearch}/auto/Gtk/Gtk.bs
%{perl_sitearch}/auto/Gtk/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gtk.so
%{perl_sitearch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.bs
%{perl_sitearch}/auto/Gtk/Gdk/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.so
%{_mandir}/man3/Gtk*
#to GDK-Pixbuf subpackage ?
%dir %{perl_sitearch}/auto/Gtk/Gdk/Pixbuf
%{perl_sitearch}/auto/Gtk/Gdk/Pixbuf/Pixbuf.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gdk/Pixbuf/Pixbuf.so
#to GLArea subpackage ?
%dir %{perl_sitearch}/auto/Gtk/GLArea
%dir %{perl_sitearch}/auto/Gtk/GLArea/Constants
%{perl_sitearch}/auto/Gtk/GLArea/GLArea.bs
%dir %{perl_sitearch}/auto/Gtk/GLArea/Constants/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/GLArea/GLArea.so

%if %{?_without_gnome:0}%{!?_without_gnome:1}
%files -n perl-gnome
%defattr(644,root,root,755)
%{perl_sitearch}/Gnome
%{perl_sitearch}/Gnome.pm
%dir %{perl_sitearch}/auto/Gnome
%{perl_sitearch}/auto/Gnome/Gnome.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gnome/Gnome.so

%if %{?_without_gnomeprint:0}%{!?_without_gnomeprint:1}
%dir %{perl_sitearch}/auto/Gnome/Print
%{perl_sitearch}/auto/Gnome/Print/Print.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gnome/Print/Print.so
%endif

%{_mandir}/man3/Gnome*
# to GladeXML subpackage ?
%dir %{perl_sitearch}/auto/Gtk/GladeXML
%{perl_sitearch}/auto/Gtk/GladeXML/autosplit.ix
%{perl_sitearch}/auto/Gtk/GladeXML/GladeXML.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/GladeXML/GladeXML.so
%endif
