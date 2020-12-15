import twint
# Configure
c = twint.Config()
c.Search = "日経"
c.Format = " Tweet: {tweet}"
c.Output = 'nikkei'
c.Store_csv = True
c.Since = 2016-6-25
c.Until = 2017-6-27
# Run
twint.run.Search(c)
