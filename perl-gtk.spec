#
# TODO: GtkHTML, Bonobo and Mozilla (don't build now - need fixes or API update)
#
# Conditional build:
# _with_gtkhtml		- with Gtk::HTML module (gtkhtml library)
# _without_applets	- without Gnome::Applet module (gnome-applets libraries) [not done yet]
# _without_gdkimlib	- without Gtk::Gdk::ImlibImage module (imlib library)
# _without_gdkpixbuf	- without Gtk::Gdk::Pixbuf module (gdk-pixbuf library)
# _without_glade	- without Gtk::GladeXML module (libglade library)
# _without_gnome	- without Gnome module (gnome-libs)
# _without_gnomeprint	- without Gnome::Print module (gnome-print library)
# _without_gtkglarea	- without Gtk::GLArea module (gtkglarea library)
# _without_gtkxmhtml	- without Gtk::XmHTML module (gtkxmhtml library)
#
%{?_without_gnome:%define	_without_applets	1}
%{?_without_gnome:%define	_without_gnomeprint	1}
# because libgtkxmhtml is not separated from gnome-libs...:
%{?_without_gnome:%define	_without_gtkxmhtml	1}
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk
%define		pnam	Perl
Summary:	Perl extensions for Gtk+ (the Gimp ToolKit)
Summary(cs):	Roz���en� Perlu pro Gtk+ (Gimp ToolKit)
Summary(da):	Perl udvidelser for Gtk+
Summary(de):	Perl-Erweiterungen f�r Gtk+ (das Gimp ToolKit)
Summary(es):	Extensiones Perl para Gtk+
Summary(fr):	Extensions Perl pour Gtk+ (l'ensemble d'outils GIMP)
Summary(it):	Estensioni Perl per Gtk+ (Gimp Toolkit)
Summary(ja):	Gtk+ (the Gimp ToolKit) �Ѥ� Perl ��ĥ
Summary(no):	Perlmodul for Gtk+
Summary(pl):	Rozszerzenie Perl dla Gtk+
Summary(pt):	Uma extens�o de Perl para o Gtk+ (Gimp Toolkit)
Summary(pt_BR):	Extens�es Perl para o Gtk+
Summary(ru):	����������� ������ Perl ��� Gtk+ (Gimp Toolkit)
Summary(sl):	Perlovske raz�iritve za Gtk+ (Gimp ToolKit)
Summary(sv):	Perl-utvidgning f�r Gtk+ (the Gimp ToolKit)
Name:		perl-gtk
Version:	0.7008
Release:	14
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-fix.patch
Patch1:		%{name}-gtkgl.patch
URL:		http://www.gtkperl.org/
%{!?_without_gdkpixbuf:BuildRequires:	gdk-pixbuf-devel}
%{!?_without_applets:BuildRequires:	gnome-core-devel}
%{!?_without_applets:BuildRequires:	control-center-devel}
%{!?_without_gnome:BuildRequires:	gnome-libs-devel}
%{!?_without_gnomeprint:BuildRequires:	gnome-print-devel}
BuildRequires:	gtk+-devel
%{!?_without_gtkglarea:BuildRequires:	gtkglarea-devel}
%{?_with_gtkhtml:BuildRequires:		gtkhtml-devel}
%{!?_without_gdkimlib:BuildRequires:	imlib-devel}
%{!?_without_glade:BuildRequires:	libglade-devel}
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Writer
BuildRequires:	perl-devel >= 5.005_03-10
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Gtk-perl

%description
This package includes Perl extensions for Gtk+ (the Gimp ToolKit), a
library used for creating graphical user interfaces for the X Window
System. The extensions provided in this package allow you to write
graphical interfaces using Perl and Gtk+. If you install this package,
you'll need to also have Perl and Gtk+ installed.

%description -l cs
Bal��ek obsahuje roz���en� Perlu o Gtk+ (Gimp ToolKit), kter� umo��uje
vytv��et grafick� u�ivatelsk� rozhran� pro prost�ed� X Window System.
Bal��ek pot�ebuje pro svou funkci Perl a Gtk+.

%description -l da
Denne pakke indeholder perl-moduler for Gtk+, et bibliotek som bruges
for at lave grafiske gr�nseflade for X. Modulerne i denne pakke g�r
det mulig at lave grafiske programmer ved hj�lp af perl og Gtk+. For
at kunne installere denne pakke skal b�de perl og Gtk+ v�re
installeret.

%description -l de
Dieses Paket enth�lt Perl-Erweiterungen f�r Gtk+ (das Gimp-ToolKit),
eine Bibliothek, die f�r die Erzeugung von grafischen
Benutzeroberfl�chen f�r das X Window-System verwendet wird. Die in
diesem Paket enthaltenen Erweiterungen erm�glichen es Ihnen, grafische
Schnittstellen mithilfe von Perl und Gtk+ zu schreiben. Wenn Sie
dieses Paket installieren, m�ssen auch Perl und Gtk+ installiert sein.

%description -l es
Este paquete incluye las extensiones de Perl para Gtk+ (El Kit de
herramientas de Gimp), una biblioteca usada para crear interfaces
gr�ficos de usuario para el Sistema X Window. Las extensiones
proporcionadas en este paquete le permiten escribir interfaces
gr�ficos usando Perl y Gtk+. Si instala este paquete, necesitar� tener
instalados tambi�n Perl y Gtk+.

%description -l fr
Ce paquetage contient des extensions Perl pour Gtk+ (ensemble d'outils
GIMP), une biblioth�que utilis�e pour cr�er des interfaces utilisateur
graphiques pour le syst�me X Window. Les extensions fournies dans ce
paquetage vous permettent de cr�er des interfaces graphiques � l'aide
de Perl et Gtk+. Si vous installez ce paquetage, vous devrez aussi
installer Perl et Gtk+.

%description -l it
Questo pacchetto include le estensioni Perl per Gtk+ (Gimp Toolkit);
una libreria utilizzata per creare interfaccia utente grafiche per il
Sistema X Window. L'estensione fornita in questo pacchetto vi consente
di creare interfacce grafiche usando Perl e Gtk+. Con questo
pacchetto; sara necessario installare anche Perl e Gtk+.

%description -l ja
���Υѥå������ˤϡ�Gtk+ (Gimp ToolKit) �Ѥ� Perl �������ƥ󥷥�� X
Window System �ѤΥ���ե�����桼�������󥿡��ե�������������뤿���
���Ѥ����饤�֥�꤬�ޤޤ�Ƥ��ޤ������Υѥå����������äƤ���
�������ƥ󥷥��ˤ�äơ�Perl �� Gtk+
��Ȥäƥ���ե����륤�󥿡��ե�����
��������뤳�Ȥ��Ǥ��ޤ������Υѥå������򥤥󥹥ȡ��뤹����ϡ�
Perl �� Gtk+ �⥤�󥹥ȡ��뤷�ʤ���Фʤ�ޤ���

%description -l no
Denne pakken inneholder perl-moduler for Gtk+, et bibliotek som brukes
for � lage grafiske grensesnitt for X. Modulene i denne pakken gj�r
det mulig � lage grafiske programmer ved hjelp av perl og Gtk+. For �
kunne installere denne pakken m� b�de perl og Gtk+ v�re installert.

%description -l pl
Gtk+-perl pozwoli ci na pisanie interfejsu graficznego przy u�yciu
perl'a i gtk.

%description -l pt_BR
Este pacote cont�m extens�es Perl para o Gtk+.

%description -l sv
Detta paket inneh�ller Perlutvidgningar f�r Gtk+ (verktygsl�dan Gimp),
ett bibliotek anv�nt f�r att skapa grafiska anv�ndargr�nssnitt f�r X.
Utvidgningen som tillhandah�lls i detta paket l�ter dig skapa grafiska
gr�nssnitt med Perl och Gtk+. Om du installerar detta paket beh�ver du
�ven ha Perl och Gtk+ installerade.

%package Gdk-ImlibImage
Summary:	Imlib support for perl-gtk
Summary(pl):	Obs�uga Imlib dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Gdk-ImlibImage
Gtk::Gdk::ImlibImage module - Imlib library support for perl-gtk.

%description Gdk-ImlibImage -l pl
Modu� Gtk::Gdk::ImlibImage - obs�uga biblioteki Imlib dla perl-gtk.

%package Gdk-Pixbuf
Summary:	Gdk-Pixbuf support for perl-gtk
Summary(pl):	Obs�uga Gdk-Pixbuf dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description Gdk-Pixbuf
Gtk::Gdk::Pixbuf module - Gdk-Pixbuf library support for perl-gtk.

%description Gdk-Pixbuf -l pl
Modu� Gtk::Gdk::Pixbuf - obs�uga biblioteki Gdk-Pixbuf dla perl-gtk.

%package GLArea
Summary:	Gtk-GLArea support for perl-gtk
Summary(pl):	Obs�uga Gtk-GLArea dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description GLArea
Gtk::GLArea module - Gtk-GLArea library support for perl-gtk.

%description GLArea -l pl
Modu� Gtk::GLArea - obs�uga biblioteki Gtk-GLArea dla perl-gtk.

%package GladeXML
Summary:	libglade support for perl-gtk
Summary(pl):	Obs�uga libglade dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description GladeXML
Gtk::GladeXML module - libglade library support for perl-gtk.

%description GladeXML -l pl
Modu� Gtk::GladeXML - obs�uga biblioteki libglade dla perl-gtk.

%package XmHTML
Summary:	XmHTML support for perl-gtk
Summary(pl):	Obs�uga XmHTML dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description XmHTML
Gtk::XmHTML module - gtkxmhtml library support for perl-gtk.

%description XmHTML -l pl
Modu� Gtk::XmHTML - obs�uga biblioteki gtkxmhtml dla perl-gtk.

%package HTML
Summary:	gtkhtml support for perl-gtk
Summary(pl):	Obs�uga gtkhtml dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}

%description HTML
Gtk::HTML module - gtkhtml library support for perl-gtk.

%description HTML -l pl
Modu� Gtk::HTML - obs�uga biblioteki gtkhtml dla perl-gtk.

%package -n perl-gnome
Summary:	Perl extensions for Gnome
Summary(cs):	Roz���en� Perlu pro Gnome
Summary(da):	Perl udvidelser for Gnome
Summary(de):	Perl-Erweiterungen f�r Gnome
Summary(es):	Extensiones Perl para Gnome
Summary(fr):	Extensions Perl pour Gnome
Summary(it):	Estensioni Perl per Gnome
Summary(ja):	Gnome �Ѥ� Perl ��ĥ
Summary(no):	Perlmodul for Gnome
Summary(pl):	Rozszerzenie Perl dla Gnome
Summary(pt):	Uma extens�o de Perl para o Gnome
Summary(pt_BR):	Extens�es Perl para o Gnome
Summary(ru):	����������� ������ Perl ��� Gnome
Summary(sl):	Perlovske raz�iritve za Gnome
Summary(sv):	Perl-utvidgning f�r Gnome
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}
Requires:	%{name}-Gdk-ImlibImage = %{version}

%description -n perl-gnome
This package includes Perl extensions for Gnome.

%description -n perl-gnome -l pl
Ten pakiet zawiera rozszerzenia perla dla Gnome.

%package -n perl-gnome-Print
Summary:	Perl extensions for GnomePrint
Summary(cs):	Roz���en� Perlu pro GnomePrint
Summary(da):	Perl udvidelser for GnomePrint
Summary(de):	Perl-Erweiterungen f�r GnomePrint
Summary(es):	Extensiones Perl para GnomePrint
Summary(fr):	Extensions Perl pour GnomePrint
Summary(it):	Estensioni Perl per GnomePrint
Summary(ja):	GnomePrint �Ѥ� Perl ��ĥ
Summary(no):	Perlmodul for GnomePrint
Summary(pl):	Rozszerzenie Perl dla GnomePrint
Summary(pt):	Uma extens�o de Perl para o GnomePrint
Summary(pt_BR):	Extens�es Perl para o GnomePrint
Summary(ru):	����������� ������ Perl ��� GnomePrint
Summary(sl):	Perlovske raz�iritve za GnomePrint
Summary(sv):	Perl-utvidgning f�r GnomePrint
Group:		Development/Languages/Perl
Requires:	perl-gnome = %{version}
Requires:	%{name}-Gdk-Pixbuf = %{version}

%description -n perl-gnome-Print
This package includes Perl extensions for GnomePrint.

%description -n perl-gnome-Print -l pl
Ten pakiet zawiera rozszerzenia perla dla GnomePrint.

%package -n perl-gnome-Applet
Summary:	applets support for perl-gnome
Summary(pl):	Obs�uga aplet�w dla perl-gnome
Group:		Development/Languages/Perl
Requires:	perl-gnome = %{version}

%description -n perl-gnome-Applet
Gnome::Applet module - applets support for perl-gnome.

%description -n perl-gnome-Applet -l pl
Modu� Gnome::Applet - obs�uga aplet�w dla perl-gnome.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__perl} Makefile.PL \
	--without-guessing \
%{?_without_gdkpixbuf:	--without-gdkpixbuf}	%{!?_without_gdkpixbuf:	--with-gdkpixbuf-force} \
%{?_without_gdkimlib:	--without-gdkimlib}	%{!?_without_gdkimlib:	--with-gdkimlib-force} \
%{?_without_glade:	--without-glade}	%{!?_without_glade:	--with-glade-force} \
%{?_without_gnome:	--without-gnome}	%{!?_without_gnome:	--with-gnome-force} \
%{?_without_gnomeprint:	--without-gnomeprint}	%{!?_without_gnomeprint:--with-gnomeprint-force} \
%{?_without_gtkglarea:	--without-gtkglarea}	%{!?_without_gtkglarea:	--with-gtkglarea-force} \
%{!?_with_gtkhtml:	--without-gtkhtml}	%{?_with_gtkhtml:	--with-gtkhtml-force} \
%{?_without_gtkxmhtml:	--without-gtkxmhtml}	%{!?_without_gtkxmhtml:	--with-gtkxmhtml-force} \
%{?_without_applets:	--without-applets}	%{!?_without_gnome:	--with-applets-force}

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
%{perl_sitearch}/Gtk.pm
%dir %{perl_sitearch}/Gtk
%{perl_sitearch}/Gtk/[ACIKLTil]*
%{perl_sitearch}/Gtk/Gdk.pm
%dir %{perl_sitearch}/Gtk/Gdk
%dir %{perl_sitearch}/auto/Gtk
%{perl_sitearch}/auto/Gtk/Gtk.bs
%{perl_sitearch}/auto/Gtk/autosplit.ix
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gtk.so
%dir %{perl_sitearch}/auto/Gtk/Gdk
%{perl_sitearch}/auto/Gtk/Gdk/autosplit.ix
%{_mandir}/man3/Gtk.3pm*
%{_mandir}/man3/Gtk::[Ca-z]*.3pm*

%if %{?_without_gdkimlib:0}%{!?_without_gdkimlib:1}
%files Gdk-ImlibImage
%defattr(644,root,root,755)
%{perl_sitearch}/Gtk/Gdk/ImlibImage.pm
%{perl_sitearch}/Gtk/Gdk/ImlibImage
%dir %{perl_sitearch}/auto/Gtk/Gdk/ImlibImage
%{perl_sitearch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.so
%{_mandir}/man3/Gtk::Gdk::ImlibImage*
%endif

%if %{?_without_gdkpixbuf:0}%{!?_without_gdkpixbuf:1}
%files Gdk-Pixbuf
%defattr(644,root,root,755)
%{perl_sitearch}/Gtk/Gdk/Pixbuf.pm
%{perl_sitearch}/Gtk/Gdk/Pixbuf
%dir %{perl_sitearch}/auto/Gtk/Gdk/Pixbuf
%{perl_sitearch}/auto/Gtk/Gdk/Pixbuf/Pixbuf.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gdk/Pixbuf/Pixbuf.so
%{_mandir}/man3/Gtk::Gdk::Pixbuf*
%endif

%if %{?_without_gtkglarea:0}%{!?_without_gtkglarea:1}
%files GLArea
%defattr(644,root,root,755)
%{perl_sitearch}/Gtk/GLArea.pm
%{perl_sitearch}/Gtk/GLArea
%dir %{perl_sitearch}/auto/Gtk/GLArea
%{perl_sitearch}/auto/Gtk/GLArea/GLArea.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/GLArea/GLArea.so
%dir %{perl_sitearch}/auto/Gtk/GLArea/Constants
%{perl_sitearch}/auto/Gtk/GLArea/Constants/autosplit.ix
%endif

%if %{?_without_glade:0}%{!?_without_glade:1}
%files GladeXML
%defattr(644,root,root,755)
%{perl_sitearch}/Gtk/GladeXML.pm
%{perl_sitearch}/Gtk/GladeXML
%dir %{perl_sitearch}/auto/Gtk/GladeXML
%{perl_sitearch}/auto/Gtk/GladeXML/autosplit.ix
%{perl_sitearch}/auto/Gtk/GladeXML/GladeXML.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/GladeXML/GladeXML.so
%{_mandir}/man3/Gtk::GladeXML*
%endif

%if %{?_without_gtkxmhtml:0}%{!?_without_gtkxmhtml:1}
%files XmHTML
%defattr(644,root,root,755)
%{perl_sitearch}/Gtk/XmHTML.pm
%{perl_sitearch}/Gtk/XmHTML
%dir %{perl_sitearch}/auto/Gtk/XmHTML
%{perl_sitearch}/auto/Gtk/XmHTML/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/XmHTML/*.so
%endif

%if %{?_with_gtkhtml:1}%{!?_with_gtkhtml:0}
%files HTML
%defattr(644,root,root,755)
%{perl_sitearch}/Gtk/HTML.pm
%{perl_sitearch}/Gtk/HTML
%dir %{perl_sitearch}/auto/Gtk/HTML
%{perl_sitearch}/auto/Gtk/HTML/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/HTML/*.so
%endif

%if %{?_without_gnome:0}%{!?_without_gnome:1}
%files -n perl-gnome
%defattr(644,root,root,755)
%{perl_sitearch}/Gnome.pm
%dir %{perl_sitearch}/Gnome
%{perl_sitearch}/Gnome/[IT]*
%dir %{perl_sitearch}/auto/Gnome
%{perl_sitearch}/auto/Gnome/Gnome.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gnome/Gnome.so
%{_mandir}/man3/Gnome.3pm*
%{_mandir}/man3/Gnome::reference.3pm*
%endif

%if %{?_without_gnomeprint:0}%{!?_without_gnomeprint:1}
%files -n perl-gnome-Print
%defattr(644,root,root,755)
%{perl_sitearch}/Gnome/Print.pm
%{perl_sitearch}/Gnome/Print
%dir %{perl_sitearch}/auto/Gnome/Print
%{perl_sitearch}/auto/Gnome/Print/Print.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gnome/Print/Print.so
%{_mandir}/man3/Gnome::Print*
%endif

%if %{?_without_applets:0}%{!?_without_applets:1}
%files -n perl-gnome-Applet
%defattr(644,root,root,755)
%{perl_sitearch}/Gnome/Applet.pm
%{perl_sitearch}/Gnome/Applet
%dir %{perl_sitearch}/auto/Gnome/Applet
%{perl_sitearch}/auto/Gnome/Applet/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/Gnome/Applet/*.so
%{_mandir}/man3/Gnome::Applet*
%endif
