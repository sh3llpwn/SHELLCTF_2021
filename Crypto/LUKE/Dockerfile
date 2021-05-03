FROM ubuntu:16.04


RUN apt update 
RUN apt-get install libgcrypt11-dev libdevmapper-dev libpopt-dev uuid-dev libtool automake autopoint debhelper xsltproc docbook-xsl dpkg-dev -y
RUN apt install libgcrypt11-dev libdevmapper-dev libpopt-dev uuid-dev libselinux1-dev libsepol1-dev libtool autoconf automake autopoint debhelper xsltproc docbook-xml docbook-xsl po-debconf git -y
RUN apt install dmsetup initramfs-tools plymouth -y 

RUN cp /etc/apt/sources.list /etc/apt/sources.list~
RUN sed -Ei 's/^# deb-src /deb-src /' /etc/apt/sources.list
RUN apt-get update

COPY luksaddnuke/libgcrypt11_1.5.4-2ubuntu1.1_amd64.deb  /root/libgcrypt.deb
RUN dpkg -i /root/libgcrypt.deb
COPY luksaddnuke/cryptsetup_1.6.1-1ubuntu1_amd64.deb     /root/cryptsetup.deb
COPY luksaddnuke/cryptsetup-bin_1.6.1-1ubuntu1_amd64.deb /root/cryptsetup2.deb

COPY luksaddnuke/libcryptsetup4_1.6.1-1ubuntu1_amd64.deb /root/libcryptsetup.deb
COPY luksaddnuke/libcryptsetup4_1.6.1-1ubuntu1_amd64.deb /root/libcryptsetup2.deb

RUN dpkg -i /root/*.deb;exit 0