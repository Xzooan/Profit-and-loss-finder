
sp=float(input("The selling price="))
print(sp)
cp=float(input("The cost price="))
print(cp)
if sp>cp:
   profit=sp-cp
   print("Profit",'=',profit,'rupees')
   _profit=profit*100/cp
   print("Profit %",'=',_profit)
else:
   loss=cp-sp
   print("Loss",'=',loss,'rupees')
   _loss=loss*100/cp
   print("Loss %",'=',_loss)
 
print("=========end=========") 
