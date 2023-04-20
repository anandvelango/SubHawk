## Subhawk
![image](https://user-images.githubusercontent.com/50573902/233224889-92c317b9-64a2-42a7-9f24-345a749c33ce.png)


Subhawk is a python worlist-based tool that is used for discovering subdomains associated with a target domain in a fast efficient manner by utilising asynchronous programming techniques. SubHawk enumerates subdomains by reading through a wordlist file line by line, combining each entry with the target domain and it then sends asynchronous HTTP requests to each subdomain. This assists bug bounty hunters and penetration tester

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
![image](https://user-images.githubusercontent.com/50573902/233226148-5f4e1487-4d03-49d6-8147-c0cad0836ae2.png)
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
