SELECT Users.id, Users.name,
Teams1.Name as team1ID, Teams2.Name as team2ID, 
Teams3.Name as team3ID, Teams4.Name as team4ID, 
Teams5.Name as team5ID, Teams6.Name as team6ID,
Teams7.Name As more_goals_for, Teams8.Name as less_goals_for, 
Teams9.Name As more_goals_against, Teams10.Name as less_goals_against,
Teams11.Name As winner, Teams12.Name As more_goals_total
FROM PorraEuro.Users, PorraEuro.Teams As Teams1, PorraEuro.Teams As Teams2,
PorraEuro.Teams As Teams3, PorraEuro.Teams As Teams4,
PorraEuro.Teams As Teams5, PorraEuro.Teams As Teams6,
PorraEuro.Teams As Teams7, PorraEuro.Teams As Teams8,
PorraEuro.Teams As Teams9, PorraEuro.Teams As Teams10,
PorraEuro.Teams As Teams11, PorraEuro.Teams As Teams12
WHERE Users.team1ID=Teams1.id AND Users.team2ID=Teams2.id
AND Users.team3ID=Teams3.id AND Users.team4ID=Teams4.id
AND Users.team5ID=Teams5.id AND Users.team6ID=Teams6.id
AND Users.more_goals_for=Teams7.id AND Users.less_goals_for=Teams8.id
AND Users.more_goals_against=Teams9.id AND Users.less_goals_against=Teams10.id
AND Users.winner=Teams11.id AND Users.more_goals_total=Teams12.id;