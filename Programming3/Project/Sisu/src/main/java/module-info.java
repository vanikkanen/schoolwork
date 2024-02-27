module fi.tuni.prog3.sisu {
    requires javafx.controls;
    requires javafx.fxml;
    requires com.google.gson;
    requires javafx.web;
    requires org.jsoup;
    requires com.fasterxml.jackson.core;
    requires com.fasterxml.jackson.databind;
    
    
    opens fi.tuni.prog3.sisu to javafx.fxml;
    exports fi.tuni.prog3.sisu;
    
}
