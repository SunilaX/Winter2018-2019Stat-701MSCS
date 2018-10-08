#
#        Sunila Tahir
#        2017-ag-5212



library(scatterplot3d)


hypo_test = function(){
  

  Fstats = round(summary(reg)$fstatistic[1], 3)   # Extract F stats value
  
  cat("\n\n")
  print(paste("Testing Hypothesis", hypo_stmnt, "on  F table value", Fval,"...", collapse = " "),
        quote=FALSE)

  
  if(Fstats > Fval) {
    print(paste("Since Fc =", Fstats,
                "fall in CR, so reject H0 at alpha = 5%",
                collapse = " "),
          quote=FALSE)
  }
  
  else {
    print(paste("Since Fc =", Fstats,
                "does not fall in CR, so accept H0 at alpha = 5%",
                collapse = " "),
          quote=FALSE)
  }
  
  
}




reganalysis = function() {
  
  cat("\n\nSUMMARY\n")
  print(summary(reg))
  
  cat("\n\n")
  print(coefficients(reg))
  
  cat("\n\nFitted values\n")
  print(fitted(reg))
  
  cat("\n\n")
  print(anova(reg))
  
  cat("\n\n")
  r2 = round(summary(reg)$r.squared, 3)
  sigma2 = round(summary(reg)$sigma^2, 3)
  
  print(paste("Coefficient Of determination =", r2,
              collapse = " "),
        quote=FALSE)
  print(paste("Mean Square Error =", sigma2,
              collapse = " "),
        quote=FALSE)
  

  # V(b0) and V(b1) values
  variance = setNames( c(round(vcov(reg)[1,1], 5), round(vcov(reg)[2,2], 5)),
                       c("v(intercept)", "v(b1)")
                       )
  
  
  cat("\n\nConfidence Interval\n")
  print(confint(reg))
  
  return(variance)
  
}


plot_reg = function(){
  
  if(input == 1) {
  
    plot(dfSLR,
         main = "Regression Line for Expenditures ~ Income",
         xlab = "Income",
         ylab = "Expenditures",
         col= 'blue', pch = 16)
    
    abline(reg, lwd = 2, col='red')
  
  }
  else
    {
      plot = scatterplot3d(dfMLR, 
                           main= titlestr,
                           xlab = xlabstr,
                           ylab = ylabstr,
                           zlab = zlabstr,
                           box=FALSE, pch = 16, color = "green"
                           
                       )
      plot$plane3d(reg)
  }
  
}



numInput = function(){
  
  tryCatch(
   {   # Takes integer input from user 
  
  number = readline(prompt= "")
  }
  , error = function(e)                         # Display Error Msg
   {
     print("You must enter a number (1-3)")
     numInput()
   }
   )
  # Input Validation
  if (number == "1" || number == "2" || number == "3"){
    
    return(number)
    
  }
  
  else {
    print("You must enter a number between 1 & 3")
    numInput()
    
  }
  
}



# START OF THE PROGRAM


cat("Enter a number to perform Linear Regression:
    \n1 for SLR\n2 for MLR (Yield)\n3 for MLR (y_x1_x2)\n")

input = numInput()


if(input == "1") {
  
  
  dfSLR = data.frame(
    Income = c(80,100,120,140,160,180,200,220,240,260),
    Expend = c(70, 65, 90, 95, 110, 115, 120, 140, 155, 150)
    )
  print(dfSLR)
  
  reg = lm(Expend ~ Income, data = dfSLR)
  
  Fval= 5.318
  
  variance = reganalysis()
  cat("\n\n")
  print(variance)
  
  #Hypothesis
  hypo_stmnt = "H0: B1 = 0"
  hypo_test()
  
  plot_reg()
  
} else {
  
  if(input == 2L) {
    
    dfMLR = data.frame(
    x1 = c(100,200,300,400,500,600,700),          # Fertilizer data
    x2 = c(10, 20, 10, 30, 20, 20, 30),           # Rainfall data
    y = c(40,50,50,70,65,65,80))                  # Yield data
  
    Fval= 6.94
    
    titlestr = "Regression Line for Yield ~ Fertilizer + Rainfall"
    xlabstr = "Fertilizer"
    ylabstr = "Rainfall"
    zlabstr = "Yield"
    }
  
    else if (input == 3L)
      {
      
      dfMLR = data.frame(
      x1 = c(0, 0, 10, 10, 20, 20),
      x2 = c(0, 0, 100, 100, 400, 400),
      y = c(5, 7, 15, 17, 9, 11))
      
      Fval= 9.55
      
      titlestr = "Regression Line for y ~ x1 + x2l"
      xlabstr = "y"
      ylabstr = "x1"
      zlabstr = "x2"
      
      }
      
  print(dfMLR)
  reg = lm(y ~ x1 + x2, data = dfMLR)
  
  variance = reganalysis()
  variance = append(variance, setNames(c(round(vcov(reg)[3,3], 5)),
                                       c("v(b2)")), after = 2 )
  cat("\n\n")
  print(variance)
  
  #Hypothesis
  hypo_stmnt = "H0: B1 = B2 = B3 = 0"
  hypo_test()
  plot_reg()
  
  }

