from commonModuleImport import *
from mergeCSV import mergeFiles
from getStockReturns import getStockReturns
from generateHTML import generateHTML

if __name__ == "__main__":
    COMPANY_NAME = ['LICI', 'JIOFIN', 'IRFC', 'ADANIENSOL', 'ZOMATO', 'LODHA', 'MANKIND', 'NYKAA', 'TATATECH', 'AWL', 'JSWINFRA', 'PAYTM', 'SONACOMS', 'KALYANKJIL', 'POLICYBZR', 'METROBRAND', 'STARHEALTH', 'MANYAVAR', 'LLOYDSME', 'TCS', 'HDFCBANK', 'ICICIBANK', 'INFY', 'HINDUNILVR', 'BHARTIARTL', 'ITC', 'SBIN', 'LT', 'BAJFINANCE', 'HCLTECH', 'KOTAKBANK', 'AXISBANK', 'ASIANPAINT', 'TITAN', 'ADANIENT', 'MARUTI', 'ULTRACEMCO', 'SUNPHARMA', 'NTPC', 'BAJAJFINSV', 'DMART', 'TATAMOTORS', 'ONGC', 'NESTLEIND', 'ADANIGREEN', 'WIPRO', 'COALINDIA', 'ADANIPORTS', 'POWERGRID', 'JSWSTEEL', 'M&M', 'ADANIPOWER', 'BAJAJ-AUTO', 'HAL', 'LTIM', 'IOC', 'DLF', 'TATASTEEL', 'VBL', 'SBILIFE', 'SIEMENS', 'GRASIM', 'HDFCLIFE', 'HINDALCO', 'PIDILITIND', 'BEL', 'HINDZINC', 'BRITANNIA', 'PFC', 'INDUSINDBK', 'TECHM', 'BANKBARODA', 'GODREJCP', 'INDIGO', 'EICHERMOT', 'RECLTD', 'ATGL', 'TRENT', 'GAIL', 'TATAPOWER', 'CHOLAFIN', 'PNB', 'DIVISLAB', 'AMBUJACEM', 'SHREECEM', 'TATACONSUM', 'CIPLA', 'ABB', 'DABUR', 'BPCL', 'DRREDDY', 'TVSMOTOR', 'VEDL', 'UNIONBANK', 'HAVELLS', 'BAJAJHLDNG', 'HEROMOTOCO', 'POLYCAB', 'APOLLOHOSP', 'IOB', 'MCDOWELL-N', 'CANBK', 'TORNTPHARM', 'IDEA', 'SHRIRAMFIN', 'ICICIPRULI', 'JINDALSTEL', 'SRF', 'IDBI', 'SBICARD', 'IRCTC', 'MARICO', 'BERGEPAINT', 'ICICIGI', 'ZYDUSLIFE', 'CGPOWER', 'MOTHERSON', 'COLPAL', 'TIINDIA', 'HDFCAMC', 'BHEL', 'JSWENERGY', 'MAXHEALTH', 'NAUKRI', 'BOSCHLTD', 'NHPC', 'AUROPHARMA', 'IDFCFIRSTB', 'INDHOTEL', 'ALKEM', 'YESBANK', 'NMDC', 'SOLARINDS', 'LUPIN', 'MUTHOOTFIN', 'SUPREMEIND', 'BHARATFORG', 'PATANJALI', 'PERSISTENT', 'INDIANB', 'HINDPETRO', 'PGHH', 'GODREJPROP', 'LTTS', 'MRF', 'TATAELXSI', 'CUMMINSIND', 'GICRE', 'INDUSTOWER', 'PIIND', 'ASHOKLEY', 'AUBANK', 'OBEROIRLTY', 'CONCOR', 'FACT', 'SUZLON', 'MPHASIS', 'BANKINDIA', 'ASTRAL', 'SAIL', 'TATACOMM', 'SCHAEFFLER', 'BALKRISIND', 'GMRINFRA', 'LINDEINDIA', 'UCOBANK', 'PRESTIGE', 'UBL', 'JSL', 'MAZDOCK', 'TORNTPOWER', 'UPL', 'CENTRALBK', 'ABCAPITAL', 'PAGEIND', 'DALBHARAT', 'APLAPOLLO', '3MINDIA', 'ACC', 'KPITTECH', 'L&TFH', 'FLUOROCHEM', 'OIL', 'PHOENIXLTD', 'UNOMINDA', 'DIXON', 'SUNDARMFIN', 'BANDHANBNK', 'COFORGE', 'FEDERALBNK', 'RVNL', 'JUBLFOOD', 'COROMANDEL', 'THERMAX', 'OFSS', 'SJVN', 'NLCINDIA', 'AIAENG', 'NIACL', 'M&MFIN', 'DEEPAKNTR', 'POONAWALLA', 'PETRONET', 'ESCORTS', 'MFSL', 'HONAUT', 'VOLTAS', 'GLAXO', 'MAHABANK', 'GUJGASLTD', 'CRISIL', 'GLAND', 'FORTIS', 'BDL', 'ZFCVINDIA', 'BSE', 'BIOCON', 'LICHSGFIN', 'KEI', 'IGL', 'ANGELONE', 'JKCEMENT', 'ITI', 'PSB', 'APOLLOTYRE', 'DELHIVERY', 'IPCALAB', 'SYNGENE', 'KPRMILL', 'TATACHEM', 'SUNTV', 'NAM-INDIA', 'IREDA', 'MSUMI', 'ENDURANCE', 'EXIDEIND', 'KANSAINER', 'AJANTPHARM', 'HINDCOPPER', 'ZEEL', 'SUNDRMFAST', 'GRINDWELL', 'MEDANTA', '360ONE', 'CREDITACC', 'CYIENT', 'HATSUN', 'HUDCO', 'JBCHEPHARM', 'IRB', 'GODREJIND', 'EMAMILTD', 'NH', 'TIMKEN', 'APARINDS', 'NATIONALUM', 'RAMCOCEM', 'GLENMARK', 'RATNAMANI', 'AARTIIND', 'DEVYANI', 'MRPL', 'ISEC', 'LAURUSLABS', 'IIFL', 'SKFINDIA', 'RELAXO', 'KIOCL', 'POWERINDIA', 'RADICO', 'TATAINVEST', 'LALPATHLAB', 'FIVESTAR', 'ABFRL', 'BATAINDIA', 'CARBORUNIV', 'GILLETTE', 'ATUL', 'PEL', 'SONATSOFTW', 'KAJARIACER', 'BRIGADE', 'ASTERDM', 'PNBHOUSING', 'IDFC', 'SUMICHEM', 'CROMPTON', 'BSOFT', 'CHOLAHLDNG', 'PFIZER', 'BLUESTARCO', 'NAVINFLUOR', 'CDSL', 'SANOFI', 'TRIDENT', 'MOTILALOFS', 'SUVENPHAR', 'PPLPHARMA', 'AFFLE', 'VINATIORGA', 'TTML', 'CIEINDIA', 'COCHINSHIP', 'CASTROLIND', 'RRKABEL', 'JYOTHYLAB', 'CESC', 'BLUEDART', 'WHIRLPOOL', 'JBMA', 'GSPL', 'ELGIEQUIP', 'CENTURYPLY', 'RBLBANK', 'CELLO', 'KAYNES', 'RHIM', 'CLEAN', 'FINCABLES', 'INDIAMART', 'INOXWIND', 'PVRINOX', 'IRCON', 'DCMSHRIRAM', 'SHYAMMETL', 'APTUS', 'CGCL', 'KIMS', 'TVSHLTD', 'EIHOTEL', 'CHAMBLFERT', 'CONCORDBIO', 'FINEORG', 'KEC', 'NSLNISP', 'IEX', 'APLLTD', 'TEJASNET', 'NATCOPHARM', 'TANLA', 'NBCC', 'LAXMIMACH', 'MANAPPURAM', 'WELCORP', 'CHALET', 'POLYMED', 'HONASA', 'TITAGARH', 'WELSPUNLIV', 'ASAHIINDIA', 'GESHIP', 'ARE&M', 'ZENSARTECH', 'REDINGTON', 'ASTRAZEN', 'NUVOCO', 'BIKAJI', 'CENTURYTEX', 'HAPPSTMNDS', 'HSCL', 'KARURVYSYA', 'J&KBANK', 'ABSLAMC', 'SWANENERGY', 'SFL', 'TRITURBINE', 'BASF', 'JINDALSAW', 'BLS', 'JWL', 'RKFORGE', 'FINPIPE', 'CAMS', 'ALKYLAMINE', 'GMDCLTD', 'GET&D', 'FSL', 'WESTLIFE', 'ECLERX', 'VGUARD', 'NUVAMA', 'MAHSEAMLES', 'ERIS', 'AEGISCHEM', 'SIGNATURE', 'JAIBALAJI', 'AAVAS', 'RAINBOW', 'HBLPOWER', 'RITES', 'KSB', 'HFCL', 'SYRMA', 'EQUITASBNK', 'AKZOINDIA', 'MGL', 'BEML', 'AETHER', 'GNFC', 'KPIL', 'RAYMOND', 'INTELLECT', 'CRAFTSMAN', 'BAJAJELEC', 'ANURAS', 'VTL', 'UJJIVANSFB', 'BIRLACORPN', 'GRINFRA', 'OLECTRA', 'CUB', 'UTIAMC', 'BBTC', 'GODFRYPHLP', 'NEWGEN', 'RAILTEL', 'ANANDRATHI', 'RAJESHEXPO', 'GRAPHITE', 'GODREJAGRO', 'ZYDUSWELL', 'GPIL', 'ALOKINDS', 'IBULHSGFIN', 'JKLAKSHMI', 'AMBER', 'RTNINDIA', 'SPLPETRO', 'MAPMYINDIA', 'NCC', 'DATAPATTNS', 'ELECON', 'CHENNPETRO', 'CANFINHOME', 'CAPLIPOINT', 'TTKPRESTIG', 'PRAJIND', 'CERA', 'SWSOLAR', 'RENUKA', 'ROUTE', 'GRSE', 'EIDPARRY', 'ACE', 'GALAXYSURF', 'INGERRAND', 'GRANULES', 'CEATLTD', 'JKTYRE', 'SCHNEIDER', 'HAPPYFORGE', 'ENGINERSIN', 'GSFC', 'ANANTRAJ', 'JPPOWER', 'SBFC', 'KIRLOSENG', 'LEMONTREE', 'PCBL', 'JMFINANCIL', 'LATENTVIEW', 'SOBHA', 'SPARC', 'SAFARI', 'PRSMJOHNSN', 'MINDACORP', 'NETWORK18', 'ESABINDIA', 'SAPPHIRE', 'USHAMART', 'PNCINFRA', 'MMTC', 'MEDPLUS', 'SARDAEN', 'RPOWER', 'RCF', 'TVSSCS', 'JUBLPHARMA', 'TV18BRDCST', 'BALAMINES', 'MASTEK', 'TECHNOE', 'METROPOLIS', 'KRBL', 'DEEPAKFERT', 'RATEGAIN', 'CCL', 'CAMPUS', 'VIPIND', 'MAHSCOOTER', 'VARROC', 'SURYAROSNI', 'MAHLIFE', 'GAEL', 'RELINFRA', 'BALRAMCHIN', 'IONEXCHANG', 'KFINTECH', 'HOMEFIRST', 'PGHL', 'PRINCEPIPE', 'RESPONIND', 'PTCIL', 'KTKBANK', 'JUBLINGREA', 'GLS', 'MANINFRA', 'SPANDANA', 'INDIACEM', 'ACI', 'INOXINDIA', 'LXCHEM', 'TMB', 'CHEMPLASTS', 'ALLCARGO', 'EMIL', 'SANDUMA', 'MIDHANI', 'QUESS', 'TEGA', 'MHRIL', 'SHOPERSTOP', 'DOMS', 'SCI', 'GRAVITA', 'TRIVENI', 'GPPL', 'HEG', 'EDELWEISS', 'DBREALTY', 'MARKSANS', 'RUSTOMJEE', 'VESUVIUS', 'STARCEMENT', 'PDSL', 'CSBBANK', 'IFCI', 'GMMPFAUDLR', 'ISGEC', 'KNRCON', 'EASEMYTRIP', 'SAREGAMA', 'JLHL', 'INDIGOPNTS', 'LTFOODS', 'KIRLOSBROS', 'RELIGARE', 'JAICORPLTD', 'VIJAYA', 'JKPAPER', 'UJJIVAN', 'ROLEXRINGS', 'GARFIBRES', 'ARVIND', 'JUSTDIAL', 'GREENLAM', 'VRLLOG', 'MTARTECH', 'NEULANDLAB', 'POWERMECH', 'GOCOLORS', 'ZENTEC', 'NETWEB', 'SIS', 'VOLTAMP', 'ELECTCAST', 'BECTORFOOD', 'VAIBHAVGBL', 'TEXRAIL', 'SUNTECK', 'RSYSTEMS', 'REDTAPE', 'IWEL', 'FDC', 'EPL', 'SHRIPISTON', 'TCI', 'THOMASCOOK', 'BLUEJET', 'NAVA', 'HNDFDS', 'MOIL', 'NESCO', 'PGEL', 'SYMPHONY', 'WOCKPHARMA', 'ICIL', 'SHAREINDIA', 'INDIASHLTR', 'JINDWORLD', 'CMSINFO', 'GENUSPOWER', 'INFIBEAM', 'STAR', 'NIITMTS', 'UTKARSHBNK', 'TIIL', 'FUSION', 'BORORENEW', 'ASKAUTOLTD', 'ASTRAMICRO', 'AVANTIFEED', 'JSWHL', 'GUJALKALI', 'STLTECH', 'NAZARA', 'GABRIEL', 'SUPRAJIT', 'PTC', 'DBL', 'SOUTHBANK', 'GHCL', 'RBA', 'PARADEEP', 'HGINFRA', 'ICRA', 'RAMKY', 'KESORAMIND', 'SANSERA', 'ARVINDFASN', 'SENCO', 'AURIONPRO', 'TEAMLEASE', 'CYIENTDLM', 'AGI', 'KPIGREEN', 'HEIDELBERG', 'TCIEXP', 'VSTIND', 'GREENPANEL', 'DODLA', 'AHLUCONT', 'RAIN', 'GATEWAY', 'ORIENTCEM', 'ETHOSLTD', 'HCG', 'FEDFINA', 'GOKEX', 'PRUDENT', 'ITDCEM', 'BBOX', 'JPASSOCIAT', 'RALLIS', 'ORIENTELEC', 'RTNPOWER', 'DHANUKA', 'WSTCSTPAPR', 'WONDERLA', 'DBCORP', 'MASFIN', 'LLOYDSENGG', 'IBREALEST', 'KKCL', 'MSTCLTD', 'PATELENG', 'TI', 'PRICOLLTD', 'SHANTIGEAR', 'HGS', 'PRIVISCL', 'CHOICEIN', 'AARTIPHARM', 'BANCOINDIA', 'MAXESTATES', 'NOCIL', 'JAYNECOIND', 'WELENT', 'AARTIDRUGS', 'IIFLSEC', 'NFL', 'JAMNAAUTO', 'PURVA', 'ROSSARI', 'TIPSINDLTD', 'JKIL', 'HEMIPROP', 'GALLANTT', 'HCC', 'MUTHOOTMF', 'DATAMATICS', 'ORISSAMINE', 'JISLJALEQS', 'KALAMANDIR', 'SULA', 'HMAAGRO', 'ADVENZYMES', 'IPL', 'SINDHUTRAD', 'DCBBANK', 'PAISALO', 'AMIORG', 'LAOPALA', 'THANGAMAYL', 'AZAD', 'SHARDACROP', 'SSWL', 'TDPOWERSYS', 'JTLIND', 'EPIGRAL', 'TIMETECHNO', 'TARC', 'FCL', 'VMART', 'RAJRATAN', 'LGBBROSLTD', 'NUCLEUS', 'LUXIND', 'ASHOKA', 'DELTACORP', 'BCG', 'NEOGEN', 'WABAG', 'KIRLPNU', 'SHARDAMOTR', 'JTEKTINDIA', 'ITDC', 'BOROLTD', 'ASHAPURMIN', 'IFBIND', 'SUDARSCHEM', 'SUNFLAG', 'HATHWAY', 'HIKAL', 'TATVA', 'BALMLAWRIE', 'BHARATRAS', 'KOLTEPATIL', 'HLEGLAS', 'HINDWAREAP', 'FLAIR', 'INDOCO', 'SAMHI', 'AVALON', 'ORCHPHARMA', 'HARSHA', 'KDDL', 'BAJAJHIND', 'SANGHVIMOV', 'ESAFSFB', 'SUBROS', 'PILANIINVS', 'GULFOILLUB', 'GREAVESCOT', 'EMUDHRA', 'IDEAFORGE', 'KIRLOSIND', 'UFLEX', 'GANESHHOUC', 'DYNAMATECH', 'MAITHANALL', 'TVSSRICHAK', 'LANDMARK', 'KSCL', 'NAVNETEDUL', 'TASTYBITE', 'THYROCARE', 'SAKSOFT', 'GMRP&UI', 'DISHTV', 'CARTRADE', 'DALMIASUG', 'NILKAMAL', 'SAGCEM', 'DCXINDIA', 'POLYPLEX', 'TRIL', 'SANGHIIND', 'SHALBY', 'VSTTILLERS', 'GRWRHITECH', 'NRBBEARING', 'SUNDARMHLD', 'AUTOAXLES', 'YATHARTH', 'BANARISUG', 'GENSOL', 'BOMDYEING', 'PFOCUS', 'GUFICBIO', 'SBCL', 'BAJAJCON', 'INNOVACAP', 'INOXGREEN', 'SUNCLAY', 'SOMANYCERA', 'MOLDTKPAC', 'JCHAC', 'DIVGIITTS', 'PRAKASH', 'APOLLO', 'SANDHAR', 'GREENPLY', 'SWARAJENG', 'WENDT', 'STYLAMIND', 'CIGNITITEC', 'MPSLTD', 'IFGLEXPOR', 'KINGFA', 'SHILPAMED', 'DREAMFOLKS', 'SEPC', 'IMAGICAA', 'UNICHEMLAB', 'MUKANDLTD', 'VENUSPIPES', 'SEQUENT', 'CARERATING', 'PGIL', 'HERITGFOOD', 'BSHSL', 'TARSONS', 'PARAS', 'MAHLOG', 'JINDALPOLY', 'FIEMIND', 'PSPPROJECT', 'ISMTLTD', 'VENKEYS', 'BBL', 'PARAGMILK', 'DEN', 'ZAGGLE', 'IOLCP', 'ASHIANA', 'PFS', 'ANUP', 'IMFA', 'APOLLOPIPE', 'VPRPL', 'DCAL', 'GANDHAR', 'GOODLUCK', 'OPTIEMUS', 'SEAMECLTD', 'SATIN', 'APCOTEXIND', 'GIPCL', 'LUMAXTECH', 'DOLLAR', 'BARBEQUE', 'UNIPARTS', 'VINDHYATEL', 'MBAPL', 'GOCLCORP', 'DIAMONDYD', 'CONFIPET', 'STYRENIX', 'SUPRIYA', 'EVEREADY', 'GLOBUSSPR', 'BEPL', 'UGROCAP', 'MOREPENLAB', 'MAYURUNIQ', 'HMT', 'MUFIN', 'TIDEWATER', 'IKIO', 'REPCOHOME', 'AXISCADES', 'FOSECOIND', 'ARTEMISMED', 'SOTL', 'ANDHRAPAP', 'SIYSIL', 'HONDAPOWER', 'HINDOILEXP', 'INDIAGLYCO', 'TCNSBRANDS', 'PRECAM', 'EMSLIMITED', 'SKIPPER', 'DHANI', 'MMFL', 'VISHNU', 'ALEMBICLTD', 'LUMAXIND', 'KRSNAA', 'CAMLINFINE', 'YATRA', 'MANORAMA', 'PITTIENG', 'TIRUMALCHM', 'UDS', 'SIRCA', 'SESHAPAPER', 'BFUTILITIE', 'RISHABH', 'IRMENERGY', 'RPGLIFE', 'CARYSIL', 'SDBL', 'ADFFOODS', 'ORIENTHOT', 'FILATEX', 'PCJEWELLER', '63MOONS', 'FINOPB', 'EVERESTIND', 'RPSGVENT', 'HUHTAMAKI', 'PRECWIRE', 'GTPL', 'ASTEC', 'XPROINDIA', 'SADHNANIQ', 'GANECOS', 'GREENPOWER', 'JINDRILL', 'RUPA', 'SANGAMIND', 'ARMANFIN', 'ATFL', 'HIL', 'MTNL', 'KSL', 'ACCELYA', 'SASKEN', 'BHARATWIRE', 'SHRIRAMPPS', 'INDOSTAR', 'SALASAR', 'VIDHIING', 'TNPL', 'PARACABLES', 'KIRIINDUS', 'TCPLPACK', 'ADORWELD', 'MANGLMCEM', 'JAGRAN', 'RIIL', 'EXPLEOSOL', 'BFINVEST', 'SHK', 'PANAMAPET', 'VAKRANGEE', 'FMGOETZE', 'AEROFLEX', 'TTKHLTCARE', 'INSECTICID', 'VERANDA', 'THEJO', 'KCP', 'MOL', 'CANTABIL', 'THEMISMED', 'MARATHON', 'ARVSMART', 'QUICKHEAL', 'SJS', 'SMLISUZU', 'GNA', 'SUBEXLTD', 'DPSCLTD', 'RAMCOIND', 'JASH', 'SHAKTIPUMP', 'MUFTI', 'GEOJITFSL', 'BUTTERFLY', 'YASHO', 'TALBROAUTO', 'CAPACITE', 'RANEHOLDIN', 'GOKULAGRO', 'GOLDIAM', 'VADILALIND', 'NITINSPIN', 'NELCO', 'MADRASFERT', 'VSSL', 'HLVLTD', 'RAMASTEEL', 'ROSSELLIND', 'PIXTRANS', 'SUVEN', '5PAISA', 'UNITECH', 'PNBGILTS', 'CENTUM', 'AMRUTANJAN', 'HARIOMPIPE', 'MANINDS', 'BCLIND', 'PREMEXPLN', 'WHEELS', 'NDTV', 'DHAMPURSUG', 'PENIND', 'DCW', 'DREDGECORP', 'NSIL', 'SPCENET', 'GTLINFRA', 'SURYODAY', 'UNIVCABLES', 'SICALLOG', 'HIMATSEIDE', 'FAIRCHEMOR', 'DEEPINDS', 'DWARKESH', 'IGARASHI', 'SHANKARA', 'SERVOTECH', 'PUNJABCHEM', 'ACLGATI', 'CONTROLPR', 'COSMOFIRST', 'HPL', 'BHAGCHEM', 'AHL', 'HERANBA', 'ATULAUTO', 'GVKPIL', 'INDRAMEDCO', 'SIGACHI', 'HITECH', 'SPIC', 'AJMERA', 'MVGJL', 'VASCONEQ', 'GENESYS', 'UTTAMSUGAR', 'NIITLTD', 'SHAILY', 'NAVKARCORP', 'GEPIL', 'BAJEL', 'SPAL', 'APTECHT', 'ANDHRSUGAR', 'KUANTUM', 'KRISHANA', 'KITEX', 'CUPID', 'POKARNA', 'KABRAEXTRU', 'STOVEKRAFT', 'DPABHUSHAN', 'MONARCH', 'OMINFRAL', 'SURAJEST', 'MONTECARLO', 'NACLIND', 'KOKUYOCMLN', 'PENINLAND', 'MANGCHEFER', 'IGPL', 'BLKASHYAP', 'KICL', 'TAJGVK', 'EKC', 'JITFINFRA', 'HARDWYN', 'SYNCOMF', 'EIHAHOTELS', 'ONWARDTEC', 'KSOLVES', 'ALICON', 'AVTNPL', 'SATIA', 'VALIANTORG', 'SUMMITSEC', 'AGARIND', 'NGLFINE', 'SHREDIGCEM', 'AWHCL', 'NELCAST', 'OMAXE', 'MANALIPETC', 'HEUBACHIND', 'INDORAMA', 'COFFEEDAY', 'OAL', 'AVADHSUGAR', 'DCMSRIND', 'TEXINFRA', 'RML', 'REFEX', 'ROTO', 'GULPOLY', 'MARINE', 'SASTASUNDR', 'RAMRAT', 'SATINDLTD', 'BLISSGVS', 'SOLARA', 'ATL', 'MATRIMONY', 'GMBREW', 'STERTOOLS', 'SHALPAINTS', 'CLSEL', 'INDIANHUME', 'TVTODAY', 'REPRO', 'IMPAL', 'STEELCAS', 'HESTERBIO', 'JYOTISTRUC', 'ZOTA', 'LINCOLN', 'INDNIPPON', 'XCHANGING', 'CENTRUM', 'RICOAUTO', 'FOCUS', 'KOPRAN', 'BIGBLOC', 'SHIVALIK', 'GICHSGFIN', 'JAYBARMARU', 'DLINKINDIA', 'TFCILTD', 'EXCELINDUS', 'ONMOBILE', 'GRMOVER', 'TRACXN', 'HERCULES', 'AGSTRA', 'TREL', 'ARIHANTSUP', 'DVL', 'UNIENTER', 'LIKHITHA', 'GANESHBE', 'SKYGOLD', 'SPORTKING', 'FAZE3Q', 'KAMOPAINTS', 'CHEMCON', 'RAJRILTD', 'GFLLIMITED', 'INFOBEAN', 'CREATIVE', 'SMCGLOBAL', 'SNOWMAN', 'CONSOFINVT', 'NINSYS', 'ASIANENE', 'MKPL', 'SBGLP', 'BODALCHEM', 'RUSHIL', 'V2RETAIL', 'BAJAJHCARE', 'CSLFINANCE', 'RAMCOSYS', 'PANACEABIO', 'RSWM', 'NAHARSPING', 'JAGSNPHARM', 'SKMEGGPROD', 'DBOL', 'NCLIND', 'SMSPHARMA', 'ACL', 'VHL', 'NDRAUTO', 'LINC', 'ALLSEC', 'ONEPOINT', 'RGL', 'STEELXIND', 'KAMDHENU', 'AMBIKCO', 'KELLTONTEC', 'ICEMAKE', 'SPENCERS', 'MOTISONS', 'SRHHYPOLTD', 'MAGADSUGAR', 'GPTINFRA', 'SCHAND', 'ASIANTILES', 'DYCL', 'SUTLEJTEX', 'E2E', 'WEBELSOLAR', 'RADIANTCMS', 'PPL', 'CENTENKA', 'ZEEMEDIA', 'GANDHITUBE', 'MSPL', 'YUKEN', 'HIRECT', 'EIMCOELECO', 'UGARSUGAR', 'AMNPLST', 'HPAL', 'SREEL', 'ORIENTPPR', 'SPECIALITY', 'JUBLINDS', 'TRU', 'TNPETRO', 'VIMTALABS', 'DPWIRES', 'KERNEX', 'WINDLAS', 'DHARMAJ', 'INDOAMIN', 'SILVERTUC', 'GKWLIMITED', 'ASALCBR', 'MUNJALAU', 'ENIL', 'BLAL', 'ROHLTD', 'CHEVIOT', 'WALCHANNAG', 'MANAKSIA', 'HITECHGEAR', 'FOODSIN', 'PAKKA', 'BIRLACABLE', 'KOTHARIPET', 'SAKAR', 'TBZ', 'SANDESH', 'HEXATRADEX', 'BCONCEPTS', 'VINYLINDIA', 'OCCL', 'DMCC', '3IINFOLTD', 'STCINDIA', 'CREST', 'DENORA', 'SWELECTES', 'ZUARI', 'DECCANCE', 'DSSL', 'MOLDTECH', 'RUBYMILLS', 'DHANBANK', 'URJA', 'NAGAFERT', 'MAANALU', 'MENONBE', 'SUKHJITS', 'PLASTIBLEN', 'MEDICAMEQ', 'GSLSU', 'ADSL', 'VALIANTLAB', 'BALAJITELE', 'JAYAGROGN', 'SELAN', 'MICEL', 'VISAKAIND', 'ESTER', 'KECL', 'ELIN', 'INDOBORAX', 'ARIHANTCAP', 'DHUNINV', 'NECLIFE', 'SEMAC', 'EMAMIPAP', 'BHAGERIA', 'ELDEHSG', 'VLSFINANCE', 'VIKASLIFE', 'SHREEPUSHK', 'FCSSOFT', 'PYRAMID', 'CHEMBOND', 'MAXIND', 'INDOTECH', 'BGRENERGY', 'APEX', 'MEDICO', 'MALLCOM', 'NRAIL', 'SALZERELEC', 'AXITA', 'OSWALGREEN', 'KHAICHEM', 'HMVL', 'HCL-INSYS', 'HINDCOMPOS', 'GHCLTEXTIL', 'KAMATHOTEL', 'ASAL', 'TVSELECT', 'ARROWGREEN', 'ESSARSHPNG', 'IRISDOREME', 'RBL', 'RITCO', 'JETAIRWAYS', 'VERTOZ', 'LOKESHMACH', 'DIGISPICE', 'JPOLYINVST', 'GRPLTD', 'KHADIM', 'MIRZAINT', 'VLEGOV', 'HUBTOWN', 'SBC', 'APCL', 'DEEPENR', '20MICRONS', 'MUTHOOTCAP', 'RACE', 'SHREYAS', 'INDSWFTLAB', 'GLOBAL', 'ORIENTCER', 'JINDALPHOT', 'THEINVEST', 'MACPOWER', 'KILITCH', 'STEL', 'MINDTECK', 'ORIENTBELL', 'HTMEDIA', 'RADIOCITY', 'NIPPOBATRY', 'OSIAHYPER', 'ZUARIIND', 'KANORICHEM', 'BIRLAMONEY', 'POCL', 'MUNJALSHOW', 'INTLCONV', 'AARTISURF', 'BBTCL', 'CYBERTECH', 'ZIMLAB', 'RATNAVEER', 'PRIMESECU', 'BEDMUTHA', 'ALBERTDAVD', 'KRITI', 'NAHARPOLY', 'WINDMACHIN', 'UNIDT', 'NAHARINDUS', 'CLEDUCATE', 'PTL', 'WEL', 'VENUSREM', 'DIAMINESQ', 'WSI', 'GOKUL', 'SARVESHWAR', 'MMP', 'RADHIKAJWE', 'ORICONENT', 'CHEMFAB', 'MAZDA', 'GOACARBON', 'PROZONER', 'ASMS', 'EXXARO', 'DONEAR', 'DOLPHIN', 'NAHARCAP', 'AUTOIND', 'PAVNAIND', 'BANSWRAS', 'MEGASOFT', 'GENUSPAPER', 'PDMJEPAPER', 'NDLVENTURE', 'SIGMA', 'ORBTEXP', 'GEECEE', 'VARDHACRLC', 'GEEKAYWIRE', 'LIBERTSHOE', 'ADVANIHOTR', 'MBLINFRA', 'SARLAPOLY', 'SOUTHWEST', 'UNIVPHOTO', 'VIKASECO', 'SHIVAMAUTO', 'PARSVNATH', 'RBZJEWEL', 'IFBAGRO', 'SPMLINFRA', 'WEALTH', 'SIMPLEXINF', 'SILINV', 'NBIFIN', 'OSWALAGRO', 'DICIND', 'MODISONLTD', 'SGIL', 'ASIANHOTNR', 'SAHYADRI', 'AVG', 'BALAXI', 'RPPINFRA', 'KAYA', 'HITECHCORP', 'PLAZACABLE', 'CINELINE', 'SHYAMCENT', 'KOTARISUG', 'GOLDTECH', 'SHEMAROO', 'KRITINUT', 'OSWALSEEDS', 'UFO', 'NURECA', 'LORDSCHLO', 'BRNL', 'BPL', 'SAKUMA', 'TRIGYN', 'EMAMIREAL', 'WANBURY', 'ALANKIT', 'NRL', 'BIL', 'LYKALABS', 'IITL', 'IL&FSENGG', 'GOLDSTAR', 'KCPSUGIND', 'TPLPLASTEH', 'PODDARMENT', 'RUCHIRA', 'SHREERAMA', 'NATHBIOGEN', 'APOLSINHOT', 'EIFFL', 'NDL', 'REMSONSIND', 'VIPCLOTHNG', 'MAWANASUG', 'BROOKS', 'RAMAPHO', 'TIL', 'PVP', 'KOTHARIPRO', 'ANMOL', 'IVC', 'AURUM', 'SADBHAV', 'MEGASTAR', 'MAHEPC', 'MIRCELECTR', 'RANASUG', 'SRGHFL', 'DYNPRO', 'STARPAPER', 'ASAHISONG', 'DEVIT', 'INSPIRISYS', 'SHREYANIND', 'NILAINFRA', 'URAVI', 'AYMSYNTEX', 'REPL', 'PRAXIS', 'HINDMOTORS', 'PONNIERODE', 'SCPL', 'EMKAY', 'SMLT', 'STARTECK', 'COASTCORP', 'SINTERCOM', 'TIPSFILMS', 'PREMIERPOL', 'AIRAN', 'CAREERP', 'SAKHTISUG', 'TAKE', 'IZMO', 'PPAP', 'PASUPTAC', 'BHAGYANGR', 'PRECOT', 'ZODIACLOTH', 'MHLXMIRU', 'ASHIMASYN', 'SAH', 'RVHL', 'LOYALTEX', 'UCAL', 'DCMNVL', 'MANORG', 'HARRMALAYA', 'ESSENTIA', 'LGHL', 'GSS', 'MANAKSTEEL', 'VISHWARAJ', 'LGBFORGE', 'BASML', 'MURUDCERA', 'JAYSREETEA', 'GUJAPOLLO', 'DELPHIFX', 'PILITA', 'ELECTHERM', 'ABAN', 'TEMBO', 'INDTERRAIN', 'KRITIKA', 'HINDCON', 'PRITIKAUTO', 'AARON', 'VIRINCHI', 'RAJMET', 'ZODIAC', 'KMSUGAR', 'ELGIRUBCO', 'MARALOVER', 'RAJTV', 'MCLEODRUSS', 'PRITI', 'GULFPETRO', 'TRF', 'MEP', 'EQUIPPP', 'MANOMAY', 'SUPERHOUSE', 'NECCLTD', 'BAIDFIN', 'ARIES', 'PAR', 'SELMC', 'SUNDRMBRAK', 'RANEENGINE', 'RAMANEWS', 'KAPSTON', 'IRIS', 'KANPRPLA', 'SEJALLTD', 'RUCHINFRA', 'GINNIFILA', 'BTML', 'AHLEAST', 'SVLL', 'RHL', 'LAL', 'BYKE', 'COMPUSOFT', 'AKSHARCHEM', 'RPPL', 'ALMONDZ', 'INTENTECH', 'MGEL', 'HILTON', 'NDGL', 'DUCON', 'GILLANDERS', 'MAHESHWARI', 'CORALFINAC', 'SOFTTECH', 'AARVI', 'DTIL', 'IVP', 'PALREDTEC', 'EROSMEDIA', 'INDOTHAI', 'NITCO', 'WELINV', 'MAGNUM', 'ATAM', 'GENCON', 'CCHHL', 'GIRRESORTS', 'RELCHEMQ', 'ARSHIYA', 'VETO', 'INDOWIND', 'INVENTURE', 'SUVIDHAA', 'BAFNAPH', 'ALPA', 'BSL', 'TTL', 'LOVABLE', 'TEXMOPIPES', 'ZEELEARN', 'USK', 'MODIRUBBER', 'TREJHARA', 'MAHAPEXLTD', 'DCI', 'SURANAT&P', 'IEL', 'TOTAL', 'VIPULLTD', 'SALSTEEL', 'A2ZINFRA', 'RHFL', 'FRETAIL', 'LATTEYS', 'SPLIL', 'JOCIL', 'TARMAT', 'NOIDATOLL', 'ATLANTAA', 'UNITEDPOLY', 'AKSHOPTFBR', 'ARCHIDPLY', 'AIROLAM', 'ASPINWALL', 'VAISHALI', 'KBCGLOBAL', 'KAKATCEM', 'SIGIND', 'ARVEE', 'AVONMORE', 'VISESHINFO', 'JMA', 'AKI', 'NILASPACES', 'RAJSREESUG', 'SHIVATEX', 'FELIX', 'MANAKCOAT', 'EMMBI', 'GLOBALVECT', 'TOUCHWOOD', 'WEIZMANIND', 'SHAH', 'SMARTLINK', 'DRCSYSTEMS', 'ALPHAGEO', 'PASHUPATI', 'UMAEXPORTS', 'BEARDSELL', 'ISFT', 'BHARATGEAR', 'GVPTECH', 'NIRAJ', 'CAPTRUST', 'RKEC', 'BAGFILMS', 'MUKTAARTS', 'LOTUSEYE', 'DANGEE', 'WORTH', 'AHLADA', 'SIKKO', 'KOHINOOR', 'FCONSUMER', 'KREBSBIO', 'PRAKASHSTL', 'INDBANK', 'XELPMOC', 'AMJLAND', 'UMANGDAIRY', 'DJML', 'JHS', 'SURANASOL', 'SADBHIN', 'LAMBODHARA', 'UNITEDTEA', 'SECURKLOUD', 'SMSLIFE', 'IL&FSTRANS', 'MANAKALUCO', 'INDIANCARD', 'SUMIT', 'THOMASCOTT', 'BALPHARMA', 'PANSARI', 'INCREDIBLE', 'LAGNAM', 'VARDMNPOLY', 'MANGALAM', 'TIRUPATIFL', 'SIL', '3RDROCK', 'SALONA', 'AMDIND', 'ASTRON', 'RSSOFTWARE', 'CENTEXT', 'LASA', 'KALYANIFRG', 'DCM', 'MOTOGENFIN', 'CTE', 'CORDSCABLE', 'PRAENG', 'ACCURACY', 'AARTECH', 'SUNDARAM', 'SONAMLTD', 'SURYALAXMI', 'GOYALALUM', 'ARTNIRMAN', 'GTL', 'ALKALI', 'OMAXAUTO', 'FLEXITUFF', 'MAHASTEEL', 'SHRADHA', 'TAINWALCHM', 'ANIKINDS', 'WIPL', 'SUPREMEINF', 'OILCOUNTUB', 'SECMARK', 'PIONEEREMB', 'AAREYDRUGS', 'ENERGYDEV', 'SHAHALLOYS', 'PATINTLOG', 'SVPGLOB', 'MITCON', 'GANGESSECU', 'GTECJAINX', 'OBCL', 'NITIRAJ', 'SIMBHALS', 'TIMESGTY', 'CROWN', 'MDL', 'DIL', 'HPIL', 'PALASHSECU', 'BLBLIMITED', 'DBSTOCKBRO', 'UNIVASTU', 'PRUDMOULI', 'AAKASH', 'AGRITECH', 'DAMODARIND', 'BANKA', 'BVCL', 'S&SPOWER', 'TOKYOPLAST', 'AVROIND', 'ZENITHSTL', 'STEELCITY', 'HISARMETAL', 'AKSHAR', 'DGCONTENT', 'SOMICONVEY', 'MRO-TEK', 'AAATECH', 'YAARI', 'GROBTEA', 'MCL', 'NIBL', 'MARSHALL', 'DELTAMAGNT', 'SAMPANN', 'BHANDARI', 'PKTEA', 'LPDC', 'INDSWFTLTD', 'MBECL', 'CINEVISTA', 'PANACHE', 'FIBERWEB', 'ARCHIES', 'REGENCERAM', 'TPHQ', 'SETCO', 'CELEBRITY', 'HECPROJECT', 'AGROPHOS', 'HOVS', 'CUBEXTUB', 'AUSOMENT', 'KARMAENG', 'DHRUV', 'WEWIN', 'ATALREAL', 'TREEHOUSE', 'VINNY', 'BIOFILCHEM', 'GOLDENTOBC', 'RELIABLE', 'ZENITHEXPO', 'ASHOKAMET', 'VASWANI', 'KEYFINSERV', 'LEXUS', 'PODDARHOUS', 'ORIENTLTD', 'MORARJEE', 'SHIVAMILLS', 'CEREBRAINT', 'MAHICKRA', 'NAGREEKEXP', 'SECURCRED', 'AKG', 'TERASOFT', 'COMPINFO', 'JAIPURKURT', 'SHRENIK', 'SAMBHAAV', 'VINEETLAB', 'MOKSH', 'AROGRANITE', 'KANANIIND', 'PARASPETRO', 'SOMATEX', 'ICDSLTD', 'PNC', 'ROML', 'GANGAFORGE', 'MANUGRAPH', 'SITINET', 'ANKITMETAL', 'MALUPAPER', 'AARVEEDEN', 'BANG', 'PIGL', 'BANARBEADS', 'NGIL', 'AKASH', 'TFL', 'DNAMEDIA', 'GLOBE', 'JETFREIGHT', 'SPYL', 'FLFL', 'EXCEL', 'AJOONI', 'MADHAV', 'LFIC', 'BURNPUR', 'SEYAIND', 'VSCL', 'PEARLPOLY', 'HBSL', 'MADHUCON', 'ABMINTLLTD', 'AMBICAAGAR', 'ADL', 'KEEPLEARN', 'BINANIIND', 'RKDL', 'SUULD', 'CYBERMEDIA', 'TCLCONS', 'SANGINITA', 'FSC', '3PLAND', 'LIBAS', 'SRPL', 'SUPERSPIN', 'SAGARDEEP', 'EDUCOMP', 'HAVISHA', 'TGBHOTELS', 'ADROITINFO', 'SGL', 'GODHA', 'DIACABS', 'LAXMICOT', 'COUNCODOS', 'NEXTMEDIA', 'TNTELE', 'ACEINTEG', 'BALKRISHNA', 'KKVAPOW', 'KHANDSE', 'GATECH', 'TECILCHEM', 'WILLAMAGOR', 'BOHRAIND', 'FMNL', '21STCENMGM', 'KSHITIJPOL', 'NKIND', 'HEADSUP', 'ROLLT', 'GUJRAFFIA', 'KRIDHANINF', 'VIVIDHA', 'MITTAL', 'NARMADA', 'INFOMEDIA', 'IMPEXFERRO', 'KAUSHALYA', 'CONTI', 'KAVVERITEL', 'UNIINFO', 'MTEDUCARE', 'LCCINFOTEC', 'KHAITANLTD', 'CALSOFT', 'SILGO', 'ORIENTALTL', 'HYBRIDFIN', 'VCL', 'SUPREMEENG', 'MOHITIND', 'WINSOME', 'MASKINVEST', 'ANTGRAPHIC', 'ONELIFECAP', 'MPTODAY', 'TECHIN', 'LYPSAGEMS', 'SPENTEX', 'SHANTI', 'NAGREEKCAP', 'EASTSILK', 'ORTINLAB', 'TIJARIA', 'OMKARCHEM', 'SILLYMONKS', 'DIGJAMLMTD', 'UMESLTD', 'VIJIFIN', 'TVVISION', 'BLUECHIP', 'ARENTERP', 'GLFL', 'NORBTEAEXP', 'INNOVATIVE', 'EUROTEXIND', 'RADAAN', 'SHYAMTEL', 'TARAPUR', 'SABTN', 'PREMIER', 'BKMINDST', 'ALPSINDUS', 'DCMFINSERV', 'SANCO', 'CREATIVEYE', 'UNIVAFOODS', 'JALAN', 'BLUECOAST', 'NIRAJISPAT', 'SABEVENTS', 'MELSTAR', 'LAKPRE', 'ABHISHEK', 'AHLWEST', 'AIFL', 'AJRINFRA', 'ALCHEM', 'ANSALAPI', 'ARCOTECH', 'ARSSINFRA', 'ASIL', 'ATLASCYCLE', 'ATNINTER', 'BALLARPUR', 'BGLOBAL', 'BILENERGY', 'BIRLATYRE', 'BLUEBLENDS', 'BRFL', 'CANDC', 'CCCL', 'CELESTIAL', 'CKFSL', 'CMICABLES', 'DHARSUGAR', 'DQE', 'DSKULKARNI', 'EASUNREYRL', 'EON', 'EUROCERA', 'EUROMULTI', 'FEL', 'GAMMONIND', 'GANGOTRI', 'GAYAHWS', 'GAYAPROJ', 'GBGLOBAL', 'GFSTEELS', 'GITANJALI', 'GOENKA', 'HDIL', 'HINDNATGLS', 'ICSA', 'INDLMETER', 'INDOSOLAR', 'IVRCLINFRA', 'JAINSTUDIO', 'JBFIND', 'JIKIND', 'JINDCOT', 'JPINFRATEC', 'KGL', 'KSERASERA', 'KSK', 'LAKSHMIEFL', 'LEEL', 'MANPASAND', 'MCDHOLDING', 'MERCATOR', 'METALFORGE', 'METKORE', 'MODTHREAD', 'MOHOTAIND', 'MVL', 'NAKODA', 'NITINFIRE', 'NTL', 'NUTEK', 'OPTOCIRCUI', 'ORTEL', 'PDPL', 'PUNJLLOYD', 'QUINTEGRA', 'RAINBOWPAP', 'RAJVIR', 'RCOM', 'RELCAPITAL', 'RMCL', 'RMMIL', 'RNAVAL', 'ROLTA', 'SANWARIA', 'SATHAISPAT', 'SETUINFRA', 'SHIRPUR-G', 'SKIL', 'SPTL', 'SUMEETINDS', 'TALWALKARS', 'TALWGYM', 'TCIFINANCE', 'TECHNOFAB', 'UJAAS', 'UNIPLY', 'UNITY', 'VALECHAENG', 'VICEROY', 'VIDEOIND', 'VISASTEEL', 'VISUINTL', 'VIVIMEDLAB', 'ZICOM']
    timeList = ["1mo","1y"]

    for timeTicker in timeList:
        if(timeTicker=="1mo"):
            FINAL_DATA = 'data/STOCKS_RETURN_1mon.csv'        
        if(timeTicker=="1y"):
            FINAL_DATA = 'data/STOCKS_RETURN_1YR.csv'
        
        ExceptionList = []
        for i in COMPANY_NAME:
            tempDF = pd.read_csv(FINAL_DATA)
            if i in tempDF['Company_Name'].values:
                tempDF = tempDF[tempDF['Company_Name'] != i]
                tempDF.to_csv(FINAL_DATA,index=False)
            # stockReturn = getStockReturns(i,timeTicker)
            # ****** to reduce the function call defining getStockReturns() function in same file ******
            tickerCompany = f'{i}.NS'
            company = yf.Ticker(tickerCompany)
            hist = company.history(period=timeTicker)
            try:
                startPrice = hist[['Close']].iloc[0]['Close']
            except:
                print(Akaycolours.RED+f'[ERROR] stock data not found for {i}'+Akaycolours.RESET)
                ExceptionList.append(i)
                continue
            lastPrice = hist[['Close']].iloc[-1]['Close']
            stockReturn = (lastPrice - startPrice)/startPrice
            stockReturn = stockReturn*100
            # ****** to use the previous code comment above block and uncomment getStockReturns() API ******

            # checking for existing row, removing if existts
            print(Akaycolours.BOLD+Akaycolours.BLUE+f'finding {timeTicker} return for {i} = {stockReturn}')
            with open(FINAL_DATA, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([i, stockReturn])
            df = pd.read_csv(FINAL_DATA)
            df = df.sort_values(by='Return')
            df.to_csv(FINAL_DATA,index=False)
        generateHTML(timeTicker)
        print(ExceptionList)
