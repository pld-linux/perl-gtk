Summary:	Perl extention for gtk
Summary(pl):	Rozszerzenie Perl dla Gtk
Name:		perl-gtk
Version:	0.5121
Release:	1
Copyright:	LGPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://www.gtk.org/pub/perl/Gtk-Perl-%{version}.tar.gz
URL:		http://www.gtk.org/
BuildRequires:	perl >= 5.004
BuildRequires:	gtk+-devel
BuildRequires:	glib-devel
BuildRequires:	XFree86-devel
BuildRequires:	imlib-devel
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	Gtk-perl
Buildroot:	/tmp/%{name}-%{version}-root

%description
gtk+-perl allows you to write graphical interfaces using perl and gtk.

%description -l pl
Gtk+-perl pozwoli ci na pisanie interfejsu graficznego przy u¿yciu
perl'a i gtk.

%prep
%setup -q -n Gtk-Perl-%{version}

%build
perl Makefile.PL \
	--without-gnome \
	--without-gnome-panel \
	--without-gnome-zvt

make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install \
	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT%{_mandir}/man3

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
	README

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README.gz

%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gtk.so
%{perl_sitearch}/*.pm
%{perl_sitearch}/Gtk
%{perl_sitearch}/auto/Gtk/Gtk.bs
%dir %{perl_sitearch}/auto/Gtk
%dir %{perl_sitearch}/auto/Gtk/Gdk
%{_mandir}/man3/*
