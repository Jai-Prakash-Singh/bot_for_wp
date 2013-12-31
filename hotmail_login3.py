# view and delete e-mail using the POP3 protocol
import sys, getpass, poplib, re
import mechanize

def verification3(m):
    br = mechanize.Browser()
    br.open(m)
    #try:
    br.select_form("loginform")
    br.form["log"]="xxxxx@hotmail.com"
    br.form["pwd"]="xxxx"
    br.submit()
    verified_url = br.geturl()
    return verified_url
    #except:
    #   return None
       
def verification2(line):
    match = re.findall(r"\w*//signup.wordpress.com/activate.*", line)
    verified_url_list = []
    for m in match:
        try:
            m = m.replace("=",'')
            m = "https:"+m
            m = m.replace("0A",'')
            print m 
            verified_url = verification3(m) 
            if verified_url is not None :
                verified_url_list.append(verified_url)  
        except:
            pass

    return  verified_url_list      


def my_header_match(my_header):
    
    match = re.findall('''From: "WordPress.com" <donotreply@wordpress.com>\nSubject: Confirm your email address for''',my_header)
    if match:
        return True
    else:
        return False

def varification(POPUSER,POPPASS):
    # change according to your needs
    POPHOST = "pop3.live.com'"
    # the number of message body lines to retrieve
    MAXLINES = 10
    headers=HEADERS = "From To Subject".split()
    # headers you're actually interested in
    rx_headers = re.compile('|'.join(headers), re.IGNORECASE)
    try:
        # connect to POP3 and identify user
        pop= poplib.POP3_SSL('pop3.live.com', 995)
        pop.user(POPUSER)
        if not POPPASS or POPPASS=='=':
            # if no password was supplied, ask for it
            POPPASS = getpass.getpass("Password for %s@%s:" % (POPUSER, POPHOST))
            # authenticate user
        
        pop.pass_(POPPASS)
        # get general information (msg_count, box_size)
        stat = pop.stat( )
        # print some information
        print "Logged in as %s@%s" % (POPUSER, POPHOST)
        print "Status: %d message(s), %d bytes" % stat
        print "*"*20
        bye = 0
        count_del = 0
        for n in range(stat[0]):
            msgnum = n+1
            # retrieve headers
            response, lines, bytes = pop.top(msgnum, MAXLINES)
            # print message info and headers you're interested in
            print "Message %d (%d bytes)" % (msgnum, bytes)
            print "-" * 30
            my_header =  "\n".join(filter(rx_headers.match, lines))
            result = my_header_match(my_header)
            if result:
                print my_header
                print "-" * 30
                # input loop
                line = "\n".join(lines)
                verified_url_list = verification2(line)
         
                print "verified_url_list: " +', '.join(verified_url_list)
                print "-" * 30
         
 
        # summary
        print "Deleting %d message(s) in mailbox %s@%s" % (count_del, POPUSER, POPHOST)
        # close operations and disconnect from server
        print "Closing POP3 session"
        pop.quit( )
    except poplib.error_proto, detail:
        # possible error
        print "POP3 Protocol Error:", detail



if __name__=="__main__":
    POPUSER = "xxxxxx@hotmail.com"
    POPPASS = "xxxxxxx"
    varification(POPUSER,POPPASS)
