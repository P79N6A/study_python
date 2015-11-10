#!/usr/bin/env python

"study python"

string1 = "string1"
string2 = "string2"
nPos = string1.index("string")
print nPos

//关于字符串的切片
//postion : 是相对位置,默认是0，如 string[:1]=>p string[:3]=>pos
//length  : 切片的长度,默认是从相对位置到末尾，如 string[1:]=>tring  string[2:]=>ring
//tip : string[-4:]=>ring 相当于 string[2:], 公式应推导为:string[len(string)-ceilf(num):-num]
//
string[postion:length]
