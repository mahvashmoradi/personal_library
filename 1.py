def get_data():
    """
    function to get data
    :return: a instance of Book class
    """
    title = input('enter title: ')
    author = input('enter author: ')
    publish_year = input('enter publish_year: ')
    pages = int(input('enter pages: '))
    language = input('enter Language: ')
    price = input('enter price: ')
    book = Book(title, author, publish_year, pages, language, price)
    return book


class Book:
    """
    The Book class has
    read(self, read_x)
    get_status(self)
    _str(self)
    method
    """

    def __init__(self, title, author, publish_year, pages, language, price):
        """
        init Book the class
        :param title:
        :param author:
        :param publish_year:
        :param pages:
        :param language:
        :param price:
        """
        self.title = title
        self.author = author
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_tot = 0

    def read(self, read_x):
        """
        calculate the total read pages and inform the user that how many pages is remaining.
        :param read_x: the number of read pages
        :return:
        """
        if (self.read_tot + read_x) > self.pages:
            print("\nyour Book/Magazine has fewer pages.\nWrong input\n")
            return
        self.read_tot += read_x
        cal_page = self.pages - self.read_tot
        print(f"\nyou have read {read_x} more pages from {self.title}. There are {cal_page} pages left")

    def get_status(self):
        """
        get stutus of media (unread, reading, finish)
        :return:
        """
        cal_status = lambda x: 'unread' if (x == 0) else 'reading' if (x < self.pages) else 'finished'
        print(cal_status(self.read_tot))

    def __str__(self):
        """
        print the value of Book items
        :return:
        """
        return f"{self.title, self.author, self.publish_year, self.pages, self.language, self.price}"


list_book = []
for i in range(3):
    """
    get the information of Books and create the Book_shelf
    """
    print(f"Please enter the information of Book{i+1}")
    list_book.append(get_data())
"""list_book = [Book('No Friend But the Mountains', 'Behrouz Boochani', '2018', 374, 'English', '10'),
             Book('The Black Swan', 'Abbas Maroufi', '2007', 280, 'Percian', '20'),
             Book('Symphony of the Dead', 'Behrouz Boochani', '2018', 374, 'English', '126')]"""
print('----------------------------------------List of books----------------------------------------')
[print(i) for i in list_book]
"""
read 20 pages from Book 1 
"""
list_book[0].read(20)
"""
read 200 pages from Book 3 
"""
list_book[2].read(200)
"""
reread 200 pages from Book 3 to show that dont apply the pages more than pages of the Book
"""
list_book[2].read(200)
"""
get stutus of Books 1,2,3
"""
list_book[0].get_status()
list_book[1].get_status()
list_book[2].get_status()
