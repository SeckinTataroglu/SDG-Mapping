# -*- encoding: utf-8 -*-
"""
MIT License
Copyright (c) 2019 - present AppSeed.us
"""

import os
from decouple import config

class Config(object):

    basedir    = os.path.abspath(os.path.dirname(__file__))

    # Set up the App SECRET_KEY
    SECRET_KEY = config('SECRET_KEY', default='S#perS3crEt_007')

    # This will create a file in <app> FOLDER
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dbExt.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADS = r"""C:\Users\Seckin\OneDrive\05. Lambda BI\02. UN Sustainability\02. Gradientable\flask-dashboard-gradientable\app\base\static\assets\uploads"""
    ALLOWED_DOC_EXTENTIONS = "DOC", "DOCX", "ODT", "PDF", "TXT"
    MAX_DOC_SIZE = 0.08 * 1024 * 1024

    # ResearchKeywords = {'SDG1': ['asylum seeker', 'basic services', 'developing countries', 'disadvantaged', 'financial inclusion', 'microfinance', 'non-discrimination', 'poverty', 'refugee', 'social protection', 'third world', 'vulnerable', 'wealth distribution'], 'SDG2': ['agricultural', 'agriculture and sustainable', 'crop diversity', 'crop', 'crops', 'doha round', 'food poverty', 'farming', 'food security', 'hunger', 'hungry', 'malnourished', 'malnutrition', 'food production', 'rural development', 'sufficient food', 'small-scale food producers', 'stunted growth', 'stunting', 'trade diversity', 'undernourished', 'wasting and food', 'soil pollution', 'food gap'], 'SDG3': ['alcohol abuse', 'antenatal', 'child deaths', 'clinical', 'contraceptive use', 'death rate', 'disability', 'disorder', 'family planning', 'healthy living', 'immunisation', 'international health', 'malaria', 'mental health', 'neonatal', 'premature birth', 'reducing mortality', 'sexual health', 'substance abuse', 'vaccination', 'wellbeing', 'well-being', 'world health organisation'], 'SDG4': ['access to education', 'basic education', 'early childhood development', 'education for sustainability', 'education in developing countries', 'equal education', 'equitable education', 'gender disparities in education', 'global education', 'learning opportunities', 'lifelong learning', 'literacy skills', 'numeracy skills', 'post primary education', 'primary education', 'secondary education', 'qualified teachers', 'refugees and learning', 'school enrolment', 'teacher training', 'universal education', 'vocational training'], 'SDG5': ['empower and women', 'empower girls', 'empowering girls', 'empowering women', 'empowerment and women', 'exploitation and girls', 'exploitation and women', 'female genital mutilation', 'feminism', 'forced marriage', 'gender', 'gender and discrimination', 'gender discrimination', 'gender equality', 'gender parity', 'human trafficking', 'genital mutilation', 'governance and gender', 'human rights', 'marginalised', 'reproductive health', 'reproductive rights', 'sexual  health', 'sexual exploitation', 'sexual violence', 'social inclusion', 'violence and girls', 'violence and women', 'women in work', "women's empowerment", "women's rights", 'workplace equality'], 'SDG6': ['aquifer', 'contaminated', 'defecation', 'desalination', 'diarrhoeal diseases', 'drought', 'flood', 'floods', 'fresh water', 'freshwater', 'hydropower', 'hygiene', 'irrigation', 'river and ecosystem', 'river basins', 'toilet', 'sanitation', 'sewerage', 'sewers', 'toilets', 'untreated wastewater', 'waste water', 'wastewater', 'water access', 'water and ecosystems', 'water harvesting', 'water quality', 'water resources', 'water scarcity', 'water supply', 'water-use'], 'SDG7': ['affordable energy', 'alternative energy', 'battery', 'clean energy', 'clean energy technology', 'clean fuel', 'clean fuel technology', 'clean fuels', 'electricity', 'energy efficiency', 'fossil fuels', 'green economy', 'hydroelectric', 'natural gas', 'reliable energy', 'solar power', 'renewable energy', 'renewable power', 'solar energy', 'sustainable and energy', 'sustainable and power', 'wave energy', 'wave power', 'wind energy', 'wind power'], 'SDG8': ['child labour', 'child soldiers', 'decent work', 'development oriented policy', 'economic growth', 'economic productivity', 'entrepreneurship', 'equal pay', 'finance', 'financial services', 'forced labour', 'gdp growth', 'global resource efficiency', 'global trade', 'gross domestic product', 'job creation', 'human trafficking', 'inclusive economic growth', 'insurance', 'labour market', 'labour rights', 'micro finance', 'migrant workers', 'modern slavery', 'poverty eradication', 'poverty line', 'productive employment', 'quality jobs', 'safe work', 'secure work', 'slavery', 'social policies', 'stable employment', 'stable jobs', 'sustainable economic growth', 'sustainable tourism', 'unemployment', 'women migrants', 'work opportunities', 'youth employment', 'youth unemployment'], 'SDG9': ['clean technologies', 'communications technology', 'data banks', 'enterprises', 'environmentally sound technologies', 'financial services', 'foster innovation', 'industrial diversification', 'industrialisation', 'information and communication technology', 'infrastructure', 'internet access', 'mobile networks', 'resilient infrastructure', 'resource use efficiency', 'science', 'space exploration ?', 'sustainable industrialisation', 'sustainable infrastructure', 'technological capabilities'], 'SDG10': ['age and disabilities', 'ageism', 'classism', 'culture', 'development assistance', 'disabilities', 'disability', 'discrimination', 'discriminatory', 'equal opportunity', 'equal pay', 'equality', 'equity', 'ethnicity', 'homophobia', 'indigenous', 'human rights', 'inclusion', 'income inequality', 'inequalities', 'inequality', 'migrant remittance', 'race and discriminate', 'racism', 'racist', 'religion', 'sex and inequality', 'sexism', 'social protection', 'vulnerable nations'], 'SDG11': ['air pollution', 'air quality', 'arts and heritage', 'cultural heritage', 'decentralisation', 'development planning', 'disaster management', 'disaster risk reduction', 'disaster strategy', 'fine particulate matter', 'green spaces', 'human settlements', 'impact  of cities', 'inadequate housing', 'informal settlements', 'natural heritage', 'land consumption', 'local materials', 'natural disasters', 'overcrowding', 'public spaces', 'public transport', 'resilient buildings', 'risk reduction strategy', 'road safety', 'shanty', 'slums', 'smart cities', 'suburban', 'sustainable and city', 'sustainable and communities', 'sustainable buildings', 'sustainable urbanisation', 'tourism', 'town planning', 'urban development', 'urban planning', 'urban sustainability', 'urbanisation'], 'SDG12': ['supply chain', 'circular economy', 'consumer levels', 'consumerism', 'efficient use of resources', 'energy consumption', 'energy efficiency', 'energy use', 'fast fashion', 'food losses', 'food supply', 'food waste', 'fossil fuel', 'future proof', 'material goods', 'overconsumption', 'materialism', 'natural resources', 'obsolescence', 'procurement', 'recycle', 'recycling', 'reduce waste', 'renewable', 'resource efficiency', 'responsible production chains', 'sustainable consumption', 'sustainable tourism', 'waste', 'wasteful consumption'], 'SDG13': ['carbon emissions', 'climate action', 'climate adaptation', 'climate change', 'climate change planning', 'climate change policy', 'climate early warning', 'climate hazards', 'climate impact', 'climate mitigation', 'climate refugees', 'climate related hazards', 'climate resilience', 'cop 21', 'cop 22', 'forest fire', 'cyclone', 'drought', 'extreme weather', 'global temperature', 'global warming', 'greenhouse gas', 'greenhouse gases', 'hurricanes', 'ice loss', 'low-carbon economy', 'methan emissions', 'natural disasters', 'nitrogen oxide emissions', 'ocean warming', 'paris agreement', 'pollution', 'rising sea', 'rising sea level', 'sea level rise', 'warming'], 'SDG14': ['coastal', 'coastlines', 'conserve oceans', 'coral bleaching', 'coral reef', 'fish species', 'fish stock', 'fish stocks', 'fisheries', 'fishing practices', 'illegal fishing', 'marine', 'marine ecosystems', 'marine pollution', 'marine resources', 'overfishing', 'ocean acidification', 'ocean temperature', 'overexploitation and fish', 'productive oceans', 'protected areas', 'sea grasses'], 'SDG15': ['afforestation', 'alien species', 'biodiversity', 'biodiversity conservation', 'deforestation', 'desertification', 'drylands', 'ecosystem restoration', 'ecosystems', 'extinct', 'forest management', 'illegal wildlife products', 'illicit trafficking', 'invasive species', 'land conservation', 'manage forests', 'land degradation', 'land loss', 'land use', 'managed forests', 'permaculture', 'poaching', 'protected fauna', 'protected flora', 'reforestation', 'rewilding', 'soil degradation', 'sub-species', 'threatened species', 'vegetation', 'wetland conservation', 'wildlife'], 'SDG16': ['accountable institutions', 'arbitrary detention', 'arms trafficking', 'birth registration', 'bribery', 'combat terrorism', 'conflict resolution', 'enforced disappearance', 'hate crime', 'human trafficking', 'illegal arms', 'illicit financial flows', 'inclusive institutions', 'inclusive societies', 'inclusive society', 'national security', 'judiciary', 'justice', 'legal identity', 'non-violence', 'organized crime', 'paris principles', 'peace', 'peaceful', 'physical abuse', 'police', 'prison', 'prisons', 'psychological abuse', 'public policy', 'representative decision-making', 'rule of law', 'security threats', 'sexual abuse', 'sexual violence', 'stolen assets', 'strong institutions', 'tax evasion', 'theft', 'torture', 'un-sentenced detainees', 'unstable societies', 'victims of violence', 'violence', 'weapon', 'weapons'], 'SDG17': ['civil society partnerships', 'contemporary society', 'development assistance', 'doha development agenda', 'foreign direct investments', 'free trade', 'global partnership', 'global stability', 'international aid', 'international cooperation', 'international population', 'international support', 'knowledge sharing', 'multi-stakeholder partnerships', 'public-private partnerships', 'science cooperation agreements', 'technology cooperation agreements', 'weighted tariff average', 'world trade organization']}
    REFKeywords = {'SDG1': ['asylum seeker', 'developing', 'development', 'disadvantaged countries', 'government', 'include', 'international', 'poverty', 'refugee', 'resource', 'social', 'social protection', 'system', 'vulnerable', 'world'], 'SDG2': ['agricultural', 'agriculture', 'crop', 'developing', 'diversity', 'farming', 'food', 'food poverty', 'hunger', 'malnutrition', 'practices', 'productivity', 'reduce', 'rural', 'sustainable', 'trade'], 'SDG3': ['alcohol abuse', 'anti-cancer', 'asthma', 'autism', 'biomedical', 'bleeding', 'blindness', 'cancer', 'child health', 'chronic', 'clinical', 'deaths', 'diabetes', 'disease', 'diseases', 'disorder', 'drugs', 'healthcare', 'heart', 'immunity', 'infection', 'infectious', 'medical', 'medicine', 'mental health', 'mortality', 'neonatal', 'nhs', 'public health', 'quality of care', 'strokes', 'trauma', 'treatment', 'world health organisation'], 'SDG4': ['achievement', 'child', 'children', 'cultural', 'curricula', 'education', 'educational', 'e-learning', 'learn', 'learning', 'number skills', 'primary school', 'reading skills', 'school', 'schooling', 'science', 'secondary school', 'teach', 'teacher', 'teaching assistant', 'university'], 'SDG5': ['abuse', 'domestic violence', 'female', 'gender violence', 'male', 'rape', 'violence', 'vulnerable', 'women'], 'SDG6': ['contaminated', 'drought', 'ecosystem', 'environmental', 'fish', 'fishery', 'flood', 'fresh water', 'infrastructure', 'management', 'provide', 'quality', 'reduce', 'reducing', 'resource', 'river', 'scarcity', 'supply', 'sustainable', 'system', 'toilet', 'waste water', 'water', 'water access', 'world'], 'SDG7': ['electrical', 'energy', 'natural gas', 'nuclear power', 'power', 'space', 'technology'], 'SDG8': ['bank', 'business', 'commerce', 'commercial', 'consumer', 'debt', 'economic', 'economy', 'employment', 'enterprise', 'finance', 'financial', 'growth', 'innovation', 'investment', 'jobs', 'labour', 'market', 'monetary', 'sales', 'services', 'traders', 'unemployment', 'workforce'], 'SDG9': ['development', 'knowledge', 'science', 'space', 'technology'], 'SDG10': ['age', 'anti-discrimination', 'antisemitism', 'autism', 'disability', 'disabled', 'discrimination', 'ethnic minorities', 'exclusion', 'human rights', 'immigration', 'isolation', 'misrepresented', 'racism', 'social inclusion', 'xenophobia'], 'SDG11': ['buildings', 'city', 'communities', 'community', 'cultural', 'development', 'heritage', 'living conditions', 'local', 'public', 'society', 'sustainable', 'tourism', 'urban areas', 'urban regeneration'], 'SDG12': ['built environment', 'cultural', 'heritage', 'local', 'manufacture', 'material', 'museum', 'resource efficiency', 'resources', 'social', 'tourist'], 'SDG13': ['climate', 'climate change', 'global', 'mitigation', 'sea', 'sea surface', 'temperature', 'emission'], 'SDG14': ['animal', 'animals', 'biodiversity', 'conservation', 'lake', 'lake', 'water', 'water access', 'water poverty', 'whaling'], 'SDG15': ['animal', 'animal protection', 'animals', 'biodiversity', 'conservation', 'environmental', 'forests', 'land use', 'peatlands', 'plantation', 'treatment', 'wild'], 'SDG16': ['conviction', 'court', 'crime', 'criminal', 'evidence', 'intelligence', 'judicial', 'justice', 'law', 'offender', 'police', 'probation', 'reoffending', 'security', 'suspects', 'victim', 'witnesses'], 'SDG17': ['contemporary society', 'internationally', 'population', 'stimulating partnerships', 'worldwide']}
    OperationsKeywords = {'SDG1': ['asylum seeker', 'deprivation', 'poverty', 'refugee', 'social protection', 'vulnerable'], 'SDG2': ['community kitchen', 'food', 'food crops', 'food poverty', 'fruit', 'hunger', 'local', 'malnutrition', 'seasonal', 'surplus food', 'sustainable', 'sustainably sourced', 'vegetables', 'malnourished', 'sufficient food', 'sustainable food', 'sustainable catering', 'responsibly sourced', 'food waste'], 'SDG3': ['abuse', 'addiction', 'alcohol', 'allergies', 'antenatal', 'appointments', 'child', 'childbirth', 'clinical', 'conditions', 'death', 'disorder', 'drug', 'first aid', 'health', 'healthcare', 'healthy', 'healthy living', 'human health', 'ill', 'illness', 'infection', 'medical', 'medication', 'medicine', 'mental health', 'misuse', 'nhs', 'passive smoking', 'physical health', 'pregnant', 'public health', 'sickness', 'substance', 'tobacco', 'trauma', 'treatment', 'wellbeing'], 'SDG4': ['academic', 'curricula', 'curriculum', 'education', 'employability', 'equal', 'learning', 'quality', 'teaching', 'widening participation', 'e-learning', 'learn', 'teach', 'learning opportunities', 'lifelong learning', 'vocational training'], 'SDG5': ['discrimination', 'domestic violence', 'equality', 'exploitation', 'female', 'gender', 'gender discrimination', 'gender equality', 'gender identity', 'girl', 'human rights', 'human trafficking', 'male', 'mother', 'pay gap', 'same-sex', 'transgender', 'violence', 'vulnerable', 'women', 'workplace equality'], 'SDG6': ['environmentally damaging', 'hazardous', 'substances', 'waste water', 'water', 'water efficiency', 'drought', 'environmental', 'flood', 'infrastructure', 'management', 'quality', 'reduce', 'scarcity', 'supply', 'sustainable', 'water access', 'hygiene'], 'SDG7': ['clean energy', 'energy efficiency', 'energy recovery', 'fossil fuel', 'low carbon', 'regulated energy', 'technology', 'unregulated energy', 'zero carbon', 'clean fuel', 'renewable energy'], 'SDG8': ['compulsory labour', 'development', 'diverse talent', 'economic', 'employability', 'employment', 'enterprise', 'entrepreneur', 'equal opportunities', 'exploitation', 'finance', 'forced labour', 'human rights', 'innovative', 'investment', 'jobs', 'modern slavery', 'servitude', 'slavery', 'study', 'training', 'unemployment', "workers' rights", 'workforce'], 'SDG9': ['development', 'knowledge', 'technology'], 'SDG10': ['age', 'belief', 'bullying', 'civil partnership', 'disability', 'disabled', 'discrimination', 'diverse', 'diversity', 'equal pay', 'ethnic minorities', 'ethnicity', 'exclusion', 'exploit', 'gender', 'gender identity', 'gender reassignment', 'harassment', 'human rights', 'inclusive', 'race', 'racism', 'religion', 'religious belief', 'sex', 'sexual orientation', 'sexuality', 'transgender', 'victimisation', 'vulnerable'], 'SDG11': ['green spaces', 'public transport', 'recyclable', 'recycle', 're-use', 'sustainable', 'sustainable travel', 'transport', 'waste', 'waste hierarchy', 'waste management'], 'SDG12': ['food waste', 'supply chain', 'sustainable consumption', 'material', 'resources', 'resource efficiency'], 'SDG13': ['carbon emissions', 'climate', 'climate change', 'co2', 'drought', 'resilience', 'sequester', 'extreme weather'], 'SDG14': ['sustainable fishing', 'biodiversity', 'conservation', 'environmental', 'water', 'environmental stewardship'], 'SDG15': ['biodiversity', 'biodiversity offsetting', 'biological diversity', 'breeding', 'ecological', 'ecosystem services', 'environment', 'extinction', 'flower-rich', 'grassland', 'habitats', 'hedgerows', 'insect', 'local', 'native', 'natural', 'pollinator', 'protection', 'species', 'threatened', 'trees', 'vegetation', 'wild', 'wildflower', 'wildlife', 'wildlife corridors', 'environmental stewardship'], 'SDG16': ['abuse', 'crime', 'criminal', 'criminal action', 'criminal offence', 'discrimination', 'duty of care', 'harm', 'illegal', 'judicial', 'justice', 'law', 'moral responsibility', 'probation', 'protection', 'radicalisation', 'safe environment', 'unethical', 'victimisation', 'whistleblowing'], 'SDG17': ['global', 'link', 'linked', 'partnerships', 'worldwide']}


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY  = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config( 'DB_ENGINE'   , default='postgresql'    ),
        config( 'DB_USERNAME' , default='appseed'       ),
        config( 'DB_PASS'     , default='pass'          ),
        config( 'DB_HOST'     , default='localhost'     ),
        config( 'DB_PORT'     , default=5432            ),
        config( 'DB_NAME'     , default='appseed-flask' )
    )

class DebugConfig(Config):
    DEBUG = True

# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug'     : DebugConfig
}