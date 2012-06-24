#
# Conditional build:
# _without_gnome
#
%define		_noautoreq "perl(Gtk::TypesLazy)" "perl(Gnome::TypesLazy)"
%include	/usr/lib/rpm/macros.perl
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
Release:	7
License:	LGPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	��ȯ/����/Perl
Group(no):	Utvikling/Programmeringsspr�k/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Group(sv):	Utveckling/Spr�k/Perl
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
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(da):	Udvikling/Sprog/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(it):	Sviluppo/Linguaggi/Perl
Group(ja):	��ȯ/����/Perl
Group(no):	Utvikling/Programmeringsspr�k/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Group(sv):	Utveckling/Spr�k/Perl
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
