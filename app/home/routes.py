# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

import os
import re
import time

from flask import (Flask, current_app, flash, redirect, render_template,
                   request, url_for)
from jinja2 import TemplateNotFound
from werkzeug.utils import secure_filename

from app import login_manager
from app.home import blueprint
from app.home.models import (allowed_doc, checkDB, checkSQL51000, getFile,
                             pdfParser, removePunc, sdgCount, sdgCountTotal, SDGQueryGenerator,
                             getResearchResults)
from flask_login import current_user, login_required
# from flask_sqlalchemy import SQLAlchemy



@blueprint.route('/index')
@login_required
def index():
    return render_template('index.html')



@blueprint.route("/uploadFile", methods=["GET", "POST"])
def upload_file():
    msg = ""
    if request.method == "POST":
        
        if request.files:
            
            # Allowed File Size over Cookies!!! / Check Models
            # if not models.allowed_file_size(request.cookies.get("filesize")):
            #     print("File exceeded maximum size")
            #     return redirect(request.url)
            
            # print("files[]")
            if "files[]" not in request.files:
                msg = "Document(s) must have filename(s)"
                # return redirect(url_for("home_blueprint.upload_file", msg=msg))
                return render_template("/operations.html", msgDanger=msg)

            documents = request.files.getlist("files[]")

            if not allowed_doc(documents):
                msg = "Document extension(s) are not allowed"
                # return redirect(url_for("home_blueprint.upload_file", msg=msg))
                return render_template("/operations.html", msgDanger=msg)
            else:
                
                fileNamesList = []
                for file in documents:
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(current_app.config["UPLOADS"], filename))
                    fileNamesList.append(filename)
                    

            msg = "Document(s) saved"
            # return redirect(url_for("home_blueprint.upload_file", msg=msg))


            return render_template("/operations.html", msgSuccess=fileNamesList)
    
    

    return render_template("/operations.html", msgSuccess=msg)


# @blueprint.route("/uploadFile", methods=["GET", "POST"])
# def upload_file():
#     documents = request.files.getlist("files[]")
#     # print(documents.filesize)
#     # print(documents[0].filename)
#     fileNamesList = []
#     SDGResults = {}
#     for file in documents:
#         fileNamesList.append(file.filename)
#         SDGResults[file.filename] = checkDB(file)
#         checkDBResult = checkDB(file)
#         if checkDBResult is False:
#             print("insert files")
    
#     # checkSQL51000(documents)


#     return render_template("/uploadFile.html", msgSuccess=SDGResults)


# @blueprint.route("/getFiles", methods=["GET", "POST"])
# def return_file():
#     textBody = getFile()
#     return render_template("/uploadFile.html", textBody=textBody)


# @blueprint.route("/researchSDG", methods=["GET", "POST"])
# def research_SDG():
#     ResearchKeywords = {'SDG1': ['asylum seeker', 'basic services', 'developing countries', 'disadvantaged', 'financial inclusion', 'microfinance', 'non-discrimination', 'poverty', 'refugee', 'social protection', 'third world', 'vulnerable', 'wealth distribution'], 'SDG2': ['agricultural', 'agriculture and sustainable', 'crop diversity', 'crop', 'crops', 'doha round', 'food poverty', 'farming', 'food security', 'hunger', 'hungry', 'malnourished', 'malnutrition', 'food production', 'rural development', 'sufficient food', 'small-scale food producers', 'stunted growth', 'stunting', 'trade diversity', 'undernourished', 'wasting and food', 'soil pollution', 'food gap'], 'SDG3': ['alcohol abuse', 'antenatal', 'child deaths', 'clinical', 'contraceptive use', 'death rate', 'disability', 'disorder', 'family planning', 'healthy living', 'immunisation', 'international health', 'malaria', 'mental health', 'neonatal', 'premature birth', 'reducing mortality', 'sexual health', 'substance abuse', 'vaccination', 'wellbeing', 'well-being', 'world health organisation'], 'SDG4': ['access to education', 'basic education', 'early childhood development', 'education for sustainability', 'education in developing countries', 'equal education', 'equitable education', 'gender disparities in education', 'global education', 'learning opportunities', 'lifelong learning', 'literacy skills', 'numeracy skills', 'post primary education', 'primary education', 'secondary education', 'qualified teachers', 'refugees and learning', 'school enrolment', 'teacher training', 'universal education', 'vocational training'], 'SDG5': ['empower and women', 'empower girls', 'empowering girls', 'empowering women', 'empowerment and women', 'exploitation and girls', 'exploitation and women', 'female genital mutilation', 'feminism', 'forced marriage', 'gender', 'gender and discrimination', 'gender discrimination', 'gender equality', 'gender parity', 'human trafficking', 'genital mutilation', 'governance and gender', 'human rights', 'marginalised', 'reproductive health', 'reproductive rights', 'sexual  health', 'sexual exploitation', 'sexual violence', 'social inclusion', 'violence and girls', 'violence and women', 'women in work', "women's empowerment", "women's rights", 'workplace equality'], 'SDG6': ['aquifer', 'contaminated', 'defecation', 'desalination', 'diarrhoeal diseases', 'drought', 'flood', 'floods', 'fresh water', 'freshwater', 'hydropower', 'hygiene', 'irrigation', 'river and ecosystem', 'river basins', 'toilet', 'sanitation', 'sewerage', 'sewers', 'toilets', 'untreated wastewater', 'waste water', 'wastewater', 'water access', 'water and ecosystems', 'water harvesting', 'water quality', 'water resources', 'water scarcity', 'water supply', 'water-use'], 'SDG7': ['affordable energy', 'alternative energy', 'battery', 'clean energy', 'clean energy technology', 'clean fuel', 'clean fuel technology', 'clean fuels', 'electricity', 'energy efficiency', 'fossil fuels', 'green economy', 'hydroelectric', 'natural gas', 'reliable energy', 'solar power', 'renewable energy', 'renewable power', 'solar energy', 'sustainable and energy', 'sustainable and power', 'wave energy', 'wave power', 'wind energy', 'wind power'], 'SDG8': ['child labour', 'child soldiers', 'decent work', 'development oriented policy', 'economic growth', 'economic productivity', 'entrepreneurship', 'equal pay', 'finance', 'financial services', 'forced labour', 'gdp growth', 'global resource efficiency', 'global trade', 'gross domestic product', 'job creation', 'human trafficking', 'inclusive economic growth', 'insurance', 'labour market', 'labour rights', 'micro finance', 'migrant workers', 'modern slavery', 'poverty eradication', 'poverty line', 'productive employment', 'quality jobs', 'safe work', 'secure work', 'slavery', 'social policies', 'stable employment', 'stable jobs', 'sustainable economic growth', 'sustainable tourism', 'unemployment', 'women migrants', 'work opportunities', 'youth employment', 'youth unemployment'], 'SDG9': ['clean technologies', 'communications technology', 'data banks', 'enterprises', 'environmentally sound technologies', 'financial services', 'foster innovation', 'industrial diversification', 'industrialisation', 'information and communication technology', 'infrastructure', 'internet access', 'mobile networks', 'resilient infrastructure', 'resource use efficiency', 'science', 'space exploration ?', 'sustainable industrialisation', 'sustainable infrastructure', 'technological capabilities'], 'SDG10': ['age and disabilities', 'ageism', 'classism', 'culture', 'development assistance', 'disabilities', 'disability', 'discrimination', 'discriminatory', 'equal opportunity', 'equal pay', 'equality', 'equity', 'ethnicity', 'homophobia', 'indigenous', 'human rights', 'inclusion', 'income inequality', 'inequalities', 'inequality', 'migrant remittance', 'race and discriminate', 'racism', 'racist', 'religion', 'sex and inequality', 'sexism', 'social protection', 'vulnerable nations'], 'SDG11': ['air pollution', 'air quality', 'arts and heritage', 'cultural heritage', 'decentralisation', 'development planning', 'disaster management', 'disaster risk reduction', 'disaster strategy', 'fine particulate matter', 'green spaces', 'human settlements', 'impact  of cities', 'inadequate housing', 'informal settlements', 'natural heritage', 'land consumption', 'local materials', 'natural disasters', 'overcrowding', 'public spaces', 'public transport', 'resilient buildings', 'risk reduction strategy', 'road safety', 'shanty', 'slums', 'smart cities', 'suburban', 'sustainable and city', 'sustainable and communities', 'sustainable buildings', 'sustainable urbanisation', 'tourism', 'town planning', 'urban development', 'urban planning', 'urban sustainability', 'urbanisation'], 'SDG12': ['supply chain', 'circular economy', 'consumer levels', 'consumerism', 'efficient use of resources', 'energy consumption', 'energy efficiency', 'energy use', 'fast fashion', 'food losses', 'food supply', 'food waste', 'fossil fuel', 'future proof', 'material goods', 'overconsumption', 'materialism', 'natural resources', 'obsolescence', 'procurement', 'recycle', 'recycling', 'reduce waste', 'renewable', 'resource efficiency', 'responsible production chains', 'sustainable consumption', 'sustainable tourism', 'waste', 'wasteful consumption'], 'SDG13': ['carbon emissions', 'climate action', 'climate adaptation', 'climate change', 'climate change planning', 'climate change policy', 'climate early warning', 'climate hazards', 'climate impact', 'climate mitigation', 'climate refugees', 'climate related hazards', 'climate resilience', 'cop 21', 'cop 22', 'forest fire', 'cyclone', 'drought', 'extreme weather', 'global temperature', 'global warming', 'greenhouse gas', 'greenhouse gases', 'hurricanes', 'ice loss', 'low-carbon economy', 'methan emissions', 'natural disasters', 'nitrogen oxide emissions', 'ocean warming', 'paris agreement', 'pollution', 'rising sea', 'rising sea level', 'sea level rise', 'warming'], 'SDG14': ['coastal', 'coastlines', 'conserve oceans', 'coral bleaching', 'coral reef', 'fish species', 'fish stock', 'fish stocks', 'fisheries', 'fishing practices', 'illegal fishing', 'marine', 'marine ecosystems', 'marine pollution', 'marine resources', 'overfishing', 'ocean acidification', 'ocean temperature', 'overexploitation and fish', 'productive oceans', 'protected areas', 'sea grasses'], 'SDG15': ['afforestation', 'alien species', 'biodiversity', 'biodiversity conservation', 'deforestation', 'desertification', 'drylands', 'ecosystem restoration', 'ecosystems', 'extinct', 'forest management', 'illegal wildlife products', 'illicit trafficking', 'invasive species', 'land conservation', 'manage forests', 'land degradation', 'land loss', 'land use', 'managed forests', 'permaculture', 'poaching', 'protected fauna', 'protected flora', 'reforestation', 'rewilding', 'soil degradation', 'sub-species', 'threatened species', 'vegetation', 'wetland conservation', 'wildlife'], 'SDG16': ['accountable institutions', 'arbitrary detention', 'arms trafficking', 'birth registration', 'bribery', 'combat terrorism', 'conflict resolution', 'enforced disappearance', 'hate crime', 'human trafficking', 'illegal arms', 'illicit financial flows', 'inclusive institutions', 'inclusive societies', 'inclusive society', 'national security', 'judiciary', 'justice', 'legal identity', 'non-violence', 'organized crime', 'paris principles', 'peace', 'peaceful', 'physical abuse', 'police', 'prison', 'prisons', 'psychological abuse', 'public policy', 'representative decision-making', 'rule of law', 'security threats', 'sexual abuse', 'sexual violence', 'stolen assets', 'strong institutions', 'tax evasion', 'theft', 'torture', 'un-sentenced detainees', 'unstable societies', 'victims of violence', 'violence', 'weapon', 'weapons'], 'SDG17': ['civil society partnerships', 'contemporary society', 'development assistance', 'doha development agenda', 'foreign direct investments', 'free trade', 'global partnership', 'global stability', 'international aid', 'international cooperation', 'international population', 'international support', 'knowledge sharing', 'multi-stakeholder partnerships', 'public-private partnerships', 'science cooperation agreements', 'technology cooperation agreements', 'weighted tariff average', 'world trade organization']}
#     path = r"C:\Users\Seckin\OneDrive\05. Lambda BI\02. UN Sustainability\02. Gradientable\flask-dashboard-gradientable\app\base\static\assets\uploads\UoL_Carbon_Management_Plan.pdf"
    
#     fileNameParsed = re.findall("uploads(.+)", path)[0][1:]

#     text = removePunc(pdfParser(r"{}".format(path), 5))
    
#     ResearchSDGResults = sdgCountTotal(sdgCount(text, ResearchKeywords))
#     return render_template("/research.html", ResearchSDGResults=ResearchSDGResults, fileNameParsed=fileNameParsed)



@blueprint.route("/SDGQuery", methods=["GET", "POST"])
def SDGQuery():
    yearWarningMsg = None
    universityName, yearFrom, yearTo = None, None, None
    uniChart, ukChart, citCount, collab = dict(), dict(), dict(), dict()

    if request.method == "POST":
        if request.form:
            universityName = str(request.form['universitySelection'])
            yearFrom = str(request.form["yearFromSelection"])
            yearTo = str(request.form["yearToSelection"])
            print("SDG Query has run!", universityName, yearFrom, yearTo)
            # Year Warning
            
            if int(yearFrom) > int(yearTo):
                yearWarningMsg = """"From" Selection cannot be greater than "To" Selection"""
                return render_template("/research.html", yearWarningMsg=yearWarningMsg)




            uniChart, ukChart, citCount, collab = getResearchResults(universityName, yearFrom, yearTo)
            

    uniValues = [values for keys, values in uniChart.items()]
    ukValues = [values for keys, values in ukChart.items()]

    


    return render_template("/research.html", yearWarningMsg=yearWarningMsg, 
                                                universityName = universityName,
                                                uniChart=uniChart,
                                                ukChart=ukChart,
                                                citCount=citCount,
                                                collab=collab,
                                                yearFrom=yearFrom,
                                                yearTo=yearTo,
                                                uniValues=uniValues,
                                                ukValues=ukValues
                                                )






@blueprint.route('/<template>')
def route_template(template):

    try:

        if not template.endswith( '.html' ):
            template += '.html'

        return render_template( template )

    except TemplateNotFound:
        return render_template('page-404.html'), 404
    
    except:
        return render_template('page-500.html'), 500
