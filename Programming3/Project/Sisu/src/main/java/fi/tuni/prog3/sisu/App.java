package fi.tuni.prog3.sisu;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.io.IOException;
import javafx.scene.image.Image;

/**
 * JavaFX App
 */
public class App extends Application {
    
    private static Scene scene;

    /**
     * Opens a new instance of sisu.
     * @param stage a stage for the application.
     * @throws IOException
     */
    @Override
    public void start(Stage stage) throws IOException {
        scene = new Scene(loadFXML("primary"), 500, 700);
        
        Image img = new Image("file:SisuDino.png");
        stage.getIcons().add(img);
        stage.setTitle("SISU V2");
        stage.setScene(scene);
        stage.show();
        
    }
    /**
     * Sets the stage root with string parameter
     * @param fxml String that tells the fxml files name
     * @throws IOException 
     */
    static void setRoot(String fxml) throws IOException {
        scene.setRoot(loadFXML(fxml));
    }
    /**
     * Sets the stage root with FXML loader parameter
     * @param loader loader that has the desired controller
     * @throws IOException 
     */
    static void setRoot(FXMLLoader loader) throws IOException {
        scene.setRoot(loader.load());
    }
    
    
    /**
     * Resizes the window
     * @param width double containing the width value for the window
     * @param height double containing the height value for the window
     */
    static void resize(double width, double height) {
        Stage stage = (Stage) scene.getWindow();
        stage.setWidth(width);
        stage.setHeight(height);
    }
    
    /**
     * Creates the correct fxmlLoader from given string
     * @param fxml String that tells what .fxml to use
     * @return returns the loaded fxml
     * @throws IOException 
     */
    private static Parent loadFXML(String fxml) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(App.class.getResource(fxml + ".fxml"));
        return fxmlLoader.load();
    }
    
    /**
     * The main.
     */
    public static void main() {
        launch();
    }

}