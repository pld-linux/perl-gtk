Summary:	Perl extention for gtk
Summary(pl):	Rozszerzenie Perl dla Gtk
Name:		perl-gtk
Version:	0.6123
Release:	1
Copyright:	LGPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://www.gtk.org/pub/perl/Gtk-Perl-%{version}.tar.gz
URL:		http://www.gtk.org/
BuildRequires:	perl >= 5.005_03-10
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
install -d $RPM_BUILD_ROOT%{perl_archlib}

make install \
	DESTDIR=$RPM_BUILD_ROOT 

sed -e "s#$RPM_BUILD_ROOT##g" \
	$RPM_BUILD_ROOT%{perl_sitearch}/auto/Gtk/.packlist \
        > $RPM_BUILD_ROOT%{perl_sitearch}/auto/Gtk/.packlist.wrk
mv $RPM_BUILD_ROOT%{perl_sitearch}/auto/Gtk/.packlist.wrk \
	        $RPM_BUILD_ROOT%{perl_sitearch}/auto/Gtk/.packlist

strip --strip-unneeded $RPM_BUILD_ROOT%{perl_sitearch}/auto/*/*.so

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
%{perl_sitearch}/auto/Gtk/.packlist
%dir %{perl_sitearch}/auto/Gtk
%dir %{perl_sitearch}/auto/Gtk/Gdk
%{_mandir}/man3/*
