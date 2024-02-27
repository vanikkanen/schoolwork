/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Other/File.java to edit this template
 */

/**
 *
 * @author vanik
 */

import java.io.*;
import java.util.*;

public class WordGame {
    
    private ArrayList<String> words = new ArrayList<>();
    private boolean is_game_active = false;
    private WordGameState activeGame;
    private String wordToGuess = "";
    
    static class WordGameState {
        
        private String word;
        private int mistakes = 0;
        private int mistakeLimit;
        private int missingChars;
        
        private WordGameState(String word, int mistakeLimit){
            this.word = word;
            this.mistakeLimit = mistakeLimit;
        }
        
        public String getWord() {
            return word;
        }
        public int getMistakes() {
            return mistakes;
        }
        public int getMistakeLimit() {
            return mistakeLimit;
        }
        public int getMissingChars() {
            return missingChars;
        }
    }
    
    public WordGame(String filename) throws FileNotFoundException, IOException {
        
        try(var input = new BufferedReader(new FileReader(filename))) {
            
            String line;
             
            while ((line = input.readLine()) != null) {
                words.add(line);
            }
    
        }
    }
    
    public void initGame(int wordIndex, int mistakeLimit) {
        is_game_active = true;
        wordToGuess = words.get(wordIndex % words.size());
        String wordToPass = "_".repeat(wordToGuess.length());
        activeGame = new WordGameState(wordToPass,mistakeLimit);
        
        activeGame.missingChars = wordToGuess.length();

    }
    public boolean isGameActive() {
        return is_game_active;
    }
    
    public WordGameState getGameState() throws GameStateException {
        if (!is_game_active) {
            throw new GameStateException("There is currently no active word game!");
        }
        else {
            return activeGame;
        }
    }
    
    public WordGameState guess(char c) throws GameStateException {
        if (!is_game_active) {
            throw new GameStateException("There is currently no active word game!");
        }
        else {
            boolean guess_correct = false;
            String new_word_state = "";
            for (int i = 0; i < wordToGuess.length(); ++i) {
                if (activeGame.word.charAt(i) == Character.toLowerCase(c)) {
                    break;
                }
                else if (wordToGuess.charAt(i) == Character.toLowerCase(c)) {
                    guess_correct = true;
                    activeGame.missingChars -= 1;
                    new_word_state += Character.toLowerCase(c);
                }
                else {
                    new_word_state += activeGame.word.charAt(i);
                }
            }
            if (guess_correct) {
                activeGame.word = new_word_state;
                if (activeGame.missingChars == 0) {
                    is_game_active = false;
                }
            }
            else {
                activeGame.mistakes += 1;
                if (activeGame.mistakes  > activeGame.mistakeLimit) {
                    is_game_active = false;
                    activeGame.word = wordToGuess;
                }
            }
            return activeGame;
        }   
    }
    
    public WordGameState guess(String word) throws GameStateException {
        if (!is_game_active) {
            throw new GameStateException("There is currently no active word game!");
        }
        else {
            if (word.equals(wordToGuess)) {
                activeGame.missingChars = 0;
                activeGame.word = wordToGuess;
                is_game_active = false;
            }
            else {
                activeGame.mistakes += 1;
                if (activeGame.mistakes > activeGame.mistakeLimit) {
                    is_game_active = false;
                    activeGame.word = wordToGuess;
                }
            }
            return activeGame;
        }
    }
       
}
