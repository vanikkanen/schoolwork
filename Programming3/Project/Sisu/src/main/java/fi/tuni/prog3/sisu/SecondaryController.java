package fi.tuni.prog3.sisu;

import java.io.IOException;
import java.util.*;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.fxml.FXML;
import javafx.geometry.Insets;
import javafx.scene.Node;
import javafx.scene.control.Accordion;
import javafx.scene.control.Button;
import javafx.scene.control.CheckBox;
import javafx.scene.control.Label;
import javafx.scene.control.ListCell;
import javafx.scene.control.ListView;
import javafx.scene.control.ProgressBar;
import javafx.scene.control.SelectionMode;
import javafx.scene.control.SplitPane;
import javafx.scene.control.TextArea;
import javafx.scene.control.TitledPane;
import javafx.scene.image.Image;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundImage;
import javafx.scene.layout.BackgroundPosition;
import javafx.scene.layout.BackgroundRepeat;
import javafx.scene.layout.BackgroundSize;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.util.Callback;

/**
 * Controller to represent the degree view. Shows all the modules and courses in
 * the chosen degree. Courses can be selected and the chosen courses can be
 * saved into a json file.
 * Also displays information about the modules and degrees when hovered over.
 * Tracks the progress of the degree by credits.
 */
public class SecondaryController {

    @FXML private Accordion moduleList;
    @FXML private ProgressBar creditProgress;
    @FXML private TextArea infoArea;
    @FXML private CheckBox discoMode;
    @FXML private Button saveStudentButton;
    @FXML private SplitPane rootNode;
    @FXML private Button exitButton;
    @FXML private Label accCreditLabel;
    @FXML private Label degreeProgramLabel;
    @FXML private Label studentNameLabel;
    
    private String degreeString;
    private PrimaryController controller1;
    private sisuData data;
    private Student studentToLoad = null;
    private int selectedCredits;
    private int degreeCredits;
    private String studentName;
    private ArrayList<Integer> selectedCourses;
    
    Image imgDino = new Image("file:SisuDino.gif");

    BackgroundImage bImgDino = new BackgroundImage(imgDino,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundPosition.DEFAULT,
                                   new BackgroundSize(1.0, 1.0, true, true,
                                           false, false));
    Background bGroundDino = new Background(bImgDino);
    
    Image img = new Image("file:bgVertical.jpeg");

    BackgroundImage bImg = new BackgroundImage(img,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundRepeat.NO_REPEAT,
                                   BackgroundPosition.DEFAULT,
                                   new BackgroundSize(1.0, 1.0, true, true,
                                           false, false));
    Background bGround = new Background(bImg);
    
    /**
     * Constructor for the controller when creating a new degree
     * @param controllerP Starting controller from which this degree view
     * (SecondaryController) created
     * @param data sisuData object that contains the loaded degree data
     */
    public SecondaryController(PrimaryController controllerP, sisuData data) {
        controller1 = controllerP;
        this.data = data;
    }
    
    /**
     * Constructor for the controller when loading an existing student
     * @param controllerP Starting controller from which this degree view 
     * (SecondaryController) created
     * @param data sisuData object that contains the loaded degree data
     * @param studentToLoad the student object that is to be loaded into the UI
     */
    public SecondaryController(PrimaryController controllerP, sisuData data,
            Student studentToLoad) {
        controller1 = controllerP;
        this.studentToLoad = studentToLoad;
        this.data = data;
    }
    
    /**
     * Initializes the controller
     * @throws IOException 
     */
    @FXML
    public void initialize() throws IOException {
        selectedCredits = 0;
        if (studentToLoad == null) {
            selectedCourses = new ArrayList<>();
            degreeString = controller1.setDegreeString();
            studentName = controller1.setStudentName();
        }
        else {
            selectedCourses = studentToLoad.courses;
            degreeString = studentToLoad.degree;
            studentName = studentToLoad.name;
        }

        saveStudentButton.setText("Save: " + studentName);
        
        Module module = data.getModule(degreeString);
        if(module == null){
            infoArea.setText("Virhe tutkinto-ohjelmaa haettaessa");
        }
        else{
            degreeCredits = module.getCredits();

            degreeProgramLabel.setText(degreeString);
            studentNameLabel.setText(studentName);

            //Creating the degree view
            TitledPane pane = new TitledPane(degreeString + " " + degreeCredits,
                    fillAccordion(module));
            pane.setOnMouseEntered(e -> {
                setInfoAreaTextModule(module);
                });
            moduleList.getPanes().add(pane);
        }
        initDiscoMode();
        rootNode.setBackground(bGround);
        
    }
    
    /**
     * Switches back to the starting view
     * @throws IOException 
     */
    @FXML
    private void switchToPrimary() throws IOException {
        App.resize(500, 700);
        App.setRoot("primary");
    }
 
    /**
     * Initializes the discoMode checkBox
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
     * Sets the text in the textBox to the modules info text.
     * @param module 
     */
    private void setInfoAreaTextModule(Module module) {
        String infoString = module.getName();
            infoString += "\n";
            infoString += "\n";
            infoString += module.getInfo();
            infoArea.setText(infoString);
    }
    
    /**
     * Populates the accordion with modules and courses that the original 
     * degree program contains. Goes recursively through every module.
     * @param module Module to be looped through.
     * @return returns VBox filled up with modules that are filled with other 
     * modules or courses.
     */
    private VBox fillAccordion(Module module) {
        
        Set<Map.Entry<String, Module>> innerModules = module.getModules()
                .entrySet();
        Set<Map.Entry<String, Course>> courses = module.getCourses().entrySet();
        VBox moduleBox = new VBox();
        moduleBox.setPadding(new Insets(0, 0, 0, 10));
        
        if (!innerModules.isEmpty()) {
            for (var entry : innerModules) {
                TitledPane newPane = new TitledPane(entry.getKey() + " "
                        +  entry.getValue().getCredits(),
                        fillAccordion(entry.getValue()));
                newPane.setExpanded(false);
                newPane.setOnMouseEntered(e -> {
                    setInfoAreaTextModule(entry.getValue());
                });
                moduleBox.getChildren().add(newPane);
            }
        }
        
        ArrayList<Course> coursesList = new ArrayList<>();
        
        ListView allCourses = courseListView(coursesList);
        
        if (!courses.isEmpty()) {
            int i = 0;
            for (var course : courses) {
                allCourses.getItems().add(presentCourse(course.getValue()));
                coursesList.add(course.getValue());
                if (selectedCourses.contains(course.getValue().getId())) {
                    allCourses.getSelectionModel().select(i);
                    selectedCredits += course.getValue().getCredits();
                }
                updateProgress();
                i++;
            }
    
            moduleBox.getChildren().add(allCourses);
            
        }

        return moduleBox;
    }
    
    /**
     * Updates the progress bar every time a new course is selected or 
     * unselected.
     */
    private void updateProgress() {
        if (degreeCredits > 0) {
            double progressValue = Double.valueOf(selectedCredits)/Double
                    .valueOf(degreeCredits);
            creditProgress.setProgress(progressValue);
            accCreditLabel.setText("Valitut opintopisteet: " + selectedCredits 
                    + "/" + degreeCredits);
        }
    }
    
    /**
     * Creates a HBox that is then placed inside another container from the 
     * given course
     * @param course Course whose information is to presented
     * @return HBox that contains Nodes depicting course information
     */
    private HBox presentCourse(Course course) {
        
                HBox courseBox = new HBox();
                Label nameLabel = new Label(course.getName());
                Label codeLabel = new Label(course.getCode());
                Label textLabel = new Label("Opintopisteet: ");
                Label creditLabel = new Label(Integer.toString(course
                        .getCredits()));

                courseBox.getChildren().addAll(nameLabel, codeLabel, textLabel,
                        creditLabel);
                courseBox.setSpacing(10);
                
                return courseBox;
                
    }
    
    /**
     * Creates a listView for the courses in the given arrayList. Also makes 
     * the courses in the ListView selectable and unselectable.
     * Also makes it so when a course is hovered its info text is shown in the 
     * UI.
     * @param coursesList ArrayList containing Course objects
     * @return ListView Node that contain selectable, unselectable and hoverable
     * Course presentations
     */
    private ListView courseListView(ArrayList<Course> coursesList) {
        
        ListView<HBox> allCourses = new ListView();
        
        allCourses.getSelectionModel().setSelectionMode(SelectionMode.MULTIPLE);
        allCourses.getItems().clear();
        
        allCourses.addEventFilter(MouseEvent.MOUSE_PRESSED, evt -> {
            Node node = evt.getPickResult().getIntersectedNode();
            
            while (node != null && node != allCourses 
                    && !(node instanceof ListCell)) {
            node = node.getParent();
            }

            if (node instanceof ListCell) {

                evt.consume();

                ListCell cell = (ListCell) node;
                ListView lv = cell.getListView();

                lv.requestFocus();

                if (!cell.isEmpty()) {
                    int index = cell.getIndex();
                    if (cell.isSelected()) {
                        lv.getSelectionModel().clearSelection(index);
                        
                        selectedCredits -= coursesList.get(index).getCredits();
                        
                        if (selectedCourses.contains(coursesList.get(index)
                                .getId())) {
                            for (int i = 0; i < selectedCourses.size(); i++) {
                                if (selectedCourses.get(i) == coursesList
                                        .get(index).getId()) {
                                    selectedCourses.remove(i);
                                    break;
                                }
                            }
                        }
                    } 
                    else {
                        lv.getSelectionModel().select(index);
                        selectedCredits += coursesList.get(index).getCredits();
                        
                        selectedCourses.add(coursesList.get(index).getId());
                    }
                }
                updateProgress();
            }
        });
        
            allCourses.setCellFactory(new Callback<ListView<HBox>,
                    ListCell<HBox>>() {
                @Override
                public ListCell<HBox> call(ListView<HBox> myObjectListView) {
                    ListCell<HBox> cell = new ListCell<HBox>()
                    {
                        @Override
                        protected void updateItem(HBox item, boolean b) {
                            super.updateItem(item, b);
                            if(item != null) {
                                setGraphic(item);
                            }
                        }
                    };
                   
                    cell.setOnMouseEntered(e -> {
                            if (cell.getIndex() < coursesList.size()) {
                                String infoString = coursesList.get(cell
                                        .getIndex()).getName();
                                infoString += "\n";
                                infoString += coursesList.get(cell.getIndex())
                                        .getCode();
                                infoString += "\n";
                                infoString += "\n";
                                infoString += coursesList.get(cell.getIndex())
                                        .getInfo();
                                infoArea.setText(infoString);
                            }
                        });

                    return cell;
                }          
            });
        
      return allCourses;  
    }
    
    /**
     * Saves the current state of the degree to a JSON file under the students
     * name
     * @throws IOException 
     */
    @FXML
    public void saveCurrent() throws IOException{
        
        Student student = new Student(studentName, degreeString, selectedCourses
                .toArray(new Integer[selectedCourses.size()]));
        student.saveStudent();
    }
    
    /**
     * Quits the program 
     */
    @FXML 
    void exitProgram() {
        Stage stage = (Stage)exitButton.getScene().getWindow();
        stage.close();
    }
}