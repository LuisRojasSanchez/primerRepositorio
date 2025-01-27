import javax.swing.*;
import java.awt.*;

public class GradientPanel extends JPanel {
    private Color startColor;
    private Color endColor;

    // Constructor para inicializar los colores del degradado
    public GradientPanel(Color startColor, Color endColor) {
        this.startColor = startColor;
        this.endColor = endColor;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;

        // Crear el degradado
        GradientPaint gradient = new GradientPaint(0, 0, startColor, 0, getHeight(), endColor);
        g2d.setPaint(gradient);
        g2d.fillRect(0, 0, getWidth(), getHeight());
    }

    // Métodos para actualizar los colores si es necesario
    public void setStartColor(Color startColor) {
        this.startColor = startColor;
        repaint();
    }

    public void setEndColor(Color endColor) {
        this.endColor = endColor;
        repaint();
    }
}
