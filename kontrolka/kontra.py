"""
Дан каталог книг. Про книгу  известно: уникальный номер, автор, название,
год издания. Реализовать CRUD(создание-чтение-изменение-удаление),
показ всех книг на экран и поиск по каждому из полей.
Учитывать, что каждое поле соответствует определенному типу данных.
"""


class Catalog(object):

    books = list()

    def search_for(self):
        # print the search menu
        print('-------------------------------')
        print(' Search in')
        print('-------------------------------')
        print(' 1 - Authors')
        print(' 2 - Titles')
        print(' 3 - Year')
        print(' 4 - Exit')
        searchin = input('Enter Search Type -> ')
        if searchin != '4' and searchin == '1':
            key = input('Enter author: ')
            for i in range(len(self.books)):
                if key in self.books[i][0]:
                    au = list()
                    au.append(self.books[i])
                    print(au)
        elif searchin == '2':
            key = input('Enter title -> ')
            for i in range(len(self.books)):
                if key in self.books[i][1]:
                    au = list()
                    au.append(self.books[i])
                    print(au)
        elif searchin == '3':
            key = input('Enter year -> ')
            for i in range(len(self.books)):
                if key in self.books[i][2]:
                    au = list()
                    au.append(self.books[i])
                    print(au)
        elif searchin == '4':
            print('Exiting')
        else:
            print('Wtf? Try again..')

    def add_a_book(self):
        loop = True
        while loop:
            ans = input('Add a book? Y/N -> ')
            if ans == 'Y' or ans == 'y':
                print('Add author title year')
                row = [s for s in input().split(' ')]
                self.books.append(row)
            elif ans == 'N' or ans == 'n':
                loop = False
                print(self.books)
            else:
                print('wtf, maybe again?')
        return self.books

    def show_all_books(self):
        for i in range(len(self.books)):
            print(i + 1, end='. ')
            for j in range(len(self.books[i])):
                print(self.books[i][j], end=' ')
            print()

    def delete_book(self):
        for i in range(len(self.books)):
            print(i + 1, end='. ')
            for j in range(len(self.books[i])):
                print(self.books[i][j], end=' ')
            print()

        k = input('Choose book you want to delete. Enter ID of a book -> ')
        k = int(k)
        del self.books[k-1]
        print(self.books)

    def save_file(self):
        filename = input('Enter path (for ex. C:/Users\My_Usr\Desktop\File.txt)-> ')
        x = open(filename, 'a')
        x.close()
        x = open(filename, 'w')
        for row in self.books:
            x.write(' '.join(row) + '\n')
        x.close()
        x = open(filename, 'r')
        print(x.read())


def menu():
    ctg = Catalog()
    loop = True
    while loop:
        print('===============================================')
        print('               BOOK CATALOG')
        print('===============================================')
        print(' 1 - Show All Books')
        print(' 2 - Search for ...')
        print(' 3 - Add a book')
        print(' 4 - Delete a book')
        print(' 5 - Save catalog as a file')
        print(' 6 - Exit')
        print('===============================================')
        print("      DON'T FORGET TO ADD BOOKS FIRST!!!")
        response = input('Please, enter -> ')

        if response == '1':  # Show all books
            ctg.show_all_books()
        elif response == '2':  # Search for smth
            ctg.search_for()
        elif response == '3':  # Add book
            ctg.add_a_book()
        elif response == '4':  # Delete book
            ctg.delete_book()
        elif response == '5':  # Save file
            ctg.save_file()
        elif response == '6':  # Exit the program
            print('Bye-Bye')
            loop = False
        else:
            print('Wtf? Try again..')


print(menu())
