#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-CircStats
Version  : 0.2.6
Release  : 25
URL      : https://cran.r-project.org/src/contrib/CircStats_0.2-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/CircStats_0.2-6.tar.gz
Summary  : Circular Statistics, from "Topics in Circular Statistics" (2001)
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
Version 0.2-5 2018/06/30
This is an R port of CircStats package of Ulric Lund <ulund@calpoly.edu> from
"Topics in circular Statistics" (2001) S. Rao Jammalamadaka and A. SenGupta, World Scientific.

%prep
%setup -q -c -n CircStats

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571810058

%install
export SOURCE_DATE_EPOCH=1571810058
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library CircStats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library CircStats
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library CircStats
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc CircStats || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/CircStats/COPYRIGHTS
/usr/lib64/R/library/CircStats/DESCRIPTION
/usr/lib64/R/library/CircStats/INDEX
/usr/lib64/R/library/CircStats/Meta/Rd.rds
/usr/lib64/R/library/CircStats/Meta/data.rds
/usr/lib64/R/library/CircStats/Meta/features.rds
/usr/lib64/R/library/CircStats/Meta/hsearch.rds
/usr/lib64/R/library/CircStats/Meta/links.rds
/usr/lib64/R/library/CircStats/Meta/nsInfo.rds
/usr/lib64/R/library/CircStats/Meta/package.rds
/usr/lib64/R/library/CircStats/NAMESPACE
/usr/lib64/R/library/CircStats/R/CircStats
/usr/lib64/R/library/CircStats/R/CircStats.rdb
/usr/lib64/R/library/CircStats/R/CircStats.rdx
/usr/lib64/R/library/CircStats/data/rao.table.rda
/usr/lib64/R/library/CircStats/help/AnIndex
/usr/lib64/R/library/CircStats/help/CircStats.rdb
/usr/lib64/R/library/CircStats/help/CircStats.rdx
/usr/lib64/R/library/CircStats/help/aliases.rds
/usr/lib64/R/library/CircStats/help/paths.rds
/usr/lib64/R/library/CircStats/html/00Index.html
/usr/lib64/R/library/CircStats/html/R.css
