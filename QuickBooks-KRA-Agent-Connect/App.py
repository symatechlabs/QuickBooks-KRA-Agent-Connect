from QuickBooksConnect import QuickBooksConnect
from Sales import Sales;

qConnet = QuickBooksConnect();

sales = Sales();

#print(qConnet.getAuthCode());
#print(qConnet.getTokens());
#print(qConnet.refreshToken(""));

print(sales.getSalesReceipts("","", "5"))
