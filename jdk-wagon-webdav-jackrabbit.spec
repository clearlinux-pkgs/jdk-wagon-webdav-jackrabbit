Name     : jdk-wagon-webdav-jackrabbit
Version  : 2.2
Release  : 1
URL      : http://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-webdav-jackrabbit/2.2/wagon-webdav-jackrabbit-2.2.jar
Source0  : http://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-webdav-jackrabbit/2.2/wagon-webdav-jackrabbit-2.2.jar
Source1  : http://repo.maven.apache.org/maven2/org/apache/maven/wagon/wagon-webdav-jackrabbit/2.2/wagon-webdav-jackrabbit-2.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : javapackages-tools
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six

%description
No detailed description available

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/maven-poms
mkdir -p %{buildroot}/usr/share/maven-metadata
mkdir -p %{buildroot}/usr/share/java

mv %{SOURCE0} %{buildroot}/usr/share/java/wagon-webdav-jackrabbit.jar
mv %{SOURCE1} %{buildroot}/usr/share/maven-poms/wagon-webdav-jackrabbit.pom

# Creates metadata
python3 /usr/share/java-utils/maven_depmap.py \
-n "" \
--pom-base %{buildroot}/usr/share/maven-poms \
--jar-base %{buildroot}/usr/share/java \
%{buildroot}/usr/share/maven-metadata/wagon-webdav-jackrabbit.xml \
%{buildroot}/usr/share/maven-poms/wagon-webdav-jackrabbit.pom \
%{buildroot}/usr/share/java/wagon-webdav-jackrabbit.jar \

%files
%defattr(-,root,root,-)
/usr/share/maven-metadata/wagon-webdav-jackrabbit.xml
/usr/share/maven-poms/wagon-webdav-jackrabbit.pom
/usr/share/java/wagon-webdav-jackrabbit.jar
