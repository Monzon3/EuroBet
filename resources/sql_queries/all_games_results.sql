SELECT Games.id, Games.Date,
Teams1.Name, Teams2.Name,
Games.goals1, Games.goals2
FROM PorraEuro.Games
INNER JOIN PorraEuro.Teams As Teams1 ON Games.team1ID=Teams1.id
INNER JOIN PorraEuro.Teams As Teams2 ON Games.team2ID=Teams2.id
ORDER BY Games.id;