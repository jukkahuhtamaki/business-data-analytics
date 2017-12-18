<!-- PITCHME.md

# Hello, World! -->

# Course plan for a course in Business Data Analytics (10 minutes)

---
## Outline

- Introduction to business analytics
- Collecting and accessing business data |
- Exploratory and descriptive BDA, unsupervised learning |
- Predictive BDA, supervised learning |
<!-- * Supervised and unsupervised learning -->
- Data-driven decision making culture |
- Data products and prescriptive analytics |
- Visualization for sensemaking and decision-making |
<!-- * Ecosystem analytics -->

---

## Analytics 3.0

is a "a new resolve to apply powerful data-gathering and analysis methods not just to a company’s operations but also to its offerings–to embed data smartness into the products and services customers buy."

([Thomas Davenport, 2013](https://hbr.org/2013/12/analytics-30))

---

## Business data

![Business data big picture](week-01-introduction/image/bigdata_diagram.png)

<!-- ![Business data big picture](https://2xbbhjxc6wk3v21p62t8n4d4-wpengine.netdna-ssl.com/wp-content/uploads/2012/05/bigdata_diagram.png) -->

  <!-- bigdata_diagram.png "Business data big picture") -->

Image source: https://hortonworks.com/blog/7-key-drivers-for-the-big-data-market/

---

## Course technology stack

We take an interactive computing approach to data analytics (cf. data science)

* Python3*
* Pandas & SFrame (Scipy)
* scikit-learn ([Apple Turi](https://github.com/apple/turicreate))
* NetworkX
* Jupyter, IPython, [CSC Notebooks](https://www.csc.fi/web/blog/post/-/blogs/notebooks-enemman-aikaa-opetuksen-ytimelle)
* Highcharts, D3.js

<span style="font-size: small;">\*Compatibility with basic studies and specialization studies in machine learning, e.g.,
[SGN-41007 Pattern Recognition and Machine Learning](http://www.cs.tut.fi/courses/SGN-41007/)</span>

---

## Learning outcomes 1/2

<!-- Osaamisperusteisessa opetussuunnitelmassa pääpaino on opiskelijassa ja hänen oppimistyössään. Opetussuunnitelma pohjautuu osaamistavoitteisiin (learning outcomes), jossa tutkintojen, opintokokonaisuuksien ja opintojaksojen tavoitteet kuvataan opiskelijan tavoiteltuna oppimistuloksina. Osaamistavoitteet esittävät tavoiteltua tilaa, jotka ilmaistaan tietoina, taitoina ja asenteina.
* osaamistavoitteet laaditaan ydinainesanalyysin pohjalta
* osaamistavoitekuvaus alkaa aina lausekkeella "Opintojakson suoritettuaan opiskelija osaa..."
* osaamistavoitteiden kuvuksessa käytetään verbejä (Bloomin taksonomia), joista ilmenee vaadittu osaamisen vähimmäistaso. -->

After completing the course, the student knows ...

- a core set of BDA approaches and their applications |
- the sources of business data and data quality requirements conducive to data-driven culture |
- the difference between exploratory, descriptive, predictive, and prescriptive analytics in the context of BDA |

---
## Learning outcomes 2/2

After completing the course, the student is able to ...

- apply unsupervised, semi-supervised, and supervised learning to conduct BDA |
- utilize visual analytics to share BDA insights to support decision-making |
- design data-processing pipelines for reproducible BDA |

---

## Approach /Philosophy

* **Flipped classroom**: students will receive material before each lecture where we focus on hands-on analytics in an interactive manner
* **Connected learning**: we use real-life tools and information sources
* **Authentic learning**: real-life business data (you can bring or select your own)
* **Social constructivist:** exercise work is built in phases and presented to other students for peer learning

---

## Learning diary

You will describe each weeks' topic from your viewpoint

* **Applied vs. list-like**: synthesize course content further
* **Reflective**: describe how course content relates to your knowledge
* **Extending and generalizing**: build on what you learned and point to future directions
* **Completeness and validity**: cover the core topics and get the facts straight

---

## Exercise work

Exercise work is split into six steps, each of which is reported on course social media platform:

* **Data source**: select or collect
* **Refine data**: clean data, design features
* **Explore and describe the data**
* **Implement BDA of choice**: predict, classify, segment
* **Data product**: implement prescriptive feature or build a dashboard
* **Evaluate and report**

---
<!--
Philosophy

Introduction to business analytics
* Analytics 3.0 (Davenport)
* Examples and use cases

Code clinic: Vuorovaikutteinen laskenta  
* Komentorivityövälineet
* Setting up data analytics pipeline: Anaconda; Pandas, scikit-learn; SFrame; IPython; Jupyter

Collecting and accessing business data
* Business data categories
* ETL (business intelligence) vs. crawling & scraping (data science)
* Data formats and means to process: structured, tabular, temporal, network
* Code clinic: data-centric programming

Datan kerääminen ja siivoaminen
* Raapijat ja ryömijät; dataformaatit ja niiden ohjelmallinen käsittely; datakeskeinen ohjelmointi  

Predictive analytics
* Linear regression
* Multiple regression
* Business analytics applications: churn analysis
* Ennakoiva analytiikka Lineaarinen regressio; monimuuttujaregressio  

Supervised and unsupervised learning
* Classification
* Clustering
* Market basket analysis, http://pbpython.com/market-basket-analysis.html
* Ohjaamaton ja ohjattu oppiminen Luokittelu; ryvästäminen  

Visualization for sensemaking and decision-making
* Datatuotteet ja ohjelmallinen visualisointi
* Datatuotteen arkkitehtuuri
* Vuorovaikutteisen visualisoinnin toteuttaminen
* Javascript-visualisointikirjastot
 -->

---

# Short teaching demonstration (15 minutes)

---

# Data-driven culture

1. Single source of truth
2. Data dictionary
3. Broad data access
4. Data literacy
5. Decision making

Cf. Anderson and Li ([2017](https://techcrunch.com/2017/06/23/five-building-blocks-of-a-data-driven-culture/))

---
## 0. Discussion

Before we begin, let's discuss the exercise on [predicting Airbnb listing prices](https://mapr.com/blog/predicting-airbnb-listing-prices-scikit-learn-and-apache-spark/)

* Which level of performance did you reach?
* What were the key design decision that led to this performance?
* How should the dataset be developed further to improve the performance?
* Give three examples of business decisions on basis of your analysis!

---

## 1. Single source of truth

<!-- Starting point: [master data](https://en.wikipedia.org/w/index.php?title=Master_data&oldid=815247077) -->

<blockquote style="font-size: smaller; text-align: left;">"The management of master data (such as customer, material, and supplier data) plays an important role for companies in responding to a number of business drivers such as regulatory compliance, integrated customer management, and efficient reporting in the sense of a 'single version of the truth' [22]. Master data management (MDM) is an application-independent process for the description, ownership and management of core business data entities
[[2](https://dl.acm.org/citation.cfm?id=1593444&CFID=841672660&CFTOKEN=35335552),
[17](http://aisel.aisnet.org/cais/vol23/iss1/4/)]." ([Otto and Reichert, 2010](https://doi.org/10.1145/1774088.1774111))</blockquote>

Example 1: [Inside Airbnb](http://insideairbnb.com/get-the-data.html)

---

## 2. Data dictionary

<blockquote style="font-size: smaller; text-align: left;">"Metadata is arguably the foundation upon which Data Governance is built; it is critical for Master Data hubs to conform to governance protocols to advantageously affect business processes and the underlying data required for them." ([Kempe, 2015](http://www.dataversity.net/confluence-metadata-master-data-management-data-modeling/))</blockquote>

---
## 3. Broad data access

Cohen et al. ([2009](https://doi.org/10.14778/1687553.1687576)) suggest that modern business data analysis insists MAD skills (competences)

* **Magnetic**: Data repositories should draw instead of repel dataset
* **Agile**: "easily ingest, digest, produce and adapt data at a rapid pace"
* **Deep**:  "enormous datasets without resorting to samples and extracts"

---
# 4. Data literacy

<!-- ---
<div style="height=800;">![Modern data scientist](http://i.imgur.com/4ZBBvb0.png)</div> -->

---?image=http://i.imgur.com/4ZBBvb0.png&size=auto 90%

---
## Methodology big picture

<p><img width="800" src="http://nirvacana.com/thoughts/wp-content/uploads/2013/07/RoadToDataScientist1.png" alt="Road to data scientist" /></p>

Image source: http://nirvacana.com/thoughts/becoming-a-data-scientist/

---

---

# 5. Decision making
---
## Avoiding HiPPos

In [Big Data: The Management Revolution](https://hbr.org/2012/10/big-data-the-management-revolution)
McAfee and Brynjolfsson

* suggest that businesses should commit to data-driven decision making culture
* to mute the HiPPOs - "the highest-paid person’s opinion"

---
## Process 1: CRISP-DM
<p><a href="https://commons.wikimedia.org/wiki/File:CRISP-DM_Process_Diagram.png#/media/File:CRISP-DM_Process_Diagram.png"><img width="563" height="564" src="https://upload.wikimedia.org/wikipedia/commons/b/b9/CRISP-DM_Process_Diagram.png" alt="CRISP-DM Process Diagram.png"></a><br>By <a href="//commons.wikimedia.org/w/index.php?title=User:Kennethajensen&amp;action=edit&amp;redlink=1" class="new" title="User:Kennethajensen (page does not exist)">Kenneth Jensen</a> - Own work based on: <a rel="nofollow" class="external free" href="ftp://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/18.0/en/ModelerCRISPDM.pdf">ftp://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/18.0/en/ModelerCRISPDM.pdf</a> (Figure 1), <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=24930610">Link</a></p>

---

## Process 2: Lean analytics

<!-- <div style="width: 600px; text-align: center"> -->

![Lean analytics cycle](https://github.com/jukkahuhtamaki/business-data-analytics/raw/master/week-01-introduction/image/lean-analytics-cycle.png)

<!-- </div> -->

---

## Recap

How to enable data-driven decision-making culture in business context?

---

## Outlook: next week

...
