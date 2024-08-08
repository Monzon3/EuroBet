SELECT Games.date, 
Teams1.Name as Team1, Teams2.Name as Team2,
Games.goals1, Games.goals2
FROM PorraEuro.Games
INNER JOIN PorraEuro.Teams as Teams1 ON Games.team1ID=Teams1.id
INNER JOIN PorraEuro.Teams as Teams2 ON Games.team2ID=Teams2.id;