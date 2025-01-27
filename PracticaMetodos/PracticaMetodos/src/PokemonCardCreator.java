import javax.swing.*;
import java.awt.*;
import java.util.List;

public class PokemonCardCreator {
        public static JButton createPokemonCard(Pokemon pokemon, JLabel pokemonImageLabel, JTextArea pokemonInfoArea,
                        JPanel evolutionPanel, List<Pokemon> pokemons) {
                JButton card = new JButton();
                card.setLayout(new BorderLayout());
                card.setPreferredSize(new Dimension(200, 300)); // Tamaño fijo

                // Imagen del Pokémon
                ImageIcon icon = new ImageIcon(pokemon.getImagen());
                Image scaledImage = icon.getImage().getScaledInstance(150, 200, Image.SCALE_SMOOTH);
                JLabel imageLabel = new JLabel(new ImageIcon(scaledImage));
                card.add(imageLabel, BorderLayout.CENTER);

                // Nombre del Pokémon

                JLabel nameLabel = new JLabel(pokemon.getNombre(), SwingConstants.CENTER);
                nameLabel.setFont(new Font("Arial", Font.BOLD, 14));
                card.add(nameLabel, BorderLayout.SOUTH);

                // Acción al hacer clic en la tarjeta
                card.addActionListener(e -> {
                        // Mostrar imagen ampliada
                        pokemonImageLabel.setIcon(
                                        new ImageIcon(icon.getImage().getScaledInstance(200, 200, Image.SCALE_SMOOTH)));

                        // Mostrar información completa del Pokémon
                        pokemonInfoArea.setText("Nombre: " + pokemon.getNombre() +
                                        "\nTipo: " + pokemon.getTipo() +
                                        "\nNúmero de Pokédex: " + pokemon.getNumeroPokedex() +
                                        "\nDescripción: " + pokemon.getDescripcion() +
                                        "\nHabilidades Especiales: " + (pokemon.getHabilidadesEspeciales() != null
                                                        ? String.join(", ", pokemon.getHabilidadesEspeciales())
                                                        : "N/A")
                                        + "\nDebilidades: " + (pokemon.getDebilidades() != null
                                                        ? String.join(", ", pokemon.getDebilidades())
                                                        : "N/A")
                                        + "\nAtaques: " + (pokemon.getAtaques() != null
                                                        ? String.join(", ", pokemon.getAtaques())
                                                        : "N/A")
                                        + "\nRegión: " + pokemon.getRegion() +
                                        "\nNivel: " + pokemon.getNivel());

                        // Mostrar cadena evolutiva como cartas
                        evolutionPanel.removeAll();
                        JLabel evolutionLabel = new JLabel("Evolución:");
                        evolutionPanel.add(evolutionLabel);
                        // Cambiar la fuente a negrita y tamaño 16
                        evolutionLabel.setFont(new Font("Arial", Font.BOLD, 20));
                        for (String evolutionName : pokemon.getEvoluciones()) {
                                // Buscar el Pokémon de evolución en la lista de pokemons
                                for (Pokemon evoPokemon : pokemons) {
                                        if (evoPokemon.getNombre().equalsIgnoreCase(evolutionName)) {
                                                JButton evolutionCard = createEvolutionCard(evoPokemon,
                                                                pokemonImageLabel, pokemonInfoArea,
                                                                evolutionPanel, pokemons);
                                                evolutionPanel.add(evolutionCard);
                                        }
                                }
                        }
                        evolutionPanel.revalidate();
                        evolutionPanel.repaint();
                });

                return card;
        }

        public static JButton createEvolutionCard(Pokemon evolutionPokemon, JLabel pokemonImageLabel,
                        JTextArea pokemonInfoArea, JPanel evolutionPanel, List<Pokemon> pokemons) {
                JButton evolutionCard = new JButton();
                evolutionCard.setLayout(new BorderLayout());
                evolutionCard.setPreferredSize(new Dimension(100, 100)); // Tamaño fijo

                // Imagen de la evolución (simulada)
                ImageIcon icon = new ImageIcon(evolutionPokemon.getImagen()); // Simulación de ruta
                Image scaledImage = icon.getImage().getScaledInstance(100, 100, Image.SCALE_SMOOTH);
                JLabel imageLabel = new JLabel(new ImageIcon(scaledImage));
                evolutionCard.add(imageLabel, BorderLayout.CENTER);

                evolutionCard.addActionListener(e -> {
                        // Actualizar la celda de detalles con la información del Pokémon evolucionado
                        pokemonImageLabel.setIcon(
                                        new ImageIcon(icon.getImage().getScaledInstance(200, 200, Image.SCALE_SMOOTH)));
                        pokemonInfoArea.setText("Nombre: " + evolutionPokemon.getNombre() +
                                        "\nTipo: " + evolutionPokemon.getTipo() +
                                        "\nNúmero de Pokédex: " + evolutionPokemon.getNumeroPokedex() +
                                        "\nDescripción: " + evolutionPokemon.getDescripcion() +
                                        "\nHabilidades Especiales: "
                                        + (evolutionPokemon.getHabilidadesEspeciales() != null
                                                        ? String.join(", ", evolutionPokemon.getHabilidadesEspeciales())
                                                        : "N/A")
                                        + "\nDebilidades: " + (evolutionPokemon.getDebilidades() != null
                                                        ? String.join(", ", evolutionPokemon.getDebilidades())
                                                        : "N/A")
                                        + "\nAtaques: " + (evolutionPokemon.getAtaques() != null
                                                        ? String.join(", ", evolutionPokemon.getAtaques())
                                                        : "N/A")
                                        + "\nRegión: " + evolutionPokemon.getRegion() +
                                        "\nNivel: " + evolutionPokemon.getNivel());
                });

                return evolutionCard;
        }
}
