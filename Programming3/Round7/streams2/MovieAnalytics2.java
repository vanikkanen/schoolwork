/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;
import java.util.stream.*;
import java.io.*;

public class MovieAnalytics2 {

     private ArrayList<Movie> data;
    
    
    MovieAnalytics2() {
        data = new ArrayList<>();
    }

    public void populateWithData(String filename) throws IOException {
        
        try(var br = new BufferedReader(new FileReader(filename))) {
            List<Movie> dataList = br.lines()
                    .map(line -> {
                        String[] movieData = line.split(";");
                        return new Movie(
                        movieData[0],
                        Integer.parseInt(movieData[1]),
                        Integer.parseInt(movieData[2]),
                        movieData[3],
                        Double.parseDouble(movieData[4]),
                        movieData[5]);
                    }).collect(Collectors.toList()); 
            data.addAll(dataList);
        }
    }
    
    public void printCountByDirector(int n) {
        data.stream()
            .collect(Collectors.groupingBy(Movie::getDirector, Collectors.counting()))
            .entrySet().stream()
            .sorted(Map.Entry.<String, Long>comparingByValue(Comparator.reverseOrder()).thenComparing(Map.Entry::getKey))
            .limit(n)
            .forEach(entry -> System.out.format("%s: %d movies%n", entry.getKey(), entry.getValue()));
    }
    
    public void printAverageDurationByGenre() {
        data.stream()
            .collect(Collectors.groupingBy(Movie::getGenre, Collectors.averagingInt(Movie::getDuration)))
            .entrySet().stream()
            .sorted(Map.Entry.<String, Double>comparingByValue().thenComparing(Map.Entry::getKey))
            .forEach(entry -> System.out.format("%s: %.2f%n", entry.getKey(), entry.getValue()));
    }
    
    public void printAverageScoreByGenre() {
        data.stream()
            .collect(Collectors.groupingBy(Movie::getGenre, Collectors.averagingDouble(Movie::getScore)))
            .entrySet().stream()
            .sorted(Map.Entry.<String, Double>comparingByValue().reversed().thenComparing(Map.Entry::getKey))
            .forEach(entry -> System.out.format("%s: %.2f%n", entry.getKey(), entry.getValue()));
    }
    
}
