"""
Usage:
    linkedin_scraper.py mine_proxies <destination_file>
    linkedin_scraper.py mine_profiles <destination_file> [--query=<query>] [--num=<num>] [--proxies=<proxies>]
    linkedin_scraper.py scrape_profiles <profiles_links> [--proxies=<proxies>]
    linkedin_scraper.py (-h | --help)
    linkedin_scraper.py --version

Options:
    -h --help       show this screen.
    --version       show version
    --query=<query> Google query to get Linkedin profiles links
    --num=<num>     The number of search results (default=10,max=100)           
"""

from docopt import docopt


#import configs
from configs import configs
#import helpers
import helpers.helpers as hlp
from helpers.get_profiles_links import get_profiles_links
from helpers.get_proxies import get_proxies
from helpers.scrape_profiles import scrape_profiles




def Main():
    args = docopt(__doc__,version="Linkedin Scraper 0.1")

    if args["mine_proxies"]:
        #get fresh (https only) proxies from free-proxy-list and save to file
        proxies = get_proxies()
        hlp.save_to_file(proxies,args.get("<destination_file>"))
    elif args["mine_profiles"]:
        query = hlp.GoogleQuery()
        query.q = configs.GOOGLE_QUERY
        query.num = configs.GOOGLE_NUM_RESULTS
        query.arguments = configs.GOOGLE_QUERY_ARGUMENTS

        if args.get("--query"):
            query.q = args["--query"]
        if args.get("--num"):
            query.num = args["--num"]

        proxies=None
        if args.get("--proxies"):
            proxies = hlp.read_file(args["--proxies"])

        profiles_links = get_profiles_links(query,proxies)
        hlp.save_to_file(profiles_links,args["<destination_file>"])

    elif args["scrape_profiles"]:
        pass

    '''
    #lookup linkedIn profiles on Google
    query = 'site%3Alinkedin.com%2Fin%2F+AND+"python"+AND+%28"Maroc"+OR+"Morocco"%29'
    linkedin_urls = get_profiles_links(query)

    #test
    if len(linkedin_urls):
        print(len(linkedin_urls))
        for link in linkedin_urls:
            print(link)
    '''

if __name__=="__main__":
    Main()