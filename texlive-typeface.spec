# revision 27046
# category Package
# catalog-ctan /macros/latex/contrib/typeface
# catalog-date 2012-07-02 21:55:35 +0200
# catalog-license lppl1.3
# catalog-version 0.1
Name:		texlive-typeface
Version:	0.1
Release:	9
Summary:	Select a balanced set of fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/typeface
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeface.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeface.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/typeface.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
