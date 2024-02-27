package fi.tuni.prog3.wordle;

import java.util.*;
import java.io.*;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.scene.layout.Background;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.layout.Border;
import javafx.scene.layout.BorderStroke;
import javafx.scene.layout.BorderStrokeStyle;
import javafx.scene.layout.BorderWidths;
import javafx.scene.layout.CornerRadii;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.*;
import javafx.stage.Stage;

/**
 * JavaFX App
 */
public class Wordle extends Application {

    private Scene scene;
    private ArrayList<String> words = new ArrayList<>();
    private int index = 0;
    private String word;
    private int wordLength;
    private VBox board;
    private int wordIndex = 0;
    private int guess = 0;
    private Label statusText;
    private boolean isNotOver = true;
    
    @Override
    public void start(Stage stage) throws IOException {
        
        VBox layout = new VBox();
        
        Button newGameBtn = new Button("Start new game");
        newGameBtn.setId("newGameBtn");
        
        newGameBtn.setOnAction((ActionEvent e) -> {
            try {
                layout.getChildren().remove(1);
                initBoard();
                layout.getChildren().add(board);
                statusText.setText("");
                scene.setRoot(layout);
                guess = 0;
                wordIndex = 0;
                isNotOver = true;
                selectNextField(0);
            } catch (IOException ex) {
                ex.printStackTrace();

            }
        });
        
        statusText = new Label("");
        statusText.setId("infoBox");
        
        HBox firstRow = new HBox();
        firstRow.getChildren().addAll(newGameBtn, statusText);
        
        layout.getChildren().add(firstRow);
        initBoard();
        layout.getChildren().add(board);

        selectNextField(0);
        
        scene = new Scene(layout, 700, 650);
        scene.setOnKeyPressed(this::handle);
        board.requestFocus();
        stage.setScene(scene); 
        stage.show();
    }
    
    private void handle(KeyEvent t) {
        
            if(t.getCode().equals(KeyCode.BACK_SPACE) && isNotOver) {
                if ("".equals(getField().getText())) {
                    selectNextField(-1);
                    getField().setText("");
                }
                else{
                    getField().setText("");
                    selectNextField(-1);
                }    

            }
            else if(t.getCode().equals(KeyCode.ENTER) && isNotOver) {
                String guessedWord = getGuess();
                if (guessedWord.length() != wordLength) {
                    statusText.setText("Give a complete word before pressing Enter!");
                }
                else {
                    Boolean isCorrect = checkGuess(guessedWord);
                    if (isCorrect) {
                        statusText.setText("Congratulations, you won!");
                        isNotOver = false;
                    }
                    else if (!isCorrect && guess == 5) {
                        statusText.setText("Game over, you lost!");
                        
                    }
                }
            }
            else if (t.getCode().isLetterKey() && isNotOver) {
                System.out.println("text");
                if ("".equals(getField().getText())) {
                    getField().setText(t.getCode().getChar().toUpperCase());
                    selectNextField(1);
                }
                else {
                    selectNextField(1);
                    if ("".equals(getField().getText())) {
                        getField().setText(t.getCode().getChar().toUpperCase());
                    }
                }

            }
        }
    
    private boolean checkGuess(String guessedWord) {
        
        HBox row = (HBox)board.getChildren().get(guess);
        
        System.out.println(guessedWord);
        System.out.println(word);
        
        for (int i = 0; i < wordLength; i++) {
            Label field = (Label)row.getChildren().get(i); 
            char c = guessedWord.toLowerCase().charAt(i);
            
            if (c == word.charAt(i)) {
                 field.setBackground(new Background(new BackgroundFill(Color.GREEN, null, null)));
            }
            else if(word.contains(String.valueOf(c))) {
                field.setBackground(new Background(new BackgroundFill(Color.ORANGE, null, null)));
            }
            else {
                field.setBackground(new Background(new BackgroundFill(Color.GREY, null, null)));
            }
            field.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.SOLID, CornerRadii.EMPTY,
            BorderWidths.DEFAULT)));
            field.setTextFill(Color.WHITE);
        }
        if (guess < 5) {
            guess += 1;
        }
        wordIndex = 0;
        statusText.setText("");
        selectNextField(0);
        
        return word.equals(guessedWord.toLowerCase());
    }
    
    private String getWord() throws FileNotFoundException, IOException {

        if(words.isEmpty()) {
            try(var input = new BufferedReader(new FileReader("words.txt"))) {
                words = new ArrayList<>();
                String line;
                while ((line = input.readLine()) != null) {
                    words.add(line);
                }
            }
        }

        String word = words.get(index);
        index += 1;
        return word;
    }
    
    private void initBoard() throws IOException {
        
        word = getWord();
        wordLength = word.length();
        
        board = new VBox();

        int rows = 6;
        int columns = word.length();
        
        for(int i = 0; i < rows; i++) {
            HBox new_row = new HBox();
            for (int j = 0; j < columns; j++) {
                new_row.getChildren().add(initField(i, j));
            }
            board.getChildren().add(new_row); 
        }
    }
    
    private Label initField(int row, int column) {
        
        Label newField = new Label("");
        newField.setTextAlignment(TextAlignment.CENTER);
        newField.setPrefSize(60, 60);
        newField.setId(String.format("%d_%d", row, column));
        newField.setFont(Font.font("",FontWeight.BOLD, 50));
        newField.setBackground(new Background(new BackgroundFill(Color.WHITE, null, null)));
        newField.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.DASHED, CornerRadii.EMPTY,
                        BorderWidths.DEFAULT)));

        return newField;
    }
    
    private void selectNextField(int value) {
        
        //Deselecting current
        Label field = getField();
        field.setBorder(new Border(new BorderStroke(Color.BLACK, BorderStrokeStyle.DASHED, CornerRadii.EMPTY,
            BorderWidths.DEFAULT)));
        field.setFocusTraversable(false);
        if (wordIndex + value < wordLength && wordIndex + value >= 0) {
            wordIndex += value;
        }
        
        System.out.println(wordIndex);
        
        // Selecting next/previous
        field = getField();
        field.setBorder(new Border(new BorderStroke(Color.BLUE, BorderStrokeStyle.SOLID, CornerRadii.EMPTY,
            BorderWidths.DEFAULT)));
        field.setFocusTraversable(true);
        field.requestFocus();
    }
    
    private Label getField () {
        HBox row = (HBox)board.getChildren().get(guess);
        Label field = (Label)row.getChildren().get(wordIndex);
        return field;
    }
    
    private String getGuess() {
        String guessedWord = "";
        for (int i = 0; i < wordLength; i++) {
            HBox row = (HBox)board.getChildren().get(guess);
            Label field = (Label)row.getChildren().get(i);
            String c = field.getText();
            guessedWord += c;
        }
        return guessedWord;
    }
    
    public static void main(String[] args) {
        launch();
    }

}