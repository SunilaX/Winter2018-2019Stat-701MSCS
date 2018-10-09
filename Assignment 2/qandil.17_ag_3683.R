# Qandil Fatima, 17-AG-3671, MSCS(3rd)

library("scatterplot3d")

dframe = data.frame(
  x1_val = c(0, 0, 10, 10, 20, 20),
  x2_val = c(0, 0, 100, 100, 400, 400),
  y_val = c(5, 7, 15, 17, 9, 11))


print(dframe)
fit = lm(y_val ~ x1_val + x2_val, data = dframe)

print(summary(fit))

cat("\n\n\n")
print(coefficients(fit))

cat("\n\n\nY_hat\n")
print(fitted(fit))

cat("\n\n\n")
print(anova(fit))

cat("\n\n\n")
r_sqr = summary(fit)$r.squared
sigma_sqr = summary(fit)$sigma^2

print(paste("R2 =", r_sqr,
            collapse = " "))
print(paste("MSE =", sigma_sqr,
            collapse = " "))

plot = scatterplot3d(dframe, type = "h", color = "red"
                     ,grid=TRUE,
                     
                     main = "Linear Regression of x1, x2 and y",
                     xlab = "X1", ylab = "x2",
                     zlab = "y"
)  

cat("\n\n")
print(vcov(fit))