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

public class Standings {
    
    private ArrayList<Team> teams = new ArrayList<>();

    public static class Team {
        
        private String name;
        private int wins = 0;
        private int ties = 0;
        private int losses = 0;
        private int scored = 0;
        private int allowed = 0;
        private int points = 0;
         
        public Team(String team_name){
            name = team_name;
        }
        
        public int getWins() {
            return this.wins;
        }
        public int getTies() {
            return this.ties;
        }
        public int getLosses() {
            return this.losses;
        }
        public int getScored() {
            return this.scored;
        }
        public int getAllowed() {
            return this.allowed;
        }
        public int getPoints() {
            return this.points;
        }
        public String getName() {
            return this.name;
        }   
    }
    
    public Standings() {
        
    }
    
    public Standings(String filename) throws IOException {
        readMatchData(filename);
    }
    
    public void readMatchData(String filename) throws FileNotFoundException, IOException {
        
         try(var input = new BufferedReader(new FileReader(filename))) {
            
             String line;
             
             while ((line = input.readLine()) != null) {
                String[] data = line.split("\\t");
                
                String teamA = data[0];
                String teamB = data[2];
                String[] scores = data[1].split("-");
                int scoreA = Integer.parseInt(scores[0]);
                int scoreB = Integer.parseInt(scores[1]);
                
                addMatchResult(teamA, scoreA, scoreB, teamB);
                
            }
        }
    }
    
    public void addMatchResult(String teamA,int scoreA, int scoreB, String teamB) {
 
        Boolean notfoundA = true;
        Boolean notfoundB = true;
        
        for (Team team : teams){
            
            if (team.name.equals(teamA)) {
                updateTeam(team, scoreA, (scoreA>scoreB), scoreB, (scoreA == scoreB));
                notfoundA = false;
            }
            else if (team.name.equals(teamB)) {
                updateTeam(team, scoreB, (scoreB>scoreA), scoreA, (scoreB == scoreA));
                notfoundB = false;
            }
        }
        if (notfoundA) {
            Team new_team = new Team(teamA);
            updateTeam(new_team, scoreA, (scoreA>scoreB), scoreB, (scoreA == scoreB));
            teams.add(new_team);
        }
        if (notfoundB) {
            Team new_team = new Team(teamB);
            updateTeam(new_team, scoreB, (scoreB>scoreA), scoreA, (scoreB == scoreA));
            teams.add(new_team);
        }
    }
    
    public ArrayList<Team> getTeams() {
        
        teams.sort(
        Comparator.comparing((Team t) -> t.points)
                .thenComparing(t -> (t.scored - t.allowed))
                .thenComparingInt(t -> t.scored)
                .thenComparing(t -> t.name)
                .reversed()

        );
        return teams;
    }
        
    public void printStandings() {
        ArrayList<Team> sorted = getTeams();
        
        int max_size = 0;
        for (Team team : sorted) {
            if (team.name.length() > max_size)
                max_size = team.name.length();
        }
        for (Team team : sorted) {
            // Team name
            System.out.format("%" + -max_size + "s", team.name);
            // Matches, Wins, Ties, Losses
            System.out.format("%4d%4d%4d%4d", (team.wins + team.ties + team.losses), team.wins, team.ties, team.losses);
            //Scored-Allowed
            String score = Integer.toString(team.getScored()) + "-" + Integer.toString(team.getAllowed());
            System.out.format("%7s", score);
            //Points
            System.out.format("%4d%n", team.getPoints());
        }
    }  
    
     private void updateTeam(Team t, int goals, boolean win, int allowed_goals, boolean tie) {
            
            if (win) {
                ++t.wins;
                t.points += 3;
            }
            else if (tie) {
                ++t.ties;
                t.points += 1;
            }
            else {
                ++t.losses;
            }
            t.scored += goals;
            t.allowed += allowed_goals;
     }
     /*
    public static void main(String[] args)

        throws FileNotFoundException, IOException {
        Standings standings = new Standings();
        standings.addMatchResult("Brazil", 0, 3, "Cook Islands");
        standings.addMatchResult("Samoa", 3, 2, "American Samoa");
        standings.addMatchResult("Cook Islands", 1, 0, "Samoa");
        standings.addMatchResult("Tonga", 1, 2, "American Samoa");
        standings.addMatchResult("Tonga", 0, 3, "Samoa");
        standings.addMatchResult("American Samoa", 2, 0, "Cook Islands");
        standings.printStandings();
    
  }

*/
}
