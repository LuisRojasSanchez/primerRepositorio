
import java.util.List;

public class Pokemon {
    private String nombre;
    private String tipo;
    private String descripcion;
    private List<String> habilidadesEspeciales;
    private List<String> debilidades;
    private List<String> ataques;
    private int nivel;
    private String region;
    private String imagen; // Ruta de la imagen del Pokémon
    private int numeroPokedex;
    private List<String> evoluciones;

    // Constructor
    public Pokemon(String nombre, String tipo, String descripcion, List<String> habilidadesEspeciales,
            List<String> debilidades, List<String> ataques, int nivel, String region, String imagen, int numeroPokedex,
            List<String> evoluciones) {
        this.nombre = nombre;
        this.tipo = tipo;
        this.descripcion = descripcion;
        this.habilidadesEspeciales = habilidadesEspeciales;
        this.debilidades = debilidades;
        this.ataques = ataques;
        this.nivel = nivel;
        this.region = region;
        this.imagen = imagen;
        this.numeroPokedex = numeroPokedex;
        this.evoluciones = evoluciones;
    }

    // Getters y setters
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public void setDescripcion(String descripcion) {
        this.descripcion = descripcion;
    }

    public List<String> getHabilidadesEspeciales() {
        return habilidadesEspeciales;
    }

    public void setHabilidadesEspeciales(List<String> habilidadesEspeciales) {
        this.habilidadesEspeciales = habilidadesEspeciales;
    }

    public List<String> getDebilidades() {
        return debilidades;
    }

    public void setDebilidades(List<String> debilidades) {
        this.debilidades = debilidades;
    }

    public List<String> getAtaques() {
        return ataques;
    }

    public void setAtaques(List<String> ataques) {
        this.ataques = ataques;
    }

    public int getNivel() {
        return nivel;
    }

    public void setNivel(int nivel) {
        this.nivel = nivel;
    }

    public String getRegion() {
        return region;
    }

    public void setRegion(String region) {
        this.region = region;
    }

    public String getImagen() {
        return imagen;
    }

    public void setImagen(String imagen) {
        this.imagen = imagen;
    }

    public int getNumeroPokedex() {
        return numeroPokedex;
    }

    public void setNumeroPokedex(int numeroPokedex) {
        this.numeroPokedex = numeroPokedex;
    }

    public List<String> getEvoluciones() {
        return evoluciones;
    }

    public void setEvoluciones(List<String> evoluciones) {
        this.evoluciones = evoluciones;
    }
}
