# Author : Bendidi Ihab
# This is a wrapper for the urllib.robotparser library


# Import Libraries
import urllib.robotparser as urobot



# Author : Ihab bendidi
# This function returns the crawl delay and the request rate of any inputed website
# The output is in the form of a list
class robotsParser :
    def get_details_url(self, url) :

        # Initializing the robotparser
        rp = urobot.RobotFileParser()

        # Getting the url of the robots.txt file
        robots_url = 'https://' + url.split('/')[2] + '/robots.txt'

        # Sets the url referring the the robots file
        rp.set_url(robots_url)

        # Reads the robots.txt URL and feeds it to the parser
        rp.read()

        # Setting the parameters
        if rp.request_rate("*").requests :
            requester = rp.request_rate("*").requests
        else :
            requester = 'Non Specified'

        if rp.request_rate("*").seconds :
            rate = rp.request_rate("*").seconds
        else :
            rate = 'Non Specified'

        if rp.crawl_delay("*") :
            crawl = rp.crawl_delay("*")
        else :
            crawl = 'Non Specified'

        # Output result
        results = [requester, rate, crawl]

        # END
        return results



    def is_allowed(self, url) :
        # Initializing the robotparser
        rp = urobot.RobotFileParser()

        # Getting the url of the robots.txt file
        robots_url = 'https://' + url.split('/')[2] + '/robots.txt'

        # Sets the url referring the the robots file
        rp.set_url(robots_url)

        # Reads the robots.txt URL and feeds it to the parser
        rp.read()

        # Returns True if the useragent is allowed to fetch the url according to the rules contained in the parsed robots.txt file
        allowance = rp.can_fetch("*", url)

        return allowance
