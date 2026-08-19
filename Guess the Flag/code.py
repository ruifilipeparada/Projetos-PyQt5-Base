import random
import unicodedata

class GameLogic:
    def __init__(self):
        
        self.country_map = {
            "af": "Afeganistão", "ax": "Ilhas Åland", "al": "Albânia", "dz": "Argélia",
            "as": "Samoa Americana", "ad": "Andorra", "ao": "Angola", "ai": "Anguilla",
            "aq": "Antártida", "ag": "Antígua e Barbuda", "ar": "Argentina",
            "am": "Arménia", "aw": "Aruba", "au": "Austrália", "at": "Áustria",
            "az": "Azerbaijão", "bs": "Bahamas", "bh": "Bahrein", "bd": "Bangladeche",
            "bb": "Barbados", "by": "Bielorrússia", "be": "Bélgica", "bz": "Belize",
            "bj": "Benin", "bm": "Bermudas", "bt": "Butão", "bo": "Bolívia",
            "bq": "Bonaire, Santo Eustáquio e Saba", "ba": "Bósnia e Herzegovina",
            "bw": "Botsuana", "bv": "Ilha Bouvet", "br": "Brasil", "io": "Território Britânico do Oceano Índico",
            "bn": "Brunei", "bg": "Bulgária", "bf": "Burquina Faso", "bi": "Burundi",
            "kh": "Camboja", "cm": "Camarões", "ca": "Canadá", "cv": "Cabo Verde",
            "ky": "Ilhas Caimã", "cf": "República Centro-Africana", "td": "Chade",
            "cl": "Chile", "cn": "China", "cx": "Ilha Christmas", "cc": "Ilhas Cocos",
            "co": "Colômbia", "km": "Comores", "cg": "Congo", "cd": "República Democrática do Congo",
            "ck": "Ilhas Cook", "cr": "Costa Rica", "ci": "Costa do Marfim", "hr": "Croácia",
            "cu": "Cuba", "cw": "Curaçau", "cy": "Chipre", "cz": "República Checa",
            "dk": "Dinamarca", "dj": "Djibuti", "dm": "Dominica", "do": "República Dominicana",
            "ec": "Equador", "eg": "Egipto", "sv": "El Salvador", "gq": "Guiné Equatorial",
            "er": "Eritreia", "ee": "Estónia", "sz": "Essuatíni", "et": "Etiópia",
            "fk": "Ilhas Malvinas", "fo": "Ilhas Faroé", "fj": "Fiji", "fi": "Finlândia",
            "fr": "França", "gf": "Guiana Francesa", "pf": "Polinésia Francesa",
            "tf": "Territórios Franceses do Sul", "ga": "Gabão", "gm": "Gâmbia",
            "ge": "Geórgia", "de": "Alemanha", "gh": "Gana", "gi": "Gibraltar",
            "gr": "Grécia", "gl": "Groenlândia", "gd": "Granada", "gp": "Guadalupe",
            "gu": "Guam", "gt": "Guatemala", "gg": "Guernsey", "gn": "Guiné",
            "gw": "Guiné-Bissau", "gy": "Guiana", "ht": "Haiti", "hm": "Ilhas Heard e McDonald",
            "va": "Santa Sé", "hn": "Honduras", "hk": "Hong Kong", "hu": "Hungria",
            "is": "Islândia", "in": "Índia", "id": "Indonésia", "ir": "Irão",
            "iq": "Iraque", "ie": "Irlanda", "im": "Ilha de Man", "il": "Israel",
            "it": "Itália", "jm": "Jamaica", "jp": "Japão", "je": "Jersey",
            "jo": "Jordânia", "kz": "Cazaquistão", "ke": "Quénia", "ki": "Quiribáti",
            "kp": "Coreia do Norte", "kr": "Coreia do Sul", "kw": "Kuwait", "kg": "Quirguistão",
            "la": "Laos", "lv": "Letónia", "lb": "Líbano", "ls": "Lesoto",
            "lr": "Libéria", "ly": "Líbia", "li": "Liechtenstein", "lt": "Lituânia",
            "lu": "Luxemburgo", "mo": "Macau", "mg": "Madagáscar", "mw": "Malawi",
            "my": "Malásia", "mv": "Maldivas", "ml": "Mali", "mt": "Malta",
            "mh": "Ilhas Marshall", "mq": "Martinica", "mr": "Mauritânia",
            "mu": "Maurícia", "yt": "Mayotte", "mx": "México", "fm": "Estados Federados da Micronésia",
            "md": "Moldova", "mc": "Mónaco", "mn": "Mongólia", "me": "Montenegro",
            "ms": "Montserrat", "ma": "Marrocos", "mz": "Moçambique", "mm": "Myanmar",
            "na": "Namíbia", "nr": "Nauru", "np": "Nepal", "nl": "Países Baixos",
            "nc": "Nova Caledónia", "nz": "Nova Zelândia", "ni": "Nicarágua", "ne": "Níger",
            "ng": "Nigéria", "nu": "Niue", "nf": "Ilha Norfolk", "mk": "Macedónia do Norte",
            "mp": "Ilhas Marianas do Norte", "no": "Noruega", "om": "Omã", "pk": "Paquistão",
            "pw": "Palau", "ps": "Palestina", "pa": "Panamá", "pg": "Papua Nova Guiné",
            "py": "Paraguai", "pe": "Peru", "ph": "Filipinas", "pl": "Polónia",
            "pt": "Portugal", "pr": "Porto Rico", "qa": "Catar", "re": "Reunião",
            "ro": "Roménia", "ru": "Rússia", "rw": "Ruanda", "bl": "São Bartolomeu",
            "sh": "Santa Helena", "kn": "São Cristóvão e Neves", "lc": "São Lúcia",
            "mf": "São Martinho", "pm": "São Pedro e Miquelão", "vc": "São Vicente e Granadinas",
            "ws": "Samoa", "sm": "San Marino", "st": "São Tomé e Príncipe",
            "sa": "Arábia Saudita", "sn": "Senegal", "rs": "Sérvia", "sc": "Seicheles",
            "sl": "Serra Leoa", "sg": "Singapura", "sx": "Sint Maarten", "sk": "Eslováquia",
            "si": "Eslovénia", "sb": "Ilhas Salomão", "so": "Somália", "za": "África do Sul",
            "gs": "Geórgia do Sul e Sandwich do Sul", "ss": "Sudão do Sul", "es": "Espanha",
            "lk": "Sri Lanka", "sd": "Sudão", "sr": "Suriname", "sj": "Svalbard e Jan Mayen",
            "se": "Suécia", "ch": "Suíça", "sy": "Síria", "tw": "Taiwan",
            "tj": "Tajiquistão", "tz": "Tanzânia", "th": "Tailândia", "tl": "Timor‑Leste",
            "tg": "Togo", "tk": "Tokelau", "to": "Tonga", "tt": "Trinidad e Tobago",
            "tn": "Tunísia", "tr": "Turquia", "tm": "Turcomenistão", "tc": "Ilhas Turcas e Caicos",
            "tv": "Tuvalu", "ug": "Uganda", "ua": "Ucrânia", "ae": "Emirados Árabes Unidos",
            "gb": "Reino Unido", "us": "Estados Unidos", "um": "Ilhas Menores Distantes dos EUA",
            "uy": "Uruguai", "uz": "Uzbequistão", "vu": "Vanuatu", "ve": "Venezuela",
            "vn": "Vietname", "vg": "Ilhas Virgens Britânicas", "vi": "Ilhas Virgens dos EUA",
            "wf": "Wallis e Futuna", "eh": "Saara Ocidental", "ye": "Iémen",
            "zm": "Zâmbia", "zw": "Zimbábue"
        }
        

        self.iniciante = [
            "br","us","fr","it","de","es","pt","ca","cn","jp","au","in","mx","ar","za","ru","gr","nl","be","se",
            "ch","dk","no","fi","ie","hu","pl","tr","kr","th","vn"
        ]

        self.facil = [
            "cl","co","pe","ph","my","sg","ee","lv","lt","hr","si","ro","bg","md","ge","kz","pk","ae","gb","hk",
            "is","il","jp","au","nz","mx","ar","za","eg","ng","ke","gh","tz","ug","dz","ma"
        ]

        self.moderado = [
            "tn","ly","ci","sn","zw","zm","mw","mz","ao","cm","cf","td","er","et","bw","na","ls","mu","sc","km",
            "dj","bi","rw","mg","mv","bt","bn","tl","nc","nr","nu","tv","wf","tf","hm","gs","sj","um","bq","cx",
            "ck","bv","ax","im","je","gg","fo","mq","pf","re","pm","bl","mf","sh","ws","sm","st","vc","kn","lc"
        ]

        self.dificil = [
            "la","mm","mn","np","cv","sb","ws","to","tk","tc","vg","vi","eh","iq","jo","lb","sy","ye","ps","as",
            "ad","ai","ag","an","aw","hm","io","bv","hm","mq","pf","re","pm","bl","mf","sh","cx","ck","bv","ax",
            "im","je","gg","fo"
        ]

        self.geografo = [
            "tm","tj","kg","uz","kp","la","mm","mn","np","bn","cv","sb","ws","to","tk","tc","vg","vi","um","eh",
            "aq","bv","tf","hm","gs","sj","um"
        ]


        self.difficulty_flags = {
            "iniciante": self.iniciante.copy(),
            "facil": self.facil.copy(),
            "moderado": self.moderado.copy(),
            "dificil": self.dificil.copy(),
            "geografo": self.geografo.copy()
        }

        self.selected_difficulty = None
        self.remaining_flags = []
        self.current_flag = None
        self.score = 0
        self.round = 0
        self.total_rounds = 10

    def choose_difficulty(self, level):
        if level not in self.difficulty_flags:
            raise ValueError(f"Nível inválido: {level}")
        self.selected_difficulty = level
        self.remaining_flags = self.difficulty_flags[level].copy()
        random.shuffle(self.remaining_flags)
        self.round = 0
        self.score = 0

    def normalize(self, text):
        text = text.strip().lower()
        text = unicodedata.normalize("NFD", text)
        text = "".join(c for c in text if unicodedata.category(c) != "Mn")
        return text

    def next_flag(self):
        if self.round >= self.total_rounds or not self.remaining_flags:
            self.current_flag = None
            return None
        self.current_flag = self.remaining_flags.pop(0)
        self.round += 1
        return self.current_flag

    def check_answer(self, user_input):
        if not self.current_flag:
            return False, ""
        correct_name = self.country_map[self.current_flag]
        ans = self.normalize(user_input)
        correct_normalized = self.normalize(correct_name)
        if ans == correct_normalized:
            self.score += 1
            return True, correct_name
        else:
            return False, correct_name

    def get_score(self):
        return self.score

    def game_over(self):
        return self.round >= self.total_rounds