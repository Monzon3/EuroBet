SELECT Users.Name, 
Teams1.Name as Team1, Teams2.Name as Team2,
Bets.goals1, Bets.goals2, 
Games.date
FROM PorraEuro.Bets
INNER JOIN PorraEuro.Users ON Bets.userID=Users.id
INNER JOIN PorraEuro.Games ON Bets.gameID=Games.id
INNER JOIN PorraEuro.Teams as Teams1 ON Games.team1ID=Teams1.id
INNER JOIN PorraEuro.Teams as Teams2 ON Games.team2ID=Teams2.id;