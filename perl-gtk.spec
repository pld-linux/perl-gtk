Summary:	Perl extention for gtk
Summary(pl):	Rozszerzenie Perl dla Gtk
Name:		Gtk-perl
Version:	0.5000
Release:	1d
Copyright:	LGPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
Source:		ftp://www.gtk.org/pub/perl/Gtk-%{version}.tar.gz
URL:		http://www.gtk.org
Requires:	perl >= 5.005_02
Requires:	gtk+ = 1.1.15
Buildroot:	/tmp/%{name}-%{version}-root

%description
gtk+-perl allows you to write graphical interfaces using perl and gtk.

%description -l pl
Gtk+-perl pozwoli ci na pisanie interfejsu graficznego przy u¿yciu
perl'a i gtk.

%prep
%setup -q -n Gtk-%{version}
perl Makefile.PL

%build
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install \
	PREFIX=$RPM_BUILD_ROOT/usr \
	INSTALLMAN3DIR=$RPM_BUILD_ROOT/usr/man/man3

bzip2 -9 README
gzip -9fn $RPM_BUILD_ROOT/usr/man/man3/*

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README.bz2

%attr(644,root, man) /usr/man/man3/*

/usr/lib/perl5/site_perl/*/*/*.pm
/usr/lib/perl5/site_perl/*/*/Gtk

%dir /usr/lib/perl5/site_perl/*/*/auto/Gtk
%dir /usr/lib/perl5/site_perl/*/*/auto/Gtk/Gdk

/usr/lib/perl5/site_perl/*/*/auto/Gtk/Gtk.bs

%attr(755,root,root) /usr/lib/perl5/site_perl/*/*/auto/Gtk/Gtk.so

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
