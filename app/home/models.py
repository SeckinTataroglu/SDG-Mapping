
from flask import current_app
from os import walk
import sqlite3
import pdfminer
from pdfminer.high_level import extract_text
import docx2txt
from docx2txt import process
import pandas as pd
import string
import re
from io import TextIOWrapper
import ast
# import os

# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# import __init__ as init

# # current_app.config["SQLALCHEMY_DATABASE_URI"]
# dbName = SQLALCHEMY_DATABASE_URI
# print(dbName)




# PDF Parser
def pdfParser(file, maxPage = None):
    return extract_text(file, maxpages=maxPage)

# DOCX Parser
def docxParser(filePath):
    return process(filePath)

# Punctuation Mark Remover
def removePunc(text):
    text = re.sub(r"’", "'", text) # Quotation mark stability
    return " ".join(re.findall(r"[\w\-\—']+", text))  # C-Level code, the fastest ever


# Total Word Counter
def wordCount(text):
    textSplitted = text.lower().split()    
    iterStep = len(textSplitted) #-word.count(" ")    
    countAll = dict()
    for wordIndex in range(iterStep):        
        countAll[textSplitted[wordIndex]] = countAll.get(textSplitted[wordIndex], 0) + 1
    
    return countAll


# SDG Counter
def sdgCount(text, keywords):
    print("started function")
    textSplitted = text.lower().split()
    # print(textSplitted)
    countSDG = dict()
    for key, wordList in keywords.items():
        countSDG[key] = {}

        for word in wordList:
            # print(key, word)
            if word.count(" ") == 0:    # If it is a single word
                tmpCount = textSplitted.count(word)
                if tmpCount != 0:
                    countSDG[key][word] = tmpCount
            else:                       # If it is a phrase
                iterStep = len(textSplitted)-word.count(" ")
                inputWordCount = word.count(" ") + 1
                inputWordList = word.split()

                for wordIndex in range(iterStep):
                    # print(textSplitted[wordIndex:wordIndex+inputWordCount])
                    if textSplitted[wordIndex:wordIndex+inputWordCount] == inputWordList:
                        countSDG[key][word] = countSDG[key].get(word, 0) + 1
                    
    return countSDG


# SDG Counts Total
def sdgCountTotal(countDict):
    SDGTotal = dict()
    for k, v in countDict.items():
        SDGTotal[k] = sum(v.values())
    
    return SDGTotal


# Allowed Document Types
def allowed_doc(filename):
    if any("." not in doc.filename for doc in filename):
        return False

    
    ext = []
    for files in filename:
        print("filename", files.filename)
        ext.append(files.filename.rsplit(".", 1)[1].upper())

    for i in ext:
        print("ext name", i)
    if all(doc in current_app.config["ALLOWED_DOC_EXTENTIONS"] for doc in ext):
        return True
    else:
        return False


# Return The File
def getFile():

    fullText = {}
    path = current_app.config["UPLOADS"]

    # Getting Files List
    filesList = []
    for (dirpath, dirnames, filenames) in walk(path):
        filesList.extend(filenames)
    # Placing Everything in a Dictionary
    maxPages = 3
    for files in filesList:
        if files[-3:].lower() == "pdf":
            fullText[files] = removePunc(pdfParser(r"{}\{}".format(path, files), maxPages))[:1000]    
        else:
            fullText[files] = removePunc(docx2txt.process(r"{}\{}".format(path, files)))[:1000]
    print(fullText.keys)
    return fullText.keys









# Check DB for 5 pages
def checkSQL51000(filePath):

    ResearchKeywords = {'SDG1': ['asylum seeker', 'basic services', 'developing countries', 'disadvantaged', 'financial inclusion', 'microfinance', 'non-discrimination', 'poverty', 'refugee', 'social protection', 'third world', 'vulnerable', 'wealth distribution'], 'SDG2': ['agricultural', 'agriculture and sustainable', 'crop diversity', 'crop', 'crops', 'doha round', 'food poverty', 'farming', 'food security', 'hunger', 'hungry', 'malnourished', 'malnutrition', 'food production', 'rural development', 'sufficient food', 'small-scale food producers', 'stunted growth', 'stunting', 'trade diversity', 'undernourished', 'wasting and food', 'soil pollution', 'food gap'], 'SDG3': ['alcohol abuse', 'antenatal', 'child deaths', 'clinical', 'contraceptive use', 'death rate', 'disability', 'disorder', 'family planning', 'healthy living', 'immunisation', 'international health', 'malaria', 'mental health', 'neonatal', 'premature birth', 'reducing mortality', 'sexual health', 'substance abuse', 'vaccination', 'wellbeing', 'well-being', 'world health organisation'], 'SDG4': ['access to education', 'basic education', 'early childhood development', 'education for sustainability', 'education in developing countries', 'equal education', 'equitable education', 'gender disparities in education', 'global education', 'learning opportunities', 'lifelong learning', 'literacy skills', 'numeracy skills', 'post primary education', 'primary education', 'secondary education', 'qualified teachers', 'refugees and learning', 'school enrolment', 'teacher training', 'universal education', 'vocational training'], 'SDG5': ['empower and women', 'empower girls', 'empowering girls', 'empowering women', 'empowerment and women', 'exploitation and girls', 'exploitation and women', 'female genital mutilation', 'feminism', 'forced marriage', 'gender', 'gender and discrimination', 'gender discrimination', 'gender equality', 'gender parity', 'human trafficking', 'genital mutilation', 'governance and gender', 'human rights', 'marginalised', 'reproductive health', 'reproductive rights', 'sexual  health', 'sexual exploitation', 'sexual violence', 'social inclusion', 'violence and girls', 'violence and women', 'women in work', "women's empowerment", "women's rights", 'workplace equality'], 'SDG6': ['aquifer', 'contaminated', 'defecation', 'desalination', 'diarrhoeal diseases', 'drought', 'flood', 'floods', 'fresh water', 'freshwater', 'hydropower', 'hygiene', 'irrigation', 'river and ecosystem', 'river basins', 'toilet', 'sanitation', 'sewerage', 'sewers', 'toilets', 'untreated wastewater', 'waste water', 'wastewater', 'water access', 'water and ecosystems', 'water harvesting', 'water quality', 'water resources', 'water scarcity', 'water supply', 'water-use'], 'SDG7': ['affordable energy', 'alternative energy', 'battery', 'clean energy', 'clean energy technology', 'clean fuel', 'clean fuel technology', 'clean fuels', 'electricity', 'energy efficiency', 'fossil fuels', 'green economy', 'hydroelectric', 'natural gas', 'reliable energy', 'solar power', 'renewable energy', 'renewable power', 'solar energy', 'sustainable and energy', 'sustainable and power', 'wave energy', 'wave power', 'wind energy', 'wind power'], 'SDG8': ['child labour', 'child soldiers', 'decent work', 'development oriented policy', 'economic growth', 'economic productivity', 'entrepreneurship', 'equal pay', 'finance', 'financial services', 'forced labour', 'gdp growth', 'global resource efficiency', 'global trade', 'gross domestic product', 'job creation', 'human trafficking', 'inclusive economic growth', 'insurance', 'labour market', 'labour rights', 'micro finance', 'migrant workers', 'modern slavery', 'poverty eradication', 'poverty line', 'productive employment', 'quality jobs', 'safe work', 'secure work', 'slavery', 'social policies', 'stable employment', 'stable jobs', 'sustainable economic growth', 'sustainable tourism', 'unemployment', 'women migrants', 'work opportunities', 'youth employment', 'youth unemployment'], 'SDG9': ['clean technologies', 'communications technology', 'data banks', 'enterprises', 'environmentally sound technologies', 'financial services', 'foster innovation', 'industrial diversification', 'industrialisation', 'information and communication technology', 'infrastructure', 'internet access', 'mobile networks', 'resilient infrastructure', 'resource use efficiency', 'science', 'space exploration ?', 'sustainable industrialisation', 'sustainable infrastructure', 'technological capabilities'], 'SDG10': ['age and disabilities', 'ageism', 'classism', 'culture', 'development assistance', 'disabilities', 'disability', 'discrimination', 'discriminatory', 'equal opportunity', 'equal pay', 'equality', 'equity', 'ethnicity', 'homophobia', 'indigenous', 'human rights', 'inclusion', 'income inequality', 'inequalities', 'inequality', 'migrant remittance', 'race and discriminate', 'racism', 'racist', 'religion', 'sex and inequality', 'sexism', 'social protection', 'vulnerable nations'], 'SDG11': ['air pollution', 'air quality', 'arts and heritage', 'cultural heritage', 'decentralisation', 'development planning', 'disaster management', 'disaster risk reduction', 'disaster strategy', 'fine particulate matter', 'green spaces', 'human settlements', 'impact  of cities', 'inadequate housing', 'informal settlements', 'natural heritage', 'land consumption', 'local materials', 'natural disasters', 'overcrowding', 'public spaces', 'public transport', 'resilient buildings', 'risk reduction strategy', 'road safety', 'shanty', 'slums', 'smart cities', 'suburban', 'sustainable and city', 'sustainable and communities', 'sustainable buildings', 'sustainable urbanisation', 'tourism', 'town planning', 'urban development', 'urban planning', 'urban sustainability', 'urbanisation'], 'SDG12': ['supply chain', 'circular economy', 'consumer levels', 'consumerism', 'efficient use of resources', 'energy consumption', 'energy efficiency', 'energy use', 'fast fashion', 'food losses', 'food supply', 'food waste', 'fossil fuel', 'future proof', 'material goods', 'overconsumption', 'materialism', 'natural resources', 'obsolescence', 'procurement', 'recycle', 'recycling', 'reduce waste', 'renewable', 'resource efficiency', 'responsible production chains', 'sustainable consumption', 'sustainable tourism', 'waste', 'wasteful consumption'], 'SDG13': ['carbon emissions', 'climate action', 'climate adaptation', 'climate change', 'climate change planning', 'climate change policy', 'climate early warning', 'climate hazards', 'climate impact', 'climate mitigation', 'climate refugees', 'climate related hazards', 'climate resilience', 'cop 21', 'cop 22', 'forest fire', 'cyclone', 'drought', 'extreme weather', 'global temperature', 'global warming', 'greenhouse gas', 'greenhouse gases', 'hurricanes', 'ice loss', 'low-carbon economy', 'methan emissions', 'natural disasters', 'nitrogen oxide emissions', 'ocean warming', 'paris agreement', 'pollution', 'rising sea', 'rising sea level', 'sea level rise', 'warming'], 'SDG14': ['coastal', 'coastlines', 'conserve oceans', 'coral bleaching', 'coral reef', 'fish species', 'fish stock', 'fish stocks', 'fisheries', 'fishing practices', 'illegal fishing', 'marine', 'marine ecosystems', 'marine pollution', 'marine resources', 'overfishing', 'ocean acidification', 'ocean temperature', 'overexploitation and fish', 'productive oceans', 'protected areas', 'sea grasses'], 'SDG15': ['afforestation', 'alien species', 'biodiversity', 'biodiversity conservation', 'deforestation', 'desertification', 'drylands', 'ecosystem restoration', 'ecosystems', 'extinct', 'forest management', 'illegal wildlife products', 'illicit trafficking', 'invasive species', 'land conservation', 'manage forests', 'land degradation', 'land loss', 'land use', 'managed forests', 'permaculture', 'poaching', 'protected fauna', 'protected flora', 'reforestation', 'rewilding', 'soil degradation', 'sub-species', 'threatened species', 'vegetation', 'wetland conservation', 'wildlife'], 'SDG16': ['accountable institutions', 'arbitrary detention', 'arms trafficking', 'birth registration', 'bribery', 'combat terrorism', 'conflict resolution', 'enforced disappearance', 'hate crime', 'human trafficking', 'illegal arms', 'illicit financial flows', 'inclusive institutions', 'inclusive societies', 'inclusive society', 'national security', 'judiciary', 'justice', 'legal identity', 'non-violence', 'organized crime', 'paris principles', 'peace', 'peaceful', 'physical abuse', 'police', 'prison', 'prisons', 'psychological abuse', 'public policy', 'representative decision-making', 'rule of law', 'security threats', 'sexual abuse', 'sexual violence', 'stolen assets', 'strong institutions', 'tax evasion', 'theft', 'torture', 'un-sentenced detainees', 'unstable societies', 'victims of violence', 'violence', 'weapon', 'weapons'], 'SDG17': ['civil society partnerships', 'contemporary society', 'development assistance', 'doha development agenda', 'foreign direct investments', 'free trade', 'global partnership', 'global stability', 'international aid', 'international cooperation', 'international population', 'international support', 'knowledge sharing', 'multi-stakeholder partnerships', 'public-private partnerships', 'science cooperation agreements', 'technology cooperation agreements', 'weighted tariff average', 'world trade organization']}


    # Creating a DataFrame
    columns = ["Section",
                    "FileName",
                    "ShortText",
                    "SDG1",
                    "SDG2",
                    "SDG3",
                    "SDG4",
                    "SDG5",
                    "SDG6",
                    "SDG7",
                    "SDG8",
                    "SDG9",
                    "SDG10",
                    "SDG11",
                    "SDG12",
                    "SDG13",
                    "SDG14",
                    "SDG15",
                    "SDG16",
                    "SDG17",
                    "FullText",
                    "RawSDG",
                    "RawWordCount"
                    ]

    uploadedFiles = pd.DataFrame(columns=columns)
    uploadedFiles = uploadedFiles.fillna(0) 
    uploadedFiles
    
    conn = sqlite3.connect(r"C:\Users\Seckin\OneDrive\05. Lambda BI\02. UN Sustainability\02. Gradientable\appSdgMapping\dbExt.sqlite3")
    c = conn.cursor()

    shortTextQuery = """select FileName,
                                ShortText
                        from uploadedFiles"""

    uploadedFilesDf = pd.read_sql(sql=shortTextQuery, con=conn)

    Section = "Research"

    # filename
    # fileName = re.findall("UoL Policies(.+)", filePath)[0][1:]
    fileName = filePath.filename
    shortText = ""

    #filetext
    maxPages = 5
    if fileName[-3:] == "pdf":
        shortText = removePunc(pdfParser(filePath, maxPages))[:1000]
    elif fileName[-3:] == "docx":
        shortText = removePunc(docxParser(filePath))[:1000]


    # check file name here and continue
    if uploadedFilesDf["FileName"].str.contains(fileName).any() and \
        uploadedFilesDf["ShortText"].str.contains(shortText).any(): 
    #     return True
    # else:
    #     return False
        # fileQuery = """select /*Section,*/
        #                     FileName,
        #                     ShortText,
        #                     /*FullText,*/
        #                     RawSDG
        #                     /*RawWordCount*/
        #         from uploadedFiles
        #         where ShortText = "{}" """.format(shortText)
    
        # fileQueryDf = pd.read_sql(sql=fileQuery, con=conn)
        # print("{} was fetched from sql".format(fileName))
        # sdgDict = eval(fileQueryDf["RawSDG"][0])
        sdgDict = "{} uploaded".format(fileName)
        return sdgDict

    else:
        print("The file {} not found.".format(fileName))
        print("{} will be processed. It may take some time".format(fileName))

        #filetext
        if fileName[-3:] == "pdf":
            fullText = removePunc(pdfParser(filePath))
            shortText = fullText[:1000]
        elif fileName[-3:] == "docx":
            fullText = removePunc(docxParser(filePath))
            shortText = fullText[:1000]
        print(fullText)
        print(ResearchKeywords)
        # SDG Counts
        ResearchSDGResults = sdgCount(fullText, ResearchKeywords)
        # Raw SDG
        rawSDG = ResearchSDGResults
        # SDG Total
        ResearchSDGTotal = dict()
        for k, v in ResearchSDGResults.items():
            ResearchSDGTotal[k] = sum(v.values())

        # All words Count
        rawWordCount = wordCount(fullText)
        print("{} process finished. Sql is processing".format(fileName))

        tmpDF = pd.DataFrame([[
            Section,
            fileName,
            shortText,
            ResearchSDGTotal["SDG1"],
            ResearchSDGTotal["SDG2"],
            ResearchSDGTotal["SDG3"],
            ResearchSDGTotal["SDG4"],
            ResearchSDGTotal["SDG5"],
            ResearchSDGTotal["SDG6"],
            ResearchSDGTotal["SDG7"],
            ResearchSDGTotal["SDG8"],
            ResearchSDGTotal["SDG9"],
            ResearchSDGTotal["SDG10"],
            ResearchSDGTotal["SDG11"],
            ResearchSDGTotal["SDG12"],
            ResearchSDGTotal["SDG13"],
            ResearchSDGTotal["SDG14"],
            ResearchSDGTotal["SDG15"],
            ResearchSDGTotal["SDG16"],
            ResearchSDGTotal["SDG17"],
            fullText,
            str(rawSDG),
            str(rawWordCount)
        ]],
        columns = columns)                          

        uploadedFiles = uploadedFiles.append(tmpDF)
        print("Dataframe created")
        
        queryTable = """select * from uploadedFiles"""
        sqlDf = pd.read_sql(sql=queryTable, con=conn)
        print("SQL table fetched.")
        
        uploadedFilesCopy = uploadedFiles.copy()
        sqlDfCopy = sqlDf.copy()

        allDf = pd.concat((uploadedFilesCopy, sqlDfCopy)).drop_duplicates(subset=["Section",
                                                                            "FileName",
                                                                            "ShortText",
                                                                            ], keep="first")

        allDf.to_sql('uploadedFiles', con=conn, if_exists='replace', index = False)
        print("{} has been recorded into the DB.".format(fileName))
        sdgDict = rawSDG
        
        return sdgDict


# class FileContents(db.Model):
#     name = db.Column(db.string)



# Check DB for 5 pages 2
def checkDB(filePath):
    conn = sqlite3.connect(r"C:\Users\Seckin\OneDrive\05. Lambda BI\02. UN Sustainability\02. Gradientable\appSdgMapping\dbExt.sqlite3")
    # con.row_factory = sql.row_factory


    # filename
    fileName = filePath.filename
    shortText = ""

    #filetext
    maxPages = 2
    if fileName[-3:] == "pdf":
        shortText = removePunc(pdfParser(filePath, maxPages))[:1000]
    elif fileName[-3:] == "docx":
        shortText = removePunc(docxParser(filePath))[:1000]

    cur = conn.cursor()
    query = """select exists(select FileName, ShortText 
                    from uploadedFiles
                    where FileName = "{}" and
                    ShortText = "{}" LIMIT 1) """.format(fileName, shortText)
    cursor = cur.execute(query).fetchall()
    # print(cursor[0][0])

    if cursor[0][0] > 0:
        return True
    else:
        # print(fileName)
        # print(filePath.read())
        # insert files to db
        # query = """insert into uploadedFilesTmp (FileName, FileContent)
        #                                 values ("{}", "{}")""".format(fileName, filePath.read())
        # cursor = cur.execute(query)

        print("Filepath: ", filePath)
        query = """INSERT INTO uploadedFilesTmp(FileName, FileContent)
                                            VALUES(?, ?)"""
        cur.execute(query, (fileName, filePath.read()))
        conn.commit()
        # conn.commit()

        # db = SQLAlchemy()
        # class FileContents(db.Model):
        #     name = db.Column(db.String(500))
        #     data = db.Column(db.LargeBinary)

        # newFile = FileContents(name=fileName, data=file.read())
        # db.session.add(newFile)
        # db.session.commit()

        return "{} saved.".format(fileName)

    
    
    return "saved"



# # Get File From DB
# def getSDGfromDB():

#     conn = sqlite3.connect(r"C:\Users\Seckin\OneDrive\05. Lambda BI\02. UN Sustainability\02. Gradientable\flask-dashboard-gradientable\db.sqlite3")
#     c = conn.cursor()

#     fileQuery = """select Section,
#                             FileName,
#                             ShortText,
#                             FullText,
#                             RawSDG,
#                             RawWordCount
#                 from uploadedFiles
#                 where ShortText = "{}" """.format(shortText)
    
#     fileQueryDf = pd.read_sql(sql=fileQuery, con=conn)
#     print("{} was fetched from sql".format(fileName))
#     sdgDict = eval(fileQueryDf["RawSDG"][0])
#     return sdgDict


# basedir    = os.path.abspath(os.path.dirname(__file__))
# DATABASE = 'sqlite:///' + os.path.join(basedir, 'dbExt.sqlite3')

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect("dbExt.sqlite3")
#     return db


def SDGQueryGenerator(universityName, yearFrom, yearTo):
    query = f"""SELECT * 
                    FROM SDG1 
                    WHERE Institution={universityName} AND
                            {yearFrom} >= yearColumn AND 
                            {yearTo} <= yearColumn"""
    return query



def getResearchResults(universityName, yearFrom, yearTo):
    conn = sqlite3.connect("dbExt.sqlite3")
    c = conn.cursor()
    
    yearFrom = int(yearFrom)
    yearTo = int(yearTo)

    # QUERY DICTIONARIES 
    uniQueryDict = {}
    ukQueryDict = {}
    for i in range(17):
        if i < 9: sdg = f"SDG0{i+1}"
        else: sdg = f"SDG{i+1}"
        uniQuery = f"""SELECT * 
                    FROM Research{sdg} 
                    WHERE Institution = "{universityName}" AND
                    CoverDate > {yearFrom} AND
                    CoverDate < {yearTo + 1}"""

        ukQuery = f"""SELECT round(avg(SDGCount),1) as "UK Average"
                        FROM
                        (
                        SELECT count(Institution) as SDGCount
                        FROM Research{sdg}
                        WHERE CoverDate > {yearFrom} AND 
                        CoverDate < {yearTo + 1}
                        GROUP BY Institution
                        )"""

        uniQueryDict[sdg] = uniQuery
        ukQueryDict[sdg] = ukQuery


    # EXCEL OUTPUT DATAFRAMES
    uniSqlDf = pd.DataFrame()
    for sdg, query in uniQueryDict.items(): # UNI DATAFRAME
        tempDf = pd.read_sql(sql=query, con=conn)
        tempDf.insert(0, "SDG", sdg)
        uniSqlDf = uniSqlDf.append(tempDf)
    uniSqlDf = uniSqlDf.reset_index(drop=True)

    ukSqlDf = pd.DataFrame()
    for sdg, query in ukQueryDict.items(): # UK DATAFRAME
        tempDf = pd.read_sql(sql=query, con=conn)
        tempDf.insert(0, "SDG", sdg)
        ukSqlDf = ukSqlDf.append(tempDf)
    ukSqlDf = ukSqlDf.reset_index(drop=True)

    
    # RETURNS

   # Uni SDG Polar Chart Dictionary
    uniSdgChartDf = uniSqlDf.groupby("SDG").count()["ScopusID"]
    uniSdgChartDict = {}
    for sdg in range(17):
        if sdg < 9: sdgName = f"SDG0{sdg+1}"
        else: sdgName = f"SDG{sdg+1}"

        if sdgName in uniSdgChartDf:
            uniSdgChartDict[f"SDG{sdg+1}"] = uniSdgChartDf[sdgName]
        else:
            uniSdgChartDict[f"SDG{sdg+1}"] = 0




    # UK SDG Polar Chart Dictionary
    ukSdgChartDict = {}
    for sdg in range(len(ukSqlDf.index)):
        ukSdgChartDict[f"SDG{sdg+1}"] = ukSqlDf.iloc[sdg, 1]


    # CitationCount Table Dictionary
    citationCountDf = uniSqlDf.groupby("SDG").sum()["CitationCount"]
    citationCount = {}
    for citi in range(len(citationCountDf)):
        citationCount[f"SDG{citi+1}"] = citationCountDf[citi]


    # Collaborators
    counts = {}
    for i, entry in enumerate(uniSqlDf["Collaboration"]):
        entryTmp = ast.literal_eval(entry)
        for affil in entryTmp:
            counts[affil] = counts.get(affil, 0) + 1
    collaborators = {k: v for k, v in sorted(counts.items(), key=lambda item: item[1], reverse=True)}     
    # del collaborators[universityName]
    
    return uniSdgChartDict, ukSdgChartDict, citationCount, dict(list(collaborators.items())[:10]) # TOP 10 results





# fullText = {}

# path = r"C:\Users\Seckin\OneDrive\04. Lambda BI\02. UN Sustainability\07. Gradientable\flask-dashboard-gradientable\app\base\static\assets\uploads"

# # Getting Files List
# filesList = []
# for (dirpath, dirnames, filenames) in walk(path):
#     filesList.extend(filenames)

# # Placing Everything in a Dictionary
# for files in filesList:
#     fullText[files] = docx2txt.process(r"{}\{}".format(path, files))

# for key in fullText:
#     print("FILE : {} , TEXT : {}".format(key,fullText[key]) + "\n\n")


    
# path = r"C:\Users\Seckin\Downloads"
# fileName = r"shortStory1.docx"
# fullPath = "{}\{}".format(path, fileName)
# text = docx2txt.process(fullPath)



# Allowed File Size
# def allowed_file_size(filesize):

#     if int(filesize) <= current_app.config["MAX_DOC_SIZE"]:
#         return True
#     else:
#         return False