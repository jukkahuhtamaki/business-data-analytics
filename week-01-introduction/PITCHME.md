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

## Methodology big picture

![Road to data scientist](http://nirvacana.com/thoughts/wp-content/uploads/2013/07/RoadToDataScientist1.png)

Image source: http://nirvacana.com/thoughts/becoming-a-data-scientist/

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

## Learning outcomes

<!-- Osaamisperusteisessa opetussuunnitelmassa pääpaino on opiskelijassa ja hänen oppimistyössään. Opetussuunnitelma pohjautuu osaamistavoitteisiin (learning outcomes), jossa tutkintojen, opintokokonaisuuksien ja opintojaksojen tavoitteet kuvataan opiskelijan tavoiteltuna oppimistuloksina. Osaamistavoitteet esittävät tavoiteltua tilaa, jotka ilmaistaan tietoina, taitoina ja asenteina.
* osaamistavoitteet laaditaan ydinainesanalyysin pohjalta
* osaamistavoitekuvaus alkaa aina lausekkeella "Opintojakson suoritettuaan opiskelija osaa..."
* osaamistavoitteiden kuvuksessa käytetään verbejä (Bloomin taksonomia), joista ilmenee vaadittu osaamisen vähimmäistaso. -->

After completing the course, the student knows a core set of BDA approaches and their applications and is able to ...

- identify main sources of business data and data quality requirements conducive to data-driven culture |
- explain the difference between exploratory, descriptive, predictive, and prescriptive analytics in the context of BDA |
- apply unsupervised, semi-supervised, and supervised learning to conduct BDA |
- utilize visual analytics to share BDA insights to support decision-making |
- design data-processing pipelines for reproducible BDA |

---

## Approach /Philosophy

* Flipped classroom: students will receive tasks, videos, and material before each class
* Connected learning: we use real-life tools and information sources
* Authentic learning: real-life business data (you can bring your own)
* Social constructivist: exercise work is built in phases and presented to other students for peer learning

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

## 1. Single source of truth

* Starting point: [master data](https://en.wikipedia.org/w/index.php?title=Master_data&oldid=815247077)
* Example 1: [Inside Airbnb](http://insideairbnb.com/get-the-data.html)


---
## Five dimensions

*  

---

## Process model: CRISP-DM
<p><a href="https://commons.wikimedia.org/wiki/File:CRISP-DM_Process_Diagram.png#/media/File:CRISP-DM_Process_Diagram.png"><img src="https://upload.wikimedia.org/wikipedia/commons/b/b9/CRISP-DM_Process_Diagram.png" alt="CRISP-DM Process Diagram.png" height="900" width="898"></a><br>By <a href="//commons.wikimedia.org/w/index.php?title=User:Kennethajensen&amp;action=edit&amp;redlink=1" class="new" title="User:Kennethajensen (page does not exist)">Kenneth Jensen</a> - Own work based on: <a rel="nofollow" class="external free" href="ftp://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/18.0/en/ModelerCRISPDM.pdf">ftp://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/18.0/en/ModelerCRISPDM.pdf</a> (Figure 1), <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=24930610">Link</a></p>

---

## Process model: Lean analytics

---

---

![Modern data scientist](http://i.imgur.com/4ZBBvb0.png)

---

 ## The End.






# End of introduction
