#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


# Function to execute SQL functions
def executeSql(query):
    """Function to run SQL queries."""

    # Start connection and execute query
    conn = connect()
    c = conn.cursor()
    c.execute(str(query))
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""

    query = "DELETE FROM player;"
    executeSql(query)


def deleteMatches():
    """Remove all the match records from the database."""

    query = "DELETE FROM match;"
    executeSql(query)


def countPlayers():
    """Returns the number of players currently registered."""

    # Query to count the number of players in the player table
    query = "SELECT COUNT(*) FROM player;"

    # Start connection and execute query
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    count = c.fetchone()[0]
    conn.commit()
    conn.close()

    return count



def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    # Query to add new player into players table
    query = "INSERT INTO player (name) VALUES (%s);"

    # Start connection and execute query
    conn = connect()
    c = conn.cursor()
    c.execute(query, (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """

    # Query to get current standings from standings view
    query = "SELECT * FROM standings;"

    # Start connection and execute query
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    standings = c.fetchall()
    conn.commit()
    conn.close()

    # Return standings from query
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    # Query to add new match with winner and loser
    query = "INSERT INTO match (winner, loser) VALUES (%s, %s);" % (winner, loser)

    # Execute query
    executeSql(query)



def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    # Query to return all from standings view
    query = "SELECT * FROM standings;"

    # Start connection and execute query
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    s = c.fetchall()
    conn.commit()
    conn.close()

    # Create list to hold pairs
    pairs = []

    # Set counter for adding items to pairs list
    i = 0

    # Loop through standings and pair players in order of standings
    while (i < len(s)):
        # Add pair containing players ids and names to pairs list
        pairs.append((s[i][0], s[i][1], s[i + 1][0], s[i + 1][0]))
        # Increment counter by 2 since two players are in each pair
        i += 2

    return pairs
