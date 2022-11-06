In this project it will be apporached the extraction on valuable data regarding Nobel Prize Laureates.

Data Preparation:

- Wikipedia information will be pulled out using the Wikipedia package making use of the built-in API.
- In order to pull the information, the list of people names will be pulled out. 
(ISSUES: It has been found a total of 950 winners. However not all of them consitute personal entities, including organizations. Stated in the column <ind_or_org>, only individuals will be inlcuded in the analysis)
(EVOLUTION: Year vs Prize)
(DATA PREPARATION: After pulling the names, it will be removed the "Sir" monosyillabus, to optimize the query process.)