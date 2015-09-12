${SegmentFile}

Var Exists_IobitUninstaller_Scheduled_Task

${SegmentPrePrimary}
	${If} ${FileExists} "$SYSDIR\Tasks\Uninstaller_SkipUac_Administrator"
		StrCpy $Exists_IobitUninstaller_Scheduled_Task true
	${EndIf}
!macroend


${SegmentPostPrimary}
	Delete $DataDirectory\uninstaller\SoftwareCache.ini
	
	${If} $Exists_SmartDefrag_Scheduled_Task != true
		nsExec::Exec /TIMEOUT=10000 `"schtasks.exe" /delete /tn Uninstaller_SkipUac_Administrator /f`
		Pop $0
	${EndIf}
	
	System::Call "wininet::DeleteUrlCacheEntryW(t'http://download.iobit.com/uninstaller3/UninstallRote.dbd')i .r2"
	System::Call "wininet::DeleteUrlCacheEntryW(t'http://download.iobit.com/uninstaller4/UninstallRote.dbd')i .r2"
!macroend