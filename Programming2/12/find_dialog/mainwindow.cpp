#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include <QDebug>
#include <QString>
#include <iostream>
#include <fstream>

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_findPushButton_clicked()
{
    QString filename = ui->fileLineEdit->text();
    QString keyword = ui->keyLineEdit->text();
    std::ifstream file(filename.toStdString());

    if (not file)
    {
        ui->textBrowser->setText("File not found");
         //qDebug() << "File not found";
    }

    else if (keyword == "")
    {
        ui->textBrowser->setText("File found");
        //qDebug() << "File found";
    }

    else
    {
        std::string line = "";
        bool word_found = false;
        while (getline(file, line) and !word_found)
        {
            std::vector<std::string> words;
            words = string_to_vector(line);
            
            for (auto word : words)
            {
                QString qword = QString::fromStdString(word);

                if(!(ui->matchCheckBox->isChecked()))
                {
                    keyword = to_upper(keyword.toStdString());
                    qword = to_upper(word);
                }

                if (keyword == qword)
                {
                    ui->textBrowser->setText("Word found");
                    word_found = true;
                    //qDebug() << "Word found";
                    break;
                }
            }
        }
        if(!word_found)
        {
            ui->textBrowser->setText("Word not found");
            //qDebug() << "Word not found";
        }
    }
    file.close();
}
