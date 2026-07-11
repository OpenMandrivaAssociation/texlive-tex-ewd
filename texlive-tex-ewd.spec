%global tl_name tex-ewd
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Macros to typeset calculational proofs and programs in Dijkstras style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/tex-ewd
License:	bsd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ewd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tex-ewd.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Edsger W. Dijkstra and others suggest a unique style to present
mathematical proofs and to construct programs. This package provides
macros that support calculational proofs and Dijkstra's "guarded command
language".

