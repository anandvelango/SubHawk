## Subhawk
![image](https://user-images.githubusercontent.com/50573902/232264242-adee7c20-4ad3-49b1-b2e5-ad1be3cd4536.png)
Subhawk is a python program that is used for discovering subdomains associated with a target domain in a fast efficient manner by utilising asynchronous programming techniques. SubHawk enumerates subdomains by reading through a wordlist file line by line, combining each entry with the target domain and it then sends asynchronous HTTP requests to each subdomain. This assists bug bounty hunters and penetration tester

## Features
- Asynchronous (fast results and customisable)
- Capable of using large wordlist files
- Option for outputting the results in a .txt file

## Installation

1. Clone the repository: 
```
git clone https://github.com/anandvelango/SubHawk.git
```
2. Change directory:
```
cd SubHawk
```
3. Install all the required modules
```
pip3 install -r requirements.txt
```

## Python Version Required
SubHawk supports at least Python 3.6.x so make sure you have at least Python 3.6.x installed on your system.

## Modules
- asyncio
- httpx
- time
- argparse
- colorama

## Wordlist file
You can use our current sample wordlist file `wordlists/subdomains.txt` from our repository but you can also use wordlists from your Kali machine or download some from internet. Use whichever you need.

## Usage

| Short form | Long form       | Description                                              |
|------------|-----------------|----------------------------------------------------------|
| -d         | --domain        | Domain in which you want to enumerate subdomains         |
| -w         | --wordlist-file | Path to wordlist file                                    |
| -o         | --output        | Output the results in a .txt file                        |
| -s         | --semaphores    | Adjust the semaphores (speed) if required (by default it's set to 60) |
| -h         | --help          | Show this help message and exit                          |

## Examples
- To get help about the tool:
```
python3 subhawk.py -h
```
- To find subdomains (always requires a wordlist file)
```
python3 subhawk.py -d example.com -w <path to wordlist file>
```
- Save the results in a file
```
python3 subhawk.py -d example.com -w <path to file> -o <file>.txt
```
- Adjust the semaphores (speed)
```
python3 subhawk.py -d example.com -w <path to file> -s <semaphores: int>
```

## Update Plans
- add a feature to validate domains and files specified by the user
- find URLs for cloud storage services like S3
- add more smaller and larger subdomain wordlists
