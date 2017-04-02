-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Remove tournament database to start fresh
DROP DATABASE IF EXISTS tournament;

-- Create tournament database
CREATE DATABASE tournament;

-- Connect to tournament database
\c tournament;

-- Create player table
CREATE TABLE player ( id SERIAL PRIMARY KEY,
                     --  tournament_id INTEGER NOT NULL REFERENCES tournament,
                      name TEXT);

-- Create match table
CREATE TABLE match ( id SERIAL PRIMARY KEY,
                     -- tournament_id INTEGER NOT NULL REFERENCES tournament,
                     winner INTEGER REFERENCES player (id),
                     loser INTEGER REFERENCES player (id));

-- Create standings view and order by number of wins
CREATE VIEW standings AS
SELECT p.id as id,
p.name as name,
(SELECT count(*) FROM match WHERE p.id = match.winner) as wins,
(SELECT count(*) FROM match WHERE p.id in (winner, loser)) as matches
FROM player p
GROUP BY p.id
ORDER BY wins DESC;
