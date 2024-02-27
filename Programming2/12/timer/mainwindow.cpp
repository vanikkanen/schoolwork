#include "mainwindow.hh"
#include "ui_mainwindow.h"
#include <QTimer>
#include <QObject>
#include <QApplication>
#include <QDebug>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{   
    timer = new QTimer(this);
    ui->setupUi(this);
    timer->setInterval(1000);
    connect(timer, SIGNAL(timeout()), this, SLOT(update_timers()));
    ui->lcdNumberMin->setPalette(Qt::green);
    ui->lcdNumberMin->setAutoFillBackground(true);

    ui->lcdNumberSec->setPalette(Qt::cyan);
    ui->lcdNumberSec->setAutoFillBackground(true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_resetButton_clicked()
{
    ui->lcdNumberMin->display(0);
    ui->lcdNumberSec->display(0);
}

void MainWindow::on_stopButton_clicked()
{
    timer->stop();
}

void MainWindow::update_timers()
{
    int secnum = ui->lcdNumberSec->intValue();
    int minnum = ui->lcdNumberMin->intValue();
    ++secnum;

    if (secnum == 60){
        ++minnum;
        secnum = 0;
        ui->lcdNumberMin->display(minnum);
    }
    ui->lcdNumberSec->display(secnum);
}


void MainWindow::on_startButton_clicked()
{
    timer->start();
}
