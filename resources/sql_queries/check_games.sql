SELECT Games.date,
Teams1.Name as Team1, Teams2.Name as Team2,
Games.goals1, Games.goals2 
FROM PorraEuro.Games, 
PorraEuro.Teams As Teams1, PorraEuro.Teams As Teams2
WHERE Games.team1ID=Teams1.id AND Games.team2ID=Teams2.id;


Cambiar todas estas consultas por INNER JOIN