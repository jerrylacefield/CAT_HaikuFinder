CREATE TABLE Artists (
	artist_link VARCHAR(256),
	artist_name VARCHAR(256),
	curr_working BOOLEAN,
	is_done BOOLEAN,
	timestamp DATETIME,
	PRIMARY KEY (artist_link)
);

CREATE TABLE Songs (
	song_link VARCHAR(256),
	artist_link VARCHAR(256),
	song_lyrics TEXT,
	curr_working BOOLEAN,
	is_done BOOLEAN,
	timestamp DATETIME,
	PRIMARY KEY (song_link),
	FOREIGN KEY (artist_link) REFERENCES Artists(artist_link)
		ON DELETE NO ACTION
);

CREATE TABLE Haikus (
	haiku_id INT AUTO_INCREMENT,
	song_link VARCHAR(256) NOT NULL,
	haiku TEXT,
	PRIMARY KEY (haiku_id),
	FOREIGN KEY (song_link) REFERENCES Songs(song_link)
		ON DELETE NO ACTION
);

CREATE TABLE Errors (
	error_id INT AUTO_INCREMENT,
	song_link VARCHAR(256) NOT NULL,
	error_reason VARCHAR(256),
	PRIMARY KEY (error_id),
	FOREIGN KEY (song_link) REFERENCES Songs(song_link)
		ON DELETE NO ACTION
);