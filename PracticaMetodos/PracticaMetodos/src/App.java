import javax.sound.sampled.*;
import java.io.File;
import java.io.IOException;
import javax.swing.*;
import java.awt.*;
import java.util.List;

public class App {
        public static void main(String[] args) {
                // Crear ventana principal

                // Ruta del archivo de audio
                String audioFilePath = "PracticaMetodos\\PracticaMetodos\\src\\IMAGENES\\spotifydown.com - Littleroot Town (From _Pokemon Ruby_).wav";

                playBackgroundMusic(audioFilePath);

                JFrame frame = new JFrame("Pokedex");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setSize(1000, 800);

                JPanel mainPanel = new JPanel() {
                        @Override
                        protected void paintComponent(Graphics g) {
                                super.paintComponent(g);
                                Graphics2D g2d = (Graphics2D) g;
                                // Crear el gradiente de color usando Color directamente.
                                GradientPaint gradient = new GradientPaint(0, 0, new Color(204, 204, 255), 0,
                                                getHeight(), new Color(204, 204, 255));
                                g2d.setPaint(gradient);
                                g2d.fillRect(0, 0, getWidth(), getHeight());
                        }
                };

                mainPanel.setLayout(new BorderLayout());

                // Panel superior para filtros y búsqueda
                JPanel topPanel = new JPanel(new FlowLayout());
                topPanel.setOpaque(false);

                // Campo de búsqueda
                JTextField searchField = new JTextField(20);
                topPanel.add(new JLabel("Buscar:"));
                topPanel.add(searchField);

                // Botón de buscar
                JButton searchButton = new JButton("Buscar");
                topPanel.add(searchButton);

                // Lista desplegable para filtrar por tipo
                String[] tipos = { "Todos", "Eléctrico", "Fuego", "Planta", "Veneno", "Normal", "Volador", "Agua" };
                JComboBox<String> typeFilter = new JComboBox<>(tipos);
                topPanel.add(new JLabel("Filtrar por tipo:"));
                topPanel.add(typeFilter);

                mainPanel.add(topPanel, BorderLayout.NORTH);

                // Panel central para tarjetas
                JPanel cardPanel = new JPanel(new FlowLayout(FlowLayout.LEFT, 10, 10));
                cardPanel.setOpaque(false);

                JScrollPane cardScrollPane = new JScrollPane(cardPanel);
                cardScrollPane.setOpaque(false);
                cardScrollPane.getViewport().setOpaque(false);
                mainPanel.add(cardScrollPane, BorderLayout.CENTER);

                // Agregar un MouseWheelListener al JScrollPane de las tarjetas
                cardScrollPane.addMouseWheelListener(e -> {
                        int rotation = e.getWheelRotation();
                        int increment = (int) (rotation * 100);

                        JScrollBar verticalScrollBar = cardScrollPane.getVerticalScrollBar();
                        verticalScrollBar.setValue(verticalScrollBar.getValue() + increment);

                        e.consume();
                });

                // Panel inferior para detalles del Pokémon
                JPanel detailsPanel = new JPanel(new GridLayout(1, 3, 10, 10));
                detailsPanel.setOpaque(false);
                detailsPanel.setPreferredSize(new Dimension(1000, 250));

                // Celda 1: Imagen ampliada
                JLabel pokemonImageLabel = new JLabel("", SwingConstants.CENTER);
                detailsPanel.add(pokemonImageLabel);

                // Celda 2: Información del Pokémon
                JTextArea pokemonInfoArea = new JTextArea();
                pokemonInfoArea.setOpaque(false);
                pokemonInfoArea.setForeground(Color.black);
                pokemonInfoArea.setEditable(false);
                pokemonInfoArea.setLineWrap(true);
                pokemonInfoArea.setWrapStyleWord(true);

                // Cambiar la fuente a negrita y tamaño 16
                pokemonInfoArea.setFont(new Font("Arial", Font.BOLD, 15));

                JScrollPane infoScrollPane = new JScrollPane(pokemonInfoArea);
                infoScrollPane.setOpaque(false);
                infoScrollPane.getViewport().setOpaque(false);
                detailsPanel.add(infoScrollPane);

                // Celda 3: Cadena evolutiva
                JPanel evolutionPanel = new JPanel(new FlowLayout());
                evolutionPanel.setOpaque(false);
                detailsPanel.add(evolutionPanel);

                mainPanel.add(detailsPanel, BorderLayout.SOUTH);

                // Lógica de la Pokédex
                Pokedex pokedex = new Pokedex(); // Instancia de la Pokédex
                List<Pokemon> pokemons = pokedex.getAllPokemons(); // Obtener todos los Pokémon

                // Método para mostrar las tarjetas
                Runnable updateCards = () -> {
                        cardPanel.removeAll();
                        String searchText = searchField.getText().toLowerCase();
                        String selectedType = (String) typeFilter.getSelectedItem();

                        for (Pokemon pokemon : pokemons) {
                                if (!searchText.isEmpty() && !pokemon.getNombre().toLowerCase().contains(searchText)) {
                                        continue; // Filtrar por búsqueda
                                }
                                if (!selectedType.equals("Todos")) {
                                        String[] tiposPokemon = pokemon.getTipo().toLowerCase().split("/");
                                        boolean tipoCoincide = false;
                                        for (String tipo : tiposPokemon) {
                                                if (tipo.trim().equalsIgnoreCase(selectedType)) {
                                                        tipoCoincide = true;
                                                        break;
                                                }
                                        }
                                        if (!tipoCoincide) {
                                                continue; // Filtrar por tipo si no hay coincidencia
                                        }
                                }

                                JButton card = PokemonCardCreator.createPokemonCard(pokemon, pokemonImageLabel,
                                                pokemonInfoArea, evolutionPanel, pokemons);
                                cardPanel.add(card);
                        }

                        cardPanel.revalidate();
                        cardPanel.repaint();
                };

                // Actualizar las tarjetas al buscar o filtrar
                searchButton.addActionListener(e -> updateCards.run());
                typeFilter.addActionListener(e -> updateCards.run());

                // Mostrar todos los Pokémon al iniciar
                updateCards.run();

                // Agregar panel principal al marco y hacerlo visible
                frame.setContentPane(mainPanel);
                frame.setVisible(true);
        }

        public static void playBackgroundMusic(String audioFilePath) {
                try {
                        // Cargar el archivo de audio
                        File audioFile = new File(audioFilePath);
                        AudioInputStream audioStream = AudioSystem.getAudioInputStream(audioFile);
                        Clip clip = AudioSystem.getClip();
                        clip.open(audioStream);

                        // Reproducir la música en bucle
                        clip.loop(Clip.LOOP_CONTINUOUSLY);

                        // Iniciar la reproducción
                        clip.start();
                } catch (UnsupportedAudioFileException | IOException | LineUnavailableException e) {
                        e.printStackTrace();
                }
        }
}
