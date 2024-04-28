from PyQt6.QtWidgets import *
import re
import csv
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Basic function
        """
        super().__init__()
        self.__total_votes = {'No vote': 0, 'Dingas': 0, 'Pingas': 0, 'Wingas': 0, 'Zingas': 0}
        self.__age = None
        self.__name = None
        self.__SSN = None
        self.__vote = None
        self.setupUi(self)

        self.button_vote.clicked.connect(lambda: self.submit())
        self.button_exit.clicked.connect(lambda: self.exit())

    def submit(self):
        """
        Sets variables
        :return: Void function
        """
        self.__name = self.input_name.text()
        self.__age = self.input_age.text()
        self.__SSN = self.input_SSN.text()

        if self.check_information(self.__name, self.__age, self.__SSN):
            # Checking for vote
            if self.radio_candDingas.isChecked():
                self.__vote = 'Dingas'
            elif self.radio_candPingas.isChecked():
                self.__vote = 'Pingas'
            elif self.radio_candWingas.isChecked():
                self.__vote = 'Wingas'
            elif self.radio_candZingas.isChecked():
                self.__vote = 'Zingas'
            elif self.radio_candNoVote.isChecked():
                self.__vote = 'No vote'

            self.write(self.__name, self.__age, self.__SSN, self.__vote)
            self.label_agenda.setText('Voting successful. Thank you for your time.')

    def check_information(self, name, age, SSN):
        """
        Checks to see if submitted information is valid. Only returns True (valid) if all requirements are met.
        :param name: the name entered in the gui. No digits.
        :param age: the age entered in the gui. Must be between 18 - 120. Only digits.
        :param SSN: the SSN entered in the gui. Must be 9 characters. Only digits
        :return: True if requirements met. False otherwise
        """

        # Checking name
        if re.search(r'\d', name):
            self.label_agenda.setText('Name cannot contain digit')
            return False
        else:
            self.label_agenda.clear()

        # Checking age
        try:
            int(age)
        except ValueError:
            self.label_agenda.setText('Invalid age')
            return False
        else:
            self.label_agenda.clear()

            if int(age) > 120 or int(age) < 18:
                self.label_agenda.setText('Age must be between 18 - 120')
                return False

        # Checking SSN
        if not SSN.isdigit():
            self.label_agenda.setText('SSN must only be digits')
            return False
        if not len(SSN) == 9:
            self.label_agenda.setText('SSN must be 9 digits long')
            return False

        # Will return True ONLY if avoided all False returns
        return True


    def write(self, name, age, SSN, vote):
        """
        Writes the vote to votes.csv
        :param name: The name of the voter
        :param age: The age of the voter
        :param SSN: The SSN of the voter
        :param vote: The vote of the voter
        :return: Void function
        """
        with open('votes.csv', 'a') as f:
            f.write(name.capitalize())
            f.write(',')
            f.write(age)
            f.write(',')
            f.write(SSN)
            f.write(',')
            f.write(vote)
            f.write(',')
            f.write('valid')
            f.write('\n')

    def exit(self):
        """
        Reads the csv file and counts up votes. Exits program.
        """

        with open('votes.csv') as f:
            for i in f.readlines():
                vote = i.split(',')[3]
                if vote == 'No vote':
                    self.__total_votes[vote] += 1
                if vote == 'Dingas':
                    self.__total_votes[vote] += 1
                elif vote == 'Pingas':
                    self.__total_votes[vote] += 1
                elif vote == 'Wingas':
                    self.__total_votes[vote] += 1
                elif vote == 'Zingas':
                    self.__total_votes[vote] += 1

            print('No vote: ', end='')
            print(self.__total_votes['No vote'])
            print('Dingas: ', end='')
            print(self.__total_votes['Dingas'])
            print('Pingas: ', end='')
            print(self.__total_votes['Pingas'])
            print('Wingas: ', end='')
            print(self.__total_votes['Wingas'])
            print('Zingas: ', end='')
            print(self.__total_votes['Zingas'])

            exit()

