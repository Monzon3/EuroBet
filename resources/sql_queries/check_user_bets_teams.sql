SELECT Users.id, Users.name,
Teams1.Name as team1ID, Teams2.Name as team2ID, 
Teams3.Name as team3ID, Teams4.Name as team4ID, 
Teams5.Name as team5ID, Teams6.Name as team6ID,
Teams7.Name As more_goals_for, Teams8.Name as less_goals_for, 
Teams9.Name As more_goals_against, Teams10.Name as less_goals_against,
Teams11.Name As winner, Teams12.Name As more_goals_total
FROM PorraEuro.Users
INNER JOIN PorraEuro.Teams as Teams1 ON Users.team1ID=Teams1.id
INNER JOIN PorraEuro.Teams as Teams2 ON Users.team1ID=Teams2.id
INNER JOIN PorraEuro.Teams as Teams3 ON Users.team1ID=Teams3.id
INNER JOIN PorraEuro.Teams as Teams4 ON Users.team1ID=Teams4.id
INNER JOIN PorraEuro.Teams as Teams5 ON Users.team1ID=Teams5.id
INNER JOIN PorraEuro.Teams as Teams6 ON Users.team1ID=Teams6.id
INNER JOIN PorraEuro.Teams as Teams7 ON Users.more_goals_for=Teams7.id
INNER JOIN PorraEuro.Teams as Teams8 ON Users.less_goals_for=Teams8.id
INNER JOIN PorraEuro.Teams as Teams9 ON Users.more_goals_against=Teams9.id
INNER JOIN PorraEuro.Teams as Teams10 ON Users.less_goals_against=Teams10.id
INNER JOIN PorraEuro.Teams as Teams11 ON Users.winner=Teams11.id
INNER JOIN PorraEuro.Teams as Teams12 ON Users.more_goals_total=Teams12.id;