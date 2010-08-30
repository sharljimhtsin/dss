Summary: Darwin Streaming Server
Vendor: M2X BV
Name: dss
Version: 6.0.3
Release: 1
License: Apple Public Source License
URL: http://dss.macosforge.org/
Group: Applications/Multimedia
Source0: DarwinStreamingSrvr6.0.3-Source.tar
Source1: dss
Patch0: dss-6.0.3.patch
Patch1: dss-hh-20080728-1.patch
Patch2: 0001-Adjust-configuration-file-paths-for-better-complianc.patch
BuildRoot: /var/tmp/%{name}
Prefix: /usr

Requires: perl >= 5.002

Provides: DarwingStreamingServer

%description
Darwin Streaming Server is the Open Source version of Apple's (tm) product
QuickTime Streaming Server. It offers the same features as QTSS, but comes
without Apple's support.

%prep
%setup -n DarwinStreamingSrvr%version-Source
%patch0 -p1
%patch1 -p1
%patch2 -p1
cp $RPM_SOURCE_DIR/dss dss

%clean
rm -fr $RPM_BUILD_ROOT

%build
rm -fr $RPM_BUILD_ROOT
./Buildit

%install
# Install binaries
install -d %{buildroot}/usr/bin
install -d %{buildroot}/usr/sbin

install -m 755 DarwinStreamingServer    %{buildroot}%{_sbindir}
install -m 755 WebAdmin/src/streamingadminserver.pl %{buildroot}%{_sbindir}

install -m 755 MP3Broadcaster/MP3Broadcaster %{buildroot}%{_bindir}

install -m 755 PlaylistBroadcaster.tproj/PlaylistBroadcaster %{buildroot}%{_bindir}

install -m 755 qtpasswd.tproj/qtpasswd %{buildroot}%{_bindir}

install -m 755 StreamingProxy.tproj/StreamingProxy %{buildroot}%{_sbindir}
install -m 755 StreamingLoadTool/StreamingLoadTool %{buildroot}%{_bindir}

# Install modules and tools
install -m 755 APIModules/QTSSDemoAuthorizationModule.bproj/QTSSDemoAuthorizationModule %{buildroot}%{_bindir}
install -m 755 APIModules/QTSSHomeDirectoryModule/QTSSHomeDirectoryModule %{buildroot}%{_bindir}
install -m 755 APIModules/QTSSRawFileModule.bproj/QTSSRawFileModule %{buildroot}%{_bindir}
install -m 755 APIModules/QTSSRefMovieModule/QTSSRefMovieModule %{buildroot}%{_bindir}
install -m 755 APIModules/QTSSSpamDefenseModule.bproj/QTSSSpamDefenseModule %{buildroot}%{_bindir}

install -m 755 QTFileTools/QTBroadcaster.tproj/QTBroadcaster %{buildroot}%{_bindir}
install -m 755 QTFileTools/QTFileInfo.tproj/QTFileInfo %{buildroot}%{_bindir}
install -m 755 QTFileTools/QTFileTest.tproj/QTFileTest %{buildroot}%{_bindir}
install -m 755 QTFileTools/QTRTPFileTest.tproj/QTRTPFileTest %{buildroot}%{_bindir}
install -m 755 QTFileTools/QTRTPGen.tproj/QTRTPGen %{buildroot}%{_bindir}
install -m 755 QTFileTools/QTSDPGen.tproj/QTSDPGen %{buildroot}%{_bindir}
install -m 755 QTFileTools/QTSampleLister.tproj/QTSampleLister %{buildroot}%{_bindir}
install -m 755 QTFileTools/QTTrackInfo.tproj/QTTrackInfo %{buildroot}%{_bindir}

install -m 600 APIModules/QTSSHomeDirectoryModule/createuserstreamingdir %{buildroot}%{_bindir}

# Install manpages
install -d %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man8/

install -m 644 ./Documentation/man/qtss/createuserstreamingdir.8 %{buildroot}%{_mandir}/man8/
install -m 644 ./Documentation/man/qtss/QuickTimeStreamingServer.8 %{buildroot}%{_mandir}/man8/
install -m 644 ./Documentation/man/qtss/StreamingLoadTool.8 %{buildroot}%{_mandir}/man8/
install -m 644 ./Documentation/man/qtss/streamingadminserver.pl.8 %{buildroot}%{_mandir}/man8/

install -m 644 ./Documentation/broadcasterctl.1 %{buildroot}%{_mandir}/man1/
install -m 644 ./Documentation/man/qtss/PlaylistBroadcaster.1 %{buildroot}%{_mandir}/man1/
install -m 644 ./Documentation/man/qtss/MP3Broadcaster.1 %{buildroot}%{_mandir}/man1/
install -m 644 ./Documentation/man/qtss/qtpasswd.1 %{buildroot}%{_mandir}/man1/

# Install Configuration
install -d %{buildroot}/etc/dss
install -d %{buildroot}/var/lib/dss
install -d %{buildroot}/var/lib/dss/logs
install -m 770 -d %{buildroot}/var/lib/dss/playlist

install -m 600 streamingserver.xml %{buildroot}/etc/dss
install -m 600 relayconfig.xml-Sample %{buildroot}/etc/dss/relayconfig.xml
install -m 600 qtaccess %{buildroot}/etc/dss
install -m 600 qtusers  %{buildroot}/etc/dss
install -m 600 qtgroups %{buildroot}/etc/dss
install -m 600 StreamingLoadTool/streamingloadtool.conf %{buildroot}/etc/dss

# Install WebAdminHtml
install -d %{buildroot}/var/lib/dss/AdminHtml
install -d %{buildroot}/var/lib/dss/AdminHtml/images
install -d %{buildroot}/var/lib/dss/AdminHtml/includes
install -d %{buildroot}/var/lib/dss/AdminHtml/javascripts
install -d %{buildroot}/var/lib/dss/AdminHtml/logs
install -d %{buildroot}/var/lib/dss/AdminHtml/settings
install -d %{buildroot}/var/lib/dss/AdminHtml/status

install -m 600 WebAdmin/streamingadminserver.pem %{buildroot}/etc/dss

install -m 600 WebAdmin/WebAdminHtml/*.{html,cgi,pl} %{buildroot}/var/lib/dss/AdminHtml
install -m 600 WebAdmin/WebAdminHtml/images/*  %{buildroot}/var/lib/dss/AdminHtml/images
install -m 600 WebAdmin/WebAdminHtml/includes/* %{buildroot}/var/lib/dss/AdminHtml/includes

# Startup sysvinit script
install -d %{buildroot}/etc/init.d
install -m 755 dss %{buildroot}/etc/init.d/

# Install Documents
install -d %{buildroot}/usr/share/docs/dss-%{version}
install Documentation/*.{pdf,txt,rtf,html} %{buildroot}/usr/share/docs/dss-%{version}

# Install sample movies
install -m 755 -d %{buildroot}/var/lib/dss/movies

install sample_100kbit.mov %{buildroot}/var/lib/dss/movies
install sample_300kbit.mov %{buildroot}/var/lib/dss/movies
install sample_100kbit.mp4 %{buildroot}/var/lib/dss/movies
install sample_300kbit.mp4 %{buildroot}/var/lib/dss/movies
install sample.mp3 %{buildroot}/var/lib/dss/movies
install sample_50kbit.3gp %{buildroot}/var/lib/dss/movies
install sample_h264_100kbit.mp4 %{buildroot}/var/lib/dss/movies
install sample_h264_300kbit.mp4 %{buildroot}/var/lib/dss/movies
install sample_h264_1mbit.mp4 %{buildroot}//var/lib/dss/movies

%files
%defattr(-,root,root,-)
/etc/init.d/dss

%config %attr(-,qtss,qtss) /etc/dss

%{_sbindir}/DarwinStreamingServer
%{_sbindir}/streamingadminserver.pl
%{_sbindir}/StreamingProxy

%{_bindir}/PlaylistBroadcaster
%{_bindir}/MP3Broadcaster
%{_bindir}/qtpasswd
%{_bindir}/StreamingLoadTool

%{_bindir}/QTSSDemoAuthorizationModule
%{_bindir}/QTSSHomeDirectoryModule
%{_bindir}/QTSSRawFileModule
%{_bindir}/QTSSRefMovieModule
%{_bindir}/QTSSSpamDefenseModule

%{_bindir}/QTBroadcaster
%{_bindir}/QTFileInfo
%{_bindir}/QTFileTest
%{_bindir}/QTRTPFileTest
%{_bindir}/QTRTPGen
%{_bindir}/QTSDPGen
%{_bindir}/QTSampleLister
%{_bindir}/QTTrackInfo

%{_bindir}/createuserstreamingdir

%dir %attr(-,qtss,qtss) /var/lib/dss/AdminHtml
%attr(-,qtss,qtss) /var/lib/dss/AdminHtml/*

%{prefix}/share/docs/dss-%{version}/*

%{_mandir}/man1/broadcasterctl.1.gz
%{_mandir}/man1/PlaylistBroadcaster.1.gz
%{_mandir}/man1/MP3Broadcaster.1.gz
%{_mandir}/man1/qtpasswd.1.gz

%{_mandir}/man8/createuserstreamingdir.8.gz
%{_mandir}/man8/QuickTimeStreamingServer.8.gz
%{_mandir}/man8/StreamingLoadTool.8.gz
%{_mandir}/man8/streamingadminserver.pl.8.gz

%pre
#
# check group and user
/usr/sbin/groupadd -r qtss 2> /dev/null || :
/usr/sbin/useradd -r qtss -g qtss -M -c "Darwin Streaming Server" -s /sbin/false -d /var/lib/dss 2> /dev/null || :

%post
#
# add sysv initscript
/sbin/chkconfig --add dss
/sbin/chkconfig --level=2345 dss off
#
# default configuration
if [ ! -f /etc/sysconfig/dss ] ; then
    cat > /etc/sysconfig/dss << EOF
# QTSS Default configuration
EOF
fi

%postun
/sbin/chkconfig --del dss

#-------------------------------------------------

%package samples
Summary: Darwin Streaming Server Movie samples
Group: Applications/Multimedia
Requires: dss

%description samples
Darwin Streaming Server is the Open Source version of Apple's (tm) product
QuickTime Streaming Server. It offers the same features as QTSS, but comes
without Apple's support.

%files samples
%defattr(644,qtss,qtss,-)
%attr(-,qtss,qtss) /var/lib/dss/movies/*

%changelog
* Thu Aug 27 2010 Jean-Paul Saman <jean-paul.saman@m2x.nl>
- Release 1
