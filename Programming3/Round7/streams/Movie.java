/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */
public class Movie {

    private String title;
    private int releaseYear;
    private int duration;
    private String genre;
    private double score;
    private String director;
    
    Movie (String title, int releaseYear, int duration, String genre, double score, String director) {
        this.title = title;
        this.releaseYear = releaseYear;
        this.duration = duration;
        this.genre = genre;
        this.score = score;
        this.director = director;
    }
    
    public String getTitle() {
        return title;
    }
    
    public int getReleaseYear() {
        return releaseYear;
    }
    
    public int getDuration() {
        return duration;
    }
    
    public String getGenre() {
        return genre;
    }
    
    public double getScore() {
        return score;
    }
    
    public String getDirector() {
        return director;
    }
    
}
