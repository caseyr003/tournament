#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def executeSql(query):
    """Function to run SQL queries."""
    conn = connect()
    c = conn.cursor()
    c.execute(str(query))
    conn.commit()
    conn.close()


def deleteTournaments():
    """Remove all the tournament records from the database."""
    query = "DELETE FROM tournament;"
    executeSql(query)


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
    query = "SELECT COUNT(*) FROM player;"
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
    query = "INSERT INTO player (name) VALUES (%s);"
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
    query = "SELECT * FROM standings;"
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    standings = c.fetchall()
    conn.commit()
    conn.close()
    return standings


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    query = "INSERT INTO match (winner, loser) VALUES (%s, %s);"
    conn = connect()
    c = conn.cursor()
    c.execute(query, (winner, loser))
    conn.commit()
    conn.close()


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

    query = "SELECT * FROM standings;"
    conn = connect()
    c = conn.cursor()
    c.execute(query)
    standings = c.fetchall()
    conn.commit()
    conn.close()
    count = len(standings)
    pairs = []
    num = 0
    while (num < count):
        id1 = standings[num][0]
        name1 = standings[num][1]
        id2 = standings[num + 1][0]
        name2 = standings[num + 1][1]
        pairs.append((id1, name1, id2, name2))
        num += 2

    return pairs
