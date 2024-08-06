SELECT Users.Name,
Teams1.Name as Team1, Teams2.Name as Team2,
Bets.goals1, Bets.goals2,
Games.date
FROM PorraEuro.Bets, PorraEuro.Users, PorraEuro.Games,
PorraEuro.Teams As Teams1, PorraEuro.Teams As Teams2
WHERE Bets.userID=Users.id
AND Bets.gameID=Games.id
AND Games.team1ID=Teams1.id AND Games.team2ID=Teams2.id;