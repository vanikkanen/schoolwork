#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include <QDebug>
#include <string>
#include <cmath>

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

void MainWindow::on_countButton_clicked()
{
    double weight = ui->weightLineEdit->text().toInt();
    double height = ui->heightLineEdit->text().toInt();

    double bmi = weight/pow((height/100), 2);
    ui->resultLabel->setText(QString::number(bmi));

    if (bmi < 18.5) {
        ui->infoTextBrowser->setText("You are underweight.");
    } else if (bmi > 25) {
        ui->infoTextBrowser->setText("You are overweight.");
    } else {
        ui->infoTextBrowser->setText("Your weight is normal.");
    }
}
