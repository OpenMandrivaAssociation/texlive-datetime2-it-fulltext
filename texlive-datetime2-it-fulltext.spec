Name:		texlive-datetime2-it-fulltext
Version:	54779
Release:	1
Summary:	Italian full text styles for the datetime2 package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-it-fulltext
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-it-fulltext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-it-fulltext.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-it-fulltext.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Italian date and time styles that use words for the numbers and
ordinals. This package provides the following date and time
styles: "it-fulltext" and "it-fulltext-twenty-four". The first
style uses a format "am pm", the second a format "24 hours".
The necessary packages are datetime2, itnumpar, ifxetex, and
ifluatex. This package is the translation and adaptation of
datetime2-en-fulltext.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/datetime2-it-fulltext
%{_texmfdistdir}/tex/latex/datetime2-it-fulltext
%doc %{_texmfdistdir}/doc/latex/datetime2-it-fulltext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
