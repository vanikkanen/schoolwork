/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
import java.util.*;
import java.io.*;
import java.util.stream.Stream;
import java.util.function.Consumer;
        
public class MovieAnalytics {

    private ArrayList<Movie> data;
    
    
    MovieAnalytics() {
        data = new ArrayList<>();
    }

    public void populateWithData(String filename) {
        
        try(var file = new BufferedReader(new FileReader(filename))) {
            String line;
            String[] movieData;
            while((line = file.readLine()) != null) {
                movieData = line.split(";");           
                data.add(new Movie(movieData[0],Integer.parseInt(movieData[1]),Integer.parseInt(movieData[2]),movieData[3],Double.parseDouble(movieData[4]),movieData[5]));
            }
        }
        catch(Exception e) {
            System.out.println("File error");
        }
    }

    public static Consumer<Movie> showInfo()  {
         Consumer<Movie> consumer = (Movie m) -> System.out.println(m.getTitle() + " (By " + m.getDirector() + ", " + m.getReleaseYear() + ")");
         return consumer;
    }

    public Stream<Movie> moviesAfter(int year) {
        return data.stream()
                .filter(movie -> movie.getReleaseYear() >= year)
                .sorted(Comparator.comparingInt(Movie::getReleaseYear).thenComparing(Movie::getTitle));

    }
    
    public Stream<Movie> moviesBefore(int year) {
        return data.stream()
                .filter(movie -> movie.getReleaseYear() <= year)
                .sorted(Comparator.comparingInt(Movie::getReleaseYear).thenComparing(Movie::getTitle));
                              
    }
    
    public Stream<Movie> moviesBetween(int yearA, int yearB) {
        return data.stream()
                .filter((movie) -> (movie.getReleaseYear() >= yearA && movie.getReleaseYear() <= yearB))
                .sorted(Comparator.comparingInt(Movie::getReleaseYear).thenComparing(Movie::getTitle));
    }
    
    public Stream<Movie> moviesByDirector(String director) {
        return data.stream()
                .filter((movie) -> (director.equals(movie.getDirector())))
                .sorted(Comparator.comparingInt(Movie::getReleaseYear).thenComparing(Movie::getTitle));
    } 
}
