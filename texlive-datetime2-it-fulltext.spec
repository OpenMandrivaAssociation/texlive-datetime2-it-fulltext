%global tl_name datetime2-it-fulltext
%global tl_revision 54779

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Italian full text styles for the datetime2 package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-contrib/datetime2-it-fulltext
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-it-fulltext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-it-fulltext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-it-fulltext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(iftex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Italian date and time styles that use words for the numbers and
ordinals. This package provides the following date and time styles: "it-
fulltext" and "it-fulltext-twenty-four". The first style uses a format
"am pm", the second a format "24 hours". The necessary packages are
datetime2, itnumpar, ifxetex, and ifluatex. This package is the
translation and adaptation of datetime2-en-fulltext.

