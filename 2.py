"""
This program is a personal book_shelf. It can included Book, Magazine, Podcast and audiobook. User can add media to its
shelf. Also, he/she can read from each of media and get stutus of the media in the shelf. he/she can see the sorted
shelf base on progress of reading/listening
"""


class Book:
    """
    The Book class has
    getdata(self)
    read(self, read_x)
    get_status(self)
    set_progress(self)
    method
    """

    def __init__(self, title=None, author=None, publish_year=None, pages=None, language=None, price=None):
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
        self.progress = 0

    def getdata(self):
        """
        function to get data from user and
        set the attribute of the Book class
        """
        self.title = input('enter title: ')
        self.author = input('enter author: ')
        self.publish_year = input('enter publish_year: ')
        self.pages = int(input('enter pages: '))
        self.language = input('enter Language: ')
        self.price = input('enter price: ')

    def read(self, read_x):
        """
        calculate the total read pages and inform the user that how many pages is remaining.
        :param read_x: the number of read pages
        :return:
        """
        if (self.read_tot + read_x) > self.pages:
            print("your Book/Magazine has fewer pages.\nWrong input")
            return
        self.read_tot += read_x
        cal_page = self.pages - self.read_tot
        print(f"you have read {read_x} more pages from {self.title}. There are {cal_page} pages left")

    def get_status(self):
        """
        get stutus of media (unread, reading, finish)
        :return:
        """
        cal_status = lambda x: 'unread' if (x == 0) else 'reading' if (x < self.pages) else 'finished'
        print(cal_status(self.read_tot))

    def set_progress(self):
        """
        set the progress of media
        :return:
        """
        self.progress = round((self.read_tot / self.pages) * 100)

    def __str__(self):
        """
        print the value of Book items
        :return:
        """
        return f"title={self.title}, author= {self.author}, publish_year= {self.publish_year}, pages= {self.pages},\
        Language= {self.language}, price={self.price}"


class Magazine(Book):
    """
    The magazine class inheritance from Book class and no need to def method which has been introduced in book class
    """

    def __init__(self, title=None, author=None, publish_year=None, pages=None, language=None, price=None, issue=None):
        """
        init the Magazine class
        :param title:
        :param author:
        :param publish_year:
        :param pages:
        :param language:
        :param price:
        :param issue:
        """
        Book.__init__(self, title, author, publish_year, pages, language, price)
        self.issue = issue

    def getdata(self):
        """
               function to get data from user and
               set the attribute of the Magazine class
               """
        Book.getdata(mazine)
        self.issue = input('enter issue: ')

    def __str__(self):
        """
        print the value of Magazine items
        :return:
        """
        # Book.__str__(mazine)
        return f"title={self.title}, author= {self.author}, publish_year= {self.publish_year}, pages= {self.pages},\
                Language= {self.language}, price={self.price},issue={self.issue}"


class PodcastEpisode(Book):
    """
    The PodcastEpisode class inheritance from Book class and override Book methods
    """

    def __init__(self, title=None, speaker=None, publish_year=None, time=None, language=None, price=None):
        """
        init the PodcastEpisode class
        :param title:
        :param speaker:
        :param publish_year:
        :param time:
        :param language:
        :param price:
        """
        Book.__init__(self, title=title, publish_year=publish_year, language=language, price=price, author=None,
                      pages=None)
        self.speaker = speaker
        self.time = time
        self.progress = 0

    def getdata(self):
        """
               function to get data from user and
               set the attribute of the Podcast class
               """
        self.title = input('enter title: ')
        self.speaker = input('enter speaker: ')
        self.publish_year = input('enter publish_year: ')
        self.time = int(input('enter time: '))
        self.language = input('enter Language: ')
        self.price = input('enter price: ')

    def read(self, read_x):
        """
        calculate the total read times and inform the user that how many times is listen.
        :param read_x: the number of read pages
        :return:
        """
        if (self.read_tot + read_x) > self.time:
            print("your Book/Magazine has fewer pages.\nWrong input")
            return
        self.read_tot += read_x
        cal_page = self.time - self.read_tot
        print(f"you have listen {read_x} more time from {self.title}. There are {cal_page} time left")

    def get_status(self):
        """
        get stutus of media (unread, reading, finish)
        :return:
        """
        cal_status = lambda x: 'unread' if (x == 0) else 'reading' if (x < self.time) else 'finished'
        print(cal_status(self.read_tot))

    def set_progress(self):
        """
        set the progress of media
        :return:
        """
        self.progress = round((self.read_tot / self.time) * 100)

    def __str__(self):
        """
        print the value of Podcast items
        :return:
        """
        return f"title={self.title}, speaker= {self.speaker}, publish_year={self.publish_year}, time={self.time},\
         language={self.language}, price={self.price}"


class AudioBook(Book):
    """
    The AudioBook class inheritance from Book class and override Book methods
    """

    def __init__(self, title=None, speaker=None, author=None, publish_year=None, \
                 pages=None, booklanguage=None, audiolanguage=None, time=None, price=None):
        """
        init the AudioBook class
        :param title:
        :param speaker:
        :param author:
        :param publish_year:
        :param pages:
        :param booklanguage:
        :param audiolanguage:
        :param time:
        :param price:
        """
        Book.__init__(self, title, author, publish_year, pages, price=price, language=None)
        '''PodcastEpisode.__init__(self, title=title, speaker=speaker, time=time, language=None, publish_year=None,
                                price=None)'''
        self.speaker = speaker
        self.time = time
        self.booklanguage = booklanguage
        self.audiolanguage = audiolanguage
        self.progress = 0

    def getdata(self):
        """
               function to get data from user and
               set the attribute of the AudioBook class
               """
        self.title = input('enter title: ')
        self.speaker = input('enter speaker: ')
        self.author = input('enter author: ')
        self.publish_year = input('enter publish_year: ')
        self.pages = int(input('enter pages: '))
        self.time = int(input('enter time: '))
        self.booklanguage = input('enter book_Language: ')
        self.audiolanguage = input('enter audio_Language: ')
        self.price = input('enter price: ')

    def read(self, read_x):
        """
        calculate the total read times and inform the user that how many times is listen.
        :param read_x: the number of read pages
        :return:
        """
        if (self.read_tot + read_x) > self.time:
            print("your Book/Magazine has fewer pages.\nWrong input")
            return
        self.read_tot += read_x
        cal_page = self.time - self.read_tot
        print(f"you have listen {read_x} more time from {self.title}. There are {cal_page} time left")

    def get_status(self):
        """
        get stutus of media (unread, reading, finish)
        :return:
        """
        cal_status = lambda x: 'unread' if (x == 0) else 'reading' if (x < self.time) else 'finished'
        print(cal_status(self.read_tot))

    def set_progress(self):
        """
        set the progress of media
        :return:
        """
        self.progress = round((self.read_tot / self.time) * 100)

    def __str__(self):
        """
        print the value of AudioBook items
        :return:
        """
        return f"title={self.title}, speaker= {self.speaker}, author= {self.author},publish_year={self.publish_year}\
                ,pages= {self.pages}, time= {self.time}, booklanguage= {self.booklanguage},\
                audiolanguage= {self.audiolanguage}, price={self.price}"


list_shelf = []
while (True):
    print(
        "What do you do:\n1-add a media to bookshelf\n2-show my bookshelf\n3-add read page or time listen\n"
        "4-get stutus of your shelf\n5-sort my bookshelf")
    select = input("Please select a above items\n")
    if select == '1':
        print("---------------------------------------add media to your shelf-----------------------------------")
        while (True):
            """
            base on user input select the on of items
            """
            _str = input(
                "please enter the type of your media\nType Quit to back the home:  \n1-Book\n2-Magazine\n3-Podcast\n"
                "4-AudioBook\n")
            if _str == 'Quit':
                print(
                    "--------------------------------------------------------------------------------------------------")
                break
            elif _str == '1':
                """
                create the class and then set the attribute of the class with the getdata method and append to shelf
                """
                book = Book()
                book.getdata()
                list_shelf.append(book)
            elif _str == '2':
                mazine = Magazine()
                mazine.getdata()
                list_shelf.append(mazine)
            elif _str == '3':
                pdepisode = PodcastEpisode()
                pdepisode.getdata()
                list_shelf.append(pdepisode)
            elif _str == '4':
                aubook = AudioBook()
                aubook.getdata()
                list_shelf.append(aubook)
            else:
                print("undefined input")
    elif select == '2':
        print("----------------------------------------list of your shelf---------------------------------------")
        if len(list_shelf) == 0:
            print("your shelf is empty")
        [print(media + 1, ": ", list_shelf[media]) for media in range(len(list_shelf))]
        print("-------------------------------------------------------------------------------------------------")
    elif select == '3':
        while (True):
            print("In below list you can see the list of your media\nWhich one do you read")
            [print(media + 1, ": ", list_shelf[media]) for media in range(len(list_shelf))]
            _str = input("Type Quit to back the home:\n")
            if _str == 'Quit':
                print(
                    "--------------------------------------------------------------------------------------------------")
                break
            try:
                pg = int(input("Enter your page read or time listen: "))
                list_shelf[int(_str) - 1].read(pg)
            except IndexError:
                print("your shelf has not the input record. Please enter correct input")
    elif select == '4':
        print("---------------------------------------stutus of your shelf--------------------------------------")
        if len(list_shelf) == 0:
            print("your shelf is empty")
        for media in list_shelf:
            print(media.title, ": ")
            media.get_status()
        print("-------------------------------------------------------------------------------------------------")
    elif select == '5':
        print("----------------------------------progress percentage of your shelf-------------------------------")
        for media in range(len(list_shelf)):
            list_shelf[media].set_progress()
        s_list_shelf = sorted(list_shelf, key=lambda x: x.progress, reverse=True)
        [print(media + 1, ": ", type(s_list_shelf[media]).__name__, s_list_shelf[media].title,
               s_list_shelf[media].progress) for media in range(len(s_list_shelf))]
        print("--------------------------------------------------------------------------------------------------")
    else:
        print("undefined input")
