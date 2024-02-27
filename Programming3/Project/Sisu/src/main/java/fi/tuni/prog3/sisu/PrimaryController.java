package fi.tuni.prog3.sisu;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Paths;
import java.util.*;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.EventHandler;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.ComboBox;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.image.Image;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundImage;
import javafx.scene.layout.BackgroundPosition;
import javafx.scene.layout.BackgroundRepeat;
import javafx.scene.layout.BackgroundSize;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;

/**
 * Controller for the Starting view of the UI. Here the degreeprogram is 
 * selected and student name is given. Alternatively an already saved student 
 * file can be loaded.
 * Main purpose is to make the selections and move to the degree view.
 */
public class PrimaryController {
    
    @FXML private TextField nameField;
    @FXML private ComboBox degreeBoxCB;
    @FXML private CheckBox discoMode;
    @FXML private ComboBox savedStudents;
    @FXML private VBox rootNode;
    @FXML private Label instructionLabel;
    @FXML private Button exitButton;
    
    AutoCompleteComboBoxListener degreeBox;
    private List<String> degrees;
    private sisuData data;
    
    Image imgDino = new Image("file:SisuDino.gif");

    BackgroundImage bImgDino = new BackgroundImage(imgDino,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundPosition.DEFAULT,
                                   new BackgroundSize(1.0, 1.0,
                                           true, true, false, false));
    Background bGroundDino = new Background(bImgDino);
    
    Image img = new Image("file:bgVertical.jpeg");

    BackgroundImage bImg = new BackgroundImage(img,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundPosition.DEFAULT,
                                   new BackgroundSize(1.0, 1.0,
                                           true, true, false, false));
    Background bGround = new Background(bImg);
    
    /**
     * Initializes an instance of a starting view.
     */
    public void initialize(){
        
        data = new sisuData();
        
        if(data.getDataFoundStatus()){
            degrees = data.getDegrees();
            for (int i = 0; i < degrees.size(); i++) {
                degreeBoxCB.getItems().add(degrees.get(i));
            }
            degreeBox = new AutoCompleteComboBoxListener<>(degreeBoxCB);
            populateStudents();
            

            instructionLabel.setText("Valitse tutkinto-ohjelma ja luo uusi"
                    + " opiskelija, tai lataa tallennettu opiskelija.");
        }
        else{
            instructionLabel.setText("Virhe tietojen hakemisessa.");
        }
        initDiscoMode();
        rootNode.setBackground(bGround);
    }

    /**
     * Switches to degree view and resizes the window
     * @throws IOException 
     */
    @FXML
    private void switchToSecondary() throws IOException {
        
        if(degrees != null
                && nameField.getText() != ""
                && degrees.contains(degreeBoxCB.getValue().toString())) {
            
            SecondaryController controller2 = 
                    new SecondaryController(this, data);
            App.resize(1200, 700);
            FXMLLoader fxmlLoader = new FXMLLoader(
                    App.class.getResource(
                            "secondary.fxml"
                    ));

            fxmlLoader.setController(controller2);

            App.setRoot(fxmlLoader);
        }
        else {
             instructionLabel.setText("Valitse tutkinto-ohjelma ja aseta nimi."
                     + " tai lataa tallennettu opiskelija");
        }
    }
    
    /**
     * Returns the chosen degrees name
     * @return the chosen degrees name
     */
    public String setDegreeString(){
        return degreeBoxCB.getValue().toString();
    }
    
    /**
     * Returns the students name
     * @return the students name
     */
    public String setStudentName() {
        return nameField.getText();
    }
    
    /**
     * Class for a searchable Combo box asset fo the UI
     * @param <T> String in this case. A list of the degreeProgram names
     */
    private class AutoCompleteComboBoxListener<T> 
            implements EventHandler<KeyEvent> {

        private ComboBox comboBox;
        private StringBuilder sb;
        private ObservableList<T> data;
        private boolean moveCaretToPos = false;
        private int caretPos;
        
        /**
         * Constructor for the auto completing combo box
         * @param comboBox the original combo box that is being transformed
         */
        public AutoCompleteComboBoxListener(final ComboBox comboBox) {
            this.comboBox = comboBox;
            sb = new StringBuilder();
            data = comboBox.getItems();

            this.comboBox.setEditable(true);
            this.comboBox.setOnKeyPressed(new EventHandler<KeyEvent>() {

                @Override
                public void handle(KeyEvent t) {
                    comboBox.hide();
                }
            });
            this.comboBox.setOnKeyReleased(AutoCompleteComboBoxListener.this);
        }
        
        /**
         * Overrides the original combo boxes handle function to be responsive 
         * to key presses
         * @param event KeyEvent that triggers the handle function
         */
        @Override
        public void handle(KeyEvent event) {

            if(event.getCode() == KeyCode.UP) {
                caretPos = -1;
                moveCaret(comboBox.getEditor().getText().length());
                return;
            } else if(event.getCode() == KeyCode.DOWN) {
                if(!comboBox.isShowing()) {
                    comboBox.show();
                }
                caretPos = -1;
                moveCaret(comboBox.getEditor().getText().length());
                return;
            } else if(event.getCode() == KeyCode.BACK_SPACE) {
                moveCaretToPos = true;
                caretPos = comboBox.getEditor().getCaretPosition();
            } else if(event.getCode() == KeyCode.DELETE) {
                moveCaretToPos = true;
                caretPos = comboBox.getEditor().getCaretPosition();
            }

            if (event.getCode() == KeyCode.RIGHT 
                    || event.getCode() == KeyCode.LEFT
                    || event.isControlDown() || event.getCode() == KeyCode.HOME
                    || event.getCode() == KeyCode.END 
                    || event.getCode() == KeyCode.TAB) {
                return;
            }

            ObservableList list = FXCollections.observableArrayList();
            for (int i=0; i<data.size(); i++) {
                if(data.get(i).toString().toLowerCase().startsWith(
                    AutoCompleteComboBoxListener.this.comboBox
                    .getEditor().getText().toLowerCase())) {
                    list.add(data.get(i));
                }
            }
            String t = comboBox.getEditor().getText();

            comboBox.setItems(list);
            comboBox.getEditor().setText(t);
            if(!moveCaretToPos) {
                caretPos = -1;
            }
            moveCaret(t.length());
            if(!list.isEmpty()) {
                comboBox.show();
            }
        }

        private void moveCaret(int textLength) {
            if(caretPos == -1) {
                comboBox.getEditor().positionCaret(textLength);
            } else {
                comboBox.getEditor().positionCaret(caretPos);
            }
            moveCaretToPos = false;
        }
    }
    
    /**
     * Initializes the discoMode checkBox to change the background to and
     * back from discoMode
     */
    private void initDiscoMode() {
        discoMode.selectedProperty().addListener(new ChangeListener<Boolean>() {
            @Override
            public void changed(ObservableValue<? extends Boolean> observable,
                    Boolean oldValue, Boolean newValue) {
                if (newValue) {
                    rootNode.setBackground(bGroundDino);
                }
                else {
                    rootNode.setBackground(bGround);
                }
            }
        });
    }
    
    /**
     * Reads and populates the comboBox with saved student files
     */
    private void populateStudents() {
        File folder = new File("students\\");
        File[] fileList = folder.listFiles();
        for (var file : fileList) {
            if (file.getName().contains(".json")) {
                savedStudents.getItems().add(file.getName().substring(0,
                        file.getName().length() - 5));
            }
        }
    }
    
    /**
     * Loads the selected students degree view. Resizes the window.
     * @throws IOException if errors in reading/finding the correct file throws
     * this but this shouldn't happen.
     */
    @FXML
    public void loadStudent() throws IOException {
        
        ObjectMapper mapper = new ObjectMapper();
        Student loadedStudent = null;
        String fileName = "students\\";
        if (savedStudents.getValue() != null) {
            fileName += savedStudents.getValue().toString() + ".json";
        
            try {
                loadedStudent = mapper.readValue(Paths.get(fileName).toFile(),
                        Student.class);

                SecondaryController controller2 = new SecondaryController(this,
                        data, loadedStudent);

                FXMLLoader fxmlLoader = new FXMLLoader(
                        App.class.getResource(
                                "secondary.fxml"
                        ));

                fxmlLoader.setController(controller2);

                App.resize(1200, 700);
                App.setRoot(fxmlLoader);

            } catch (FileNotFoundException ex) {
                System.out.println("File not found: " + fileName);
                instructionLabel.setText("Tiedostoa ei löytynt");
            } catch (JsonProcessingException ex) {
                System.out.println("Error in the student file");
                instructionLabel.setText("Ongelma tiedostossa");
            }
        }
        else {
            instructionLabel
                    .setText("Valitse opiskelija tai luo uusi opintonäkymä");
        }
    }
    
    /**
     * Quits the program
     */
    @FXML void exitProgram() {
        Stage stage = (Stage)exitButton.getScene().getWindow();
        stage.close();
    }
    
}