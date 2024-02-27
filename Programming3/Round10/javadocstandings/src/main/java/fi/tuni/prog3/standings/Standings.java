
package fi.tuni.prog3.standings;


import java.util.*;
import java.io.*;

/**
 * A class for maintaining team statistics and standings. Team standings are determined by the following rules:
 * <ul>
 *      <li>Primary rule: points total. Higher points come first.</li>
 *      <li>Secondary rule: goal difference (scored minus allowed). Higher difference comes first.</li>
 *      <li>Tertiary rule: number of goals scored. Higher number comes first.</li>
 *      <li>Last rule: natural String order of team names.</li>
 * </ul>    
 */
public class Standings {
    
    private ArrayList<Team> teams = new ArrayList<>();

    /**
     * A class for storing statistics of a single team. The class offers only public getter functions. The enclosing class Standings is responsible for setting and updating team statistics.
     */
    public static class Team {
        
        private String name;
        private int wins = 0;
        private int ties = 0;
        private int losses = 0;
        private int scored = 0;
        private int allowed = 0;
        private int points = 0;
         
        /**
         * Constructs a Team object for storing statistics of the named team.
         * @param name the name of the team whose statistics the new team object stores.
         */
        public Team(String name){
            this.name = name;
        }
        
        /**
         * Returns the name of the team.
         * @return the name of the team.
         */
        public String getName() {
            return this.name;
        }
        
        /**
         * Returns the number of wins of the team.
         * @return the number of wins of the team.
         */
        public int getWins() {
            return this.wins;
        }
        
        /**
         * Returns the number of ties of the team.
         * @return the number of ties of the team.
         */
        public int getTies() {
            return this.ties;
        }
        
        /**
         * Returns the number of losses of the team.
         * @return the number of losses of the team.
         */
        public int getLosses() {
            return this.losses;
        }
        
        /**
         * Returns the number of goals scored by the team.
         * @return the number of goals scored by the team.
         */
        public int getScored() {
            return this.scored;
        }
        
        /**
         * Returns the number of goals allowed (conceded) by the team.
         * @return the number of goals allowed (conceded) by the team.
         */
        public int getAllowed() {
            return this.allowed;
        }
        
        /**
         * Returns the overall number of points of the team.
         * @return the overall number of points of the team.
         */
        public int getPoints() {
            return this.points;
        }

    }
    /**
     * Constructs an empty Standings object.
     */
    public Standings() {
        
    }
    
    /**
     * Constructs a Standings object that is initialized with the game data read from the specified file. The result is identical to first constructing an empty Standing object and then calling readMatchData(filename).
     * @param filename the name of the game data file to read.
     * @throws IOException if there is some kind of an IO error (e.g. if the specified file does not exist).
     */
    public Standings(String filename) throws IOException {
        readMatchData(filename);
    }
    
    /**
     * <p>Reads game data from the specified file and updates the team statistics and standings accordingly.</p>
     * <p>The match data file is expected to contain lines of form "teamNameA\tgoalsA-goalsB\tteamNameB". Note that the '\t' are tabulator characters.</p>
     * <p>E.g. the line "Iceland\t3-2\tFinland" would describe a match between Iceland and Finland where Iceland scored 3 and Finland 2 goals.</p>
     * @param filename the name of the game data file to read.
     * @throws IOException if there is some kind of an IO error (e.g. if the specified file does not exist).
     */
    public final void readMatchData(String filename) throws IOException {
        
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
    
    /**
     * Updates the team statistics and standings according to the match result described by the parameters.
     * @param teamNameA the name of the first ("home") team.
     * @param goalsA the number of goals scored by the first team.
     * @param goalsB the number of goals scored by the second team.
     * @param teamNameB the name of the second ("away") team.
     */
    public void addMatchResult(String teamNameA,int goalsA, int goalsB, String teamNameB) {
 
        Boolean notfoundA = true;
        Boolean notfoundB = true;
        
        for (Team team : teams){
            
            if (team.name.equals(teamNameA)) {
                updateTeam(team, goalsA, (goalsA>goalsB), goalsB, (goalsA == goalsB));
                notfoundA = false;
            }
            else if (team.name.equals(goalsB)) {
                updateTeam(team, goalsB, (goalsB>goalsA), goalsA, (goalsB == goalsA));
                notfoundB = false;
            }
        }
        if (notfoundA) {
            Team new_team = new Team(teamNameA);
            updateTeam(new_team, goalsA, (goalsA>goalsB), goalsB, (goalsA == goalsB));
            teams.add(new_team);
        }
        if (notfoundB) {
            Team new_team = new Team(teamNameB);
            updateTeam(new_team, goalsB, (goalsB>goalsA), goalsA, (goalsB == goalsA));
            teams.add(new_team);
        }
    }
    
    /**
     * Returns a list of the teams in the same order as they would appear in a standings table.
     * @return a list of the teams in the same order as they would appear in a standings table.
     */
    public List<Team> getTeams() {
        teams.sort(
        Comparator.comparing((Team t) -> t.points)
                .thenComparing(t -> (t.scored - t.allowed))
                .thenComparingInt(t -> t.scored)
                .thenComparing(t -> t.name)
                .reversed()

        );
        return teams;
    }
        
    /**
     * Prints a formatted standings table to the provided output stream.
     * @param out the output stream to use when printing the standings table.
     */
    public void printStandings(PrintStream out) {
        
        List<Team> sorted = getTeams();
        
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
}

