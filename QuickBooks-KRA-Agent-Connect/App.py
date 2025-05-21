from QuickBooksConnect import QuickBooksConnect
from Sales import Sales;

qConnet = QuickBooksConnect();

sales = Sales();

#print(qConnet.getAuthCode());
#print(qConnet.getTokens());
#print(qConnet.refreshToken("RT1-38-H0-1756576215796cwos6969iy279scrw"));

print(sales.getSalesReceipts("eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwieC5vcmciOiJIMCJ9..4SlIZuw7EZ8q2FrwRPqu6g.LHxPk8RcQHiRGlI_Gip8Qo-IWvSYNUlHYqbTssPr-YHjNDcV25x5JeI1p-hHvcnAt1KIygvWUmI1U80kJfrOfex9QeJTGlLvRFKwfbt8ubNni9YK_3J1_-Hy5BHQV44kJ7p4ivmHmtK7xOMp9UsrYY7PRnV3h3QCEv5lr8mmVHtzLO19q9E8Eu0ZXEN9QwGJ-Wt_6QRf3cArV5-A405nGD8qcyUN45NeuPrC1C0yaJEaTjH_Fc91YfFpcXljal4-vb_2UOZO340tCtRcnXQflRiWSlDZa7ONht87OJRRIQHarZe0U9_8Qk0Xyx2cb2sObkGE5oLN_L-SSldWKz0g7okyUSmcbddb3vZM2UNI9-LRLLLlF4IaF9Y53szxqCaeWrxcUkqF5qMoO3fQEMoKxX_EpbG7dyW9MI5cie0NDjTl-e19st_MdD_DChIZC6uualkaJiRtPi7uwMiolOHPxXLCjNWFdqAyzWnm-GAmDWw.toTRAy0n4-c5uF5unmyKAg",
                       "9341454713836312", "5"))