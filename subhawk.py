# modules
import asyncio
import httpx
import time
import argparse
import re
import sys
import colorama
from colorama import Fore

colorama.init(autoreset=True)

# banner
banner = f"""
{Fore.LIGHTBLUE_EX}              .:=+  
{Fore.LIGHTBLUE_EX}-:            *=#%*-
{Fore.LIGHTBLUE_EX}+@*-          %@@@@*
{Fore.LIGHTBLUE_EX} %@@%-      .+@@@@@%
{Fore.LIGHTBLUE_EX}  .#@@+     *@@@@@@+    
{Fore.LIGHTBLUE_EX}    @@@= :+%@@@@@@# 
{Fore.LIGHTBLUE_EX}   -%@@@%@@@@@@@@@: 
{Fore.LIGHTBLUE_EX}  -@@@@@@@@@@@@*+.  
{Fore.LIGHTBLUE_EX}  .: #@@@@@#-.      {Fore.YELLOW}╔═╗┬ ┬┌┐ ╦ ╦┌─┐┬ ┬┬┌─
{Fore.LIGHTBLUE_EX}  ..#@%@@@@@@#=.    {Fore.YELLOW}╚═╗│ │├┴┐╠═╣├─┤│││├┴┐
{Fore.LIGHTBLUE_EX} :-*-.#@%@@@@@@%    {Fore.YELLOW}╚═╝└─┘└─┘╩ ╩┴ ┴└┴┘┴ ┴
{Fore.LIGHTBLUE_EX}    +#=.  :--:. 

{Fore.YELLOW} # Asynchronous subdomain scanner that finds subdomains fast and efficiently
{Fore.YELLOW} # Created by @anz1x
""" 

# parsing args
def parse_args():
    parser = argparse.ArgumentParser(
        prog="subhawk.py",
        description=print(banner),
        )
        
    parser.add_argument(
        "-d", 
        "--domain", 
        help="Domain name (e.g. google.com)",
        type=str, 
        required=True
        )
    parser.add_argument(
        "-w", 
        "--wordlist-file", 
        help="Path to wordlist file (e.g. /usr/share/wordlists/rockyou.txt)",
        type=str, 
        required=True
        )
    parser.add_argument(
        "-o",
        "--output",
        help="Output the results in a .txt file (e.g. <file>.txt)",
        type=str,
        required=False
    )
    parser.add_argument(
        "-s",
        "--semaphores",
        help="By default its 100 but adjust it to your needs (anywhere 50-250 is recommended and you can increase it even more if needed)",
        type=int,
        required=False
    )
    
    return parser.parse_args()

# args
args = parse_args()

def get_domain():
    domain = args.domain
    pattern = re.compile("^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$")
    if pattern.match(domain) == None:
        print(f"{Fore.RED}[!]{Fore.RESET} {domain} is not a valid domain")
        sys.exit(1)
        
    return domain 

# gets semaphores (default if not specified by the user)
def get_semaphores():
    if args.semaphores:
        semaphore = asyncio.Semaphore(args.semaphores)
        return semaphore
    else:
        semaphore = asyncio.Semaphore(100)
        return semaphore

# gets the subdomains from the wordlist file
def get_subdomains():
    file = args.wordlist_file    
    f = open(file, "r")
    content = f.read()
    subdomains = content.splitlines()
    f.close()
    
    return subdomains

# handles each request made to the subdomain
async def request(semaphore, url):
    async with semaphore:
        async with httpx.AsyncClient(timeout=5) as client:
            try: 
                response = await client.get(url)
                if response.status_code < 400:
                    return url
            except (httpx.RequestError, httpx.TimeoutException):
                pass

# grabs the subdomains        
async def main():
    reqs = []
    domain = get_domain()
    subdomains = get_subdomains()
    semaphore = get_semaphores()
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        req = asyncio.ensure_future(asyncio.ensure_future(request(semaphore, url)))
        reqs.append(req)
            
    responses = await asyncio.gather(*reqs)
    valid_responses = filter(lambda x: x != None, responses)
    results = ""
    for response in valid_responses:
        print(f"{Fore.LIGHTGREEN_EX}[!]{Fore.RESET} {response}")   
        results += f"{response}\n"
    
    # if the user specifies to output the results in a file
    output = args.output
    file = args.wordlist_file
    if output:
        with open(output, "w") as f:
            f.write("SubHawk Results\n")
            f.write(f"Target: {domain}\n")
            f.write(f"Wordlist used: {file}\n")
            f.write(f"Subdomains found: \n")
            f.write(results)
        print(f"{Fore.YELLOW}[>]{Fore.RESET} Results saved in {Fore.YELLOW}{output}")
               

if __name__ == "__main__":        
    
    print(f"{Fore.LIGHTBLUE_EX}[*]{Fore.RESET} Enumerating subdomains for {Fore.LIGHTGREEN_EX}{get_domain()}\n")

    start_time = time.perf_counter()        
    asyncio.run(main())
    end_time = time.perf_counter()

    total_duration = end_time-start_time
    print(f"{Fore.YELLOW}[>]{Fore.RESET} Total Duration: {Fore.YELLOW}{round((total_duration), 2)}s")
