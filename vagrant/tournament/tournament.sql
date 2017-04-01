-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

-- CREATE TABLE tournament ( id SERIAL PRIMARY KEY,
--                           name TEXT);

CREATE TABLE player ( id SERIAL PRIMARY KEY,
                     --  tournament_id INTEGER NOT NULL REFERENCES tournament,
                      name TEXT);

CREATE TABLE match ( id SERIAL PRIMARY KEY,
                     -- tournament_id INTEGER NOT NULL REFERENCES tournament,
                     winner INTEGER REFERENCES player (id),
                     loser INTEGER REFERENCES player (id));

CREATE VIEW standings AS
SELECT p.id as id,
p.name as name,
(SELECT count(*) FROM match WHERE p.id = match.winner) as wins,
(SELECT count(*) FROM match WHERE p.id in (winner, loser)) as matches
FROM player p
GROUP BY player.id
ORDER BY won DESC;
