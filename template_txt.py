import pandas as pd

columns_of_txt = [
            'E',
            'G',
            'H',
            'I',
            'J',
            'M',
            'N',
            'AI',
            'AH',
            'R',
            'X',
            'Y',
            'Z',
            'AA',
            'AB',
            'AC',
            'AF',
            'AG',
            'AJ',
            'AK',
            'AL',
            'K',
            'L',
            'T',
            'W',
            'BE',
            'BF',
            'BG',
            'BH',
            'BI',
            'BJ',
            'BK',
            'BL',
            'BM',
            'BN',
            'BO',
            'BP',
            'BQ',
            'BR',
            'BS',
            'BT',
            'BU',
            'BB',
            'Q',
            'V',
            'HS_IB',
            'S',
            'O',
            'P',
            'BC',
            'AM',
            'REV',
            'A',
            'B',
            'C',
            'D',
            'D1',
            'D2',
            'D3',
            'D4',
            'D5',
            'D6',
            'D7',
            'D8',
            'D9',
            'D10',
            'D11',
            'D12',
            'D13',
            'D14',
            'D15',
            'D16',
            'D17',
            'D18',
            'D19',
            'D20',
            'D21',
            'D22',
            'D23',
            'D24',
            'D25',
            'D26',
            'D27',
            'D28',
            'D29',
            'D30',
            'D31',
            'D32',
            'D33',
            'D34',
            'D35',
            'D36',
            'D37',
            'D38',
            'D39',
            'D40',
            'D41',
            'D42',
            'D43',
            'D44',
            'D45',
            'D46']

columns_of_txt_ds = pd.Series(columns_of_txt)
keys_to_columns = {
    'E': 'Name drawing',
    'G': 'Drawing number',
    'H': 'Date',
    'M': 'Quantity',
    'N': 'Volume',
    'I': 'Revision',
    'AI': 'Concrete',
    'AH': 'Concrete min',
    'X': 'Strands bottom quantity',
    'Y': 'Bottom strands dim',
    'Z': 'Bottom strands force',
    'AA': 'Top strands quantity',
    'AB': 'Top strands dim',
    'AC': 'Top strands force',
    'AF': 'Fire resistance',
    'AG': 'Exposure class',
    'AJ': 'X-dim',
    'AK': 'Y-dim',
    'AL': 'Z-dim',
    'K': 'Drawing status',
    'L': 'Factory',
    'O': 'Mass',
    'P': 'Assembly mass',
    'A': 'Name',
    'B': 'Type',
    'D3': 'User',
    'D4': 'Steel formwork',
    'D16': 'Max aggregate',
    'D17': 'Steel type',
    'D24': 'Chamfer',
    'D1': 'Prj index',
    'D18': 'Precamber',
    'D20': 'w/c',
    'BE': 'd4 mass',
    'BF': 'd5 mass',
    'BG': 'd6 mass',
    'BH': 'd8 mass',
    'BI': 'd10 mass',
    'BJ': 'd12 mass',
    'BK': 'd14 mass',
    'BL': 'd16 mass',
    'BM': 'd18 mass',
    'BN': 'd20 mass',
    'BO': 'd22 mass',
    'BP': 'd25 mass',
    'BQ': 'd28 mass',
    'BR': 'd32 mass',
    'BS': 'd40 mass',
    'BT': '42d mass',
    'BU': '45d mass',
    'D21': 'Years',
    'D20': 'W/C'
    }

keys_to_columns_inv = {v: k for k, v in keys_to_columns.items()}
keys_to_columns_ds = pd.Series(keys_to_columns)

df_empty = pd.DataFrame(columns=columns_of_txt)

keys_to_name = {
    'FS':  'Stopa fundamentowa/Spot footing',
    'FC':  'Lawa fundamentowa/Continuous footing',
    'FSL': 'Stopa kielichowa/Sleeve footing',
    'FSLP':'Szklanka do zespolenia/Socket foundations for integration',
    'C':   'Slup/Column',
    'CC':  'Slup okrągły/Circular column',
    'DOK': 'Dok/Dock',
    'B':   'Belka/beam',
    'BR':  'Belka/beam',
    'BL':  'Belka/beam',
    'BT':  'Belka/beam',
    'I':   'Dzwigar typ I/Girder type I',
    'IV':  'Dzwigar typ IV/Girder type IV',
    'IVO': 'Dzwigar typ IVO/Girder type IVO',
    'IW':  'Dzwigar typ IW/Girder type IW',
    'IT':  'Dzwigar typ IT/Girder type IT',
    'PL':  'Platew/Purlin',
    'PLT':  'Platew typu T/Purlin type T',
    'PLV':  'Platew typu V/Purlin type V',
    'PLI':  'Platew typu I/Purlin type I',
    'SB':   'Plyty balkonowe/Balcony slab',
    'FB':   'Plyty balkonowe filigranowe/Filigree balcony',
    'SC':   'Plyty nakrywkowe/Cover slab',
    'SR':   'Plyta pelna zbrojona/Reinforcement solid slab',
    'SP':   'Plyty pelne sprezone/Prestressed solid slab',
    'F':    'Plyta typu filigran/Filigree slab',
    'FP':   'Sprezona plyta typu filigran/prestressed filigree slab',
    'TT':   'Plyta TT/TT slab',
    'W': 	'Sciana pelna/Wall',
    '2F':	'Sciana z podwojnego filigranu',
    '2FI':	'Sciana z podwojnego filigranu z izolacja',
    'WSH': 	'Sciana 2 – warstwowa/Half sandwich wall',
    'WS': 	'Sciana 3 – warstwowa/Sandwich wall',
    'WSB':	'Sciana 3 - warstwowa z elewacją z cegiel/Brick sandwich wall',
    'WR':	'Sciana oporowa/Retaining wall',
    'WG':	'Podwalina/Ground wall',
    'WGSH':	'Podwalina 2 warstwowa/Ground half sandwich wall',
    'WGS':	'Podwalina 3 warstwowa/Ground sandwich wall',
    'STL': 	'Spocznik/Landing',
    'STF': 	'Bieg schodowy/Flight of stairs',
    'KNG':	'Belki typu kujan NG/Beams of KUJAN type NG',
    'KSG':	'Belki typu kujan SG/Beams of KUJAN type SG',
    'KT':	'Belki typu kujan T/Beams of KUJAN type T',
    'T':	'Belki typu T/Beams of T type',
    'PKX':	'Belki typu PKX/Beams of PKX type',
    'DS':	'Belki typu DS/Beams of DS type',
    'IG':	'Belki typu IG/Beams of IG type',
    'BC':	'Przepusty skrzynkowe/Box culverts',
    'BHC':	'Przepusty skrzynkowe 1/2/Box half culverts',
    'SHE':	'Lupiny prefabrykowane/Prefabricated shells',
    'AB':	'przyczółki mostowe/Bridge abutments',
    'TAN':	'Zbiorniki/Tanks',
    'FBA':	'Niecki fontann/Fountain basins',
    'TU':	'Tubingi/Tubings',
    'RBS':	'Podtorza/Railroad bed slabs',
    'AP':	'Ekrany akustyczne/Acoustic panels'
}

