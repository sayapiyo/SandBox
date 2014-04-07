#!/usr/bin/enc python2.7
# -*- coding: utf-8 -*-

import sqlite3
#郵便番号のリスト
postno = [[u"東京都千代田区", "100-0000"],
		  [u"東京都千代田区飯田橋", "102-0072"],
		  [u"東京都千代田区一番町", "102-0082"],
		  [u"東京都千代田区岩本町", "101-0032"], ]
# コネクションオブジェクト作る
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("""CREATE TABLE postdb(
				address text,postno text)""")
for item in postno:
		cur.execute("""INSERT INTO postdb(address,postno)
			VALUES(?,?)""",item)
cur.execute("SELECT * FROM postdb WHERE postno =?",("101-0032",))
data = cur.fetchone()
print data[1],data[0]
