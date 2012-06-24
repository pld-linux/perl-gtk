#
# TODO: GtkHTML, Bonobo and Mozilla (don't build now - need fixes or API update)
#
%{?_without_gnomeall:%global	_without_gnome		1}
%{?_without_gnomeall:%global	_without_gtkxmhtml	1}
%{?_without_gnome:%global	_without_applets	1}
%{?_without_gnome:%global	_without_gnomeprint	1}
#
# Conditional build:
%bcond_with	tests		# perform "make test" (require valid DISPLAY)
%bcond_with	gtkhtml		# build Gtk::HTML module (gtkhtml library)
%bcond_with	applets		# build Gnome::Applet module (gnome-applets libs) [NFY]
%bcond_without	gdkimlib	# don't build Gtk::Gdk::ImlibImage module (imlib library)
%bcond_without	gdk_pixbuf	# don't build Gtk::Gdk::Pixbuf module (gdk-pixbuf library)
%bcond_without	glade		# don't build Gtk::GladeXML module (libglade library)
%bcond_without	gnome		# don't build Gnome module (and other requiring gnome-libs)
%bcond_without	gnomeall	# as above, including Gtk::XmHTML (gtkxmhtml GNOME1 component)
%bcond_without	gnomeprint	# don't build Gnome::Print module (gnome-print library)
%bcond_without	gtkglarea	# don't build Gtk::GLArea module (gtkglarea library)
%bcond_without	gtkxmhtml	# don't build Gtk::XmHTML module (gtkxmhtml library)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Gtk
%define		pnam	Perl
Summary:	Perl extensions for GTK+ (the Gimp ToolKit)
Summary(cs):	Roz���en� Perlu pro GTK+ (Gimp ToolKit)
Summary(da):	Perl udvidelser for GTK+
Summary(de):	Perl-Erweiterungen f�r GTK+ (das Gimp ToolKit)
Summary(es):	Extensiones Perl para GTK+
Summary(fr):	Extensions Perl pour GTK+ (l'ensemble d'outils GIMP)
Summary(it):	Estensioni Perl per GTK+ (Gimp Toolkit)
Summary(ja):	GTK+ (the Gimp ToolKit) �Ѥ� Perl ��ĥ
Summary(nb):	Perlmodul for GTk+
Summary(pl):	Rozszerzenie Perla dla GTK+
Summary(pt):	Uma extens�o de Perl para o GTK+ (Gimp Toolkit)
Summary(pt_BR):	Extens�es Perl para o GTK+
Summary(ru):	����������� ������ Perl ��� GTK+ (Gimp Toolkit)
Summary(sl):	Perlovske raz�iritve za GTK+ (Gimp ToolKit)
Summary(sv):	Perl-utvidgning f�r GTK+ (the Gimp ToolKit)
Name:		perl-gtk
Version:	0.7009
Release:	2
# same as perl or LGPL
License:	LGPL or GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	72ce462caa1afe57d60a8e654d63204b
Patch0:		%{name}-fix.patch
Patch1:		%{name}-gtkgl.patch
Patch2:		%{name}-inc.patch
URL:		http://www.gtkperl.org/
%{?with_applets:BuildRequires:	control-center-devel < 1.99}
%{?with_gdk_pixbuf:BuildRequires:	gdk-pixbuf-devel}
%{?with_applets:BuildRequires:	gnome-core-devel}
%{?with_gnome:BuildRequires:	gnome-libs-devel}
%{?with_gnomeprint:BuildRequires:	gnome-print-devel}
BuildRequires:	gtk+-devel >= 1.2.0
%{?with_gtkglarea:BuildRequires:	gtkglarea1-devel < 1.99}
%{?with_gtkhtml:BuildRequires:		gtkhtml-devel}
%{?with_gtkxmhtml:BuildRequires:	gtkxmhtml-devel}
%{?with_gdkimlib:BuildRequires:	imlib-devel}
%{?with_glade:BuildRequires:	libglade-devel < 1:1.99}
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Writer
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	Gtk-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes Perl extensions for GTK+ (the Gimp ToolKit), a
library used for creating graphical user interfaces for the X Window
System. The extensions provided in this package allow you to write
graphical interfaces using Perl and GTK+. If you install this package,
you'll need to also have Perl and GTK+ installed.

%description -l cs
Bal��ek obsahuje roz���en� Perlu o GTK+ (Gimp ToolKit), kter� umo��uje
vytv��et grafick� u�ivatelsk� rozhran� pro prost�ed� X Window System.
Bal��ek pot�ebuje pro svou funkci Perl a GTK+.

%description -l da
Denne pakke indeholder Perl-moduler for GTK+, et bibliotek som bruges
for at lave grafiske gr�nseflade for X. Modulerne i denne pakke g�r
det mulig at lave grafiske programmer ved hj�lp af Perl og GTK+. For
at kunne installere denne pakke skal b�de Perl og GTK+ v�re
installeret.

%description -l de
Dieses Paket enth�lt Perl-Erweiterungen f�r GTK+ (das Gimp-ToolKit),
eine Bibliothek, die f�r die Erzeugung von grafischen
Benutzeroberfl�chen f�r das X Window-System verwendet wird. Die in
diesem Paket enthaltenen Erweiterungen erm�glichen es Ihnen, grafische
Schnittstellen mithilfe von Perl und GTK+ zu schreiben. Wenn Sie
dieses Paket installieren, m�ssen auch Perl und GTK+ installiert sein.

%description -l es
Este paquete incluye las extensiones de Perl para GTK+ (El Kit de
herramientas de Gimp), una biblioteca usada para crear interfaces
gr�ficos de usuario para el Sistema X Window. Las extensiones
proporcionadas en este paquete le permiten escribir interfaces
gr�ficos usando Perl y GTK+. Si instala este paquete, necesitar� tener
instalados tambi�n Perl y GTK+.

%description -l fr
Ce paquetage contient des extensions Perl pour GTK+ (ensemble d'outils
GIMP), une biblioth�que utilis�e pour cr�er des interfaces utilisateur
graphiques pour le syst�me X Window. Les extensions fournies dans ce
paquetage vous permettent de cr�er des interfaces graphiques � l'aide
de Perl et GTK+. Si vous installez ce paquetage, vous devrez aussi
installer Perl et GTK+.

%description -l it
Questo pacchetto include le estensioni Perl per GTK+ (Gimp Toolkit);
una libreria utilizzata per creare interfaccia utente grafiche per il
Sistema X Window. L'estensione fornita in questo pacchetto vi consente
di creare interfacce grafiche usando Perl e GTK+. Con questo
pacchetto; sara necessario installare anche Perl e GTK+.

%description -l ja
���Υѥå������ˤϡ�GTK+ (Gimp ToolKit) �Ѥ� Perl �������ƥ󥷥�� X
Window System �ѤΥ���ե�����桼�������󥿡��ե�������������뤿���
���Ѥ����饤�֥�꤬�ޤޤ�Ƥ��ޤ������Υѥå����������äƤ���
�������ƥ󥷥��ˤ�äơ�Perl �� GTK+
��Ȥäƥ���ե����륤�󥿡��ե�����
��������뤳�Ȥ��Ǥ��ޤ������Υѥå������򥤥󥹥ȡ��뤹����ϡ�
Perl �� GTK+ �⥤�󥹥ȡ��뤷�ʤ���Фʤ�ޤ���

%description -l nb
Denne pakken inneholder Perl-moduler for GTK+, et bibliotek som brukes
for � lage grafiske grensesnitt for X. Modulene i denne pakken gj�r
det mulig � lage grafiske programmer ved hjelp av Perl og GTK+. For �
kunne installere denne pakken m� b�de Perl og GTK+ v�re installert.

%description -l pl
GTK+-perl pozwala na pisanie interfejsu graficznego przy u�yciu Perla
i GTK+.

%description -l pt_BR
Este pacote cont�m extens�es Perl para o GTK+.

%description -l sv
Detta paket inneh�ller Perlutvidgningar f�r GTK+ (verktygsl�dan Gimp),
ett bibliotek anv�nt f�r att skapa grafiska anv�ndargr�nssnitt f�r X.
Utvidgningen som tillhandah�lls i detta paket l�ter dig skapa grafiska
gr�nssnitt med Perl och GTK+. Om du installerar detta paket beh�ver du
�ven ha Perl och GTK+ installerade.

%package Gdk-ImlibImage
Summary:	Imlib support for perl-gtk
Summary(pl):	Obs�uga Imlib dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Gdk-ImlibImage
Gtk::Gdk::ImlibImage module - Imlib library support for perl-gtk.

%description Gdk-ImlibImage -l pl
Modu� Gtk::Gdk::ImlibImage - obs�uga biblioteki Imlib dla perl-gtk.

%package Gdk-Pixbuf
Summary:	Gdk-Pixbuf support for perl-gtk
Summary(pl):	Obs�uga Gdk-Pixbuf dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description Gdk-Pixbuf
Gtk::Gdk::Pixbuf module - Gdk-Pixbuf library support for perl-gtk.

%description Gdk-Pixbuf -l pl
Modu� Gtk::Gdk::Pixbuf - obs�uga biblioteki Gdk-Pixbuf dla perl-gtk.

%package GLArea
Summary:	Gtk-GLArea support for perl-gtk
Summary(pl):	Obs�uga Gtk-GLArea dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description GLArea
Gtk::GLArea module - Gtk-GLArea library support for perl-gtk.

%description GLArea -l pl
Modu� Gtk::GLArea - obs�uga biblioteki Gtk-GLArea dla perl-gtk.

%package GladeXML
Summary:	libglade support for perl-gtk
Summary(pl):	Obs�uga libglade dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description GladeXML
Gtk::GladeXML module - libglade library support for perl-gtk.

%description GladeXML -l pl
Modu� Gtk::GladeXML - obs�uga biblioteki libglade dla perl-gtk.

%package XmHTML
Summary:	XmHTML support for perl-gtk
Summary(pl):	Obs�uga XmHTML dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description XmHTML
Gtk::XmHTML module - gtkxmhtml library support for perl-gtk.

%description XmHTML -l pl
Modu� Gtk::XmHTML - obs�uga biblioteki gtkxmhtml dla perl-gtk.

%package HTML
Summary:	gtkhtml support for perl-gtk
Summary(pl):	Obs�uga gtkhtml dla perl-gtk
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description HTML
Gtk::HTML module - gtkhtml library support for perl-gtk.

%description HTML -l pl
Modu� Gtk::HTML - obs�uga biblioteki gtkhtml dla perl-gtk.

%package -n perl-gnome
Summary:	Perl extensions for GNOME
Summary(cs):	Roz���en� Perlu pro GNOME
Summary(da):	Perl udvidelser for GNOME
Summary(de):	Perl-Erweiterungen f�r GNOME
Summary(es):	Extensiones Perl para GNOME
Summary(fr):	Extensions Perl pour GNOME
Summary(it):	Estensioni Perl per GNOME
Summary(ja):	GNOME �Ѥ� Perl ��ĥ
Summary(nb):	Perlmodul for GNOME
Summary(pl):	Rozszerzenie Perla dla GNOME
Summary(pt):	Uma extens�o de Perl para o GNOME
Summary(pt_BR):	Extens�es Perl para o GNOME
Summary(ru):	����������� ������ Perl ��� GNOME
Summary(sl):	Perlovske raz�iritve za GNOME
Summary(sv):	Perl-utvidgning f�r GNOME
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-Gdk-ImlibImage = %{version}-%{release}

%description -n perl-gnome
This package includes Perl extensions for GNOME.

%description -n perl-gnome -l pl
Ten pakiet zawiera rozszerzenia Perla dla GNOME.

%package -n perl-gnome-Print
Summary:	Perl extensions for GnomePrint
Summary(cs):	Roz���en� Perlu pro GnomePrint
Summary(da):	Perl udvidelser for GnomePrint
Summary(de):	Perl-Erweiterungen f�r GnomePrint
Summary(es):	Extensiones Perl para GnomePrint
Summary(fr):	Extensions Perl pour GnomePrint
Summary(it):	Estensioni Perl per GnomePrint
Summary(ja):	GnomePrint �Ѥ� Perl ��ĥ
Summary(nb):	Perlmodul for GnomePrint
Summary(pl):	Rozszerzenie Perl dla GnomePrint
Summary(pt):	Uma extens�o de Perl para o GnomePrint
Summary(pt_BR):	Extens�es Perl para o GnomePrint
Summary(ru):	����������� ������ Perl ��� GnomePrint
Summary(sl):	Perlovske raz�iritve za GnomePrint
Summary(sv):	Perl-utvidgning f�r GnomePrint
Group:		Development/Languages/Perl
Requires:	%{name}-Gdk-Pixbuf = %{version}-%{release}
Requires:	perl-gnome = %{version}

%description -n perl-gnome-Print
This package includes Perl extensions for GnomePrint.

%description -n perl-gnome-Print -l pl
Ten pakiet zawiera rozszerzenia Perla dla GnomePrint.

%package -n perl-gnome-Applet
Summary:	Applets support for perl-gnome
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
%patch2 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	--without-guessing \
%{!?with_gdk_pixbuf:	--without-gdkpixbuf}	%{?with_gdk_pixbuf:	--with-gdkpixbuf-force} \
%{!?with_gdkimlib:	--without-gdkimlib}	%{?with_gdkimlib:	--with-gdkimlib-force} \
%{!?with_glade:		--without-glade}	%{?with_glade:		--with-glade-force} \
%{!?with_gnome:		--without-gnome}	%{?with_gnome:		--with-gnome-force} \
%{!?with_gnomeprint:	--without-gnomeprint}	%{?with_gnomeprint:	--with-gnomeprint-force} \
%{!?with_gtkglarea:	--without-gtkglarea}	%{?with_gtkglarea:	--with-gtkglarea-force} \
%{!?with_gtkhtml:	--without-gtkhtml}	%{?with_gtkhtml:	--with-gtkhtml-force} \
%{!?with_gtkxmhtml:	--without-gtkxmhtml}	%{?with_gtkxmhtml:	--with-gtkxmhtml-force} \
%{!?with_applets:	--without-applets}	%{?with_applets:	--with-applets-force}

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{perl_vendorarch}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorarch}/Gtk.pm
%dir %{perl_vendorarch}/Gtk
%{perl_vendorarch}/Gtk/[ACIKLTil]*
%{perl_vendorarch}/Gtk/Gdk.pm
%dir %{perl_vendorarch}/Gtk/Gdk
%dir %{perl_vendorarch}/auto/Gtk
%{perl_vendorarch}/auto/Gtk/Gtk.bs
%{perl_vendorarch}/auto/Gtk/autosplit.ix
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk/Gtk.so
%dir %{perl_vendorarch}/auto/Gtk/Gdk
%{perl_vendorarch}/auto/Gtk/Gdk/autosplit.ix
%{_mandir}/man3/Gtk.3pm*
%{_mandir}/man3/Gtk::[Ca-z]*.3pm*

%if %{with gdkimlib}
%files Gdk-ImlibImage
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk/Gdk/ImlibImage.pm
%{perl_vendorarch}/Gtk/Gdk/ImlibImage
%dir %{perl_vendorarch}/auto/Gtk/Gdk/ImlibImage
%{perl_vendorarch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk/Gdk/ImlibImage/ImlibImage.so
%{_mandir}/man3/Gtk::Gdk::ImlibImage*
%endif

%if %{with gdk_pixbuf}
%files Gdk-Pixbuf
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk/Gdk/Pixbuf.pm
%{perl_vendorarch}/Gtk/Gdk/Pixbuf
%dir %{perl_vendorarch}/auto/Gtk/Gdk/Pixbuf
%{perl_vendorarch}/auto/Gtk/Gdk/Pixbuf/Pixbuf.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk/Gdk/Pixbuf/Pixbuf.so
%{_mandir}/man3/Gtk::Gdk::Pixbuf*
%endif

%if %{with gtkglarea}
%files GLArea
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk/GLArea.pm
%{perl_vendorarch}/Gtk/GLArea
%dir %{perl_vendorarch}/auto/Gtk/GLArea
%{perl_vendorarch}/auto/Gtk/GLArea/GLArea.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk/GLArea/GLArea.so
%dir %{perl_vendorarch}/auto/Gtk/GLArea/Constants
%{perl_vendorarch}/auto/Gtk/GLArea/Constants/autosplit.ix
%endif

%if %{with glade}
%files GladeXML
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk/GladeXML.pm
%{perl_vendorarch}/Gtk/GladeXML
%dir %{perl_vendorarch}/auto/Gtk/GladeXML
%{perl_vendorarch}/auto/Gtk/GladeXML/autosplit.ix
%{perl_vendorarch}/auto/Gtk/GladeXML/GladeXML.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk/GladeXML/GladeXML.so
%{_mandir}/man3/Gtk::GladeXML*
%endif

%if %{with gtkxmhtml}
%files XmHTML
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk/XmHTML.pm
%{perl_vendorarch}/Gtk/XmHTML
%dir %{perl_vendorarch}/auto/Gtk/XmHTML
%{perl_vendorarch}/auto/Gtk/XmHTML/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk/XmHTML/*.so
%endif

%if %{with gtkhtml}
%files HTML
%defattr(644,root,root,755)
%{perl_vendorarch}/Gtk/HTML.pm
%{perl_vendorarch}/Gtk/HTML
%dir %{perl_vendorarch}/auto/Gtk/HTML
%{perl_vendorarch}/auto/Gtk/HTML/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gtk/HTML/*.so
%endif

%if %{with gnome}
%files -n perl-gnome
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome.pm
%dir %{perl_vendorarch}/Gnome
%{perl_vendorarch}/Gnome/[IT]*
%dir %{perl_vendorarch}/auto/Gnome
%{perl_vendorarch}/auto/Gnome/Gnome.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome/Gnome.so
%{_mandir}/man3/Gnome.3pm*
%{_mandir}/man3/Gnome::reference.3pm*
%endif

%if %{with gnomeprint}
%files -n perl-gnome-Print
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome/Print.pm
%{perl_vendorarch}/Gnome/Print
%dir %{perl_vendorarch}/auto/Gnome/Print
%{perl_vendorarch}/auto/Gnome/Print/Print.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome/Print/Print.so
%{_mandir}/man3/Gnome::Print*
%endif

%if %{with applets}
%files -n perl-gnome-Applet
%defattr(644,root,root,755)
%{perl_vendorarch}/Gnome/Applet.pm
%{perl_vendorarch}/Gnome/Applet
%dir %{perl_vendorarch}/auto/Gnome/Applet
%{perl_vendorarch}/auto/Gnome/Applet/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Gnome/Applet/*.so
%{_mandir}/man3/Gnome::Applet*
%endif
