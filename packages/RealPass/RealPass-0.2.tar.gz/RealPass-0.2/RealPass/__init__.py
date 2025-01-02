import random
import numpy as np
from typing import Literal, Tuple, Union

class BasicSecurity:
    style_list=['AlphaNumeric', 'Alpha', 'Numeric']
    fruits = np.array([
        ["apple", "apricot", "avocado", "banana", "blackberry", "blackcurrant", "blueberry", 
        "cantaloupe", "cherry", "clementine", "coconut", "cranberry", "currant", "date", 
        "dragonfruit", "elderberry", "feijoa", "fig", "grape", "grapefruit", "guava", "honeydew", 
        "jackfruit", "jambolan", "jasmine", "kiwi", "kumquat", "lemon", "lime", "lychee", 
        "mandarin", "mango", "mulberry", "nectarine", "orange", "papaya", "passionfruit", "peach", 
        "pear", "persimmon", "pineapple", "plum", "pomegranate", "prickly pear", "raspberry", 
        "red currant", "starfruit", "strawberry", "tangerine", "watermelon", "acai", "allspice", 
        "almond", "amaranth", "anise", "apple pear", "apricot", "arrowroot", "artichoke", 
        "asparagus", "aubergine", "balsam apple", "banana apple", "bitter melon", "black salsify", 
        "bok choy", "broad bean", "brussels sprout", "butternut squash", "cabbage", "carrot", 
        "cauliflower", "celeriac", "chard", "chayote", "chicory", "chili pepper", "chinese cabbage", 
        "chives", "coriander", "cress", "cucumber", "dandelion greens", "dandelion root", 
        "daikon radish", "endive", "fennel", "fennel bulb", "fenugreek", "garlic", "ginger", 
        "horseradish", "jalapeno", "kale", "kohlrabi", "leek", "lettuce", "mango", "mustard greens", 
        "okra", "olive", "onion", "oregano", "paprika", "parsnip", "pea", "potato", "pumpkin", 
        "radish", "rhubarb", "rosemary", "sage", "scallion", "shallot", "spinach", "squash", 
        "sweet potato", "tarragon", "thyme", "tomato", "turnip", "yam", "zucchini", "acorn squash", 
        "arugula", "aubergine", "avocado pear", "bamboo shoot", "basil", "beetroot", "bitter gourd", 
        "bok choy", "broccoli", "brussels sprouts", "butternut squash", "cabbage", "carrot", 
        "cauliflower", "celeriac", "chayote", "chili pepper", "chinese cabbage", "chives", "coriander", 
        "cress", "cucumber", "dandelion greens", "daikon radish", "endive", "fennel", "fenugreek", 
        "garlic", "ginger", "horseradish", "jalapeno", "kale", "kohlrabi", "leek", "lettuce", 
        "mango", "mustard greens", "okra", "olive", "onion", "oregano", "paprika", "parsnip", 
        "pea", "potato", "pumpkin", "radish", "rhubarb", "rosemary", "sage", "scallion", "shallot", 
        "spinach", "squash", "sweet potato", "tarragon", "thyme", "tomato", "turnip", "yam", "zucchini", 
        "amaranth", "apple", "apricot", "avocado", "banana", "blackberry", "blackcurrant", "blueberry", 
        "cantaloupe", "cherry", "clementine", "coconut", "cranberry", "currant", "date", "dragonfruit", 
        "elderberry", "feijoa", "fig", "grape", "grapefruit", "guava", "honeydew", "jackfruit", 
        "jambolan", "jasmine", "kiwi", "kumquat", "lemon", "lime", "lychee", "mandarin", "mango", 
        "mulberry", "nectarine", "orange", "papaya", "passionfruit", "peach", "pear", "persimmon", 
        "pineapple", "plum", "pomegranate", "prickly pear", "raspberry", "red currant", "starfruit", 
        "strawberry", "tangerine", "watermelon", "zinfandel grape", "berries", "citrus", "melons", "tropical fruits",
        "ackee", "acorn squash", "african horned cucumber", "almond", "ambarella", "american persimmon", 
        "applesauce fruit", "apples", "australian finger lime", "autumn olive", "banana passionfruit", 
        "baobab fruit", "barbadine", "barberry", "bayberry", "ber", "bilberry", "bitter orange", "black cherry", 
        "black figs", "black persimmon", "black sapote", "blue java banana", "bocadillo", "bok choi", "bolivian peach", 
        "bottle gourd", "breadfruit", "brazil nut", "buddha's hand", "buffalo gourd", "burdock", "cabelluda", 
        "calamansi", "candied citron", "canistel", "capulin cherry", "cardamom", "carob", "chayote squash", "che", 
        "cherry plum", "cherry tomato", "chilean guava", "clementine mandarin", "cloudberry", "coco plum", 
        "cocoanut", "colocasia", "common fig", "cornelian cherry", "cranapple", "creeping raspberry", "cucumber melon", 
        "custard apple", "damson plum", "dawn redwood", "dewberry", "durian", "eastern redbud", "elderflower", 
        "empress plum", "feather cactus", "fennel bulb", "finger lime", "fuzzy kiwi", "gean cherry", "gala apple", 
        "galapagos tomato", "gambooge", "gaya fruit", "goya", "grape cherry", "grape hyacinth", "grapefruit", 
        "grewia", "guarana", "gull leaf", "hackberry", "hardy kiwi", "hops", "huckleberry", "ice cream bean", 
        "indian fig", "jelly palm", "jew's mallow", "jicama", "juneberry", "kiwano", "korlan", "kumquat", 
        "laburnum", "lansones", "lemon aspen", "lemonade fruit", "longan", "loquat", "lucuma", "lychee", 
        "mandala fruit", "mangaba", "mangosteen", "maui tangelo", "melinjo", "melon pear", "mesquite", "mimosa", 
        "mirabelle", "monstera", "mulberry", "muscadine", "nance", "naranjilla", "nashi pear", "natal plum", 
        "olive oil fruit", "opuntia", "orange", "otahuti", "passionfruit", "peach apple", "peanut", "pear",
        "pecan", "peppercorn", "persimmon", "pineapple guava", "pineberry", "plumcot", "plum", "pluerry", 
        "pomegranate", "popcorn plant", "prickly pear", "pulasan", "quince", "raisin", "rambutan", "red banana", 
        "red pear", "rosemaling", "ruby grape", "sacha inchi", "salak", "satsuma", "soursop", "sugar apple", 
        "sweet lime", "tamarillo", "tamarind", "tangor", "tangerine", "thai lychee", "thimbleberry", 
        "thornless blackberry", "thunder fruit", "tree tomato", "true mango", "tulip tree", "water apple", 
        "water chestnut", "wax jambu", "wild apple", "wild cherry", "wild plum", "yali pear", "yellow mombin", 
        "yellow watermelon", "zante currant", "zapote", "ziziphus"]
    ])
    flowers = np.array([
        ["acacia", "african daisy", "alstroemeria", "amaryllis", "anemone", "angelonia", "aster", 
        "azalea", "begonia", "bluebell", "bougainvillea", "bromeliad", "buttercup", "cala lily", 
        "camellia", "canna", "carnation", "cherry blossom", "chrysanthemum", "clover", "crocus", 
        "daffodil", "dahlia", "daisy", "freesia", "gardenia", "geranium", "ginger lily", "gladiolus", 
        "gloxinia", "hibiscus", "hollyhock", "hydrangea", "impatiens", "iris", "jasmine", "jewel orchid", 
        "lavender", "lily", "lupine", "magnolia", "marigold", "orchid", "pansy", "peony", "petunia", 
        "phlox", "plumeria", "primrose", "roses", "snapdragon", "sunflower", "sweet pea", "tulip", 
        "verbena", "violet", "wisteria", "zinnia", "acacia", "allium", "aster", "bellflower", "bird of paradise", 
        "bouvardia", "butterfly bush", "california poppy", "campanula", "cineraria", "clematis", "columbine", 
        "coneflower", "coreopsis", "coral vine", "cow parsnip", "cyclamen", "daffodil", "dahlia", 
        "delphinium", "dogwood", "fuchsia", "gerbera", "hebe", "hoya", "impatiens", "indigo", "jacaranda", 
        "jasmine", "lilac", "lupine", "maranta", "mimosa", "monarda", "orange blossom", "petunia", 
        "plumeria", "poinsettia", "quince", "rhododendron", "rosemary", "saffron", "sunflower", 
        "sweet william", "tiger lily", "tulip", "violet", "water lily", "yellow bells", "zinnia", 
        "azalea", "butterfly bush", "calendula", "canna lily", "celosia", "cherry blossom", "cineraria", 
        "corydalis", "cress", "daffodil", "daisy", "dandelion", "echinacea", "elephant ear", "fuchsia", 
        "geranium", "globe thistle", "gloxinia", "helenium", "hibiscus", "hollyhock", "honeysuckle", 
        "jasmine", "lupine", "marigold", "mimosa", "musk rose", "orchid", "pansy", "peony", "petunia", 
        "plumeria", "poppy", "ranunculus", "rose", "saffron", "snowdrop", "squill", "sunflower", 
        "tulip", "violet", "wisteria", "wild ginger", "zinnia"]
    ])

    animals = np.array([
        ["aardvark", "alpaca", "ant", "anteater", "armadillo", "asian elephant", "baboon", "badger", 
        "bald eagle", "bandicoot", "bat", "bear", "beaver", "bee", "bison", "booby", "buffalo", 
        "bull", "bunny", "butterfly", "camel", "canary", "capybara", "caribou", "cat", "caterpillar", 
        "cattle", "cheetah", "chicken", "chimpanzee", "chinchilla", "chipmunk", "clam", "cobra", 
        "cockroach", "cod", "cow", "coyote", "crab", "crane", "crow", "crocodile", "crow", "deer", 
        "dingo", "dog", "dolphin", "donkey", "dragonfly", "duck", "eagle", "elephant", "elk", 
        "emu", "falcon", "ferret", "fish", "flamingo", "fox", "frog", "gazelle", "giraffe", "goat", 
        "goose", "gorilla", "guinea pig", "hawk", "hedgehog", "heron", "hippopotamus", "horse", 
        "housefly", "human", "hyena", "ibex", "iguana", "impala", "jaguar", "jellyfish", "kangaroo", 
        "koala", "komodo dragon", "kookaburra", "lamb", "leopard", "lion", "lizard", "llama", 
        "lobster", "locust", "lynx", "manatee", "mandrill", "mole", "mongoose", "monkey", "moose", 
        "mouse", "octopus", "orangutan", "ostrich", "otter", "owl", "ox", "panda", "parrot", 
        "partridge", "peacock", "pelican", "penguin", "pig", "pigeon", "polar bear", "porcupine", 
        "rabbit", "raccoon", "rat", "raven", "reindeer", "rhinoceros", "rooster", "salamander", 
        "scorpion", "seahorse", "seal", "shark", "sheep", "shrimp", "skunk", "slug", "snake", 
        "spider", "squid", "squirrel", "starfish", "stoat", "swallow", "swan", "tapir", 
        "tarantula", "toad", "tortoise", "toucan", "tuna", "turkey", "turtle", "vulture", 
        "wallaby", "walrus", "warthog", "wasp", "weasel", "whale", "wild boar", "wolf", "wombat", "zebra"]
    ])
    movies = np.array([
        ["avatar", "avengers: endgame", "the dark knight", "inception", "fight club", "the godfather", 
        "pulp fiction", "the shawshank redemption", "the matrix", "forrest gump", "the lion king", 
        "star wars: a new hope", "the empire strikes back", "the return of the king", "joker", "gladiator", 
        "the godfather: part ii", "goodfellas", "schindler's list", "the silence of the lambs", "citizen kane", 
        "the dark knight rises", "star wars: the force awakens", "star wars: the last jedi", "the avengers", 
        "mad max: fury road", "interstellar", "titanic", "the princess bride", "the departed", "the social network", 
        "the wolf of wall street", "whiplash", "the big lebowski", "american beauty", "reservoir dogs", 
        "the usual suspects", "the shining", "fight club", "jaws", "casablanca", "the godfather: part iii", 
        "die hard", "jurassic park", "back to the future", "the breakfast club", "e.t. the extra-terrestrial", 
        "goodfellas", "the lion king", "scream", "harry potter and the sorcerer's stone", "harry potter and the chamber of secrets", 
        "harry potter and the prisoner of azkaban", "the matrix revolutions", "dunkirk", "moonlight", "la la land", 
        "blade runner", "the princess bride", "the grand budapest hotel", "eternal sunshine of the spotless mind", 
        "the curious case of benjamin button", "the dark knight", "once upon a time in hollywood", "fargo", "goodfellas", 
        "eternal sunshine of the spotless mind", "the pursuit of happiness", "the big short", "memento", "inception", 
        "the revenant", "her", "gladiator", "a clockwork orange", "the great gatsby", "inglourious basterds", 
        "the shape of water", "12 angry men", "american history x", "whiplash", "pulp fiction", "the princess bride", 
        "the notebook", "the sound of music", "the wizard of oz", "the martian", "crazy rich asians", "kingsman: the secret service", 
        "the hunger games", "scarface", "the shining", "the godfather", "batman begins", "captain america: the first avenger", 
        "x-men", "iron man", "the incredible hulk", "thor", "spider-man", "black panther", "guardians of the galaxy", 
        "wonder woman", "man of steel", "justice league", "avengers: infinity war", "avengers: age of ultron", "the avengers"]
    ])
    celebrities = np.array([
        ["adam sandler", "angelina jolie", "brad pitt", "beyoncé", "bill gates", "blake lively", "bradley cooper", 
        "britney spears", "charlize theron", "chris hemsworth", "chris pratt", "chris rock", "claire danes", 
        "cameron diaz", "cate blanchett", "channing tatum", "colin farrell", "dwayne johnson", "emma stone", 
        "ellen degeneres", "elizabeth taylor", "george clooney", "gisele bündchen", "helen mirren", "hugh jackman", 
        "jacob elordi", "jared leto", "jennifer aniston", "jennifer lopez", "julia roberts", "kate hudson", 
        "katy perry", "kevin hart", "leonardo dicaprio", "lupita nyong'o", "madonna", "matthew mcconaughey", 
        "megan fox", "meryl streep", "michael jackson", "miley cyrus", "morgan freeman", "nicole kidman", 
        "orlando bloom", "oscar isaac", "reese witherspoon", "robert downey jr.", "ryan gosling", "ryan reynolds", 
        "sandra bullock", "scarlett johansson", "selena gomez", "serena williams", "shakira", "sophia vergara", 
        "tom cruise", "tom hanks", "taylor swift", "the rock", "will smith", "will ferrell", "zoe saldana", 
        "zac efron", "al pacino", "angela bassett", "ben affleck", "beyoncé", "brad pitt", "cameron diaz", 
        "carrie underwood", "charlize theron", "chris evans", "chris hemsworth", "chris pratt", "claire danes", 
        "colin farrell", "dwayne johnson", "ellen degeneres", "emily blunt", "emma stone", "george clooney", 
        "gisele bündchen", "hugh jackman", "jake gyllenhaal", "jared leto", "jennifer aniston", "jennifer lopez", 
        "johnny depp", "kate winslet", "kendall jenner", "kerry washington", "kim kardashian", "kristen bell", 
        "leonardo dicaprio", "lucy liu", "matthew mcconaughey", "miley cyrus", "naomi watts", "olivia wilde", 
        "oprah winfrey", "penélope cruz", "reese witherspoon", "robert downey jr.", "ryan gosling", "ryan reynolds", 
        "sandra bullock", "scarlett johansson", "selena gomez", "shakira", "taylor swift", "tom hanks", "tom cruise"]
    ])
    anime_characters = np.array([
        ["naruto uzumaki", "sasuke uchiha", "sakura haruno", "kakashi hatake", "iruka umino", 
        "shikamaru nara", "temari", "neji hyuga", "hinata hyuga", "rock lee", 
        "matthew crawley", "sai", "jiraiya", "pain", "konan", "tobi", "minato namikaze", 
        "itachi uchiha", "kaguya otsutsuki", "obito uchiha", "madara uchiha", "kaguya otsutsuki", 
        "monkey d. luffy", "roronoa zoro", "nami", "usopp", "sanji", "tony tony chopper", 
        "nico robin", "franky", "brook", "jimbei", "portgas d. ace", "trafalgar d. water law", 
        "shanks", "bartholomew kuma", "sabo", "eustass kid", "hawkins", "fujitora", "doflamingo", 
        "kaido", "big mom", "blackbeard", "buggy the clown", "kizaru", "akainu", "zoro", "big mom", 
        "luffy", "reigen arataka", "mob", "shigeo kageyama", "teruki suwen", "tomekichi", "akihiro",
        "koyomi araragi", "hitagi senjougahara", "meme oshino", "swordfish", "aruka", "saber", 
        "rin tohsaka", "shiro emiya", "sakura matou", "kurumi tokisaki", "miku nakano", "nino nakano",
        "ichiha sasuke", "tetsuya kuroko", "ryouta kise", "taiga aisaka", "yuki nagato", "haruhi suzumiya",
        "kyo sohma", "shigure sohma", "yuki sohma", "shun", "mitsuki", "karen araragi", "hyouka", "ecchi",
        "takamatsu", "kemono", "tomoya okazaki", "kotomi ichinose", "nagisa furukawa", "yukino yukinoshita", 
        "shiro", "iruka umino", "hikigaya hachiman", "bunny", "yui", "mikasa ackerman", "eren jaeger",
        "armin arlert", "levi ackerman", "jean kirstein", "sasha blause", "connie springer", "annie leonhart",
        "bertholdt", "reiner braun", "hange zoe", "erwin smith", "mikasa ackerman", "rikka takanashi", 
        "shiro", "danganronpa", "charlotte", "touka kirishima", "kaneki ken", "toka kirishima", "maki", 
        "goku", "vegeta", "piccolo", "krillin", "bulma", "trunks", "majin buu", "frieza", "cell", "android 18",
        "broly", "kail", "tien", "yamcha", "chi-chi", "pan", "goku black", "zamasu", "jiren", "hit",
        "nozel", "yuno", "finral", "asta", "yuji itadori", "megumi fushiguro", "nobara kugisaki", "satoru gojo", 
        "yuta okkotsu", "mahito", "sukuna", "ryomen sukuna", "kamiya", "toji fushiguro", "yuji itadori", 
        "nanami kento", "shoko ieiri", "kento nanami", "maki zenin", "todos", "ryuji sakamoto", "asuka langley", 
        "shinji ikari", "rei ayanami", "gendo ikari", "misato katsuragi", "asuka langley", "kaoru nagisa", 
        "armageddon", "nina", "shinji", "nagisa shiota", "koro-sensei", "tadaomi kyogoku", "ozaki", "hanekawa",
        "hestia", "bell cranel", "aisu", "arlecchino", "meliodas", "escanor", "merlin", "ban", "king", "diane",
        "julius novachrono", "yami sukihira", "sally", "hasoka", "zoro", "chopper", "tetsuo", "goku", "allen walker",
        "kurapika", "gon freecss", "killua zoldyck", "leorio", "huge", "illumi", "knuckle", "knov", "silva",
        "kyogre", "ash ketchum", "misty", "brock", "pikachu", "serena", "chloe", "iris", "dawn", "may",
        "bulbasaur", "charizard", "squirtle", "sheldon", "team rocket", "rattata", "eevee", "snorlax",
        "electrode", "magnemite", "jigglypuff", "rapidash", "taillow", "zubat", "mawile", "lucario", "gengar",
        "machamp", "sableye", "combusken", "swampert", "seaking", "shiny", "raichu", "bulbasaur", "bruno", "claudia",
        "zeref", "akuma", "chika fujiwara", "shiro", "miyuki shirogane", "kaguya shinomiya", "kyouya mitsuboshi",
        "ishigami yu", "izumi saionji", "suzuya", "rika", "alice", "reigen arataka", "kageyama", "yuri katsuki",
        "victor nikiforov", "yuuri katsuki", "yuri", "nonon jakuzure", "makunouchi ippo", "takumi", "renji",
        "shinra kusakabe", "shinra", "maki"]  
    ])
    
    gaming_ids = np.array([
        ["shadowstrike", "nightshade", "blazeclaw", "phantomx", "stormrider", "darkninja", "frostbite", 
        "vortexviper", "cyberwolf", "soulcrusher", "ghostblade", "ironfist", "silentshadow", "flamefang", 
        "deathbringer", "shadowfury", "skybreaker", "stormhawk", "viperstrike", "dragonflare", 
        "nightwhisper", "thunderclash", "voidslinger", "reaperx", "blazeheart", "stealthstrike", 
        "warhammer", "ironclad", "moonshadow", "nightprowler", "stormrage", "viperclaw", "redhawk", 
        "cyberstorm", "shadowfire", "phantomstrike", "crimsonrage", "silverblade", "thunderstrike", 
        "deadshot", "ravenspirit", "blackthorn", "icephoenix", "darkfire", "deathknight", "skyhunter", 
        "xenonblade", "shadowhunter", "stealthwarrior", "bloodreaper", "flamecaster", "blackstorm", 
        "frostwolf", "phantomreaper", "midnightrider", "stormbringer", "darkangel", "moonblade", 
        "blazemaster", "steelfang", "ragingbull", "ironviper", "thunderwolf", "nightshade", "blazeheart", 
        "shadowforce", "galehunter", "firestrike", "wildfire", "frostbite", "dragonslayer", "nightmarex", 
        "reapersoul", "cyberclaw", "soulfire", "thunderfury", "flamethrower", "earthshaker", "soulstorm", 
        "ironblade", "shadowmancer", "blitzkrieg", "snowstorm", "flamefury", "eclipseblade", "bloodfang", 
        "stormrider", "phantomghost", "nightfury", "clashbringer", "raijun", "blademaster", "blackdragon", 
        "spartanx", "deathflare", "viperx", "stormbringer", "maverickx", "silverwolf", "goldenphoenix", 
        "infernohawk", "skyshatter", "venomstrike", "stormdragon", "crimsonblaze", "ghostrider", "soulstrike", 
        "cybershadow", "moonflare", "shadowviper", "mysticdragon", "icefang", "flameburst", "swiftblade", 
        "lightningstorm", "ironwolf", "shadowfury", "deathstorm", "moonfire", "dragonsoul", "soulshatter", 
        "neonflame", "nightstorm", "vortexfury", "bloodhunter", "bloodraven", "hellstorm", "blazeclaw", 
        "darkreaper", "doomblade", "stealthstorm", "darkphoenix", "flamestorm", "silentreaper", 
        "viperfang", "phoenixsoul", "shadowflare", "stormwraith", "reapershadow", "thunderclaw", "blackfire", 
        "frostshade", "warlockx", "thunderfury", "voidreaper", "deathblaze", "stormstrike", "bloodvenom", 
        "shadowraider", "frostphoenix", "nightblade", "blazingshadow", "darkblade", "starlightstorm", 
        "frostfang", "ironstorm", "skyshadow", "bloodthirst", "warstorm", "iceclaw", "flamereaper", 
        "shadowmist", "lightbringer", "darkphoenix", "dreadstorm", "mysticshadow", "blazeveil", "nightshade", 
        "whiteshadow", "thunderstorm", "ironfury", "flameprince", "silentblade", "neonshadow", "vortexflame", 
        "goldenglow", "darkwhisper", "flamethunder", "vortexwarrior", "nightprince", "darkangelx", 
        "firestorm", "roguemaster", "ghostflame", "neonreaper", "stormrage", "bloodstorm", "stormblade", 
        "icefire", "darkstorm", "tigerclaw", "deathstrike", "frostclaw", "flamehunter", "shadowfang", 
        "dragonheart", "nightstorm", "warstorm", "ironshadow", "stormchaser", "lightstrike", "blademaster", 
        "dragonstrike", "phantomnight", "venomshade", "flameclash", "shadowpunch", "icefury", "soulhunter", 
        "nightfang", "frostbite", "cyberwarrior", "blazeaxe", "nightstrike", "stormbringer", "dragontamer", 
        "crimsonshadow", "shadowfire", "bloodshadow", "firehawk", "steelstorm", "nightwraith", "stormguard", 
        "wildstrike", "venomrider", "fireclaw", "moonfire", "shadowstrike", "sunflare", "vortexstrike", 
        "shadowflame", "dragonsoul", "bloodflare", "lightningblade", "tigerstorm", "venomstrike", "soulflare",
        "thunderwhisper", "necroticstorm", "pyroclash", "voidreaperx", "lucidflare", "darkvortex", "stealthblade",
        "thunderflare", "roguereaper", "darkstormx", "venomstrike", "redstorm", "blazingsun", "thundersoul",
        "flamerealm", "icyblaze", "smokephantom", "redphoenix", "duskflame", "nightdeath", "vortexvenom", 
        "goldenghost", "silentfury", "voidstrike", "ravenviper", "infinityblaze", "spiritualflame", 
        "frostshadow", "typhoonrider", "flameviper", "stormragex", "nightslayer", "deathclaw", "silentfang", 
        "thunderbolt", "stormshield", "blazedancer", "phantomghost", "moonhunter", "shadowwhisper", 
        "phoenixfire", "darkfang", "mysticshadow", "ironwhisper", "shadowphantom", "thunderstrikex", 
        "stormbringerx", "ragingflame", "coldblaze", "starphoenix", "icevenom", "moonfury", "silentreaper", 
        "shadowhunterx", "blazecreek", "voidblaze", "viperwolf", "frostraider", "soulseeker", "nightfall", 
        "lightningfang", "froststrike", "crimsonshade", "darkchaser", "firewarrior", "shadowseer", "cloudflare", 
        "phantomsoul", "redfang", "shadowstrikex", "cloudrider", "deathpunch", "windbreaker", "nightstrikex", 
        "vortexkiller", "icyclash", "soulflarex", "ironreaper", "blazehunter", "darkclash", "stormhunter", 
        "thunderflame", "nightsworn", "flamestrike", "venomstorm", "darkreign", "lightshadow", "frostwraith", 
        "galeclash", "dragonscorch", "hellfire", "stormsoul", "flamefuryx", "voidflame", "thunderdance", 
        "firewraith", "flameseeker", "moonvenom", "nightflare", "phantomclaw", "stormwrath", "lightbringerx", 
        "shadowblaze", "soulcrush", "thunderstrikez", "venomburn", "crimsonpunch", "darkvenom", "soulburner", 
        "lightningwing", "flamereaver", "nightshard", "vortexcurse", "phantomstorm", "blazeflare", "ironshadowx",
        "shadowfangx", "darkwarrior", "flameblood", "lightningwhisper", "icephoton", "soulwarrior", "nightfangx",
        "stormstrikez", "cyberblaze", "soulphantom", "frostflame", "darklight", "shadowflair", "venomstrikez", 
        "lightningprince", "silentfuryx", "blazevenom", "vortexflame", "fireangel", "soulphoenix", "icyreaper", 
        "dragonslash", "shadowwhisperx", "nightstormx", "lightningblaze", "phantomclash", "nightflarex", 
        "stormbreak", "darkstrike", "crimsonflame", "bloodflame", "icystrike", "stormflare", "redflame", 
        "thunderstrikez", "ghostflame", "darkphoenixx", "soulstrikez", "blazeclash", "thundergale", "shadowphantomx"]
    ])
    numeric=list('1234567890')
    special_char=list("~`!@#$%^&*.")
    style_default=('Alpha',0)
    premods_default='Gaming_ID'
    def __init__(self, password_lenght_limit: Tuple[int, int], style: Union[Tuple[Literal['AlphaNumeric', 'Alpha', 'Numeric'], int], None] = None, special_chars: bool = False, premods: Literal['Fruits','Vegetables','Flowers','Animals','Movies','Celebrities','Anime_Characters','Gaming_ID'] = None):
        self.premods = premods
        self.premods_default = premods if premods is not None else self.premods_default  # Default premod if None is provided
        self.style_default = style if style is not None else self.style_default
        
        self.classifier={'Fruits':self.fruits,'Flowers':self.flowers,'Animals':self.animals,'Movies':self.movies,
                         'Celebrities':self.celebrities,'Anime_Characters':self.anime_characters,'Gaming_ID':self.gaming_ids}
        
        self.temp_password_container=[]
        # Validate the password length limit (min, max)
        if isinstance(password_lenght_limit, tuple) and len(password_lenght_limit) == 2 and password_lenght_limit[1]-password_lenght_limit[0]>=4:
            if special_chars is False:
                # print('Special characters not allowed.')
                # print(self.style_default)
                # print(self.premods_default)
                
                if isinstance(self.style_default, tuple) and isinstance(self.style_default[1],int) and len(self.style_default)==2:
                    if self.style_default[0].lower() == 'alphanumeric':
                        self.min=password_lenght_limit[0]
                        self.max= password_lenght_limit[1]
                        self.num=self.style_default[1]
                        
                        if self.max-self.min <= self.num  :
                            raise ValueError(f"Length of the digits can't be more than or equal to password lenght,here password length: {self.max-self.min} and digit length: {self.num}")

                        elif self.num == 0:
                            self.password_list=self.classifier.get(self.premods_default)        
                            for self.row in self.password_list:
                                for self.value in self.row:
                                    # print(self.value)
                                    if len(self.value)>=password_lenght_limit[0] and len(self.value)<=password_lenght_limit[1]:
                                        self.temp_password_container.append(self.value)
                            self.got_password= random.choice(self.temp_password_container)
                        else:
                            self.pre_num=random.choices(self.numeric, k=self.num)
                            self.end_val=self.max - self.num
                            self.password_list=self.classifier.get(self.premods_default)        
                            for self.row in self.password_list:
                                for self.value in self.row:
                                    # print(self.value)
                                    if len(self.value)>=password_lenght_limit[0] and len(self.value)<=password_lenght_limit[1]:
                                        self.temp_password_container.append(self.value)
                            try:       
                                self.pre_password = random.choice(self.temp_password_container)
                                self.final_password = self.pre_password[0:self.end_val] + ''.join(self.pre_num)
                                self.got_password= self.final_password
                            except IndexError:
                                print("Can't generate password! Minimize the minimum lenght or try diffrent premods>>")
                                self.got_password=None
                            
                        
                        # print(self.style_default[0],'10000')
                    elif self.style_default[0].lower() == 'alpha':
                        self.password_list=self.classifier.get(self.premods_default)        
                        for self.row in self.password_list:
                            for self.value in self.row:
                                # print(self.value)
                                if len(self.value)>=password_lenght_limit[0] and len(self.value)<=password_lenght_limit[1]:
                                    self.temp_password_container.append(self.value)
                        try:            
                            self.got_password= random.choice(self.temp_password_container)
                        except IndexError:
                            print("Can't generate password! Minimize the minimum lenght or try diffrent premods>>")
                            self.got_password=None
                    elif self.style_default[0].lower() == 'numeric':
                        self.pre_num_pass=random.choices(self.numeric, k=self.style_default[1])
                        self.got_password= ''.join(self.pre_num_pass)
                        # print(self.style_default[0])
                    else:
                        raise ValueError("No such option available!---->",self.style_default[0])
                else:
                    raise ValueError("'Style' accepts a tuple in the format: ('AlphaNumeric' or 'Alpha' or 'Numeric', digits lenght(int))")
            else:
                # print('Special characters allowed.')
                # print(self.style_default)
                # print(self.premods_default)
                if isinstance(self.style_default, tuple) and isinstance(self.style_default[1],int) and len(self.style_default)==2:
                    if self.style_default[0].lower() == 'alphanumeric':
                        self.min=password_lenght_limit[0]
                        self.max= password_lenght_limit[1]
                        self.num=self.style_default[1]
                        
                        if self.max-self.min <= self.num  :
                            raise ValueError(f"Length of the digits can't be more than or equal to password lenght,here password length: {self.max-self.min} and digit length: {self.num}")

                        elif self.num == 0:
                            self.password_list=self.classifier.get(self.premods_default)        
                            for self.row in self.password_list:
                                for self.value in self.row:
                                    # print(self.value)
                                    if len(self.value)>=password_lenght_limit[0] and len(self.value)<=password_lenght_limit[1]:
                                        self.temp_password_container.append(self.value)
                            self.got_password= random.choice(self.temp_password_container)+random.choice(self.special_char)
                        else:
                            self.pre_num=random.choices(self.numeric, k=self.num)
                            self.end_val=self.max - self.num
                            self.password_list=self.classifier.get(self.premods_default)        
                            for self.row in self.password_list:
                                for self.value in self.row:
                                    # print(self.value)
                                    if len(self.value)>=password_lenght_limit[0] and len(self.value)<=password_lenght_limit[1]:
                                        self.temp_password_container.append(self.value)
                            try:
                                self.pre_password = random.choice(self.temp_password_container)
                                self.final_password = self.pre_password[0:self.end_val] + ''.join(self.pre_num)
                            
                                self.got_password= self.final_password+random.choice(self.special_char)
                            except IndexError:
                                print("Can't generate password! Minimize the minimum lenght or try diffrent premods>>")
                                self.got_password=None
                            
                        
                        # print(self.style_default[0],'10000')
                    elif self.style_default[0].lower() == 'alpha':
                        self.password_list=self.classifier.get(self.premods_default)        
                        for self.row in self.password_list:
                            for self.value in self.row:
                                # print(self.value)
                                if len(self.value)>=password_lenght_limit[0] and len(self.value)<=password_lenght_limit[1]:
                                    self.temp_password_container.append(self.value)
                        try:
                            self.got_password= random.choice(self.temp_password_container)+random.choice(self.special_char)
                        except IndexError:
                            print("Can't generate password! Minimize the minimum lenght or try diffrent premods>>")
                            self.got_password=None
                        
                    elif self.style_default[0].lower() == 'numeric':
                        self.pre_num_pass=random.choices(self.numeric, k=self.style_default[1])
                        self.got_password=''.join(self.pre_num_pass)+random.choice(self.special_char)
                        # print(self.style_default[0])
                    else:
                        raise ValueError("No such option available!--->",self.style_default[0])
                else:
                    raise ValueError("'Style' accepts a tuple in the format: ('AlphaNumeric' or 'Alpha' or 'Numeric', digits lenght(int))")
        else:
            raise ValueError("'password_lenght_limit' accepts a tuple in the format: (min, max) with minimum lenght of 4")
        
    def get_password(self):
        return self.got_password