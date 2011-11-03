# revision 15878
# category Package
# catalog-ctan /macros/generic/tex-ewd
# catalog-date 2008-11-15 12:33:11 +0100
# catalog-license bsd
# catalog-version undef
Name:		texlive-tex-ewd
Version:	20081115
Release:	1
Summary:	Macros to typeset calculational proofs and programs in Dijkstra's style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/tex-ewd
License:	BSD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ewd.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ewd.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Edsger W. Dijkstra and others suggest a unique style to present
mathematical proofs and to construct programs. This package
provides macros that support calculational proofs and
Dijkstra's "guarded command language".

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/tex-ewd/dotnot.tex
%doc %{_texmfdistdir}/doc/generic/tex-ewd/README
%doc %{_texmfdistdir}/doc/generic/tex-ewd/bsdlic.txt
%doc %{_texmfdistdir}/doc/generic/tex-ewd/p0.tex
%doc %{_texmfdistdir}/doc/generic/tex-ewd/t1.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
