
/* Muistipeli
 *
 * Kuvaus (Kopioitu tehtävän annosta, https://plus.tuni.fi/comp.cs.110/spring-2021/rounds_r04/r04_08_pairs/#chapter-exercise-1):
 *  Ohjelma toteuttaa muistipelin. Pelissä on vaihteleva määrä kortteja ja
 * pelaajia. Pelin alussa käyttäjältä kysytään myös siemenluku, koska kortit
 * arvotaan satunnaisesti pelilaudalle.
 *  Joka kierroksella vuorossa oleva pelaaja antaa kahden kortin
 * koordinaatit (yhteensä neljä lukua), minkä jälkeen kyseiset kortit
 * käännetään näkyviin ja kerrotaan, ovatko ne parit vai ei.
 * Jos pelaaja sai parit, kortit poistetaan pelilaudalta, pelaajan
 * pistesaldoa kasvatetaan, ja hän saa uuden vuoron. Jos pelaaja ei saanut
 * pareja, kortit käännetään takaisin piiloon, ja vuoro siirtyy seuraavalle
 * pelaajalle.
 *  Ohjelma tarkistaa pelaajan antamat koordinaatit. Koordinaattien pitää
 * olla sellaiset, että niiden määräämä kortti löytyy pelilaudalta.
 *  Muutosten jälkeen pelilauta tulostetaan aina uudelleen. Kortit kuvataan
 * kirjaimina alkaen A:sta niin pitkälle, kuin kortteja on. Kun pelilauta
 * tulostetaan, näkyvissä oleva kortti kuvataan kyseisellä kirjaimella.
 * Piiloon käännettyä korttia kuvaa risuaita (#), ja laudalta poistetun
 * kortin kohdalle tulostetaan piste.
 *  Peli päättyy, kun kaikki parit on löydetty, ja pelilauta on tyhjä.
 * Tällöin kerrotaan, kuka tai ketkä voittivat eli saivat eniten pareja.
 *
 * Ohjelman kirjoittajat
 * Nimet: Valtteri Nikkanen, Atte Harmoinen
 * Opiskelijanumerot: 282688, 284930
 * Käyttäjätunnus: nikkanev (Koodi on tehty tällä), harmoine
 * E-Mail: valtteri.nikkanen@tuni.fi, atte.harmoinen@tuni.fi
 *
 * Huomioita ohjelmasta ja sen toteutuksesta:
 *
 * */

#include <player.hh>
#include <card.hh>
#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

const string INPUT_AMOUNT_OF_CARDS = "Enter the amount of cards (an even number): ";
const string INPUT_SEED = "Enter a seed value: ";
const string INPUT_AMOUNT_OF_PLAYERS = "Enter the amount of players (one or more): ";
const string INPUT_CARDS = "Enter two cards (x1, y1, x2, y2), or q to quit: ";
const string INVALID_CARD = "Invalid card.";
const string FOUND = "Pairs found.";
const string NOT_FOUND = "Pairs not found.";
const string GIVING_UP = "Why on earth you are giving up the game?";
const string GAME_OVER = "Game over!";

using Game_row_type = vector<Card>;
using Game_board_type = vector<vector<Card>>;

using Player_list = vector<Player>;

// Muuntaa annetun numeerisen merkkijonon vastaavaksi kokonaisluvuksi
// (kutsumalla stoi-funktiota).
// Jos annettu merkkijono ei ole numeerinen, palauttaa nollan
// (mikä johtaa laittomaan korttiin myöhemmin).
//
// Converts the given numeric string to the corresponding integer
// (by calling stoi).
// If the given string is not numeric, returns 0
// (which leads to an invalid card later).
unsigned int stoi_with_check(const string& str)
{
    bool is_numeric = true;
    for(unsigned int i = 0; i < str.length(); ++i)
    {
        if(not isdigit(str.at(i)))
        {
            is_numeric = false;
            break;
        }
    }
    if(is_numeric)
    {
        return stoi(str);
    }
    else
    {
        return 0;
    }
}

// Täyttää pelilaudan (kooltaan rows * columns) tyhjillä korteilla.
//
// Fills the game board, the size of which is rows * columns, with empty cards.
void init_with_empties(Game_board_type& g_board, unsigned int rows, unsigned int columns)
{
    g_board.clear();
    Game_row_type row;
    for(unsigned int i = 0; i < columns; ++i)
    {
        Card card;
        row.push_back(card);
    }
    for(unsigned int i = 0; i < rows; ++i)
    {
        g_board.push_back(row);
    }
}

// Etsii seuraavan tyhjän kohdan pelilaudalta (g_board) aloittamalla
// annetusta kohdasta start ja jatkamalla tarvittaessa alusta.
// (Kutsutaan vain funktiosta init_with_cards.)
//
// Finds the next free position in the game board (g_board), starting from the
// given position start and continuing from the beginning if needed.
// (Called only by the function init_with_cards.)
unsigned int next_free(Game_board_type& g_board, unsigned int start)
{
    // Selvitetään annetun pelilaudan rivien ja sarakkeiden määrät
    //
    // Finding out the number of rows and columns of the game board
    unsigned int rows = g_board.size();
    unsigned int columns = g_board.at(0).size();

    // Aloitetaan annetusta arvosta
    //
    // Starting from the given value
    for(unsigned int i = start; i < rows * columns; ++i)
    {
        if(g_board.at(i / columns).at(i % columns).get_visibility() == EMPTY) // vaihdettu
        {
            return i;
        }
    }
    // Jatketaan alusta
    //
    // Continuing from the beginning
    for(unsigned int i = 0; i < start; ++i)
    {
        if(g_board.at(i / columns).at(i % columns).get_visibility() == EMPTY)
        {
            return i;
        }
    }
    // Tänne ei pitäisi koskaan päätyä
    //
    // You should never reach this
    std::cout << "No more empty spaces" << std::endl;
    return rows * columns - 1;
}

// Alustaa annetun pelilaudan (g_board) satunnaisesti arvotuilla korteilla
// annetun siemenarvon (seed) perusteella.
//
// Initializes the given game board (g_board) with randomly generated cards,
// based on the given seed value.
void init_with_cards(Game_board_type& g_board, int seed)
{
    // Selvitetään annetun pelilaudan rivien ja sarakkeiden määrät
    //
    // Finding out the number of rows and columns of the game board
    unsigned int rows = g_board.size();
    unsigned int columns = g_board.at(0).size();

    // Arvotaan täytettävä sijainti
    //
    // Drawing a cell to be filled
    std::default_random_engine randomEng(seed);
    std::uniform_int_distribution<int> distr(0, rows * columns - 1);
    // Hylätään ensimmäinen satunnaisluku (joka on aina jakauman alaraja)
    //
    // Wiping out the first random number (that is always the lower bound of the distribution)
    distr(randomEng);

    // Jos arvotussa sijainnissa on jo kortti, valitaan siitä seuraava tyhjä paikka.
    // (Seuraava tyhjä paikka haetaan kierteisesti funktion next_free avulla.)
    //
    // If the drawn cell is already filled with a card, next empty cell will be used.
    // (The next empty cell is searched for circularly, see function next_free.)
    for(unsigned int i = 0, c = 'A'; i < rows * columns - 1; i += 2, ++c)
    {
        // Lisätään kaksi samaa korttia (parit) pelilaudalle
        //
        // Adding two identical cards (pairs) in the game board
        for(unsigned int j = 0; j < 2; ++j)
        {
            unsigned int cell = distr(randomEng);
            cell = next_free(g_board, cell);
            g_board.at(cell / columns).at(cell % columns).set_letter(c);
            g_board.at(cell / columns).at(cell % columns).set_visibility(HIDDEN);
        }
    }
}

// Tulostaa annetusta merkistä c koostuvan rivin,
// jonka pituus annetaan parametrissa line_length.
// (Kutsutaan vain funktiosta print.)
//
// Prints a line consisting of the given character c.
// The length of the line is given in the parameter line_length.
// (Called only by the function print.)
void print_line_with_char(char c, unsigned int line_length)
{
    for(unsigned int i = 0; i < line_length * 2 + 7; ++i)
    {
        cout << c;
    }
    cout << endl;
}

// Tulostaa vaihtelevankokoisen pelilaudan reunuksineen.
//
// Prints a variable-length game board with borders.
void print(const Game_board_type& g_board)
{
    // Selvitetään annetun pelilaudan rivien ja sarakkeiden määrät
    //
    // Finding out the number of rows and columns of the game board
    unsigned int rows = g_board.size();
    unsigned int columns = g_board.at(0).size();

    print_line_with_char('=', columns);
    cout << "|   | ";
    for(unsigned int i = 0; i < columns; ++i)
    {
        cout << i + 1 << " ";
    }
    cout << "|" << endl;
    print_line_with_char('-', columns);
    for(unsigned int i = 0; i < rows; ++i)
    {
        cout << "| " << i + 1 << " | ";
        for(unsigned int j = 0; j < columns; ++j)
        {
            g_board.at(i).at(j).print();
            cout << " ";
        }
        cout << "|" << endl;
    }
    print_line_with_char('=', columns);
}

// Kysyy käyttäjältä tulon ja sellaiset tulon tekijät, jotka ovat
// mahdollisimman lähellä toisiaan.
//
// Asks the desired product from the user, and calculates the factors of
// the product such that the factor as near to each other as possible.
void ask_product_and_calculate_factors(unsigned int& smaller_factor, unsigned int& bigger_factor)
{
    unsigned int product = 0;
    while(not (product > 0 and product % 2 == 0))
    {
        std::cout << INPUT_AMOUNT_OF_CARDS;
        string product_str = "";
        std::getline(std::cin, product_str);
        product = stoi_with_check(product_str);
    }

    for(unsigned int i = 1; i * i <= product; ++i)
    {
        if(product % i == 0)
        {
            smaller_factor = i;
        }
    }
    bigger_factor = product / smaller_factor;
}

// Lisää funktioita
// More functions

// Kysyy ja lisää halutun määrän pelaajia peliin. Tallentaa pelaajat pelaaja listaan.
void add_players(Player_list& list)
{
    unsigned int nro_players = 0;
    while (nro_players < 1)
    {
        std::cout << INPUT_AMOUNT_OF_PLAYERS;
        string string_nro_players = "";
        std::getline(std::cin, string_nro_players);
        nro_players = stoi_with_check(string_nro_players);
    }
    std::cout << "List " << nro_players << " players: ";
    string i = "";
    unsigned int checker = 0;
    while (std::cin >> i)
    {
        string player_name = i;
        Player player(player_name);
        list.push_back(player);
        ++checker;

        if (checker == nro_players)
            break;
    }
}

// Tarkistaa koordinaattien oikeellisuuden.
bool check_coords(unsigned int& y_factor, unsigned int& x_factor, vector<string> parts)
{
    bool is_x = true;

    for (auto part : parts)
    {

        unsigned int coord = stoi_with_check(part);

        if (is_x)
        {
            if (coord > x_factor or coord == 0)
            {
                return true;
            }
          is_x = false;
        }
        else
        {
            if (coord > y_factor or coord == 0)
            {
                return true;
            }
          is_x = true;
        }
    }
    return false;
}

// Tarkistaa onko kaikki parit löydetty ja peli sen takia ohi.
bool is_game_over(Player_list& list, int pairs)
{
    int found_pairs = 0;

    for (auto player : list)
    {
        found_pairs += player.number_of_pairs();
    }

    if (found_pairs == pairs)
        return true;
    else
        return false;
}

int main()
{
    Game_board_type game_board;
    Player_list player_list;

    unsigned int factor1 = 1, factor2 = 1;
    ask_product_and_calculate_factors(factor1, factor2);
    init_with_empties(game_board, factor1, factor2);

    string seed_str = "";
    std::cout << INPUT_SEED;
    std::getline(std::cin, seed_str);
    int seed = stoi_with_check(seed_str);
    init_with_cards(game_board, seed);

    add_players(player_list);
    std::cin.ignore();

    print(game_board);

    int x_1, y_1, x_2, y_2;
    int pairs_in_play = (factor1*factor2)/2;

    std::vector<Player>::size_type in_turn = 0;

    // Pelin main-loop
    bool game_is_on = true;
    while (game_is_on)
    {
        // Kortin valitsemisen loop
        bool picking_cards = true;
        while (picking_cards)
        {
            //Koordinaattien valitsemisen ja tarkastamisen loop
            bool not_valid_coords = true;
            while (not_valid_coords)
            {
                std::cout << player_list.at(in_turn).get_name() << ": ";
                std::string cards = "";
                std::cout << INPUT_CARDS;
                std::getline(std::cin, cards);
                if (cards.at(0) == 'q')
                {
                    std::cout << GIVING_UP << std::endl;
                    return EXIT_SUCCESS;
                }
                std::vector<std::string> parts;
                std::string::size_type line_length = cards.size();
                string line_char;
                std::string part = "";

                for (std::string::size_type i = 0; i < line_length; ++i)
                {
                    line_char = cards.at(i);

                    if (line_char == " ")
                    {
                        parts.push_back(part);
                        part = "";
                        continue;
                    }
                    else
                    {
                       part += line_char;
                    }
                }
                parts.push_back(part);

                x_1 = stoi_with_check(parts.at(0)) - 1;
                y_1 = stoi_with_check(parts.at(1)) - 1;
                x_2 = stoi_with_check(parts.at(2)) - 1;
                y_2 = stoi_with_check(parts.at(3)) - 1;

                not_valid_coords = check_coords(factor1, factor2, parts);

                if (not_valid_coords or (x_1  == x_2 and y_1 == y_2))
                {
                    std::cout << INVALID_CARD << std::endl;
                    not_valid_coords = true;
                    continue;
                }
            }

            if (game_board.at(y_1).at(x_1).get_visibility() == EMPTY or game_board.at(y_2).at(x_2).get_visibility() == EMPTY)
            {
                std::cout << INVALID_CARD << std::endl;
                continue;
            }

            //Käännetään valitut kortit
            game_board.at(y_1).at(x_1).turn();
            game_board.at(y_2).at(x_2).turn();
            picking_cards = false;
        }
        print(game_board);
        //Tarkastetaan onko pari ja lisätään kortit jos oli ja jos ei niin käännetään kortit
        if (game_board.at(y_1).at(x_1).get_letter() == game_board.at(y_2).at(x_2).get_letter())
        {
            std::cout << FOUND << std::endl;
            player_list.at(in_turn).add_card(game_board.at(y_1).at(x_1));
            player_list.at(in_turn).add_card(game_board.at(y_2).at(x_2));
        }
        else
        {
            std::cout << NOT_FOUND << std::endl;
            game_board.at(y_1).at(x_1).turn();
            game_board.at(y_2).at(x_2).turn();
        }

        //Tulostetaan pistetilanne
        for ( auto player : player_list)
            std::cout << "*** " << player.get_name() << " has " << player.number_of_pairs() << " pair(s)." << std::endl;

        print(game_board);

        //Jos oli pari niin tarkastetaan loppuuko peli jos loppuu tulostetaan tarvittavat tiedot
        //ja jos ei niin jatketaan saman pelaajan vuoroa
        if (game_board.at(y_1).at(x_1).get_letter() == game_board.at(y_2).at(x_2).get_letter())
        {
            bool is_over = false;
            is_over = is_game_over(player_list, pairs_in_play);
            if (is_over)
            {
                std::cout << GAME_OVER << std::endl;

                vector<int> player_scores;
                for (auto player : player_list)
                {
                    player_scores.push_back(player.number_of_pairs());
                }
                auto max_score = max_element(player_scores.begin(), player_scores.end());

                int max_score_count = count(player_scores.begin(), player_scores.end(), *max_score);

                if (max_score_count > 1)
                    std::cout << "Tie of " << max_score_count << " players with " << *max_score << " pairs." << std::endl;
                else
                {
                    auto it = find(player_scores.begin(), player_scores.end(), *max_score);
                    int index = it - player_scores.begin();
                    std::cout << player_list.at(index).get_name() << " has won with " << *max_score << " pairs." << std::endl;
                }

                return EXIT_SUCCESS;
            }
            else
            {
                continue;
            }

        }
        //Siirretään vuoro seuraavalle pelaajalle
        ++in_turn;
        if (in_turn > player_list.size() - 1)
            in_turn = 0;
    }

    return EXIT_SUCCESS;
}

