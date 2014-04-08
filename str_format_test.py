linkattrs = {"href":"http://hoge", "title":"Test Link"}
formatstr = """<a href= "%(href)s" title="%(title)s">
%(title)s
</a>"""
atag = formatstr % linkattrs
print atag
