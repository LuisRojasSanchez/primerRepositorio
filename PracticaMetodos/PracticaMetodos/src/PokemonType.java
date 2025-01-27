public enum PokemonType {
    ELECTRIC("Electric", "#FFD700"),
    FIRE("Fire", "#FF4500"),
    WATER("Water", "#1E90FF"),
    GRASS("Grass", "#32CD32"),
    PSYCHIC("Psychic", "#FF1493"),
    ROCK("Rock", "#B8860B"),
    GROUND("Ground", "#DEB887"),
    FLYING("Flying", "#87CEEB"),
    ICE("Ice", "#00FFFF"),
    DRAGON("Dragon", "#9400D3"),
    DARK("Dark", "#4B0082"),
    STEEL("Steel", "#B0C4DE"),
    FAIRY("Fairy", "#FFB6C1");

    private final String name;
    private final String color;

    PokemonType(String name, String color) {
        this.name = name;
        this.color = color;
    }

    public String getName() {
        return name;
    }

    public String getColor() {
        return color;
    }

    @Override
    public String toString() {
        return name;
    }
}
