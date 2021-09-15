import codecs, json
import twint

class twitterScraping():

    def dataScrape():

        ## We pull tweets and information about the marked word
        c = twint.Config()
        c.Search = "request for startup"

        ## We are converting the output to json
        c.Output = "./twitterdata.json"
        c.Store_json = True

        ## We are converting the output to csv
        c.Output = "./twitterdata.csv"
        c.Store_csv = True

        twint.run.Search(c)


    if __name__ == '__main__':
        dataScrape()