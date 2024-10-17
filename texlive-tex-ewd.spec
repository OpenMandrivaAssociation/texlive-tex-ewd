Name:		texlive-tex-ewd
Version:	15878
Release:	2
Summary:	Macros to typeset calculational proofs and programs in Dijkstra's style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/tex-ewd
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ewd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ewd.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Edsger W. Dijkstra and others suggest a unique style to present
mathematical proofs and to construct programs. This package
provides macros that support calculational proofs and
Dijkstra's "guarded command language".

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tex-ewd/dotnot.tex
%doc %{_texmfdistdir}/doc/generic/tex-ewd/README
%doc %{_texmfdistdir}/doc/generic/tex-ewd/bsdlic.txt
%doc %{_texmfdistdir}/doc/generic/tex-ewd/p0.tex
%doc %{_texmfdistdir}/doc/generic/tex-ewd/t1.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
