from stanfordcorenlp import StanfordCoreNLP

# Preset
# absolute local path to stanford-corenlp-4.5.1
path = "/home/vivitsa/Desktop/vivitsa-workspace/semantic-NER/stanford-corenlp-4.5.1"
nlp = StanfordCoreNLP(path)


# The sentence you want to parse
sentence ="""
Dear Stakeholders,
I want to begin by acknowledging a historic milestone – Wipro
crossed $10 billion in revenue this year. Congratulations!
From this vantage point, it seems impossible to believe that
Wipro was founded as a tiny oil mill in Amalner, Western India,
in 1945. No one could have predicted that one day, it would
morph into a global technology company with a presence
across 66 countries, employing over 240,000 people. I feel
humbled by the progress we have made in our 75-plus years,
but also immensely proud that we accomplished this while
remaining completely committed to our values.
(Stakeholders Relationship Committee)
Member

to reach approximately $178 billion in fiscal year
2022 and the domestic sector is forecasted to reach
approximately $49 billion in fiscal year 2022, growing at
approximately 10%.
28Wipro Limited | Ambitions Realized
Business overview
Celebrating over 75 years of innovation, Wipro is
a purpose-driven, global technology services and
consulting firm with over 240,000 employees and
business partners across 66 countries helping our
customers, communities and planet thrive in the
digital world.
We are recognized globally for our strong commitment
"""

# Recognizes named (PERSON, LOCATION, ORGANIZATION, MISC), numerical (MONEY, NUMBER, ORDINAL, PERCENT), and temporal (DATE, TIME, DURATION, SET) entities. Named entities are recognized using a combination of three CRF sequence taggers trained on various corpora, such as ACE and MUC. Numerical entities are recognized using a rule-based system. Numerical entities that require normalization, e.g., dates, are normalized to NormalizedNamedEntityTagAnnotation. For more details on the CRF tagger see this page. Sub-annotators: docdate, regexner, tokensregex, entitymentions, and sutime

test_sentence1 = """Month-Day-Year with leading zeros (02/17/2009), Day-Month-Year with leading zeros (17/02/2009), 
Year-Month-Day with leading zeros (2009/02/17), Month D, Yr, Month name-Day-Year with no leading zeros
(February 17, 2009), Month-Day-Year with no leading zeros (2/17/2009), Day-Month-Year with no leading zeros (17/2/2009),
 Year-Month-Day with no leading zeros (2009/2/17), Month-Day-Year with spaces instead of leading zeros
( 2/17/2009), Day-Month-Year with spaces instead of leading zeros
(17/ 2/2009), Year-Month-Day with spaces instead of leading zeros (2009/ 2/17), Month-Day-Year with no separators (02172009), 
Day-Month-Year with no separators (17022009), Year-Month-Day with no separators (20090217),
 Month abbreviation-Day-Year with leading zeros (Feb172009), Day-Month abbreviation-Year with leading zeros (17Feb2009),
Year-Month abbreviation-Day with leading zeros (2009Feb17), 
Year-Day of Year (counting consecutively from January  called the Julian date format), 
Day-Month name-Year (17 February, 2009), Year-Month name-Day (2009, February 17), Month abbreviation, Day with leading zeros, Year
(Feb 17, 2009), Day with leading zeros, Month abbreviation, Year
17 Feb, 2009, Year, Month abbreviation, Day with leading zeros
(2009, Feb 17). This format defaults to a two-digit year, but can be overridden to have four digits.
Month abbreviation, Day with leading zeros, Year
(Feb 17, 2014), Day with leading zeros, Month abbreviation, Year
(17 Feb, 2014), Year, Month abbreviation, Day with leading zeros
(2014, Feb 17), Eight-character hexadecimal representation of the system date.
 Valid dates range from 12/31/1969 to 01/18/2038. Valid dates may differ depending on the type of machine 
 (PC or host) and the type of CPU chip. 13-11-2017, 13.11.17. 25th December 2020, Date in words:twenty-first February, 2019.
"""

test_sentence2 = """1 The above stated investments are gross investments and are invested for short duration and redeemed thereafter.
Annexure C
Annual Report 2018-1947Strategic review Governance People and CSRMDAAbout Alembic Statutory reports Financial statements
Nature of Transaction
(whether loan/
guarantee/ investments
Date of granting loans,
giving guarantee or making
investments
Name and address of the person or body
corporate to whom it is made or given or
whose securities have been acquired
Amount
USD Million
Purpose of loan/ guarantee/
investment
Guarantee 30.04.2018 Alembic Pharmaceuticals Inc.,
750 Highway 202, Bridgewater, NJ 08807
5.00 To support step down
subsidiary of the
Company for its business
requirements
Guarantees 10.07.2018 Alembic Global Holding SA (AGH),
Rue Fritz – Courvoisier 40,
2300 La Chaux-de-Fonds, Switzerland
5.001 To support 100% subsidiary
of the Company for its
business requirements
20.08.2018 5.002
17.12.2018 5.00
1 Outstanding borrowing by AGH against the said guarantee as on 31st March, 2019 is Nil.
2 Outstanding borrowing by AGH against the said guarantee as on 31st March, 2019 is USD 2 Million.
On behalf of the Board of Directors,
Sd/-
Chirayu Amin
Chairman & Chief Executive Officer
(DIN: 00242549)
48Alembic Pharmaceuticals Limited
Secretarial Audit Report
For the financial year ended 31st March, 2019
[Pursuant to Section 204(1) of the Companies Act, 2013 and Rule 9 of the Companies (Appointment and Remuneration
of Managerial Personnel) Rules, 2014 and Regulation 24A of SEBI (Listing Obligations and Disclosures Requirements)
Regulations, 2015]
To,
The Members,
Alembic Pharmaceuticals Limited
Alembic Road,
Vadodara- 390 003
Gujarat.
We have conducted the Secretarial Audit of the compliance
of applicable statutory provisions and the adherence to
good corporate practices by Alembic Pharmaceuticals
Limited (the Company). Secretarial Audit was conducted in a
manner that provided us a reasonable basis for evaluating the
corporate conducts / statutory compliances and expressing
our opinion thereon.
"""

test_sentence3 = """
46Alembic Pharmaceuticals Limited
Particulars of Loans granted, Guarantees given or Investments made by the Company
Nature of Transaction (whether
loan/ guarantee/ investments)
Date of granting loans,
giving guarantee or
making investments
Name and address of the person or body
corporate to whom it is made or given or whose
securities have been acquired
Amount
(` in Crores)
Purpose of loan/
guarantee/ investments
Investment in Secured
Debentures
04.04.2018 Aleor Dermaceuticals Limited 5th Floor,
Administrative Building, Alembic Limited,
Alembic Road, Vadodara - 390 003
15.00 Project under
implementation /
Research &
Development
30.04.2018 20.00
Investment in Unsecured
Debentures
06.06.2018 20.00
16.07.2018 30.00
24.08.2018 25.00
01.10.2018 30.00
03.12.2018 25.00
03.01.2019 30.00
22.03.2019 12.50
Investments in liquid
scheme of Mutual Fund1
12.11.2018 Reliance Nippon Life Asset Management
Limited"""

# NER
def _create_list_for_entity(output,entity):
   entity_list = []
   entity_list.append(entity)
   for res in output:
      if res[1]==entity:
         entity_list.append(res[0])
   return entity_list



def sort_by_entity(sentence):
   sorted_output = []
   entities = ['PERSON', 'LOCATION', 'ORGANIZATION', 'MISC','MONEY', 'NUMBER', 'ORDINAL', 'PERCENT','DATE', 'TIME', 'DURATION', 'SET']
   output = nlp.ner(sentence)
   nlp.close()
   for entity in entities:
      x = _create_list_for_entity(output,entity)
      if x:
         sorted_output.append(x)
   return sorted_output
print(sort_by_entity(test_sentence3))
