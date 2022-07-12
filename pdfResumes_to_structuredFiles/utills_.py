def clean_string(cadena):
    cadena = cadena.replace('b"', "")
    cadena = cadena.replace("b'", "")
    cadena = cadena.replace('\\x00', "")
    cadena = cadena.replace('\\x01', "")
    cadena = cadena.replace('\\x02', "")
    cadena = cadena.replace('\\u0171', "u")
    cadena = cadena.replace('\\x03', "")
    cadena = cadena.replace('\\x04', "")
    cadena = cadena.replace('\\x05', "")
    cadena = cadena.replace("\\xe2\\x80\\x93", "-")
    cadena = cadena.replace("\\xe2\\x80\\x94", "-")
    cadena = cadena.replace("\\x0c", "")
    cadena = cadena.replace("\\xe2\\x80\\x99", "'")
    cadena = cadena.replace("\\xe2\\x80\\x9c", "'")
    cadena = cadena.replace(",\\xe2\\x80\\x9d", "'")
    cadena = cadena.replace("\\xe2\\x80\\x9d", "")
    cadena = cadena.replace("\\xe2\\x80\\x98", "")
    cadena = cadena.replace("\\xe2\\x80\\xa2", "")
    cadena = cadena.replace("\\xef\\x82\\xb7", "")
    cadena = cadena.replace("\\xef\\x81\\xb6", "")
    cadena = cadena.replace("\\xc3\\xa9", "e")
    cadena = cadena.replace("\\xc3\\x89", "E")
    cadena = cadena.replace("\\xc3\\xad", "i")
    cadena = cadena.replace("\\xc3\\xb3", "o")
    cadena = cadena.replace("\\xc2\\xa0", "")
    cadena = cadena.replace("\\xc2\\xb4", "")
    cadena = cadena.replace("\\xc3\\xa0", "a")
    cadena = cadena.replace("\\xc3\\xa1", "a")
    cadena = cadena.replace("\\xc2\\xab", "'")
    cadena = cadena.replace("\\xc2\\xbb", "'")
    cadena = cadena.replace("\\xc3\\xa7", "ç")
    cadena = cadena.replace("\\xc5\\x9f", "ş")
    cadena = cadena.replace("\\xc3\\xa4", 'ø')
    cadena = cadena.replace("\\xc3\\xb8", 'ø')
    cadena = cadena.replace("\\xc3\\xa8", "")
    cadena = cadena.replace("\\xc3\\xbc", "ü")
    cadena = cadena.replace("\\xc3\\xa4", "ä")
    cadena = cadena.replace("\\xc3\\x8d", "I")
    cadena = cadena.replace("\\xef\\xac\\x83", "ffi")
    cadena = cadena.replace("\\xe2\\x82\\xac", "€")
    cadena = cadena.replace("\\xef\\xac\\x82", "fl")
    cadena = cadena.replace("\\xef\\xac\\x81", "f1")
    cadena = cadena.replace("\\xef\\xac\\x80", "ff")
    cadena = cadena.replace("\\xe2\\x81\\x84", "ff")
    cadena = cadena.replace("\\xef\\x82\\xa7", "")
    cadena = cadena.replace("\\xef\\x82\\xa4", "ff")
    cadena = cadena.replace("\\xef\\xac\\x81", "fi")
    cadena = cadena.replace("\\xe2\\x80\\xa6", "...")
    cadena = cadena.replace("\\xe2\\x80\\xa1", "")
    cadena = cadena.replace("\\xe2\\x80\\x9e", '"')
    cadena = cadena.replace("\\xc3\\xa2", "â")
    cadena = cadena.replace("\\xc3\\xb1", "ñ")
    cadena = cadena.replace("\\xc3\\x83", "Ã")
    cadena = cadena.replace("\\xc3\\x97", "×")
    cadena = cadena.replace("\\xc2\\xa2", "¢")
    cadena = cadena.replace("\\xc5\\xa1", "š")
    cadena = cadena.replace("\\xc3\\x96", "Ö")
    cadena = cadena.replace("\\xc5\\x9e", "Ş")
    cadena = cadena.replace("\\xc3\\xb2", "ò")
    cadena = cadena.replace("\\xc3\\xba", "ú")
    cadena = cadena.replace("\\xc3\\x9f", "ß")
    cadena = cadena.replace("\\xc3\\xa3", "ã")
    cadena = cadena.replace("\\xc2\\xbf", "¿")
    cadena = cadena.replace("\\xc3\\xaf", "ï")
    cadena = cadena.replace("\\xc3\\xbb", "û")
    cadena = cadena.replace("\\xc3\\x93", "Ó")
    cadena = cadena.replace("\\xd3\\xa6", "Ӧ")
    cadena = cadena.replace("\\xc3\\xaa", "ê")
    cadena = cadena.replace("\\xc3\\xa5", "å")
    cadena = cadena.replace("\\xc2\\xb0", "°")
    cadena = cadena.replace("\\xc3\\xb4", "ô")
    cadena = cadena.replace("\\xc2\\xa3", "£")
    cadena = cadena.replace("\\xc2\\xb8", "¸")
    cadena = cadena.replace("\\xc3\\x98", "Ø")
    cadena = cadena.replace("\\xc3\\xab", "ë")
    cadena = cadena.replace("\\xc3\\xae", "î")
    cadena = cadena.replace("\\xcb\\x98", "")
    cadena = cadena.replace("\\xcc\\x81", "")
    cadena = cadena.replace("\\xce\\x93", "Γ")
    cadena = cadena.replace("\\xc3\\x81", "Á")
    cadena = cadena.replace("\\xe2\\x88\\x9a", "")
    cadena = cadena.replace("\\xc3\\xb6", "ö")
    cadena = cadena.replace("\\xc4\\xb1", "ı")
    cadena = cadena.replace("\\xc2\\xae", "")
    cadena = cadena.replace(" \\xcb\\x9d", "")
    cadena = cadena.replace("\\xc2\\xaa", ".")
    cadena = cadena.replace("\\xe2\\x82\\x82", "₂")
    cadena = cadena.replace("\\xe2\\x96\\xaa", "")
    cadena = cadena.replace("\\xef\\x82\\xa2", "ffi")
    cadena = cadena.replace("\\xef\\x81\\xb3", "")
    cadena = cadena.replace("\\xe2\\x80\\xa8", "")
    cadena = cadena.replace("\\xc2\\xa8", "")
    cadena = cadena.replace("\\xc3\\xa6", "ae")
    cadena = cadena.replace("\\xc3\\xb6rg\\xc3\\xb6", "örgö")
    cadena = cadena.replace("\\xef\\x81\\x93\\xef\\x80\\xbb", "")
    cadena = cadena.replace("\\xc2\\xad\\xe2\\x80\\x90", "")
    cadena = cadena.replace("\\xe5\\xbc\\xa0\\xe6\\xa9\\xb9", "")


    cadena = cadena.replace("\\xe3\\x80\\x8a\\xe6\\xb8\\x85\\xe5\\x8d\\x8e\\xe9\\x87\\x91\\xe8\\x9e\\x8d\\xe8\\xaf\\x84\\xe8\\xae\\xba\\xe3\\x80\\x8b", "")
    cadena = cadena.replace("\\xe8\\xb5\\x84\\xe4\\xba\\xa7\\xe5\\xae\\x9a", "")
    cadena = cadena.replace("\\xe4\\xbb\\xb7\\xe4\\xb8\\xad\\xe7\\x9a\\x84\\xe5\\x9b\\xa0\\xe5\\xad\\x90\\xe5\\xa4\\xa7\\xe6\\x88\\x98", "")

    cadena = cadena.replace("\\\'", "'")
    cadena = cadena.replace("\\t\\r", "")
    cadena = cadena.split("\\n")
    cadena = [i.strip() for i in cadena]
    lista = [i for i in cadena if len(i)!=0]
    return lista


def lista_cargos():
    return ['Vice Chairman','A.b.', 'Academic Visits', 'Academic visits', 'Advanced Grant', 'Advanced grant', 'advanced grant', 'Adjunct Professor', 'Adjunct Research Professor', 'Adjunct professor', 'Adjunct research professor', 'Affiliated Professor', 'Affiliated professor', 'Assistant Editor', 'Assistant Professor', 'Assistant Professor In Economics', 'Assistant editor', 'Assistant professor', 'Assistant professor in economics', 'Associate Director', 'Associate Editor', 'Associate Faculty', 'Associate Head', 'Associate Professor', 'Associate director', 'Associate editor', 'Board member', 'Associate faculty', 'Associate head', 'Associate professor', 'Award', 'B.a.', 'B.A.','B.sc', 'Bachelor', 'Board Member', 'Book Review Editor', 'Book review editor', 'Booth Professor', 'Booth professor', 'Chair', 'Chairman', 'Co-Director', 'Co-director', 'Co-editor', 'Computer Science Magnet', 'Computer science magnet', 'Council Member', 'Council Member Diplom','Council member', 'Council member diplom', 'Directeur', 'Director', 'Editor-in-chief', 'Editorial Board', 'Editorial board', 'Elected Member', 'External Examiner', 'External examiner', 'Elected member', 'Faculty Research Fellow', 'Faculty research fellow', 'Fellow', 'Fellowship', 'Former Associate Editor', 'Former associate editor', 'Full Professor', 'Full professor', 'Gastprofessor', 'Grant', 'Guest Editor', 'Guest editor', 'Instructor', 'International Research Fellow','International research fellow', 'international research fellow', 'Invited Editor', 'Invited editor', 'Laurea', 'Lecturer','MSc', 'M.a', 'M.A.','M.a.', 'M.Sc', 'm.sc','msc', 'M.sc','Member', 'Mphil', 'Msc','Panel Member', 'Panel member', 'Ph. D.', 'Ph. d.', 'Ph.d', 'Ph.d.', 'Ph.D.','Postdoctoral Researcher', 'Postdoctoral researcher', 'Prize', 'Professor', 'Professor Of Economics', 'Professor of economics', 'Project Advisor', 'Project advisor', 'Research Assistant', 'Research Associate', 'Research Chair', 'Research Fellow', 'Research Fellowship', 'Research Professor', 'Research assistant', 'Research associate', 'Research chair', 'Research fellow', 'Research fellowship', 'Research professor', 'S.m.', 'Scholarship', 'Senior Lecturer', 'Senior lecturer', 'Teaching Assistant', 'Teaching assistant', 'University Professor', 'University professor', 'Visiting Associate Professor', 'Visiting Assistant Professor', 'Visiting Fellow', 'Visiting Postdoctoral Researcher', 'Visiting Professor', 'Visiting Research Faculty', 'Visiting Research Student', 'Visiting Scholar', 'Visiting Student', 'Visiting associate professor', 'Visiting assistant professor', 'Visiting fellow', 'Visiting postdoctoral researcher', 'Visiting professor', 'Visiting research faculty', 'Research Visitor', 'Research visitor', 'research visitor','Visiting research student', 'Visiting scholar', 'Visiting student', 'Visitor', 'a.b.', 'academic visits', 'adjunct professor', 'adjunct research professor', 'affiliated professor', 'assistant editor', 'assistant professor', 'assistant professor in economics', 'associate director', 'associate editor', 'associate faculty', 'associate head', 'associate professor', 'award', 'b.a.', 'b.sc', 'bachelor', 'board member', 'book review editor', 'booth professor', 'chair', 'chairman','co-director', 'co-editor', 'computer science magnet', 'council member', 'council member diplom', 'directeur', 'director', 'editor-in-chief', 'editorial board', 'elected member', 'external examiner', 'faculty research fellow', 'fellow', 'fellowship', 'former associate editor', 'full professor', 'gastprofessor', 'grant', 'guest editor', 'instructor', 'invited editor', 'laurea', 'lecturer', 'm.a', 'm.a.', 'member', 'mphil', 'msc','panel member', 'ph. d.', 'ph.d', 'ph.d.', 'postdoctoral researcher', 'prize', 'professor', 'professor of economics', 'project advisor', 'research assistant', 'research associate', 'research chair', 'research fellow', 'research fellowship', 'research professor', 's.m.', 'scholarship', 'senior lecturer', 'teaching assistant', 'university professor', 'visiting assistant professor', 'visiting fellow', 'visiting postdoctoral researcher', 'visiting professor', 'visiting research faculty', 'visiting research student', 'visiting scholar', 'visiting student', 'visitor']

def lista_inst():
    return ["ESRC", "University of Exeter", 'Yale University', 'CREI', "Facebook", "Emerald Literati Network Awards", "Universitat Mannheim", "Journal of Financial Intermediation", "University of Oregon", "Investigaciones Económicas", "Universidad de Buenos Aires", "Tel-AViV University", "CREST-LEI, Paris", "Kyoto University", "Spanish Economic Association meetings", "RFF (Resources for the Future)", "The B.E. Journal of Theoretical Economics", "LykkeX", "Joint Infrastructure Fundation", "Northwestern Universit", "University of Central Florida", "Turkish Presidential Culture", "Mathematical Reviews", "University of Essex", "British Academy", "Universitat Autònoma de Barcelona", "Arizona State University", "The Mediocredito Centrale", "University Of Rochester", "CESSA", "F.M. Kirby Research Center", "Journal of Economic Analysis & Policy", "Universitat Autònoma", "American Bar Foundation", "Lyxor", "The Review of Economic Studies", "The Econometric Society", "MasterCard Foundation", "Academia Europaea", "Theory and Decision", "Computational Statistics and Data Analysis", "University at Albany, State University of New York", "Econometric Society.", 'Graduate School of Business','Graduate school of business','graduate school of business', "Journal of Securities Markets", "University Of International Business and Economics", "National Science Foundation Research", "Society for Economic Measurement", "International Journal of Child Care and Education Policy", "Applied Economics Research Bulletin", "University of California, Berkeley", "Annales díEconomie et de Statistique", "Julis-Rabinowitz Center for Public Policy and Finance", "Journal of Socio-Economics", "Social Choice and Welfare", "Journal of Business & Economic Statistics", "Bank of England", "Columbia University", "The University of Chicago", "Chinese Economists Society", "Center for Advanced Behavioral Studies", "European Research Council Starting", "University Of Wisconsin, Madison", "Massachussets Institute of Technology", "Empirical Economics", "Kansai University", "ESRC Project", "MBA", "U.K.", "Colorado College", "University of Copenhagen", "ERC advanced grant", "Alexander von Humboldt Foundation", "Marie Curie Research", "Review of Economic Studies", "Board of Governors of Economic Policy", "College of William and Mary", "Russell Sage Foundation", "The Game Theory Society", "Econometrical Journal", "Fullbright", "The Royal Economic Society", "Barcelona Labor Summer School", "Oxford University Press", "Sungkyunkwan University", "Journal of Business and Economic Statistics", "Carnegie Mellon University", "Society For The Advancement Of Economic Theory", "Joint Center for Poverty Research", "University of Wisconsin, Madison", "Computational Statistics And Data Analysis", "Critical Finance Review", "Minnesota Economic Science Lab", "University Of Bergamo", "Niehaus Center for Globalization and Governance", "K. U. Leuven", "International Crops Research Institute of the Semi?Arid Tropics (ICRISAT)", "Ecole Polytechnique", "University of Queensland", "Institute for Research on Poverty", "Centre interuniversitaire de recherche en economie quantitative", "Europlace Institute Of Finance", "Royal Society of Canada", "Sorbonne University", "Econometric Methods", "Birkbeck University of London", "Universidad Complutense de Madrid", "University of Zürich", "Board of Advisors", "Provost", "Charles de Gaulle University – Lille Iii", "American Political Science Association", "University of Amsterdam", "Fundación de Estudios de Economía Aplicada (FEDEA)", "University of Illinois", "Council of Economic Advisors", "University of California, Berkely", "EIEF", "Editorial Board: AEJ: Microeconomics", "Austrian Science Foundation", "US-Israel Binational Science Foundation", "Copenhagen Business School", "Shell UK Oil, London", "American Economic Journal-Microeconomics", "American Economics Association", "Stockholm University", "Imperial Oil", "Investigaciones Economicas", "Council of Canada", "Federal Reserve Board of New York", "Graduate School of Economics, FGV", "Journal of Business & Economics Statistics", "Banco de España", "Review Of Economics And Statistics", "University of Rochester", "The Board of Governors of the Federal Reserve System", "Indiana University (Bloomington)", "European Journal of Political Economy", "Diversity Fund", "RTN", "ANR", "Econometric Society Research Monographs Series", "University of Technology, Sydney", "Department of Economics", "University Lilly Family School of Philanthropy", "B.E. Journal in Theoretical Economics", "Maurice Allais Prize", "Institut d’Analisi Economica", "Kiev School of Economics", "Fundación Getúlio Vargas", "Laboratory for Information and Decision Systems", "AGM", "Impa", "Ecole des Hautes Etudes en Sciences Sociales", "School of Governance", "University Of Michigan", "Galatasaray Universitesi", "NIH", "Electrical Engineering and Computer Science Department", "University of Pennsylvania", "Northern New Jersey Chapter of the American Statistical Association", "Oslo University", "Manchester University", "Harvard Graduate Student Council", "Centre for Microdata Methods and Practice", "Nova School of Business and Economics", "University of Tilburg,", "Bank of Canada Fellowship", "Societat Econòmica Barcelonesa d’Amics del País", "University of Southampton", "University Of Primorska", "Nuffield College, Oxford", "University of New Brunswick", "Federal Reserve Bank of Chicago;", "Economics Bulletin", "Tinker Foundation", "Institute of Applied Econometrics", "Universita degli Studi di Roma “Tor Vergata”", "Center for Econometrics and Microdata", "Northwestern University", "Association of American Publishers", "Bernacer Prize", "Journal of Financial Economics", "TIAA-CREF Paul A. Samuelson", "Agence National de la Recherche (ANR)", "Pompeu Fabra", "Journal of Econometrics Annals Issue", "Queen’s University", "Generalitat de Catalunya", "Becker Friedman Institute", "CFI & BC Knowledge Development Fund", "Stanford Center on Longevity", "The B.E. Journal of Macroeconomics", "CES", "University of Warwick", "University College London", "Journal of Applied Econometrics", "Amazon. Com (Central Economics)", "International Econometric Review", "Economic and Social Research Council (ESRC) research grant", "Israel Science Foundation", "Economics Bulletin´s", "Joint Global Change Research Institute", "International Journal Game Theory", "University of Waterloo", "University of Chicago Booth School of Business", "AGAUR – SGR", "Statistica Sinica", "SSHRC", "BSI Gamma Foundation Research", "Not A Journal Of Economics", "Stern Economics Ph.D. program", "Microsoft Research", "Board of Governors, Washington", "Barcelona Graduate School Of Economics", "Banque de France Foundation", "Robert King Steele Faculty", "The Journal of Statistical Planning and Inference", "Advances in Mathematical Economics", "Bonn University Summer School", "IMPA", "Journal of The Japan Statistical Society", "University of Heidelberg", "Expansión and Actualidad Económica,", "Northeastern University", "European University Institute", "North Carolina State University", "University of Munich", "Italian Government", "Universidad Torcuato di Tella", "Sao Paulo School of Economics", "Caltech", "Collegio Carlo Alberto", "University at Albany", "University Of Pittsburgh", "Federal Ministry of Economic Affairs", "Universidad Del País Vasco", "Portuguese Economic Journal", "Hebrew University Of Jerusalem", "National Bureau of Economic Research EFMPL Group", "Massachusetts Institute of Technology.", "McMaster University", "International Asssociation for Applied Econometrics", "Society of Labor Economics", "The International Statistical Institute (ISI)", "Alfred P. Sloan Foundation", "University of St. Andrews", "Center for Economic Behavior and Inequality", "Canadian Institute for Advanced Research", "CED", "Barcelona Graduate School", "Journal of Dynamics and Games", "CFA Society of Toronto Hillsdale", "UC Berkeley", "All Souls College", "Stochastic Systems", "JEDC", "Louis Walinsky Fund in Economics", "American Academy Of Arts and Sciences", "California Institute of Technology `", "International Economic Review", "JET", "American Academy of Arts and Sciences.", "University Of Western Ontario", "European Economics Association", "Society of Financial Econometrics (SoFiE)", "Cambridge University", "University of California at los Angeles", "University of Sankt Gallen", "Editor in chief of Econometrica", "BREAD", "Center for Basic Research in the Social Sciences", "Federal Reserve Bank of Kansas City", "Journal of Risk and Uncertainty", "Economic and Social Research Council.", "National Bank of the Republic of Belarus", "Investigaciones Econ´Omicas, Moneda y Cr´Edito", "11th world congress of the econometric society", "Centre for Research and Analysis of Migration", "Danish National Research Foundation", "Journal of Economics theory", "The University of Tokyo", "Security Pacific National Bank", "Review of Asset Pricing Studies", "Tse Digital Center", "Asociación Española para la Economía Energética (AEEE)", "University of Texas", "Ibm", "Council of the Royal Economic Society", "American Finance Association", "The Society for the Advancement of Economic Theory", "Bi-national Science Foundation", "Center for Advanced Study in the Behavioral Sciences", "Greqam", "UNC", "Esther and T.W. Schultz Endowment Fund Dissertation", "London School of Economics 1996", "Society for the Advance of Economic Theory", "University of Maryland", "The Society for the Advancement of Economic", "Bernácer Prize", "Developing Economies", "UniversitÈ de Lausanne", "Economic Journa", "Columbia University, New York", "Center for Operations Research and Econometrics (CORE)", "IZA (Institute for the Study of Labor)", "Uni. of Toronto", "European Central Bank", "Journal of Financial Intermediationncial Intermediation", "Society of Labor Economists Annual Meetings", "Journal of Time Series Analysis'", "Université Paris 1 Panthéon-Sorbonne", "University College, Dublin", "Research Program for Banking at Fundación BBV,", "Centre National de la Recherche Scienti?que", "American Economic Association Committee", "Aarhus University", "BROWN UNIVERSITY", "Rajk L´aszl´o College", "Oxford", "Belarus", "Queens University", "HEC", "Paris X", "Universitat Pompeu Fabra.", "Stony Brook University", "Social Sciences And Humanities Research Council", "Tufts University", "Bundesbank", "Israeli Academy of Sciencies and Humanities", "Neubauer Family Faculty", "University of Luxembourg", "CES-Ifo", "Handbook of Financial Econometrics", "Econometric Theory,", "IFAU", "Ecole Normale Supérieure De Cachan", "Louis Walinsky Fund In Economics", "Council of the Econometric Society", "UniversitÃ© Paris Dauphine", "Foundation Banque de France", "Institute for Nonlinear Dynamical Inference", "CEMFI Summer School", "CEP", "Decision Sciences", "International Association of Financial Engineers", "Directors of CaixaBank", "Social Sciences and Humanities Research Council of Canada (SSHRC)", "Annals of Finance", "Economic Inquiry", "Philip Leverhulme Prize Fellowship", "University of Indonesia", "European Economic Review", "Studies in Nonlinear Dynamics and Econometrics", "Central European University", "National Institute of Aging Grant", "Bank of Canada, Research Department", "M.I.T.", "Quarterly Journal of Economics", "Universidad de San Andre?s", "Scientific Committe of FEDEA", "Pew Charitable Trusts", "Fundação Calouste Gulbenkian", "CIFAR", "Tinbergen Institute, Amsterdam/Rotterdam", "Bell Laboratories", "Humboldt-University Berlin,", "University of British", "International Tax and Public Finance", "Nicholas J. Nicholas Fellow", "Operations Research", "University of Technology Sydney", "Keynes Fund", "National Institute of Economic and Social Research", "Journal Of Econometric Methods", "The Federal Reserve Bank of Minneapolis", "University of British Columbia", "Monash University", "Cemfi Madrid", "Editorial Board of the Journal of Economic Growth", "Cowles Foundation for Research in Economics", "Academic Council of the Barcelona Graduate School of Economics", "Catalyst Institute", "Universitaire de France", "NICHD-PSC", "Penn State University", "Fondation Banque de France", "Japanese Economic Review", "Journal of Time Series Analysis", "Hopkins University", "Congressional Budget Office’s (CBO’s) Panel of Health Advisers", "European Finance Review", "Centre for Economic Policy Research  and the Department for International Development", "Toulouse Network for Information Technology", "The Pennsylvania State University", "Board of Governors of the Federal Reserve System", "Ohio State University", "Econometrics Journal", "Einaudi Institute for Economics and Finance", "Journal of Statistical Computation and Simulation", "Erikson Institute", "The Richard Stone Prize in Applied Econometrics", "Paris School of Economics", "Social Sciences and Humanities Research Council of Canada", "Research in Economics", "Jinan University", "Journal of Money Credit and Banking", "The Journal of Financial Markets", "CESifo Research Network", "Harvard University", "University of Cambridge", "NSF CAREER", "Econometric Society in Montreal", "Penningmarknadsmäklarna AB", "N.A", "Science of Generosity", "Maastricht", "New Economics School", "IDC (Israel).", "NICHD", "New Zealand Association Of Economists", "Hoover Institution National", "Journal Of Public Economic Theory", "Advisory Comitee for the Economic Recovery and Growth (CAREC) to the Government of Catalonia", "EFRI", "Econometrics and Statistics", "National Bureau of Economic Research Macroeconomic Annual", "DARES", "ENSAE Paris", "Economics and Politics", "University of Tokyo March", "Finance and Stochastics", "Toulouse School of Economics", "Committe on statistical studies", "Humboldt-Universität", "University of Auckland", "Clemson University", "British Telecom Group", "Econometric Reviews,", "International Tax & Public Finance", "Universit¨at Bonn", "Quantitative Finance and Economics", "Crest-Ensae", "Tel Aviv University.", "University of British Columbia.", "NY", "Econometric Theory", "Universidad de San Andr´es", "Microsoft", "Singapore Management University", "Macro-Finance Society", "Games and Economic Behavio", "EPRU", "University of Karlsruhe", "Citigroup Financial Insights Project", "The Brookings Institution", "Centre for Economic Policy Research (CEPR)", "Review of Finance", "International Society for Computational Social Science (ISCSS)", "AEA Continuing-Education Course in Game Theory", "Committee of Presidents of Statistical Societies", "Economic Science Association", "Princeton", "Berlin-Brandenburg Academy of Sciences", "Econometrics Theory", "National Bureau of Economic Research’s", "Danish National Research Foundation,", "LSE", "Ricerche Economiche", "University of Basel", "Game Theory society", "Statistical Modeling: An international journal", "EPRN", "Princeton Economics", "American University in Bulgaria", "Council of the European Economic Association (EEA)", "University of Pau and Pays de lâ€™Adour", "University of Minnesota", "UCSD", "Catholic University Leuven", "University of Notre Dame", "Amazon.com", "Journal of Econometric Theory", "International Association of Applied Econometrics", "Institute for the Study of Labor", "Rand Journal of Economics", "Amazon", "National Contest in Mathematics", "Belarus State Economic University", "Journal of Financial Econometrics", "Swiss National Science Foundation (SNSF)", "Kellogg School of Management", "MatØk-Nyt", "University of Pennsylvania Research Foundation", "IGIER", "Institute of Mathematical Statistics", "European Research Council (ERC)", "MacArthur Foundation", "Johns Hopkins University", "London School of Economics", "The Government of Israel", "National Centre for Research Methods", "Applied Microeconomics / Industrial Organization, CEPR", "RAND Corporation", "Northern JiaoTong University", "Universitat Pompeu Fabra", "American Statistical Association.", "The Danish Research Academy", "University of Wisconsin", "Econometric Theory Multa Scripsit Award", "Economics and Philosophy", "Journal of Money, Credit and Banking", "Australian Research Council", "Center for Economic Policy Research CEPR", "Centre for Economic Policy Research", "Accademia Dei Lincei", "The London School of Economics", "University Of Dortmund", "Statistical Inference For Stochastic Processes", "University of Gothenburg", "NATIONAL BUREAU OF ECONOMIC RESEARCH", "Experimental Economics", "California Institute of Technology.", "The econometric society", "E.H.E.S.S.", "CORIPE Piemonte", "University of Melbourne,", "Steering Committee of the Association for Competition Economics,", "CREI", "CESifo", "Quantitative Economics", "Sloan Foundation", "Society of Labor Economist", "International Meetings of the Society for Social Choice and Welfare", "UW-Madison", "FQRSC", "Stanford Institute", "Independent Claims Resolution Foundation", "Technical University of Berlin", "Fudan University, Shanghai", "Bell Journal of Economics", "New York University", "University Of Auckland", "University of Tel Aviv", "BE Journal in Theoretical Economics", "PUC", "Fundació Privada Aula", "Jan Wallanders and Tom Hedelius Foundation", "SWIFT Institute Advisory Council", "Swiss SNF", "CIdE Summer School of Econometrics, Bertinoro", "Canada Council for the Arts Killam", "University of Oxford", "Data Science Justice Collaboratory", "Society of Labor Economists.", "Society for the Advancement of Economic Theory,", "Alfred P. Sloan Dissertation Fellowship", "Council of the European Economic Association", "University of Oslo", "New York University Abu Dhabi", "ARC Discovery Projects", "KAEA; Maekyung Daily", "Israel Institute of Technology", "University of California", "Research Funding for Canada Research Chair", "Advisory Board", "Journal of Bond Trading and Management", "University of Bern", "Journal of Business", "National Economic Research Associates (NERA), Cambridge", "University of Porto", "International Mathematical Olympiads", "Universita della Svizzera Italiana", "STICERD", "Labour Economics", "Hebrew University of Jerusalem", "University of California,Berkeley", "University of California San Diego", "Business Week", "Norwegian Association of Economists", "Centro De Estudios Monetarios Y Financieros", "The National Institute of Child Health and Human Development", "European Systemic Risk Board", "Harvard Society of Fellows", "Sveriges Riksbank", "University of Birmingham", "National Bureau Of Economic Research", "CEPR", "Revue Economique (third recipient).", "European Economic Association.", "Seoul National University", "Chiles Foundation", "Journal of Econometric Methods", "University Of Siena", "Bocconi University", "Fiscal Studies", "Kiel Institute for World Economy", "UK Economic and Social Research Council", "Not a Journal of Economics", "American Economic Review: Insights", "Harvard Business School", "USG Swimming and Water Polo", "Financial Analysts Journal", "Momenta Technology", "Ecole Polytechnique F ?ed ?erale de Lausanne", "Kiel Institute of World Economics", "Netherlands Economic Review", "PISA 2021 Questionnaire Expert Group", "University of Houston", "University of Texas at Austin", "University of California/Berkeley", "MIT Real Estate Entrepreneurship Laboratory", "Journal of Applied Econometrics,", "NYUAD", "University of Zurich", "Executive Committee of the Econometric Society", "University of Dortmund", "John von Neumann Award", "University of South. California, Los Angeles", "Center for Research on the Wisconsin Economy (CROWE)", "Carlson School of Management Information and Decision Sciences Department", "IADB", "Oxford Review of Economic Policy", "University of Western Ontanrio", "National School of Government", "Israeli Science Foundation", "Bachelier Society", "Scandinavian Journal of Economics", "U. Wyoming", "Editor Econometric Theory", "Advisory Group of Commission for Growth and Development", "Stanford GSB", "Japanese Journal of Statistics and Data Science", "Financial Markets Groups", "Mit", "Economic Policy", "Q Group Research", "Swiss Journal of Economics and Statistics", "Bogazici University", "The Royal Academy of Engineering Sciences", "Scientific Council", "Irish Economic Association", "Institute for Economics and Finance", "King Juan Carlos I Prize", "University of Copenhagen,", "NSEE-CREST", "Economics and Econometrics sub-panel for Research Excellence Framework (REF)", "Canadian Economics Association", "SNS", "Kiel Institute for the World Economy", "University College London and Institute for Fiscal Studies", "University of Wisconsin,Madison", "N A J Economics", "Canada Council For The Arts Killam", "ICREA", "The University of Warwick", "British Heart Foundation", "Shanghai University", "Sloan Research", "Agricultural and Applied Economics Association", "Netherlands Institute for Advanced Study", "University Of California, Los Angeles", "Australian Economic Papers", "University College of Dublin", "Economic And Social Research Council", "Crest Ensae", "Stanford Graduate School of Business", "Bank of Spain Financial Stability Review", "European research counsil", "University Of California, San Diego", "American Philosophical Society", "The Mellon Foundation", "Berkeley Electronic Journals in Economic Theory", "Econometrics Society", "Journal of Mathematical Economics,", "Mathematics and Financial Economics", "Alony-Hetz Property and Investment ltd", "Mitt Romney campaign", "ECB Wim Duisenberg Fellowship", "KU Leuven", "European Economic Association", "European Community HCM", "The Rockefeller Foundation", "Public-Private Sector Research Center", "Overseas Research Students Award", "University College, London", "European Commission", "Prometeia", "University of Chicago, Chicago, Illinois", "Maastricht Graduate School of Governance", "University of Chicago Grad. School of Business", "Institute for Advanced Study", "Nobel Memorial Prize in Economic Sciences", "Melbourne University", "TaxDev", "Richard Allen Lester University Preceptor", "AU-Ideas", "Joumal of Economic Theory", "New Zealand Association of Economists", "Centre for Labour Economics", "Economic Journal", "Federal Reserve Banks", "Research Project", "DFG Mercator", "University of Michigan, Ann Arbor", "Association of Private Enterprise Economists", "Cass Business School", "Federal Reserve System", "Forum Catalunya en Expansión", "Instituto Nacional de Matemática Pura y Aplicada", "Journal of Empirical Finance", "Royal Netherlands Academy of Arts and Sciences", "Journal of Industrial Economics", "AFOSR", "De Nederlandsche Bank", "Tsinghua University", "Social Science and Humanities Research Council", "University of London", "Journal of Mechanism and Institution", "Alfred P. Sloan Doctoral Dissertation", "Journal of Human Resources", "Louis Pasteur University I, Strasbourg", "Millenium Challenge Corporation", "ASSET Meetings", "The B.E. Press Journals in Theoretical Economics", "International Growth Centre", "ECGI", "Commonwealth Scholarship Commission", "University Paris Pantheon-Sorbonne", "Kellogg", "Catholic Research Economists Discussion Organization)", "Net Institute", "Review of Financial Studies", "Applied Probability Journals", "Universidad Torcuato Di Tella", "University of Pittsburgh", "Erasmus University", "Economic Theory Chair at Paris School of Economics", "University Paris", "ARO", "University of Western", "Mathematical Social Science", "Swedish Treasury", "Swiss Finance Institute", "London School of Economics Graduate Studentship", "Mamathics and Financial Economics", "Netherlands Network of Economics (NAKE)", "Universite Catholique de Louvain", "Theseus Institute", "Center for Human Capital Studies", "Institute for Pure and Applied Mathematics", "Japan Academy Academic", "The Foerder Insitute", "Editorial Board of the Journal of Economic Literature", "NIA", "SNS (Studief ?orbundet N ?aringsliv och Samh ?alle)", "Michigan Retirement Research Center", "UniversitÃ  Bocconi", "Indian Statistical Institute", "P.R.I.M.E. Finance Foundation", "Purdue University.", "University of Windsor Research Board Grant", "King’s College Cambridge", "Universite de Paris", "Interdisciplinary Center Herzliya", "International Monetary Fund", "Institute for Empirical Macroeconomics", "Summer Institute In Behavioral Economics", "Centre for Economic Policy", "Crest", "Joseph Rowntree Foundation", "Economic Theory", "Danish Research Agency", "POSCO Research Institute", "Society of Advancement  of Economic Theory", "University of Cologne", "Universidad Carlos III Madrid", "Stockholm School Of Economics", "University of Toulouse Capitole", "Search and Matching Cambridge", "Churchill College Cambridge", "Bank of Israel", "Grand Challenges Canada", "Netherlands Institute For Advanced Studies", "Federal Reserve Bank of Philadelphia", "CEDIL ILT", "University of Warsaw", "Technical University of Darmstadt", "John Bates Clark Medal", "Hong Kong University of Science and Technology", "Jan Wallanders And Tom Hedelius Foundation", "Rice University,", "Journal of Business, Economics and Statistics", "Foundations and Trends in Econometrics", "University of Rome", "Review Of Economic Studies", "MIT International Science & Technology Initiatives", "HEC, Paris", "Quantitative Marketing and Economics", "Advanced Economic Studies", "Japan Statistical Society", "Israel Economic Association", "British Council", "U.C. Davis", "Bilkent University", "Experimental Lab VSE", "Journal Of Bioeconomics", "National Institutes of Child Health and Human Development", "Departmental award for excellent research (Queen’s University)", "Journal of Credit Risk", "King's College Cambridge", "CNRS", "International Review of Economics", "Journal of Regional Science", "Centre National de la Recherche Scientifique", "American Enterprise Institute", "PhD Program in Economics and Finance", "Journal of Money, Credit, and Banking", "Brazilian Academy of Sciences", "J.W.Goethe University", "EARIE", "London'S Global University", "Journal ofEmpirical Finance", "Ameritech Foundation/Consortium for Research on Telecommunications Policy", "PRIN", "International Association For Applied Econometrics", "Baffi-Carefin center", "Council of Economics", "Harris School of Public Policy", "Santa Fe Institute", "Carlo Alberto Medal", "Universitat Konstanz", "Quaterly Journal of Economics", "Humboldt Univerity Berlin", "American Economic Review", "59th Putnam Competitions", "Hoover Institution", "China Economics Prize", "Simon Fraser University", "The University of Iowa", "Centre for Microdata Methods And Practice", "The National Institute Child Health and Human Development", "Leverhulme Centre", "Centre for Economic Policy Research, London", "The “Fondazione Luigi Einaudi", "INRA", "Journal of Economic Theory 2016-2019", "University of Bonn", "University of Göttingen,", "The Annals of Applied Statistics", "FARFE", "Graduate Studies", "Hitotsubashi University", "University of Cambirdge", "Econometric Society World Congress", "Rajk College,", "Queen's University", "Standford University", "Review of Economics and Statistics", "Barcelona Graduate School of Economics", "ERC", "Cambridge Working Papers in Economics", "Journal of The European Economic", "Chinese Economist Scholars Association", "Prize Committee for The Sveriges Riksbank Prize in Economic Sciences in Memory of Alfred Nobel", "Graduate Studies Committe of Universidad Internacional Menéndez Pelayo", "Royal Swedish Academy of Engineering Sciences", "University of Primorska", "London Business School", "Transferator Fondkommision", "Pio Manzu Centre", "Center for Advanced Study of Behavioral Sciences", "Journal of Environmental Economics and Management", "Riksg ?alden (Swedish National Debt Office)", "Letters in Spatial and Resource Economics", "Ben Gurion University", "Connaught Funds (University of Toronto)", "International Association for Applied Econometrics", "SKAT", "Academy Health", "Acumen LLC", "Journal Of Business And Economic Statistics", "ESEWM", "Laboratoire de Finance-Assurance", "Jaedicke Merit Award", "Paris University (Dauphine)", "Inaugural Ken-ichi Miyazawa Memoria", "Journal Of Econometrics Annals Issue", "CEMFI/Madrid", "Journal of Economic Literature", "National Academy of Sciences", "American Agricultural Economics Association", "Joumal of lntemational Economics", "NYU Stern", "National Bureau of Economic Research (NBER)", "Advanced ERC", "Catalyst Institute Research", "Financial Economists Roundtable", "Spanish Ministry of Education", "University of Chicago (Spring", "Japanese Economic Association", "The University of Wisconsin, Madison", "Journal Of Macroeconomic Dynamics", "ERC Consolidator Grant", "Swiss National Bank", "Aaron Economic Policy Institute", "Universidad del CEMA", "Elected Board Member", "The Econometrics Journal", "Pacific Institute of Mathematical Sciences", "Stern NYU", "University of Lille", "American Economic Journal: Macroeconomics", "Leverhulme Trust and ESRC", "Journal of Computational Finance", "Griswold Center", "Konjunkturinstitutet", "EPFL", "Stanford Univeristy", "St Gallen University", "American Academy of Arts and Sciencies", "Computational Economics", "University of Calgary", "Citibank Exploratory", "University of Montreal", "FCAR", "Amsterdan University Press", "Journal Of Economic Theory", "Institute of Economics and Statistics", "Premi Catalunya d’Economia", "University of Wisconsin-Madison", "Academy of Sciences", "Business and Management Section of the Academia Europaea", "Economic Design", "The Nykredit Foundation", "University of Wisconsin-Stevens Point", "Journal of Bioeconomics", "Freie Universität Berlin", "Dietrich Economic Theory Center", "Episcopal Health Foundation", "Moscow State University", "The Hebrew University", "Beijing University", "UNSW", "Royal Society Of Canada", "University of Nottingham", "Quantitative Finance", "EHESS", "National Academy of Social Insurance", "Carnegie-Mellon University", "Annals of Statistics", "David A. Wells Prize", "University of Mannheim", "University of Wisconsin Institute", "The Annals of Statistics", "Beijing Normal University", "Social Sciences and Humanities Research Council", "University Paris 1", "NBER. Cambridge, MA", "Elaine Bennett Research", "Evaluation of “Familias en Accion”", "Google", "Nber", "Environmental Protection Agency", "National Institute for Economic and Social Research", "American Finance Association t", "FIRS", "University of Southern California", "Bitrish Academy", "Univeristy of Wisconsin", "University Of British Columbia", "Games And Economic Behavior", "Journal of Competition Law & Economics", "Universitat Autonoma de Barcelona", "Charles M. Harper Faculty", "Revista Española de Economía", "University of Tokyo", "The RAND Journal of Economics", "Birkbeck College University of London", "CEPS", "SED Saint Louis", "University Of California At Berkeley", "American Association for the Advancement of Science", "Asian Regional Standing Committee of Econometric Society", "Econometric Society Monographs", "Financial Services Authority", "Journal of Economic Perspectives", "U. Rochester", "Journal of Sports Economics", "Middle East Technical University", "The Israeli Academy of Sciences and Humanities", "John Simon Guggenheim Memorial Foundation", "CNRS-IDEFI", "Cornell University", "European Research Council", "Deutsche Forschungsgemeinschaft (DFG) research grant", "German Academic Exchange Service", "Institute of Economic Analysis", "The Russell Sage Foundation", "Department of the Bank of Israel", "Canada Council", "MPA Program LSE", "Review of F inancial Studies", "National University of Singapore", "The Economic Journal", "Center for Advanced Studies in the Behavioral Sciences", "University of Trieste", "Tilburg University", "Netherlands Organisation for Scientific Research", "University of chicago", "IFS", "Dennis J. Aigner", "German National Academic Foundation", "Canadian Institute For Advanced Research", "(DFG", "Arnold Foundation", "European Economic Association Congress", "Scientific Advisory Board", "Bank of Italy", "University College London,", "University of Cantabria", "KSM", "University of Orléans", "Australian National University.", "John M.Olin Foundation", "Frank P. Ramsey Prize", "University Paris 9", "Centre for Economic Performance (CEPR)", "Economía Industrial", "Society for Advancement of Economic Theory", "University of Bristol", "University of Manitoba", "Congressional Budget Oce", "Carnegie", "David Horowitz Institute", "ATA1 research", "Graduate Institute, Geneva", "University of California Berkeley", "Annual Revenue of Economics", "The British Academy", "Royal Netherlands Academy of Arts and Sciences (KNAW)", "American Economic Journal: Applied Economics", "Paris VI", "University of Toronto", "Margaret G. Reid Memorial Fund Dissertation", "The Royal Swedish Academy of Sciences", "SFB-884", "Silicon Graphics Inc", "Investment Committee of the European Economic Association", "Centro De Estudios Monetarios Y Fiancieros", "NSF", "Toulouse University", "Turkish Academy of Science", "NCCR-FINRISK", "CeMMAP International", "Hoover National", "NET Institute Research grant", "Society of Financial Econometrics", "Journal of Transport, Economic and Policy", "Econometrics Reviews", "Advisory Group of DG Industry of the European Commission", "Montgomery Blair High School", "Laurea Universita' Bocconi", "Journal of Business Economics and Statistics", "Swiss Federal Institute of Techonology", "Institute for Fiscal Studies", "German National Science Foundation", "American States, PRA", "Barcelona Economic Analysis Team", "NBER-NSF", "University of Michigan", "Trustees of the Fundació Empresa i Ciència of the Universitat Autònoma de Barcelona", "The Journal of the European Economic Association", "NSF Grant", "German-Israeli Foundation for Scientific Research & Development", "National Institute on Aging", "Nota d’Economia", "Science of Philanthropy Initiative", "Review of Economic Dynamics", "U. Toronto", "Mcgill University", "Templeton Foundation", "North American Econometric Society Annual Meetings", "University Of Wisconsin,Madison", "University of International Business and Economics", "American Statistical Association Committee on Energy Statistics", "Journal of Labor Economics", "Chinese University of Hong Kong", "Journal of finance", "ESRC-DFID", "Federal Reserve Bank of Atlanta", "University of Sorbonne", "Humbolt University", "University of the Littoral Opal Coast", "European Economic Review", "Drexel University, Philadelphia, Pennsylvania", "China Ministry of Information on Telecommunications Regulation", "Tel Aviv University", "Universidade Catolica Portuguesa", "National Institute of Aging", "ESRC Centre", "Economic and Social Research Council (ESRC)", "Ecole Polytechnique, Paris", "Society for the Advancement of Economic Theory", "Center for Economic and Policy Research", "Centro de Altísimos Estudios Ríos-Perez", "Undergraduate Studies", "U.C. Santa Barbara", "University of Victoria", "Scientific Council of the Toulouse School of Economics", "Massachusetts Institute of Technology", "Universidad del País Vasco", "The European Economic Revie", "National Opinion Research Center", "Swiss Federal Institute Of Techonology", "The Society for Economic Measurement", "CPQ Women and Child Health Journal", "UPF-GSE Barcelona", "IER", "New York Federal Reserve", "Stockholm School of Economics", "Thomas Stieltjes Institute for Mathematics", "University of Frankfurt", "Governor's Advisory Council (Massachusetts)", "University of Rouen", "American Economic Association", "Sloan Fellowship", "Journal of Institutional and Theoretical Economics", "University Of Toulouse", "Social Science Humanities and Research Council", "Columbia Economics", "Tinbergen Institute", "(CIRET/FGV)", "Not A Journal of Economics", "Journal of Finance", "Multa Scripsit", "Social Science Humanities and Research Council of Canada", "Università Commerciale Luigi Bocconi", "Chicago Booth", "London 's Global University", "AT&T", "University of Glasgow", "Humboldt-University Berlin", "Evaluation Review", "European Business Organization Law Review", "International Journal of Industrial Organization", "Initiative on Global Markets", "Statistical Models and Applications", "Binational Science Foundation", "Annales d'Economie et Statistique", "Hebrew University", "RAND Journal of Economics", "HEC School of Management", "AHRQ", "U of T Mississauga", "University of Aarhus (Denmark)", "Journal of Mathematical Economics", "Ecole Nationale de la Statistique et de l’Economie", "Society of Financial Ecnometrics", "3Ie", "Queensland  University of Technology.", "Econometric Reviews", "Thomas R. Brown Foundation", "Theoretical Economics", "University of New England", "FWO", "Gavin Prize", "National Science Fundation", "United States–Israel Binational Science Foundation", "DIW", "Global Association of Risk Professionals (GARP) Risk Management Research Program", "NICHD-PARC", "Quantitive Economics", "Journal of Public Economic Theory", "University Of Birmingham", "Society for the Advacement of Economic Theory", "CORIPE", "Ekonomikommissionen", "Positivity", "The Federal Reserve Bank of New York", "Committee to Revise U.S", "McGill University", "Stockholm University Institute for International Economic Studies", "Recherches Economiques de Louvain", "Università degli Studi di Torino", "University Of Oxford", "Institute for New Economic Thinking", "Rochester Center for Economic Research", "Alfred P.Sloan", "Theorical Economics", "University Tor Vergata Roma", "European Meeting of the Econometric Society", "La Trobe University.", "UC Irvine", "Societá Italiana degli  Economisti", "Federal Reserve Bank of Cleveland:", "Banff International Research Station", "Society for Financial Econometrics", "Neu Family Award for Excellence in Teaching In Economics", "Federal Reserve Bank of New York", "Bologna", "Leverhulme Trust", "Frontiers of Economics in China", "BE Journal of Macroeconomics", "Journal of Economics", "Centro de Estudios Monetarios y Financieros", "Anna S. Aronson Memorial Award", "Economic Theory  Bulletin", "Editorial Board of the Annual Reviews in Economics", "DiTella University", "Korea America Economic Association", "Committee on the Future of Boston", "Review of Economics Studies", "J-PAL North America", "CREST", "Asia Pacific Financial Markets", "Journal of Dynamics and Games (AIMS)", "Goethe University Frankfurt", "NSF SES – 0338619", "Fishkind & Associates, Inc", "Journal of Banking and Finance", "University of Lausanne", "Journal of Behavioral and Experimental Economics", "Scandinavian Journal Of Statistics", "European University Institute (EUI)", "Associazione Amici della Bocconi", "University of Queensland,", "U. of Cambridge", "Jilin University", "Spanish ministry of education", "CEPR-ESF", "Morgan Stanley Market Microstructure Research", "University of Illinois at Urbana-Champaign", "Ecole Nationale des Ponts et Chaussées", "China Development Research Foundation", "National Academy of Education", "School of Management", "CIFAR’s Institutions", "Berlin Social Science Center", "Social Choice and Welfar", "University of Kent", "UC Davis", "(Institut d’Analisi Economica", "Reid Teaching Award", "Regional Science and Urban Economics", "The Arnold Zellner Award", "London School of Economics (Fall Term)", "Ecole Normale Superieure", "Center,Tilburg", "Kellogg Institute for International Studies", "New Zealand Commerce Commission", "Syracuse University", "Pacific Economic Review", "Universite é d 'Auvergne", "University of California-Berkeley", "Revue dâ€™Economie Politique", "Danish Council", "University of Vienna", "Enviroment Economics and the Economy", "Bank Hapoalim", "Brookings Papers on Economic Activity", "Econometrica", "Annual FAME Research Prize", "Morris Falk institution", "Statistical Inference for Stochastic Processes", "University of Lyon", "Kiel Institute Summer School on Economic Policy", "OCFEB Research Centre for Economic Policy, Rotterdam", "Open Society Institute", "UPF Barcelona", "Cirano", "Spanish High Research Council", "Graduate Institute", "Australian National University", "Nuffield Foundation", "Bonn University", "University of Cambridge, Cambridge", "International Statistical Institute", "London School of Economics and Political Science", "EEA", "International Association", "Universite de Paris I Pantheon?Sorbonne", "The Journal of Economic Literature", "Gersenzee Studentcentrum", "The University of Chicago.", "J .L. Kellogg Graduate School of Management", "Journal Of Time Series Analysis'", "United States Federal Trade Commission", "Banco De España", "International Game Theory Review", "University of Arizona Economics Society", "Journal of Economic", "University of California at San Diego", "SAET", "Gerzensee", "University Of York", "Universidad Federal de Río de Janeiro", "Centre for European Economic Research", "Smith Richardson Foundation", "Royal Society of Edinburgh", "Alfred P. Sloan", "Journal of Business and Economics Statistics", "Journal of the Japanese and International Economies", "Munich Graduate School of Economics", "Econometric Journal", "Joint Center For Poverty", "Quantitative Finance And Economics", "BFI-MFRI", "CENTER FOR ECONOMIC POLICY RESEARCH", "Inter American Development Bank", "Institute for Advanced Studies", "58th Putnam Competitions", "National Science Foundation", "Society for Social Choice and Welfare", "Alfred P. Sloan Research", "Helsinki Center of Economic Research", "Ecole Normale Sup´erieure", "Journal of Economic Geography", "National Academy of Sciences Panel On Statistical Assessments as Evidence in the Courts", "Society of Labor Economists", "Game Theory Society Council", "California Institute of Technology", "The Kellogg School of Business", "Fundacao Ciencia e Tecnologia", "University of Urbino", "Program in Public Policy", "Foundation of Strategic Research", "Economics Letters", "Instituto Brasileño de Economía", "Center for Economic Policy Research", "European Corporate Governance Institute", "CES IFO", "Teaching assistant", "Organizations and Votes in Economics", "Federal Reserve Board of Governors", "Citibank Full", "Harvard College", "CESIfo Research Network", "International Institute of Forecasting", "K.U. Leuven", "The University of Western Ontario", "OXFORD UNIVERSITY", "Abertis Chair of Regulation", "Institut d´Economie Industrielle", "Management Science", "Unicef", "University Research Foundation", "Agence Nationale de la Recherche", "Games and Economic Behavior", "University of Utrecht", "Justice Brandeis", "INET", "Google Faculty", "Universit´e de Paris", "Department of Decision Sciences", "Rimini Centre for Economic Analysis", "Universite Libre de Bruxelles", "The Annals of Economics and Finance", "The Prize Committee for the Alfred Nobel Memorial Prize in Economic Sciences", "Oxford Economics Papers", "Risk and Uncertainty", "University of North Carolina", "Bendheim Center for Finance", "Centro de Estudios Monetarios y Fiancieros", "Banck of England", "National Research Council", "Research Centre of Excellence at the University of Copenhagen,", "Federal Reserve Bank of Cleveland", "Institute for Fiscal Studies, London", "Journal of the American Statistical Association", "NBER", "Austrian Institute of Economic Research", "French Atomic Energy Agency", "Stanford Graduate Economics Association", "University of Dayton", "SFB-TBR", "Cambridge INET iInstitute", "ARO MURI", "Macro Dynamics", "Toronto Experimental Economics Lab", "University of California at Berkeley", "The Swedish Riksbank", "Journal of Political Economy", "CGI (European Corporate Governance Institute)", "University of Science and Technology", "Review of Development Economics", "University of Tübingen", "University of Florida", "University Of Essex", "Ohio Wesleyan University, Delaware, Ohio", "University Of Western", "Game Theory Society", "CEPREMAP", "Economics Research Network and Social Science Research", "Kellogg Institute Research", "Australian National University,", "Barcelona Jocs", "ISOM", "University Of California At San Diego", "Universitat Pampeu Fabra", "University of Stockholm", "Bill and Melinda Gates Foundation", "Ministry of Finance", "Konstanz University", "Technische Universität Berlin", "Society for Research in Child Development", "Journals in Economic Analysis and Policy", "Ecole Normale Supérieure", "French National Research Agency", "INSEAD", "Osaka University", "The Ohio State University", "BEPress Journals of Theoretical Economics", "Chicago Mercantile Exchange", "Helsinki School of Economics", "IMSV", "Royal Academy of Arts and Sciences, Belgium", "Enjoji Jiro Memorial", "Premi Societat Catalana d’Economia", "U. of Chicago/Argonne Nat’l Laboratory", "Chinese Government", "American Academy of Arts and Sciences", "International Journal of Central Banking", "CEBI", "National University of Ireland, Maynooth", "Summer Institute in Behavioral Economics", "Oxford University", "The Academic College of Tel Aviv-Yaffo", "European Research Council Advanced Grant", "Banca S.Paolo-IMI", "CentER for Economic Research, Tilburg", "Ecole Polytechnique Fédérale de Lausanne", "Sveriges Riksbank, Stockholm, Sweden", "Huazhong University of Science and Technology", "Institute for the Study of Labor (IZA), Bonn", "Universit´e Toulouse", "Journal of Economic Growth", "The B.E. Journals in Theoretical Economics", "Beihang University", "Carleton University", "AEJ: Microeconomics", "Institute for Humane Studies", "University of Bocconi", "Fundação Getúlio Vargas", "The Tinbergen Institute", "NBER Working Group", "Bureau for Research in Economic Analysis of Development", "University Of Cambridge", "Sloan Research Fellowships", "University of Siena", "FRB Minneapolis", "Università Bocconi", "Bureau for Research on the Economic Analysis of Development (BREAD)", "Central Bank of Armenia", "NATO", "IZA", "Bank of Portugal", "Germanscholarsorganization", "Cowles Foundation", "Mexican Government", "Eth", "American Economics Review", "NTA-TIA", "Universitat Autònoma of Barcelona", "Northwestern Advanced Workshop for Central Bankers", "University of Paris", "CESifO", "Hicks Tinbergen", "USD", "Deutsche Bundesbank", "Pandora", "Latsis-Prize", "Journal of the Royal Statistical Society, A", "The Government Commission on Central Banking Issues", "Bernoulli", "UCL", "University of Bergamo", "CJE", "Journal Of Econometrics", "John Templeton Foundation", "The World Bank", "Institute for Fiscal Studies (IFS)", "Mistra Financial Systems", "Directors of Aula Escuela Europea SA,", "Reserve Bank of New Zealand", "Annual Review of Economics", "Fundación de Economía Analítica", "The Wall Street Journal", "Portuguese Catholic University", "Royal Statistical Society", "Journal of the American Statistical Association Case Studies and Applications", "Economyc Dynamics", "Swedish Secretariat for Environmental Earth System Sciences", "NSf", "National Science Foundation Institutional", "Statistical and Applied Mathematical Sciences Institute", "Minneapolis Federal Reserve", "University of Cambridge, King's College", "The State Street Corporation", "NORC/University of Chicago", "University of St. Gallen", "Queen Mary University of London", "University of Manchester", "Purdue University", "Advisory Council of the Pla Estrategic Metropolità de Barcelona", "Turkish Sciences Association", "Committee on National Statistics", "IAST", "CEMFI", "Royal Swedish Academy of Sciences", "The Journal of Developing Areas", "Cemmap", "Geneva Finance Research Institute", "UBS International Center of Economics in Society at the University of Zurich", "SED Annual Conference", "Institute of Mathematical", "DIW Berlin", "Massachusetts Institute Of Technology", "Tinbergen Summer School, Amsterdam", "CNAM", "Centro de Estudios de Planificación of Barcelona", "French Banking Association", "Mathematical Finance", "Catholic University of Louvain", "CalTeCh", "Robert Wood Johnson Foundation", "AQR", "National Academy of Sciences Panel on the Status of Black Americans", "Socio- and Econophysics", "American Academy of Arts & Sciences", "Guggenheim Foundation", "University of Bonn", "Institute for International Economic Studies", "Empirica", "DREAM", "Annual Review in Economics", "American Statistical Association", "British Academy’s inaugural Wiley Prize", "Batterymarch", "Forschungsinstitut fur Mathematik ETH Zurich", "The Journal of Finance", "Journal of Causal Inference", "U. of C.", "University of Verona", "Alfred P.Sloan Foundation", "Mathematics and Financial Econo", "Charles University", "California Instite of Technology, Division of the Humanities and Social Sciences", "36th International Mathematical Olympiad", "Universit´e Paris-Dauphine", "Corporate Decisions, Inc.", "Graduate School of Economics Barcelona", "Net Exposure", "ENSAE", "University Of Calgary", "Journal of Statistical Planning and Inference", "Econometrics", "Econetric Society", "Danish Operations Research Society", "Journal of Development Economics", "Economic Studies", "New Economic School", "Microsoft Research New England", "Financial Analyst Journal", "CESifo Research Network, University of Münich,", "Journal of Public Economics,", "Columbia Business School", "CESifo Economics of Digitization", "The Review of Derivatives Research", "School of Arts and Sciences", "German Scholarship Foundation", "New Palgrave Dictionary of Economics", "The Jan Wallander Award", "ENSAE, Paris", "Journal of Public Economics", "Q Group", "Econometric Society", "International Journal of Economic Theory", "Society of Economic Educators", "Georgia State University’s Center", "Robert and Helen Appel", "Jeb Bush campaign", "Le Cercle des Economistes / Le Monde", "Centre for Economic Learning and Social Evolution", "Kellogg School of Business", "University of Washington, Seattle, Washington", "Advisory Board of the Centre de Recerca en Economia Internacional", "Pennsylvania State University", "General Service Foundation", "Tel-Aviv University", "German Economic Review", "Soros Foundations Network", "SUNY Albany", "Journal Of Business and Economic Statistics", "The B.E. Journals in Economic Analysis & Policy", "University of Pavia", "Economic Science Association.", "Review of Economic", "Finance Research Letters", "Pontifical Catholic University", "Shanghai University of Finance and Economics", "University of Queensland.", "HEC Lausanne", "Journal of Financial Markets", "University of Aukland", "Federal Reserve Bank of St. Louis", "University of Perugia", "Econometrics Group", "University of California, Santa Cruz", "Stanford Institute for Economic Policy Research", "ERC Starting Grant", "Journal of Human Capital", "MIT Press Editorial Board", "Dfid", "Economic Policy Review", "University of Venice", "Expansión and Actualidad Económica,", "Institut d’Anàlisi Econòmica", "Scientific Council of the Madrid Institute for Advanced Studies in Mathematics", "Microsoft Research (previously 2010", "Erc", "Environmental and Resource Economics", "SIEPR Facult", "University of California, Los angeles", "Brookings Institution", "American Economic Journal: Microeconomics", "University of California, Los Angeles", "Sciences Po", "Novo Nordisk Foundation,", "European Academy of Sciences and Arts", "Journal of Economics Management", "University of Western Ontario", "Cambrige University", "University of Washington", "Agencia Nacional de Promocion Cientifica y Tecnologia", "University of Chicago School of Law", "Fundación Ramón Areces Graduate", "The European Economic Association", "National Univ. of Singapore", "Oxford and Corpus Christi College", "Universidad de San Andrés", "European Research Council Advanced", "Journal of Economic Dynamics and Control Mentor for the CSWEP program", "Swiss National Science Foundation", "Advances in Economic Analysis & Policy", "International Journal of Game Theory", "Royal Economics Society", "Makerere", "NEW YORK UNIVERSITY", "University of Arizona", "Department of Manpower and Inmigration", "Macroeconomic Dynamics", "Brandeis University", "Canadian Economic Association", "CREST-INSEE", "Econometrica,", "Stanford Institute for Innovation in Developing Economies", "University of Chicago Beijing Center", "MIT. Cambridge, MA.", "American Economic Journal", "DELTA", "Economie et Prévision", "National Bureau of Economic Research", "CASD", "University Of Chicago", "FTC Panel on Merger Evaluation", "BBVA Frontiers of Knowledge", "ISS", "Economic and Social Research Council", "Association for the Study of Generosity in Economics,", "Journal of Economics and Management Strategy", "University Of Kent", "Compass Lexecon", "EHESS, Greqam Marseille", "Federal Reserve Bank of Chicago", "Oxford Uiversity", "Institute For Pure And Applied Mathematics", "University Of Mannheim", "Singapore University", "Universidad Carlos III de Madrid", "Journal of Economic Dynamics and Control", "MIT", "Swiss Federal Institute of Technology", "Danish Journal of Economics", "SHUFE IO Summer School, Shanghai", "Bulletin Econ. Res", "University of Aarhus", "University of Science and Technology of China", "Humbolt University Berlin", "North American J of Econ & Finance", "Journal of the European Economic Association", "Boston University", "Mathematical Social Sciences", "Econometric Society (elected", "Congressional Budget Office", "Universidad Nacional de la Plata", "Institute For The Study Of Labor", "Tinbergen Institute, Amsterdam", "Banking University of Zurich", "NBER Grant", "Stanford Department of Economics", "Nu?ield College", "Société Canadienne de Science Économique", "University of Wyoming", "Canadian Journal of Economics", "NBER Economic Fluctuations and Growth", "Hong Kong Institute of Monetary Research", "ITS", "Financial Econometrics", "Scandinavian journal of Economics,", "European Association for Research in Industrial Economics (EARIE)", "Fundação Ciência e Tecnologia", "Annales d'Economie et de Statistique,", "New York Federal Reserve Bank", "U.S. ARMY", "Health Care Cost Institute", "The Hebrew University of Jerusalem", "Ensae", "John McCain campaign", "Princeton University", "Ecole Normale Supérieure de Lyon", "University of Virginia", "Cambridge, MA", "Charles De Gaulle University – Lille Iii", "Social Insurance’s Heinz Dissertation", "American Economic Journal: Micoreconomics", "Toyota International Centres for Economics and Related Disciplines (STICERD)", "International Tax and Public Finance,", "Harvard University,", "Renmin University", "Universidad Pablo de Olavide", "MFM", "Humboldt Universit", "Facultés N-D de la Paix", "Princeton Public Economics Program (PPP)", "John Rae Prize of the Canadian Economic Association:", "NYU Shanghai", "University of Aix-Marseille", "U.S. Department of Justice/Antitrust Division", "USCCB", "Society of Advancement of Economic Theory", "Journal of the Economic Science Association", "UBC Hampton Fund", "Journal of Population Economics", "Phylosophy and Social Sciences Section of the Institut d’Estudis Catalans", "Kiel Institute", "UFRJ", "Journal of Financial Services Research", "Journal of Pension Economics and Finance", "Annals of Economics and Finance", "AER", "L.A.C.E.A", "Life or Social Sciences", "Stanford Institute of Economic Policy Research (SIEPR)", "Econometrics And Statistics", "University of New South Wales", "Journal oprplied Econometrics", "Harvard", "Polish Vice-Prime Minister Award", "University of Bologna", "Jiangxi University of Finance and Economics", "Book Series on Econometrics", "Federal Reserve Bank", "Royal Netherlands Society for the Sciences (KHMW)", "Stochastic Processes and Their Applications", "University Of Copenhagen", "Fischer Black Prize", "Electrical Engineering And Computer Science Department", "Israel-United States Bi-National Science Foundation", "United States Department of Health and Human Services", "CIBE Research", "MICCIN", "Academic College of Tel-Aviv-Yaffo", "Advisory Board Chicago Urban League", "Sciences Po Paris (Master of Public Administration)", "Grupo de Reflexión Abertis", "Memphis State University", "AERF/CKER of the Society of Actuaries", "The Torsten and Ragnar Söderberg Prize", "University Of The Littoral Opal Coast", "Centro de Estudios Monetarios y Financieros (CEMFI)", "Journal Of Transport, Economic And Policy", "Kiel Excellence Award in Global Economic Affairs (2014)", "Universitat Autnoma de Barcelona", "Becker-Friedman Institute for Research in Economics", "IZA Journal of Labor Economics", "Commission des Opérations de Bourse, Paris", "Aalto University", "Ecole Nationale de la Statistique et de l’Administration Economique", "Federal Reserve Bank of Richmond", "Premio Rey Jaime I de Economía", "IMF Research Department", "Overseas Development Insitute", "University in Queensland,", "Duisenberg Institute", "University Of Nottingham", "Connaught Fund", "Journal of International Economics", "University of Melbourne.", "Continental Airlines", "University of York", "Journal Of Time Series Analysis", "Institut Universitaire de France", "Journal of Nonparametric Statistics", "Princeton Universit", "National R&D Infrastructures", "The Swedish Treasury", "Einaudi Institute of Economics and Finance", "Society of Social Economics", "Guinnaneís National Institute of Health", "HKUST", "The American Academy of Arts and Sciences", "Spanish Economic Review.", "Japan Society for the Promotion of Science", "Danish Social Science Research Council", "Toulouse School Of Economics", "Office of Fair Trading", "Sloan Foundation Research", "The Journal of Nonparametric Statistics", "Institute For Advanced Study in Toulouse", "Laboratory For Information And Decision Systems", "Institute for Quantitative Research in Finance", "University Amsterdam", "BEPress", "UCLA", "ACTEC Foundation", "Center for Political Studies", "American Automatic Control Council", "Annals of Applied Probability", "Center for Economics Policy", "INE", "Royal Holland Society of Sciences and Humanities", "External Review Committee for the Division of Humanities and Social Sciences of the California Institute of Technology", "Peking University", "Chief of Staff of the General Headquarters of Guardia di Finanza", "MIUR", "Journal of Econometrics", "Probability Theory and Related Fields", "Queen’s University,", "The Berkeley Journal ofTime Series Econometrics", "Eurasian Economic Review", "Economic Policy Research Network (EPRN),", "European Development Network", "Dake University", "Stephen H. Sandell Grant for Junior Scholars in Retirement Research", "University College Dublin", "Center on Demography and Economics of Aging", "University of Namur", "Graduate Institute of International Studies, Geneva", "American Economic Association.", "Scottish Institute for Research in Economics", "University of Melbourne", "CERGE-EI", "Norwegian School of Economics,", "University of Chicago China Research Initiative", "Annales díEconomie et Statistique", "University Of Lille", "Boston College", "Princeton University.", "Central Banks", "Institut National de la Recherche Agronomique", "Delhi School", "Econometric", "CREI/UPF", "Europe Institute of Finance", "Cowles Foundation (Yale)", "University of Windsor", "K.U. Brussel", "UT-Austin", "Rice University", "Scandinavian Journal of Statistics", "National Institute of Child Health and Human Development", "Hong Kong University", "Advances in Futures and Options Research", "Universidad de San Andres", "IESE Business School", "American Economic Journal:  Microeconomics", "Institute for Advanced Studies, Vienna", "Investigaciones Econ´Omicas, Moneda Y Cr´Edito", "Journal of Applied Economics", "The Royal Swedish Academy of Letters, History and Antiquities", "Caisse des Dépôts& Consignations", "Aix-Marseille School of Economics", "Journal Of The American Statistical Association", "DELTA - Ecole Normale Supérieure", "Banque Paribas", "Metron", "The Acton Society", "Journal Of Economic Literature", "Economic Research Monographs Series", "Federal Reserve Bank of Minneapolis", "Mont Pelerin Society", "Theoretical Research in Development Economics", "National Academy Of Sciences", "Microeconomic Insights", "Fundacion Libertad", "Duke University", "The Hebrew University of Jerusalen", "The Society for Financial Econometrics", "CRT Foundation", "Minneapolis FRB", "Econometric Society Monograph Series", "CORE", "Nato Science", "Executive Committee of the European Economic Association", "Ecole Nationale de la Statistique et de l'Administration Economique", "NYU", "Faculty of Arts And Sciences", "National Association for Business Economics", "Polish Science Foundation", "Institut Henri PoincarÃ©", "Center for Compassion and Altruism Research and Education", "University of Hull", "University of Iowa", "Scientific Committee of Panel Data Conferences", "Royal Economic Society", "American Academy of Political and Social Science", "Midwest Economics Association", "Bank of Canada", "Rev. Econ. Dynamics", "AMF Scientific Advisory Board", "Annual Reviews of Financial Economics", "Journal of Regulatory Economics", "Institute for Policy Reform", "Revista Brasileira de Economia", "Politecnico di Milano", "National Institutes of Health", "University of Technology Sydney, School of Finance and Economics", "Oxford Economic Papers", "University of Chicago", "Academy of Social Sciences in Australia", "Macroeconomics", "Econometric Theory Multa Scripsit", "The Rhodes Scholarship", "European Standing Committee of the Econometric Society", "Journal of Monetary Economics", "Econometric Society European Meeting", "Danish Central Bank", "Journal of Economic Theory", "IGC", "Alfred P. Sloan Research Fellowship", "Centre of Public Economics, Oslo University,", "MECOVI", "U. Illinois Champaign-Urbana", "MASSACHUSETTS INSTITUTE OF TECHNOLOGY", "Fulbright Scholar", "Society for Economic Dynamics", "Amazon LLC", "The Sasakawa International", "Technical University Munich", "ARC", "Georgetown University", "ISER Osaka", "Stockholm University Institute for International", "American Economic Journals", "Universidade Federal de Minas", "Brown University", "Institute for Fiscal Studies/Centre", "Journal ofEconomelric Methods", "Heriot-Watt University", "Rising Star", "SHASS Research Fund grant", "Stanford University", "Universidad Autónoma de Madrid", "Brigham Young University", "Special Issue of Econometric Theory on Inverse Problems", "ESRC Centre for the Microeconomic Analysis of Public Policy (CPP)", "Population Research Center", "Ecole des Ponts, Paris", "Cirano and Cireq", "Duke University, Durham", "Entrepreneurship Researc", "Gonville and Caius College", "Robert Wood Johnson Foundation Scholar", "The American Economic Review", "Centre for European Policy Research", "IAM Research Program", "University of Toulouse", "Office of Naval Research", "Financial Conduct Authority", "3IE", "Executive Committee of the Latin American and Caribbean Economic Association (LACEA)", "Journal of Economic Behavior and Organization", "New York University (Spring Semester)", "University Of Pennsylvania", "Nonprofit and Voluntary Sector Quarterly", "Review of Economic Design", "IZA - Bonn, Germany", "NYU-Shanghai", "University of California, San Diego", "Louis Vuitton Asia", "University of Pennsylania", "University of Edinburgh", "EUROPEAN CORPORATE GOVERNANCE INSTITUTE", "Carol Ann Steinfeld Memorial Prize", "Center for Poverty Research", "Central Bank of Russia", "Spanish Economic Association", "ISI Highly Cited", "International Financial Markets"]

def convert_pdf(path):

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    fp = open(path, 'rb')
    process_pdf(rsrcmgr, device, fp)
    fp.close()
    device.close()

    strr = retstr.getvalue()
    retstr.close()
    return strr

def pages_number(pdf_path):
    with open(pdf_path, 'rb') as f:
        fx = PdfFileReader(f)
        information = fx.getDocumentInfo()
        number_of_pages = fx.getNumPages()

    return number_of_pages

def extract_parser(nombres=[]):
    for nombre in nombres:
        cadena = convert_pdf("./pdfs/"+ nombre+".pdf")
        cadena = cadena.replace(":  ", ": ")
        cadena = cadena.replace(": ", ",")
        cadena = cadena.replace("“", "")
        cadena = cadena.replace("–", "-")
        cadena = cadena.replace("”", "")
        lista = cadena.split("\n")
        lista = [clean_string(i)[0] for i in lista if len(clean_string(i))>0]

        print("######################################################################################################################")

        lines = []
        indices = []
        for i in lista:
            cont = 0
            poss = []
            f1 = ""
            f2 = ""
            idx = 0
            for j in cargos:
                if j in i and ',' in i:
                    n = len(j)
                    if n>cont:
                        cont+=len(j)
                        poss.append([i, j])
                    if len(poss)>1:
                        poss = [poss[-1]]
                    inf1, inf2 = poss[0]
                    f1 = inf1
                    f2 = inf2
                else:
                    if i not in indices:
                        indices.append(i)
            lines.append([f1, f2])

        #cadena = "\n".join(indices)
        #f_text = open("{}_cadena.txt".format(nombre), "w")
        #f_text.write(cadena)
        #f_text.close()

        lines = [i for i in lines if i!=["",""]]
        try:
            nombre = nombre.split(".")[0]
            for data in lines:
                places = []
                linea, cargo = data
                print("Linea a ser analizada:", "           >>>{}<<<\n".format(linea))
                info = [i.strip() for i in linea.split(",")]
                print(info, ">>>", cargo, "> (Cargo basado en la lista existente)")
                places = [i for i in inst if i in linea]
                lol = [i for i in places if i in info]
                lol2 = []
                for p in info:
                    for q in places:
                        if q in p:
                            lol2.append(p)
                #print(places, "generic places")
                #print(lol, "lol")
                lol2 = list(set(lol2))
                print(lol, ">>> Instituciones basadas en la lista existente")

                if len(lol) > 0:
                    for t in lol:
                        linea = linea.replace(t, "")
                    #linea = linea.replace(cargo,"")
                    #print(linea, ">>>", "linea filtrada")
                else:
                    pass
                    #print(linea, ">>>", "linea no filtrada")

                lista_filtrada = [i for i in linea.split(",") if i!=""]
                lista_filtrada = [i for i in lista_filtrada if i!=" "]
                lista_filtrada = [i.strip() for i in lista_filtrada]
                lista_cargo = [i for i in lista_filtrada if cargo in i]
                rw_cargos = ""
                print(lista_cargo, ">>>", "(Cargo hallado)")
                contt = 0
                for i in lista_cargo:
                    if i not in cargos:
                        contt+=1
                if contt>0:
                    rw_cargos+="revisar/anadir cargo"
                else:
                    rw_cargos+="0"
                lista_filtrada = [i for i in lista_filtrada if i not in lista_cargo]
                lista_anios = []
                for r in rango:
                    for s in lista_filtrada:
                        if r in s:
                            lista_anios.append(s)
                lista_anios = list(set(lista_anios))
                print(lista_anios, ">>>", "years")
                lista_filtrada = [i for i in lista_filtrada if i not in lista_anios]
                lista_filtrada = [i for i in lista_filtrada if i not in lista_cargo]
                #print(lista_filtrada, "OJO OKO OJO OKO")

                if len(lista_filtrada) > 0:
                    print(lista_filtrada, ">>>", "Instituciones no registradas")
                else:
                    print(lista_filtrada, "Lista vacia: Instit. no halladas / Instit. filtradas correctamente")

                if len(lista_filtrada) > 0 and len(lol) > 0 and len(lista_anios) > 0:
                    ins1 = "_".join(lol)
                    ins2 = "_".join(lista_filtrada)
                    ins3 = "{}_{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)

                    categ = ""
                    for k in categories:
                        validar = categories[k]
                        for rt in validar:
                            if cargo in validar[rt]:
                                categ+=rt
                    if len(categ)>0:
                        print("Categoria:", categ)
                    else:
                        categ = "revisar/anadir"
                        print("Categoria no existente")

                    anio = "_".join(lista_anios)
                    print("Linea a registrar:\n")

                    linea = "{},{},{},{},{},{},revisar/anadir institucion,0\n".format(nombre,categ,cargo, ins3, anio,rw_cargos)
                    print(linea)
                    print()
                    print("Condicion 1")
                    print()
                    file.write(linea)
                    print("######################################################################################################################")

                elif len(lista_filtrada) == 0 and len(lol) == 0 and len(lista_anios) > 0:
                    ins1 = "_".join(lol)
                    ins2 = "_".join(lista_filtrada)
                    ins3 = "{}_{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)

                    categ = ""
                    for k in categories:
                        validar = categories[k]
                        for rt in validar:
                            if cargo in validar[rt]:
                                categ+=rt
                    if len(categ)>0:
                        print("Categoria:", categ)
                    else:
                        categ = "revisar/anadir"
                        print("Categoria no existente")

                    anio = "_".join(lista_anios)
                    print("Linea a registrar:\n")

                    linea = "{},{},{},{},{},{},revisar/anadir institucion,0\n".format(nombre,categ,cargo, ins3, anio,rw_cargos)
                    print(linea)
                    print()
                    print("Condicion 2")
                    print()
                    file.write(linea)
                    print("######################################################################################################################")

                elif len(lista_filtrada) > 0 and len(lol) == 0 and len(lista_anios) == 0:
                    ins1 = "_".join(lol)
                    ins2 = "_".join(lista_filtrada)
                    ins3 = "{}_{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)

                    categ = ""
                    for k in categories:
                        validar = categories[k]
                        for rt in validar:
                            if cargo in validar[rt]:
                                categ+=rt
                    if len(categ)>0:
                        print("Categoria:", categ)
                    else:
                        categ = "revisar/anadir"
                        print("Categoria no existente")

                    anio = "_".join(lista_anios)
                    print("Linea a registrar:\n")

                    linea = "{},{},{},{},{},{},0,revisar/anadir anio\n".format(nombre,categ,cargo, ins3, anio,rw_cargos)
                    print(linea)
                    print()
                    print("Condicion 3")
                    print()
                    file.write(linea)
                    print("######################################################################################################################")

                elif len(lista_filtrada) > 0 and len(lol) == 0 and len(lista_anios) > 0:
                    ins1 = "_".join(lol)
                    ins2 = "_".join(lista_filtrada)
                    ins3 = "{}_{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)

                    categ = ""
                    for k in categories:
                        validar = categories[k]
                        for rt in validar:
                            if cargo in validar[rt]:
                                categ+=rt
                    if len(categ)>0:
                        print("Categoria:", categ)
                    else:
                        categ = "revisar/anadir"
                        print("Categoria no existente")

                    anio = "_".join(lista_anios)
                    print("Linea a registrar:\n")

                    linea = "{},{},{},{},{},{},revisar/anadir intitucion,0\n".format(nombre,categ,cargo, ins3, anio,rw_cargos)
                    print(linea)
                    print()
                    print("Condicion 4")
                    print()
                    file.write(linea)
                    print("######################################################################################################################")

                elif len(lista_filtrada) == 0 and len(lol) > 0 and len(lista_anios) > 0:
                    ins1 = "_".join(lol)
                    #ins2 = "-".join(lista_filtrada)
                    #ins3 = "{}-{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)

                    categ = ""
                    for k in categories:
                        validar = categories[k]
                        for rt in validar:
                            if cargo in validar[rt]:
                                categ+=rt
                    if len(categ)>0:
                        print("Categoria:", categ)
                    else:
                        categ = "revisar/anadir"
                        print("Categoria no existente")

                    anio = "_".join(lista_anios)
                    print("Linea a registrar:\n")

                    linea = "{},{},{},{},{},{},0,0\n".format(nombre,categ,cargo, ins1, anio,rw_cargos)
                    print(linea)
                    print()
                    print("Condicion 5")
                    print()
                    file.write(linea)
                    print("######################################################################################################################")

                elif len(lista_filtrada) == 0 and len(lol) > 0 and len(lista_anios) == 0:
                    ins1 = "_".join(lol)
                    ins2 = "_".join(lista_filtrada)
                    ins3 = "{}_{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)

                    categ = ""
                    for k in categories:
                        validar = categories[k]
                        for rt in validar:
                            if cargo in validar[rt]:
                                categ+=rt
                    if len(categ)>0:
                        print("Categoria:", categ)
                    else:
                        categ = "revisar/anadir"
                        print("Categoria no existente")

                    anio = "_".join(lista_anios)
                    print("Linea a registrar:\n")

                    linea = "{},{},{},{},{},{},0,revisar/anadir anio\n".format(nombre,categ,cargo, ins3, anio,rw_cargos)
                    print(linea)
                    print()
                    print("Condicion 6")
                    print()
                    file.write(linea)
                    print("######################################################################################################################")

                elif len(lista_filtrada) > 0 and len(lol) > 0 and len(lista_anios) == 0:
                    ins1 = "_".join(lol)
                    ins2 = "_".join(lista_filtrada)
                    ins3 = "{}_{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)

                    categ = ""
                    for k in categories:
                        validar = categories[k]
                        for rt in validar:
                            if cargo in validar[rt]:
                                categ+=rt
                    if len(categ)>0:
                        print("Categoria:", categ)
                    else:
                        categ = "revisar/anadir"
                        print("Categoria no existente")

                    anio = "_".join(lista_anios)
                    print("Linea a registrar:\n")

                    linea = "{},{},{},{},{},{},0,revisar/anadir anio\n".format(nombre,categ,cargo, ins3, anio,rw_cargos)
                    print(linea)
                    print()
                    print("Condicion 7")
                    print()
                    file.write(linea)
                    print("######################################################################################################################")

                elif len(lista_filtrada) == 0 and len(lol) == 0 and len(lista_anios) == 0:
                    ins1 = "_".join(lol)
                    ins2 = "_".join(lista_filtrada)
                    ins3 = "{}_{}".format(ins1, ins2) # instituciones no registrada

                    cargo = '_'.join(lista_cargo)
                    anio = "_".join(lista_anios)

                    linea = "{},{},{},{},{},0,revisar/anadir anio\n".format(nombre,cargo, ins3, anio,rw_cargos)
                    print("\nWARNING: Linea a agrear vacia/no valida. Se sugiere revisar los datos.\n")
                    print("Condicion 8")
                    print()
                    print("######################################################################################################################")
                else:
                    print("######################################################################################################################")
                    print("LA LINEA NO FUE CREADA. VERIFICAR ERROR")
                    print("######################################################################################################################")
        except (NameError,KeyError):
            print("Error de nombre")
        except:
            print("Unexpected error:", sys.exc_info()[0])