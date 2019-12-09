import sqlite3
conn = sqlite3.connect("celebrities.db")
cursor = conn.cursor()
#data supplied as tuple. ? - are placeholders for data
sql = "insert into celebs values (?, ?, ?, ?, ?, ?, ?)"
data = ((1, "Angelina", "Jolie", 40, "angie@hollywood.us", "https://s3.amazonaws.com/isat3402019/aj.jpg", "Born in Los Angeles, California, on June 4, 1975, Angelina Jolie starred in the HBO biopic Gia before earning a best supporting actress Academy Award for Girl, Interrupted"),
(2, "Brad", "Pit", 51, "brad@hollywood.us", "https://s3.amazonaws.com/isat3402019/bp.jpg", "The son of a trucking company manager, Brad Pitt was born December 18, 1963, in Shawnee, OK. Raised in Missouri as the oldest of three children, and brought up in a strict Baptist household, Pitt enrolled at the University of Missouri, following high school graduation, studying journalism and advertising."),
(3, "Snow", "White", 21, "sw@disney.org", "https://s3.amazonaws.com/isat3402019/sw.jpg", "Snow White Biography. Snow White is a character from “Snow White and the Seven Dwarfs” (originally “Schneewittchen” or “Schneeweissen”), one of the folk tales collected and published by The Brothers Grimm in the early 19th century."),
(4, "Darth", "Vader", 29, "dv@darkside.me", "https://s3.amazonaws.com/isat3402019/dv.jpg", "Darth Vader is a fictional character in the Star Wars franchise. He is a primary antagonist in the original trilogy, but, as Anakin Skywalker, is the main protagonist of the prequel trilogy up until the third film, where he becomes one of the two main antagonists (following his conversion to the dark side of the force) along with Palpatine. Star Wars creator George Lucas has collectively referred to the first six episodic films of the franchise as the tragedy of Darth Vader."),
(5, "Taylor", "Swift", 25, "ts@1989.us", "https://s3.amazonaws.com/isat3402019/ts.jpg", "Taylor Alison Swift is a multi-Grammy award-winning American singer/songwriter who, in 2010 at the age of 20, became the youngest artist in history to win the Grammy Award for Album of the Year. In 2011 Swift was named Billboard's Woman of the Year."),
(6, "Beyonce", "Knowles", 34, "beyonce@jayz.me", "https://s3.amazonaws.com/isat3402019/bk.jpg", "Beyoncé Knowles is a multi-platinum, Grammy Award-winning recording artist who's acclaimed for her thrilling vocals, videos and live shows. Who Is Beyoncé Knowles? Born in Houston, Texas, Beyoncé Knowles first captured the public's eye as lead vocalist of the R&B group Destiny's Child."),
(7, "Selena", "Gomez", 23, "selena@hollywood.us", "https://s3.amazonaws.com/isat3402019/sg.jpg", "Selena Marie Gomez is an American singer, songwriter, actress, and television producer. After appearing on the children's series Barney & Friends, she received wider recognition for her portrayal of Alex Russo on the Emmy Award-winning Disney Channel television series Wizards of Waverly Place, which aired from 2007 until 2012."),
(8, "Stephen", "Curry", 27, "steph@golden.bb", "https://s3.amazonaws.com/isat3402019/sc.jpg", "Wardell Stephen Steph Curry II is an American professional basketball player for the Golden State Warriors of the National Basketball Association. A six-time NBA All-Star, he has been named the NBA Most Valuable Player twice and won three NBA championships with the Warriors."))
cursor.executemany(sql, data)
sql = "insert into members values (?, ?, ?, ?, ?, ?)"
data = (1, "Michael", "Davis", 23, "rdavis.va@live.com", "Michael was born in Durham, NC before moving to Winchester at the age of 10. He recieved an advanced diploma at John Handley High School before attending James Madison University with the expected graduation in May 2020.")
cursor.execute(sql, data)
#commit the changes to the database
conn.commit()
conn.close()

