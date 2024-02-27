package fi.tuni.prog3.calc;

import javafx.scene.control.Label;
import javafx.application.Application;
import javafx.scene.Scene;
import javafx.stage.Stage;
import javafx.scene.control.*;
import javafx.scene.layout.FlowPane;
import javafx.scene.layout.VBox;
import javafx.scene.layout.HBox;
import java.io.IOException;
import javafx.scene.layout.*;
import javafx.scene.layout.BackgroundFill;
import javafx.scene.paint.*;
import javafx.event.*;
import java.text.DecimalFormat;

/**
 * JavaFX App
 */
public class Calculator extends Application {

    private static Scene scene;
    private DecimalFormat df = new DecimalFormat("0.0#");

    @Override
    public void start(Stage stage) throws IOException {
        
        VBox layout = new VBox();
        
        HBox firstLine = new HBox();
        Label firstLabel = new Label();
        firstLabel.setId("labelOp1");
        firstLabel.setText("First operand:");
        TextField firstField = new TextField();
        firstField.setId("fieldOp1");
        firstLine.getChildren().addAll(firstLabel, firstField);
        layout.getChildren().add(firstLine);
        
        HBox secondLine = new HBox();
        Label secondLabel = new Label();
        secondLabel.setId("labelOp2");
        secondLabel.setText("Second operand:");
        TextField secondField = new TextField();
        secondField.setId("fieldOp2");
        secondLine.getChildren().addAll(secondLabel,secondField);
        layout.getChildren().add(secondLine);
        
        Button btnAdd = new Button("Add");
        btnAdd.setId("btnAdd");
        
        Button btnSub = new Button("Subtract");
        btnSub.setId("btnSub");
        
        Button btnMul = new Button("Multiply");
        btnMul.setId("btnMul");

        Button btnDiv = new Button("Divide");
        btnDiv.setId("btnDiv");
        
        var btnGroup = new FlowPane();
        btnGroup.getChildren().addAll(btnAdd, btnSub, btnMul, btnDiv);
        
        layout.getChildren().add(btnGroup);
        
        HBox result = new HBox();
        Label labelRes = new Label("Result:");
        labelRes.setId("labelRes");
        Label fieldRes = new Label("");
        fieldRes.setId("fieldRes");
        fieldRes.setBackground(new Background(new BackgroundFill(Color.WHITE, null, null)));
        fieldRes.setMinWidth(150);
        result.getChildren().addAll(labelRes, fieldRes);
        layout.getChildren().add(result);
        
        btnAdd.setOnAction((ActionEvent e) -> {
            var first = Double.parseDouble(firstField.getText());
            var second = Double.parseDouble(secondField.getText());
            double result1 = first+second;
            fieldRes.setText(df.format(result1));     
        });
        btnSub.setOnAction((ActionEvent e) -> {
            var first = Double.parseDouble(firstField.getText());
            var second = Double.parseDouble(secondField.getText());
            double result1 = first-second;
            fieldRes.setText(df.format(result1));     
        });
        btnMul.setOnAction((ActionEvent e) -> {
            var first = Double.parseDouble(firstField.getText());
            var second = Double.parseDouble(secondField.getText());
            double result1 = first*second;
            fieldRes.setText(df.format(result1));    
        });
        btnDiv.setOnAction((ActionEvent e) -> {
            var first = Double.parseDouble(firstField.getText());
            var second = Double.parseDouble(secondField.getText());
            double result1 = first/second;
            fieldRes.setText(df.format(result1));     
        });
        
        
        scene = new Scene(layout, 300, 150);
        stage.setScene(scene);
        stage.show();
         
        
        
    }

    public static void main(String[] args) {
        launch();
    }

}

