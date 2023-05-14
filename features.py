import whois
import os
import dns.resolver
import requests
import time
import socket
import ssl
import urllib
import urllib.request
import urllib.parse
from urllib.parse import urlparse
import tldextract
from datetime import datetime
import datetime


# Define a function to extract features from the URL


def extract_features(url):

    features = []
    
    # Dataset attributes based on URL.
    
    # Feature 1: qty_dot_url
    try:
        features.append(url.count('.') if '.' in url else 0)
    except:
        features.append(0)

    # Feature 2: qty_hyphen_url
    try:
        features.append(url.count('-') if '-' in url else 0)
    except:
        features.append(0)

    # Feature 2: qty_underline_url
    try:
        features.append(url.count('_') if '_' in url else 0)
    except:
        features.append(0)

    # Feature 4: qty_slash_url
    try:
        features.append(url.count('/') if '/' in url else 0)
        
    except:
        features.append(0)

    # Feature 18: qty_tld_url
    domain = tldextract.extract(url).domain
    suffix = tldextract.extract(url).suffix
    
    if suffix:
        features.append(len(domain + suffix) - len(suffix))
        
    elif not suffix:
        features.append(len(domain))
        
    else:
        features.append(0)
    
    # Feature 19: length_url
    try:
        features.append(len(url))
        
    except:
        features.append(0)

    # Dataset attributes based on domain URL
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    # Feature 20: qty_dot_domain
    try:
        features.append(domain.count('.') if '.' in domain else 0)
        
    except:
        features.append(0)

    # Feature 21: qty_hyphen_domain
    try:
        features.append(domain.count('-') if '-' in domain else 0)
        
    except:
        features.append(0)

    # Feature 37: qty_vowels_domain
    try:
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U'])
        qty_vowels = sum(1 for c in domain if c in vowels)
        features.append(qty_vowels)
        
    except:
        features.append(0)

    # Feature 38: domain_length
    try:
        features.append(len(domain) if domain else 0)
        
    except:
        features.append(0)

# Dataset attributes based on URL directory.
    
    parsed_url = urlparse(url)
    # url_Path = Directory
    url_path = parsed_url.path.rsplit('/', 1)[0]

    if not url_path or url_path == '/':
      # url_path = -1
      for qty in range(18):
        features.append(-1)

    else:
      # Feature 41: qty_dot_directory

      features.append(url_path.count('.') if '.' in url_path else 0)
           
      # Feature 42: qty_hyphen_directory
      features.append(url_path.count('-') if '-' in url_path else 0)
          
      # Feature 43: qty_underline_directory
      features.append(url_path.count('_') if '_' in url_path else 0)
               
      # Feature 44: qty_slash_directory
      features.append(url_path.count('/') if '/' in url_path else 0)

      # Feature 45: qty_questionmark_directory
      features.append(url_path.count('?') if '?' in url_path else 0)

      # Feature 46: qty_equal_directory
      features.append(url_path.count('=') if '=' in url_path else 0) 

      # Feature 47: qty_at_directory
      features.append(url_path.count('@') if '@' in url_path else 0)   

      # Feature 48: qty_and_directory
      features.append(url_path.count('&') if '&' in url_path else 0)  

      # Feature 49: qty_exclamation_directory
      features.append(url_path.count('!') if '!' in url_path else 0)

      # Feature 50: qty_space_directory
      features.append(url_path.count(' ') if ' ' in url_path else 0)    

      # Feature 51: qty_tilde_directory
      features.append(url_path.count('~') if '~' in url_path else 0)   

      # Feature 52: qty_comma_directory 
      features.append(url_path.count(',') if ',' in url_path else 0) 

      # Feature 53: qty_plus_directory
      features.append(url_path.count('+') if '+' in url_path else 0)   

      # Feature 54: qty_asterisk_directory
      features.append(url_path.count('*') if '*' in url_path else 0)   

      # Feature 55: qty_hashtag_directory
      features.append(url_path.count('#') if '#' in url_path else 0)

      # Feature 56: qty_dollar_directory
      features.append(url_path.count('$') if '$' in url_path else 0)  

      # Feature 57: qty_percent_directory
      features.append(url_path.count('%') if '%' in url_path else 0)

      # Feature 58: directory_length 
      features.append(len(url_path) if url_path else 0)
             
# Dataset attributes based on URL ﬁle name.

    file_name = os.path.basename(urlparse(url).path)

    if not file_name or file_name == '/':
      # file_name = -1
      for qty in range(18):
        features.append(-1)

    else: 
      # Feature 59: qty_dot_file
      features.append(file_name.count('.') if '.' in file_name else 0)
           
      # Feature 60: qty_hyphen_file
      features.append(file_name.count('-') if '-' in file_name else 0)
          
      # Feature 61: qty_underline_file
      features.append(file_name.count('_') if '_' in file_name else 0)
               
      # Feature 62: qty_slash_file
      features.append(file_name.count('/') if '/' in file_name else 0)

      # Feature 63: qty_questionmark_file
      features.append(file_name.count('?') if '?' in file_name else 0)

      # Feature 64: qty_equal_file
      features.append(file_name.count('=') if '=' in file_name else 0) 

      # Feature 65: qty_at_file
      features.append(file_name.count('@') if '@' in file_name else 0)   

      # Feature 66: qty_and_file
      features.append(file_name.count('&') if '&' in file_name else 0)  

      # Feature 67: qty_exclamation_file
      features.append(file_name.count('!') if '!' in file_name else 0)

      # Feature 68: qty_space_file
      features.append(file_name.count(' ') if ' ' in file_name else 0)    

      # Feature 69: qty_tilde_file
      features.append(file_name.count('~') if '~' in file_name else 0)   

      # Feature 70: qty_comma_file 
      features.append(file_name.count(',') if ',' in file_name else 0) 

      # Feature 71: qty_plus_file
      features.append(file_name.count('+') if '+' in file_name else 0)   

      # Feature 72: qty_asterisk_file
      features.append(file_name.count('*') if '*' in file_name else 0)   

      # Feature 73: qty_hashtag_file
      features.append(file_name.count('#') if '#' in file_name else 0)

      # Feature 74: qty_dollar_file
      features.append(file_name.count('$') if '$' in file_name else 0)  

      # Feature 75: qty_percent_file
      features.append(file_name.count('%') if '%' in file_name else 0)

      # Feature 76: file_length 
      features.append(len(file_name) if file_name else 0)
       
    
# Dataset attributes based on URL parameters.

    params = urlparse(url).query

    if not params or params == None:
        # params = -1
        for qty in range(8):
          features.append(-1)
    else:
    
      # Feature 77: qty_dot_params
      features.append(params.count('.'))
      
      # Feature 79: qty_underline_params
      features.append(params.count('_'))
        
      # Feature 82: qty_equal_params
      features.append(params.count('='))
          
      # Feature 84: qty_and_params
      features.append(params.count('&'))
          
      # Feature 87: qty_tilde_params
      features.append(params.count('~'))
          
      # Feature 89: qty_plus_params
      features.append(params.count('+'))
      
      # Feature 92: qty_dollar_params
      features.append(params.count('$'))
          
      # Feature 94: params_length_characters
      features.append(len(params))
          
              
## Dataset attributes based on resolving URL and external services.

    # Extract domain name
    parsed_url = urllib.parse.urlparse(url)
    domain = parsed_url.netloc

    # Feature 98: Time to response
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()
        features.append(end - start)
    except:
        features.append(0.207 if not None else 0.207)
    
    # Feature 99: Presence of SPF record
    try:
        spf = dns.resolver.resolve(domain, 'TXT').response.answer[0][0].to_text()
        if 'v=spf' in spf:
            features.append(1)
        else:
            features.append(0)
    except:
        features.append(-1)
    
    # Feature 100: Autonomous System Number (ASN) of IP address
    try:
        ip = socket.gethostbyname(urlparse(url).netloc)
        asn = requests.get(f"https://ipapi.co/{ip}/asn/").text.strip()
        features.append(asn.strip('AS')) if asn else asn.strip('AS')
    except:
        features.append(0)

    # Feature 101: Time to domain activation
    try:
        domain = whois.query(url)
        creation_date = domain.creation_date
        if isinstance(creation_date, list):
            creation_date = creation_date[0]
        features.append((datetime.datetime.now() - creation_date).days)
            
    except:
        features.append(-1)
    
    # Feature 102: Time to domain expiration
    try:
        expiration_date = whois.query(domain).expiration_date
        today = datetime.datetime.now()
        features.append((expiration_date - today).days)           
    except:
        features.append(-1)
    
    # Feature 103: Quantity of resolved IPs
    try:
        ip_list = socket.getaddrinfo(domain, None)
        features.append(len(ip_list))
    except:
        features.append(-1)
    
    # Feature 104: Quantity of name servers
    try:
        domain = tldextract.extract(url).registered_domain
        ns_list = dns.resolver.resolve(domain, 'NS')
        features.append(len(ns_list))
    except:
        features.append(0)
    
    # Feature 105: Quantity of MX servers
    try:
        domain = tldextract.extract(url).registered_domain
        mx_list = dns.resolver.resolve(domain, 'MX')
        features.append(len(mx_list))
    except:
        features.append(0)
    
    # Feature 106: TTL value of hostname
    try:
        domain = tldextract.extract(url).registered_domain
        ttl = dns.resolver.resolve(domain, 'NS').rrset.ttl
        features.append(ttl)
    except:
        features.append(0)
    
    # Feature 107: Presence of TLS/SSL certificate
    try:
        with socket.create_connection((urlparse(url).netloc, 443)) as sock:
            with ssl.create_default_context().wrap_socket(sock, server_hostname=urlparse(url).netloc) as ssock:
                cert = ssock.getpeercert()
                if cert:
                    features.append(1)
                else:
                    features.append(0)
    except (ssl.SSLError, socket.gaierror, ConnectionRefusedError, TimeoutError):
        features.append(0)
    except Exception:
        features.append(0)
    
    # Feature 108: Number of redirects
    try:
        response = requests.get(url)
        if not response:
          features.append(-1)
        else:
          features.append(len(response.history))
    except:
        features.append(-1)

    # Feature 111: URL shortened

    response = requests.get(url, allow_redirects=False)

    if 'location' in response.headers:
        location = response.headers['location']
        if url.split('/')[2] != location.split('/')[2]:
            features.append(1)
        else:
            features.append(0)
    else:
        features.append(0)

    return features

    