# Sales Process Automation using Python and AI/ML

A powerful sales process automation tool built to simplify lead generation, email campaigns, and lead categorization. This tool scrapes company data from websites like LinkedIn and Google. It supports two modes:

With API: Scrapes data using ScrapingDog API and SerpAPI.

Without API: Scrapes specific websites and performs multi-domain searches without requiring any API keys.

The tool handles email campaigns and provides in-depth analytics to optimize outreach efforts.
## Full Documentation Link :-
https://drive.google.com/file/d/1TIytpj_AqGQjVZNiJniATd3MMz9_4vIq/view?usp=sharing

## Table of Contents
- [Installation](#installation)
- [API Setup](#api-setup)
- [How to Use](#how-to-use)
- [Running the Tool](#running-the-tool)
- [File Structure](#file-structure)
- [Dependencies](#dependencies)
- [License](#license)

---

## Installation

Follow these steps to set up and run the **Sales Automation Tool** on your local machine:

1. **Clone the Repository**
   First, clone the repository to your local machine:
   ```bash
   git clone https://github.com/DhruvPanchal8055/Sales-Process-Automation-.git
   cd sales-automation-tool
   
##Create a Virtual Environment (optional but recommended) It's a good idea to create a virtual environment to isolate your project’s dependencies:
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

##Install Dependencies Install the required dependencies:

1. **Requirement Files**
   ```bash
     pip install -r requirements.txt

## API Setup

Using Without API (Option 1 and Option 4):
You can use this tool without the ScrapingDog API or SerpAPI for Option 1 (Specific Website Scraping) and Option 4 (Multi-Domain Search).

Option 1: Scrape a specific website directly using requests and BeautifulSoup, without needing any API key.

Option 4: Scrape Ideal Customer Profile (ICP) data from multiple domains. This option also does not require any API key.

ScrapingDog API and SerpAPI Setup (Optional for Option 2 and 3):
You can also use SerpAPI and ScrapingDog API for more advanced scraping, such as:

Option 2: General Search using SerpAPI for Google or LinkedIn searches.

Option 3: Scraping full LinkedIn company profiles using ScrapingDog API.

SerpAPI (General Search) Setup:
Sign Up for SerpAPI: To use SerpAPI, sign up at SerpAPI, and get an API key. This will allow you to scrape general search results like Google or LinkedIn.

Free Trial:
SerpAPI offers a free trial that allows you to scrape up to 10 profiles. After using up the free trial, you can choose to upgrade or wait for the quota to reset.

Set Up the API Key: Replace the placeholder your_serpapi_api_key with your actual API key in the code when you choose to scrape Google or LinkedIn search results via SerpAPI.

ScrapingDog API (LinkedIn Profile Scraping) Setup:
Sign Up for ScrapingDog: Sign up at ScrapingDog to get an API key for scraping detailed LinkedIn profiles.

Free Trial:
ScrapingDog also offers a free trial that allows you to scrape up to 10 LinkedIn profiles. Once the free trial quota is exhausted, you’ll need to upgrade or wait for it to reset.

Set Up the API Key: Replace the placeholder your_scrapingdog_api_key with your actual ScrapingDog API key in the code when scraping LinkedIn profiles.


# Run the Tool: After activating the virtual environment and installing dependencies, you can run the project using:


Copy
python main.py
Scraping Data:
You can choose from different scraping options:

Option 1: Specific Website Scraping (No API) - Scrape a specific website directly using requests and BeautifulSoup without needing any API key.

Option 2: General Search with SerpAPI - Use SerpAPI to perform Google or LinkedIn searches by specifying parameters like industry, company size, tech stack, etc. (API key required).

Option 3: Full LinkedIn Company Profiles (ScrapingDog API) - Use ScrapingDog API to scrape full LinkedIn company profiles (API key required).

Option 4: Multi-Domain Search (No API) - Scrape multiple domains for Ideal Customer Profile (ICP) data without the need for any API key.

Email Campaign Automation:
The tool also allows you to send automated email campaigns and track the results (open rates, click-through rates, etc.).

Running the Tool
To set up and automatically install dependencies, as well as run the main.py script, you can execute the setup.py:

# Run Setup:

2. ****
   First, Run This After Setup.py:
   ```bash
     python setup.py
This will:

Install all necessary dependencies.

Automatically execute the main.py script after installation.

3. ****
   File Structure:
   ```bash
     
   Sales Automation Tool
   ├── Analytics/              # Folder for storing analytics data
   ├── Scripts/                # Python scripts for different scraping modules
   ├── output/                 # Folder for storing output files
   ├── main.py                 # Main entry point for the tool
   ├── requirements.txt        # List of dependencies for the project
   ├── setup.py                # Setup script to install dependencies and run the tool
   ├── README.md               # Project documentation (this file)
     └── LICENSE                 # Project license
   


requests: For making HTTP requests.

beautifulsoup4: For parsing HTML content.

pandas: For managing and analyzing data.

openpyxl: For reading and writing Excel files.

rich: For enhanced terminal output.

serpapi: For scraping Google and LinkedIn search results (optional, for Option 2).

scrapingdog: For scraping LinkedIn company profiles (optional, for Option 3).
.

# Notes:
Be sure to replace your ScrapingDog API key and SerpAPI API key in the main.py file if you are using their services.

ScrapingDog helps you bypass CAPTCHA, IP bans, and other blocking mechanisms, making it ideal for scraping dynamic sites like LinkedIn.

You can extend this tool by adding more scraping options or improving the email campaign logic.

# Created by:
   Dhruv Panchal

Free Trial Notes:
SerpAPI and ScrapingDog both offer free trials that allow you to scrape up to 10 profiles. You can get started with these APIs and test the functionality. After the free trial is used, you'll need to upgrade to a paid plan or wait for it to reset.

## 📸 Screen Shots 📸
![1](https://github.com/user-attachments/assets/465f3cf5-aa6b-4274-b14f-c76eb69c97b9)

![image](https://github.com/user-attachments/assets/c88b38d8-86cf-4a90-a60b-9d763cccc1c3)

![image](https://github.com/user-attachments/assets/2e0be871-7e9a-4fd3-91d2-469310816acc)

![image](https://github.com/user-attachments/assets/dacb35b0-6bd6-480a-88ab-27dc338a045e)










