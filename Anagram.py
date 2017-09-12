file=open('words.txt','r')
b={}
original={i.rstrip("\r\n") for i in file}
sorted_dict={"".join(sorted(i)) for i in original}
for i in original:
    a = "".join(sorted(i))
    if a in sorted_dict:
        if a in b:
            b[a].append(i)
        else:
            b[a]=[i]
c=[]
for i in b.values():
    if len(i)>5:
        c.append(i)
t=len(c)
for v in range(t):
    for i in range(t):
        if len(c[i])<len(c[v]):
            temp=c[i]
            c[i]=c[v]
            c[v]=temp           
counter = 0
for i in c:
    counter+=1
    print(i)
    #print(len(i))
print(counter)

'''Output
104
['rapes', 'reaps', 'prase', 'parse', 'spare', 'spear', 'presa', 'pares', 'pears', 'apers', 'asper']
['artels', 'staler', 'alerts', 'slater', 'talers', 'estral', 'salter', 'alters', 'laster', 'stelar', 'ratels']
['stela', 'taels', 'setal', 'slate', 'steal', 'teals', 'tesla', 'tales', 'least', 'stale']
['niters', 'trines', 'sinter', 'insert', 'inters', 'inerts', 'triens', 'estrin', 'nitres']
['spacer', 'parsec', 'escarp', 'pacers', 'scrape', 'crapes', 'capers', 'secpar', 'recaps']
['lears', 'laser', 'lares', 'earls', 'seral', 'reals', 'rales', 'arles']
['ripes', 'piers', 'spire', 'prise', 'peris', 'pries', 'spier', 'speir']
['anestri', 'retinas', 'stearin', 'retsina', 'retains', 'nastier', 'stainer', 'ratines']
['acres', 'races', 'escar', 'scare', 'carse', 'serac', 'cares', 'acers']
['regains', 'reginas', 'reagins', 'seringa', 'searing', 'earings', 'gainers', 'erasing']
['sate', 'east', 'eats', 'etas', 'seat', 'teas', 'seta', 'ates']
['carets', 'reacts', 'caters', 'crates', 'recast', 'cartes', 'caster', 'traces']
['sepal', 'salep', 'peals', 'spale', 'pales', 'lapse', 'pleas', 'leaps']
['spares', 'parses', 'sparse', 'passer', 'spears', 'prases', 'aspers', 'repass']
['pleats', 'septal', 'pastel', 'petals', 'plates', 'staple', 'palets', 'palest']
['mitres', 'timers', 'merits', 'miters', 'remits', 'smiter', 'mister']
['septa', 'pates', 'paste', 'peats', 'spate', 'tepas', 'tapes']
['toners', 'noters', 'tensor', 'tenors', 'stoner', 'nestor', 'trones']
['mites', 'times', 'items', 'stime', 'emits', 'smite', 'metis']
['algins', 'liangs', 'ligans', 'lingas', 'signal', 'lasing', 'aligns']
['speer', 'peers', 'perse', 'peres', 'prese', 'spree', 'prees']
['tussore', 'oestrus', 'ousters', 'stoures', 'sourest', 'estrous', 'souters']
['relaid', 'ariled', 'derail', 'railed', 'dialer', 'redial', 'laired']
['beats', 'abets', 'beast', 'betas', 'baste', 'bates', 'tabes']
['panes', 'sneap', 'spean', 'napes', 'peans', 'aspen', 'neaps']
['mensa', 'means', 'amens', 'nemas', 'names', 'manse', 'manes']
['gantries', 'ingrates', 'rangiest', 'astringe', 'granites', 'ganister', 'angriest']
['stirpes', 'esprits', 'spriest', 'sprites', 'stripes', 'priests', 'persist']
['enosis', 'noesis', 'sonsie', 'essoin', 'noises', 'ossein', 'eosins']
['starer', 'terras', 'rarest', 'raters', 'raster', 'arrest', 'tarres']
['sewar', 'swear', 'wares', 'wears', 'resaw', 'sawer', 'sware']
['cruets', 'curets', 'rectus', 'recuts', 'eructs', 'cruset', 'truces']
['astride', 'tardies', 'diaster', 'staider', 'tirades', 'disrate', 'aridest']
['stere', 'ester', 'steer', 'reset', 'trees', 'reest', 'terse']
['tastier', 'artiest', 'attires', 'striate', 'iratest', 'ratites', 'artiste']
['armets', 'master', 'matres', 'ramets', 'tamers', 'maters', 'stream']
['versal', 'serval', 'salver', 'ravels', 'velars', 'slaver', 'lavers']
['sear', 'sera', 'rase', 'ares', 'ears', 'eras', 'arse']
['carte', 'cater', 'recta', 'caret', 'trace', 'crate', 'react']
['spireme', 'premise', 'premies', 'empires', 'epimers', 'imprese', 'emprise']
['diets', 'sited', 'deist', 'dites', 'edits', 'stied', 'tides']
['debars', 'breads', 'serdab', 'bardes', 'ardebs', 'sabred', 'beards']
['spader', 'padres', 'spared', 'parsed', 'drapes', 'spread', 'rasped']
['trade', 'tread', 'tared', 'dater', 'derat', 'rated']
['astir', 'sitar', 'stair', 'airts', 'tarsi', 'stria']
['seating', 'ingesta', 'easting', 'eatings', 'teasing', 'ingates']
['troches', 'tochers', 'rochets', 'torches', 'rotches', 'hectors']
['clasper', 'placers', 'parcels', 'reclasp', 'carpels', 'scalper']
['solacer', 'oracles', 'escolar', 'recoals', 'claroes', 'coalers']
['renigs', 'sering', 'resign', 'singer', 'reigns', 'signer']
['onset', 'notes', 'steno', 'stone', 'tones', 'seton']
['arils', 'rails', 'liras', 'lairs', 'liars', 'rials']
['hales', 'leash', 'shale', 'sheal', 'selah', 'heals']
['seder', 'deers', 'reeds', 'redes', 'drees', 'sered']
['tanrec', 'canter', 'nectar', 'recant', 'trance', 'centra']
['scares', 'escars', 'carses', 'crases', 'seracs', 'caress']
['reests', 'serest', 'resets', 'esters', 'steers', 'steres']
['rail', 'liar', 'lira', 'lair', 'aril', 'rial']
['salve', 'laves', 'valse', 'vales', 'slave', 'veals']
['respect', 'recepts', 'spectre', 'sceptre', 'specter', 'scepter']
['easter', 'eaters', 'teaser', 'reseat', 'seater', 'aretes']
['idols', 'sloid', 'soldi', 'diols', 'solid', 'lidos']
['deairs', 'raised', 'irades', 'resaid', 'redias', 'aiders']
['bares', 'saber', 'baser', 'bears', 'braes', 'sabre']
['tripes', 'ripest', 'priest', 'esprit', 'sprite', 'stripe']
['aspirer', 'raspier', 'praiser', 'rapiers', 'repairs', 'parries']
['seaters', 'tessera', 'teasers', 'reseats', 'searest', 'easters']
['spile', 'plies', 'piles', 'spiel', 'slipe', 'speil']
['recants', 'canters', 'nectars', 'scanter', 'trances', 'tanrecs']
['dopiest', 'deposit', 'sopited', 'topside', 'podites', 'posited']
['relive', 'levier', 'eviler', 'veiler', 'liever', 'revile']
['elastin', 'entails', 'salient', 'nailset', 'saltine', 'tenails']
['reagents', 'negaters', 'sergeant', 'estrange', 'grantees', 'greatens']
['staled', 'slated', 'desalt', 'deltas', 'salted', 'lasted']
['scoter', 'rectos', 'coster', 'sector', 'corset', 'escort']
['posture', 'petrous', 'spouter', 'proteus', 'troupes', 'pouters']
['artel', 'alert', 'later', 'alter', 'taler', 'ratel']
['pastier', 'parties', 'piaster', 'piastre', 'pirates', 'traipse']
['results', 'lustres', 'ulsters', 'lusters', 'rustles', 'sutlers']
['opts', 'stop', 'tops', 'spot', 'pots', 'post']
['selahs', 'hassel', 'lashes', 'hassle', 'shales', 'sheals']
['hardset', 'hatreds', 'hardest', 'trashed', 'dearths', 'threads']
['bared', 'debar', 'beard', 'ardeb', 'barde', 'bread']
['traps', 'prats', 'sprat', 'parts', 'tarps', 'strap']
['plate', 'palet', 'petal', 'lepta', 'leapt', 'pleat']
['steals', 'stales', 'leasts', 'slates', 'tassel', 'teslas']
['nargiles', 'signaler', 'engrails', 'aligners', 'slangier', 'realigns']
['integral', 'altering', 'alerting', 'relating', 'triangle', 'tanglier']
['rustle', 'sutler', 'result', 'lustre', 'ulster', 'luster']
['teams', 'meats', 'mates', 'steam', 'tames', 'satem']
['acred', 'raced', 'cedar', 'cadre', 'arced', 'cared']
['swat', 'wats', 'twas', 'staw', 'wast', 'taws']
['alines', 'saline', 'silane', 'aliens', 'lianes', 'elains']
['paster', 'repast', 'paters', 'trapes', 'prates', 'tapers']
['pinaster', 'painters', 'pristane', 'pertains', 'repaints', 'pantries']
['sadhe', 'shade', 'hades', 'deash', 'heads', 'ashed']
['tenser', 'nester', 'ternes', 'enters', 'rentes', 'resent']
['stapler', 'plaster', 'psalter', 'platers', 'persalt', 'palters']
['curet', 'cuter', 'truce', 'cruet', 'recut', 'eruct']
['reins', 'risen', 'resin', 'siren', 'serin', 'rinse']
['venial', 'alvine', 'veinal', 'vineal', 'alevin', 'valine']
['wots', 'stow', 'twos', 'tows', 'wost', 'swot']
['saltire', 'tailers', 'saltier', 'realist', 'retails', 'slatier']
['slide', 'idles', 'deils', 'isled', 'delis', 'sidle']
'''