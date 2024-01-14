# MK1_FightData
The primary objective of this project was to efficiently scrape web data pertaining to Mortal Kombat 1 frame data, a critical component studied by elite players for high-level gameplay. The script is specifically tailored to extract data from the website wiki.supercombo.gg, one of the few sources that comprehensively cover Mortal Kombat 1 frame data. 

The process involves constructing URLs for each character by appending their names to a base URL. An HTTP request is then made to these URLs to fetch the webpage content. Upon a successful request, Beautiful Soup is employed to parse the HTML content of the page, focusing on specific sections and tables that contain vital move data for each character, identifiable by unique HTML class attributes.

The script meticulously extracts and organizes this data, displaying move names along with their detailed attributes in a structured format. In instances of unsuccessful data retrieval, the script promptly indicates a failure to fetch data. This methodical approach

The primary objective of this project was to efficiently scrape web data pertaining to Mortal Kombat 1 frame data, a critical component studied by elite players for high-level gameplay. The script is specifically tailored to extract data from the website wiki.supercombo.gg, one of the few sources that comprehensively cover Mortal Kombat 1 frame data. 

The process involves constructing URLs for each character by appending their names to a base URL. An HTTP request is then made to these URLs to fetch the webpage content. Upon a successful request, Beautiful Soup is employed to parse the HTML content of the page, focusing on specific sections and tables that contain vital move data for each character, identifiable by unique HTML class attributes.

The script meticulously extracts and organizes this data, displaying move names along with their detailed attributes in a structured format. In instances of unsuccessful data retrieval, the script promptly indicates a failure to fetch data. This methodical approach facilitates automated and efficient data extraction from webpages with similar structures, proving invaluable for tasks such as data aggregation, analysis, and integration into other applications or databases. The ultimate goal is to format this extracted data suitably for incorporation into an Excel spreadsheet, streamlining the process of data analysis and usage.
