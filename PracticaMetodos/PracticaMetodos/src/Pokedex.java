import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Pokedex {
        private List<Pokemon> pokemons;

        public Pokedex() {
                // Inicializar la lista de Pokémon con algunos ejemplos
                this.pokemons = new ArrayList<>();
                initializePokemonList();
        }

        public List<Pokemon> getAllPokemons() {
                return pokemons;
        }

        private void initializePokemonList() {
                // Agregar Pokémon de ejemplo con sus detalles
                // Agregar los primeros 10 Pokémon con sus detalles
                pokemons.add(new Pokemon(
                                "Bulbasaur",
                                "Planta/Veneno",
                                "Bulbasaur es un Pokémon de aspecto de saurio con una planta que crece en su espalda. Es conocido por tener un carácter dócil y ser un gran compañero.",
                                Arrays.asList("Esencia de Vida", "Lanza Esferas"),
                                Arrays.asList("Sofoco"),
                                Arrays.asList("Fuego", "Hielo", "Psíquico"),
                                1,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\001.png",
                                1,
                                Arrays.asList("Ivysaur", "Venusaur")));

                pokemons.add(new Pokemon(
                                "Ivysaur",
                                "Planta/Veneno",
                                "Ivysaur es la evolución de Bulbasaur y ha crecido en tamaño y poder. La planta en su espalda florece cada vez más.",
                                Arrays.asList("Látigo Cepa", "Rayo Solar"),
                                Arrays.asList("Flor de Vida"),
                                Arrays.asList("Fuego", "Hielo", "Psíquico"),
                                16,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\002.png",
                                2,
                                Arrays.asList("Venusaur")));

                pokemons.add(new Pokemon(
                                "Venusaur",
                                "Planta/Veneno",
                                "Venusaur es la evolución final de Bulbasaur. Su gran flor en la espalda libera un aroma hipnotizante y puede usar poderosos ataques de planta.",
                                Arrays.asList("Rayo Solar", "Látigo Cepa"),
                                Arrays.asList("Flor de Vida"),
                                Arrays.asList("Fuego", "Hielo", "Psíquico"),
                                32,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\003.png",
                                3,
                                Arrays.asList()));

                pokemons.add(new Pokemon(
                                "Charmander",
                                "Fuego",
                                "Charmander es un pequeño lagarto con una llama en la punta de su cola, la cual representa su vitalidad.",
                                Arrays.asList("Espíritu de Lucha", "Mar Llama"),
                                Arrays.asList("Mar Llama"),
                                Arrays.asList("Agua", "Roca", "Tierra"),
                                5,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\004.png",
                                4,
                                Arrays.asList("Charmeleon", "Charizard")));

                pokemons.add(new Pokemon(
                                "Charmeleon",
                                "Fuego",
                                "Charmeleon es la evolución de Charmander. Es más fuerte y su llama se intensifica.",
                                Arrays.asList("Llamarada", "Puño Fuego"),
                                Arrays.asList("Llama Viva"),
                                Arrays.asList("Agua", "Roca", "Tierra"),
                                16,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\005.png",
                                5,
                                Arrays.asList("Charizard")));

                pokemons.add(new Pokemon(
                                "Charizard",
                                "Fuego/Volador",
                                "Charizard es la evolución final de Charmander. Es un Pokémon poderoso con alas de fuego.",
                                Arrays.asList("Vuelo", "Llama Infernal"),
                                Arrays.asList("Llama Solar"),
                                Arrays.asList("Agua", "Eléctrico", "Roca"),
                                36,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\006.png",
                                6,
                                Arrays.asList()));

                pokemons.add(new Pokemon(
                                "Squirtle",
                                "Agua",
                                "Squirtle es una tortuga pequeña y amigable con una coraza dura. Es conocido por ser valiente y tener un gran potencial en combate.",
                                Arrays.asList("Rayo Burbuja", "Chorro de Agua"),
                                Arrays.asList("Cascada"),
                                Arrays.asList("Eléctrico"),
                                7,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\007.png",
                                7,
                                Arrays.asList("Wartortle", "Blastoise")));

                pokemons.add(new Pokemon(
                                "Wartortle",
                                "Agua",
                                "Wartortle es la evolución de Squirtle. Tiene una gran coraza y una cola en forma de remolino. Es más rápido y ágil en combate.",
                                Arrays.asList("Hydro Pump", "Cascada"),
                                Arrays.asList("Tsunami"),
                                Arrays.asList("Eléctrico"),
                                16,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\008.png",
                                8,
                                Arrays.asList("Blastoise")));

                pokemons.add(new Pokemon(
                                "Blastoise",
                                "Agua",
                                "Blastoise es la evolución final de Squirtle. Sus cañones de agua en los hombros pueden disparar poderosos chorro de agua.",
                                Arrays.asList("Hydro Pump", "Aqua Jet"),
                                Arrays.asList("Tsunami"),
                                Arrays.asList("Eléctrico"),
                                36,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\009.png",
                                9,
                                Arrays.asList()));

                pokemons.add(new Pokemon(
                                "Pidgey",
                                "Normal/Volador",
                                "Pidgey es un pequeño pájaro de colores marrón y blanco. Es muy común y es conocido por ser uno de los Pokémon más ligeros.",
                                Arrays.asList("Golpe Aéreo", "Aliento"),
                                Arrays.asList("Ciclón"),
                                Arrays.asList("Eléctrico"),
                                10,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\016.png",
                                10,
                                Arrays.asList("Pidgeotto", "Pidgeot")));

                // Agregar los Pokémon 11 a 20 con sus detalles
                pokemons.add(new Pokemon(
                                "Pidgeotto",
                                "Normal/Volador",
                                "Pidgeotto es la evolución de Pidgey. Tiene un cuerpo más grande y es más fuerte, preparado para batallas aéreas.",
                                Arrays.asList("Ala de Acero", "Giro Aéreo"),
                                Arrays.asList("Torbellino"),
                                Arrays.asList("Eléctrico"),
                                36,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\017.png",
                                11,
                                Arrays.asList("Pidgeot")));

                pokemons.add(new Pokemon(
                                "Pidgeot",
                                "Normal/Volador",
                                "Pidgeot es la evolución final de Pidgey. Es un ave majestuosa con un poderoso vuelo y un plumaje impresionante.",
                                Arrays.asList("Sonic Boom", "Pico Taladro"),
                                Arrays.asList("Tornado"),
                                Arrays.asList("Eléctrico"),
                                36,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\018.png",
                                12,
                                Arrays.asList()));

                pokemons.add(new Pokemon(
                                "Rattata",
                                "Normal",
                                "Rattata es un ratón ágil y de pequeño tamaño que se adapta a vivir en lugares urbanos. Es conocido por su rapidez y sus dientes afilados.",
                                Arrays.asList("Mordisco", "Sorpresa"),
                                Arrays.asList("Ataque Sorpresa"),
                                Arrays.asList("Lucha"),
                                13,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\019.png",
                                13,
                                Arrays.asList("Raticate")));

                pokemons.add(new Pokemon(
                                "Raticate",
                                "Normal",
                                "Raticate es la evolución de Rattata y es mucho más grande y fuerte. Tiene un cuerpo robusto y un par de dientes afilados que le ayudan en combate.",
                                Arrays.asList("Mordisco", "Sofoco"),
                                Arrays.asList("Suerte de Raticate"),
                                Arrays.asList("Lucha"),
                                20,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\020.png",
                                14,
                                Arrays.asList()));

                pokemons.add(new Pokemon(
                                "Spearow",
                                "Normal/Volador",
                                "Spearow es un pequeño pájaro agresivo que se encuentra en los campos y bosques. Es conocido por su vuelo rápido y su actitud desafiante.",
                                Arrays.asList("Pico Taladro", "Ataque Aéreo"),
                                Arrays.asList("Pico Mortífero"),
                                Arrays.asList("Eléctrico"),
                                15,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\021.png",
                                15,
                                Arrays.asList("Fearow")));

                pokemons.add(new Pokemon(
                                "Fearow",
                                "Normal/Volador",
                                "Fearow es la evolución de Spearow y es más grande, más rápido y más poderoso. Su agudo sentido de la vista le permite detectar presas desde el aire.",
                                Arrays.asList("Picotazo", "Sombra de Vuelo"),
                                Arrays.asList("Ala de Acero"),
                                Arrays.asList("Eléctrico"),
                                20,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\022.png",
                                16,
                                Arrays.asList()));

                pokemons.add(new Pokemon(
                                "Ekans",
                                "Veneno",
                                "Ekans es una serpiente venenosa que se enrosca y se desplaza rápidamente. Es conocida por su habilidad de camuflaje y su ataque venenoso.",
                                Arrays.asList("Mordisco", "Veneno Denso"),
                                Arrays.asList("Corte Veneno"),
                                Arrays.asList("Tierra", "Psíquico"),
                                17,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\023.png",
                                17,
                                Arrays.asList("Arbok")));

                pokemons.add(new Pokemon(
                                "Arbok",
                                "Veneno",
                                "Arbok es la evolución de Ekans. Es más grande y peligroso, y sus movimientos pueden envenenar a sus enemigos con facilidad.",
                                Arrays.asList("Mordisco Venenoso", "Sofoco"),
                                Arrays.asList("Veneno Final"),
                                Arrays.asList("Tierra", "Psíquico"),
                                25,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\024.png",
                                18,
                                Arrays.asList()));

                pokemons.add(new Pokemon(
                                "Pikachu",
                                "Eléctrico",
                                "Pikachu es un Pokémon de tipo eléctrico muy popular. Es conocido por su energía positiva y su habilidad para generar electricidad.",
                                Arrays.asList("Impactrueno", "Rayo"),
                                Arrays.asList("Trueno Relámpago"),
                                Arrays.asList("Tierra"),
                                19,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\025.png",
                                19,
                                Arrays.asList("Raichu")));

                pokemons.add(new Pokemon(
                                "Raichu",
                                "Eléctrico",
                                "Raichu es la evolución de Pikachu. Es más rápido y su habilidad eléctrica es más potente, lo que le permite usar ataques devastadores.",
                                Arrays.asList("Rayo", "Trueno"),
                                Arrays.asList("Tormenta Eléctrica"),
                                Arrays.asList("Tierra"),
                                30,
                                "Kanto",
                                "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\026.png",
                                20,
                                Arrays.asList()));

                // Agregar más Pokémon si es necesario...
        }
}
