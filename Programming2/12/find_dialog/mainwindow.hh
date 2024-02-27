#ifndef MAINWINDOW_HH
#define MAINWINDOW_HH

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:


    void on_findPushButton_clicked();

private:
    Ui::MainWindow *ui;
    
    std::vector<std::string> string_to_vector(std::string str)
    {
        std::vector<std::string> words;
        std::string new_word = "";
        std::string::size_type line_length = str.size();
        std::string::size_type i = 0;
        char c;
        
        for (i = 0; i < line_length; ++i)
        {
            c = str.at(i);
            if (c == ' ')
            {
                words.push_back(new_word);
                new_word = "";
            }
            else
                new_word += c;
        }
        if (new_word != "")
            words.push_back(new_word);
        
        return words;
    }

    QString to_upper(std::string word)
    {
        QString new_word = "";
        std::string::size_type line_length = word.size();
        std::string::size_type i = 0;
        char c;

        for (i = 0; i < line_length; ++i)
        {
            c = word.at(i);
            new_word += toupper(c);
        }
        return new_word;
    }
};
#endif // MAINWINDOW_HH
