import twint
import pandas
import datetime


def scrape_reply(keywords, since, outfile):
    c = twint.Config()
    c.Search = keywords
    # c.Since = since
    c.Store_csv = True
    c.Output = "./" + outfile
   # c.Near = city
    c.Hide_output = True
    # c.Custom_csv = ["id", "user_id", "username", "tweet"]
   # c.Count = True
    # c.Limit = 10
    #c.Stats = True
   # c.Resume = 'resume.txt'
    twint.run.Search(c)

def get_date():
    return str(datetime.datetime.now() - datetime.timedelta(1))

def main():
    # scrape_reply("@RAM_Maroc",get_date() , 'repies_with_twint.csv')
    print(get_date())



if __name__ == "__main__":
    main()



