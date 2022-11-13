Name:		texlive-typeface
Version:	27046
Release:	1
Summary:	Select a balanced set of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/typeface
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeface.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeface.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeface.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the means of establishing a consistent set
of fonts for use in a LaTeX document. It allows mixing and
matching the Type 1 font sets available on the archive (and it
may be extended, via its configuration file, to support other
fonts). Font-set definition takes the form of a set of options
that are read when the package is loaded: for each typographic
category (main body font, sans-serif font, monospace font,
mathematics fonts, text figures, and so on), a font or a
transformation is given in those options. The approach enables
the user to remember their own configurations (as a single
command) and to borrow configurations that other users have
developed. The present release is designated "for review".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/typeface/typeface.cfg
%{_texmfdistdir}/tex/latex/typeface/typeface.sty
%doc %{_texmfdistdir}/doc/latex/typeface/README
%doc %{_texmfdistdir}/doc/latex/typeface/typeface-all-rm.pdf
%doc %{_texmfdistdir}/doc/latex/typeface/typeface-test.tex
%doc %{_texmfdistdir}/doc/latex/typeface/typeface.pdf
%doc %{_texmfdistdir}/doc/latex/typeface/typeface.tex
#- source
%doc %{_texmfdistdir}/source/latex/typeface/typeface-all-rm.bat

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
