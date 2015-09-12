@ECHO OFF
SET choc=chocolatey install -y
@powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
chocolatey update
%choc% sublime
%choc% classic-shell
%choc% firefox
%choc% adblockplusfirefox
%choc% googlechrome
%choc% adblockpluschrome
%choc% 7zip.install
%choc% imgburn
%choc% ccleaner
%choc% teamviewer
%choc% revo.uninstaller
%choc% vlc
chocolatey update all