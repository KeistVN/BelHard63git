# def ves_sms(sms):
#     sms=sms.lower()
#     bytes_count=0
#     lat='abcdefghijklmnopqrstuvwxyz'
#     cifr='1234567890'
#     for i in sms:
#         if i in lat or i == ' ' or i in cifr:
#             bytes_count+=1
#         else:
#             bytes_count+=2
#     return round((bytes_count/140)+0.5,0)
# print(ves_sms('asdwasfawfaывфцвфывфцаыфвфцвыамыкрыап кмп ыкирыуенмумпкумпыскпыукпфиукпмыукппфцпфывфцвфsdawr125235135'))
from math import ceil
def bankir_evrey(summa: float,procent: float) -> int:
    summax2=summa*2
    month=0
    while summa < summax2:
        month+=1
        summa=summa+summa*(procent/100)
    return ceil(month/12)
print(bankir_evrey(100,3))
