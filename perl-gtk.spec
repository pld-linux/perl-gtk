Summary:	Perl extention for gtk
Summary(pl):	Rozszerzenie Perl dla Gtk
Name:		perl-gtk
Version:	0.5121
Release:	1
Copyright:	LGPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://www.gtk.org/pub/perl/Gtk-Perl-%{version}.tar.gz
URL:		http://www.gtk.org
BuildPreReq:	perl >= 5.004
BuildPreReq:	gtk+-devel
BuildPreReq:	glib-devel
BuildPreReq:	XFree86-devel
BuildPrereq:	imlib-devel
Requires:	perl >= 5.004
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

%changelog
* Fri Feb 05 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.5000-1d]
- updated to 0.5000,
- compressed man pages && documentation.

* Sat Nov 21 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.3-2]
- simplifications in %files and %install.

* Tue Jul 14 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.3-1]
- added pl translation,
- added build-root support,
- build against GNU libc-2.1.
- minor modyfications of spec.

* Tue Jul 14 1998 The Rasterman <raster@redhat.com>
- Made it rebuild on multiple architectures (still linux only tho)
- this NEEDS to be buildrooted. not willign to do that quite yet.

* Fri Jul 10 1998 Jeff Carr <jcarr@linuxppc.org>
- Turned of -O2 on the ppc version
- I'm not sure about the LGPL part
