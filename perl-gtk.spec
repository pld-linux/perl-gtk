%include	/usr/lib/rpm/macros.perl
Summary:	Perl extensions for Gtk+ (the Gimp ToolKit)
Summary(pl):	Rozszerzenie Perl dla Gtk
Name:		perl-gtk
Version:	0.7000
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://www.gtk.org/pub/perl/Gtk-Perl-%{version}.tar.gz
URL:		http://www.gtk.org/
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	rpm-perlprov
%requires_eq	perl
Requires:	%{perl_sitearch}
Obsoletes:	Gtk-perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package includes Perl extensions for Gtk+ (the Gimp ToolKit), a
library used for creating graphical user interfaces for the X Window
System. The extensions provided in this package allow you to write
graphical interfaces using Perl and Gtk+. If you install this package,
you'll need to also have Perl and Gtk+ installed.

%description -l pl
Gtk+-perl pozwoli ci na pisanie interfejsu graficznego przy u�yciu
perl'a i gtk.

%prep
%setup -q -n Gtk-Perl-%{version}

%build
perl Makefile.PL \
	--without-gnome \
	--without-gnome-panel \
	--without-gnome-zvt

%{__make} OPTIMIZE="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS}"

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
%attr(755,root,root) %{perl_sitearch}/auto/Gtk/Gtk.so
%{perl_sitearch}/*.pm
%{perl_sitearch}/Gtk
%{perl_sitearch}/auto/Gtk/Gtk.bs
%{perl_sitearch}/auto/Gtk/Gdk
%{_mandir}/man3/*
