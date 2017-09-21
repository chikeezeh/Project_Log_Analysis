views created for question 3.

create view statusTotal as select log.time::timestamp::date as dayDate,
cast(count(log.status) as float) as statusCount from log group by dayDate;

create view statusOK as select log.time::timestamp::date as dayDate, cou
nt(log.status) as statusCount from log where log.status ='200 OK' group by dayD
ate;

create view errorStatus as select statusTotal.dayDate,(100*(1-(statusOK.
statusCount/statusTotal.statusCount))) as "error" from statusTotal join statusO
K on statusTotal.dayDate = statusOK.dayDate;