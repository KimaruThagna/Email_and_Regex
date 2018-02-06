//MPESA REGEX IN JS THIS IS TO GIVE A VIEW OF REGEX FROM ANOTHER ANGLE
var message1="MAA65OARPO Confirmed. You have received Ksh500.00 from JOHN DOE 0720000000 on 10/10/18 at 2:50 PM. New M-PESA balance is Ksh500.00.Pay bills via M-PESA";
var message2="MAA65D4RPO Confirmed. Ksh500.00 sent to JOHN DOE 0720000000 on 10/10/18 at 2:50 PM. New M-PESA balance,Ksh500.00. Transaction cost, Ksh 22.00";
var message3="MAA65A3RPO Confirmed. On 10/10/18 at 2:50 PM Give Ksh6,500.00 cash to ShopX . New M-PESA balance is Ksh500.00. Dial *231# to manage bills";
var message4="MAB35OAR12 Confirmed. On 10/10/18 at 2:50 PM Withdraw Ksh5,500.00 from 74845 T-ShpoQ . New M-PESA balance is Ksh500.00.Transaction cost, Ksh 27.00";
var message5="MAA65D4RPO Confirmed. Ksh500.00 sent to BiznaX for account IIQ23 on 10/10/18 at 2:50 PM. New M-PESA balance,Ksh500.00. Transaction cost, Ksh 22.00";

function regex(pattern,message)
{
const regex =pattern;
const str = message;
let m;
m = regex.exec(str);
return m;
}
function mpesa_digest(message)
{
  //THE REGEX PATTERNS FOR VARIOUS ITEMS
var code=regex( /^[A-Z 0-9]{10}/g,message)
var bal=regex( /balance is Ksh[0-9]*[,]?[0-9]*.\d{2}/g,message)
var txnCost=regex( /cost, Ksh[0-9]*[,]?[0-9]*.\d{2}/g,message)
var rcash=regex( /received Ksh[0-9]*[,]?[0-9]*.\d{2}/g,message)
var scash=regex( /cash Ksh[0-9]*[,]?[0-9]*.\d{2} sent/g,message)
var withdrawal=regex( /Withdraw Ksh[0-9]*[,]?[0-9]*.\d{2}/g,message)
var time=regex( /\d{1,2}[/]\d{1,2}[/]\d{1,2} at \d{1,2}[:][0-9]+ [A-Z]{1,2}/g,message)
var deposit=regex( /Give Ksh[0-9]*[,]?[0-9]*.\d{2}/g,message)
var paymnts=regex( /Ksh[0-9]*[,]?[0-9]*.\d{2} paid/g,message)

var delimited_message=new Array;
delimited_message["code"]=code;
delimited_message["bal"]=bal;
delimited_message["txnCost"]=txnCost;
delimited_message["rcash"]=rcash;
delimited_message["scash"]=scash;
delimited_message["withdrawal"]=withdrawal;
delimited_message["time"]=time;
delimited_message["deposit"]=deposit;
delimited_message["paymnts"]=paymnts;
return delimited_message; //RETURN AN ASSOCIATED ARRAY CONTAINING THE RELEVANT ITEMS
}
var digest=mpesa_digest(message1);
document.writeln("Transaction code:"+digest["code"]);
document.write("<br/>");
document.writeln("Mpesa balance:"+digest["bal"]);
document.write("<br/>");
document.writeln("Transaction time:"+digest["time"]);

















