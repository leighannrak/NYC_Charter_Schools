# NYC_Charter_Schools
This repository contains a map of all charter schools in NYC.

Data Sources:

1. NY State Education Department (NYSED)
   URL: https://www.nysed.gov/charter-schools/charter-schools-directory
   Credibility: Official New York State education agency.
   Purpose: Obtain an up-to-date list of charter schools.
   Key Information: School name, Institution ID, County.
   File: NYC_Charter_School_Directory.xlsx

2. State Education Data Reference File (SEDREF)
   URL: https://eservices.nysed.gov/sedreports/ReportList?id=1
   Report: Active Charter Schools with Payee, CEO & Physical Address Info
   Credibility: Official NYSED educational institution resource.
   Purpose: Cross-reference schools and obtain physical addresses.
   Key Information: Institution ID, Lattitude, Longitude.
   File: NYC_Charter_Schools_Address.csv

High-Level Methodology:
1. Load and clean datasets.
2. Filter schools within NYC's five counties: Bronx, Kings, New York, Queens, and Richmond.
2. Merge datasets using Institution ID.
4. Use Folium to generate an interactive map with school markers.


How To Run:
1. Open and update the API Key in line 50- it will be provided through email. Save the file.
2. Run the Python script: python merge_schools.py
3. Open index.html in your browser to see the map.
