# -*- coding: utf-8 -*-
"""
File Name:
Description: windows gui automation

Author: shutchins2
Date Created: Fri Apr 21 15:23:49 2017
Project Name: Computer Utilities
"""


from pywinauto.application import Application

app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Help->About Notepad")

app.AboutNotepad.OK.click()

app.UntitledNotepad.Edit.type_keys("Hey, Rob!!!", with_spaces = True)

app.UntitledNotepad.menu_select("File->SaveAs")

app.Save.EncodingComboBox.select('UTF-8')


app.Save.edit1.set_text("hi-rob-example.txt")

app.Save.Save.click()