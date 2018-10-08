"""
        Sunila Tahir
        2017-ag-5212

                        """
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from statsmodels.formula.api import ols
from mpl_toolkits.mplot3d import Axes3D
import math as math


def reg_analysis(reg):


    print("\n\n", reg.params)

    y_hat = reg.fittedvalues
    print("\n\nFitted Values:\n", y_hat)

    return y_hat





def plot_regression(df, y_pred, reg, str):

    if input == 1:

        plt.scatter(
            df["Income"]
            , df["Expenditure"]
            , color="red")

        plt.plot(
            df["Income"]
            , y_pred,
            color="b")

        plt.title(str[0])
        plt.xlabel(str[1])
        plt.ylabel(str[2])

        plt.show()


    else:

        axes = plt.figure().gca(projection='3d')

        axes.scatter(

            df["x1"]
            , df["x2"]
            , df["y"]
            , color="green"

        )

        axes.set_title(str[0])
        axes.set_xlabel(str[1], color="purple")
        axes.set_ylabel(str[2], color="purple")
        axes.set_zlabel(str[3], color="purple")


        x_surface = df["x1"]
        y_surface = df["x2"]


        x_surface, y_surface = np.meshgrid(x_surface, y_surface)

        ex = pd.core.frame.DataFrame({

            "x1": x_surface.ravel(), "x2": y_surface.ravel()

        })


        pred = reg.predict(exog=ex)

        axes.plot_surface(

            x_surface, y_surface
            , pred.values.reshape(x_surface.shape), alpha=0.3

        )

        plt.show()





def anova(y_bar, y, y_pred, k):


# Analysis of Variance
    n = np.size(y_pred)

    df_t = n - 1
    df_m = k - 1
    df_r = n - k

    mss = np.sum((y_pred - y_bar) ** 2)
    rss = np.sum((y - y_pred) ** 2)
    tss = mss + rss

    ms_t = tss / df_t
    ms_m = mss / df_m
    ms_r = rss / df_r

    f_stats = round(ms_m / ms_r, 4)
    r_sqr = round(mss / tss, 4)
    sigma_sqr = round(rss / df_r, 4)


    data = [['Total', df_t, tss, ms_t , f_stats], ['Model', df_m, mss, ms_m],
            ['Residual', df_r, rss, ms_r]]
    df = pd.DataFrame(data, columns=['SOV', 'df', 'SS', 'MS', 'F'])

    print("\nAnalysis of Variance \n {}".format(df))

    print("\n\nCoefficient of Determination =", r_sqr)
    print("MSE = ", sigma_sqr)

    return f_stats, sigma_sqr
	
	
	
	
def tesing_hypothesis(f_val, f_tab_val, hypo_stmt):


    print("\nTesing Hypothesis {} on F table value {}..." .format(hypo_stmt, f_tab_val))

    if(f_val > f_tab_val):
        print("Since Fc = {} doesn't fall in CR, so reject H0 at alpha = 5 %" .format(f_val))

    else:
        print("Since Fc = {} doesn't fall in CR, so accept H0 at alpha = 5%\n\n" .format(f_val))




def numInput():

    try:

        number = int(input())

    except ValueError:

        print("You must enter a number (1-3)")
        numInput()

    else:

        if number == 1 or number == 2 or number == 3:
            return number

        else:
            print("You must enter a number (1-3)")
            numInput()




def main(input):


# SLR

    if input == 1:

        dfSLR = pd.DataFrame(
            {
                "Income": [80, 100, 120, 140, 160, 180, 200, 220, 240, 260],
                "Expenditure": [70, 65, 90, 95, 110, 115, 120, 140, 155, 150]
            }
        )

        print(dfSLR)

        str = ["Regression Line of Income and Expenditure", "Income", "Expenditure"]


        reg = ols(formula = "Expenditure ~ Income", data=dfSLR).fit()

        y_pred = reg_analysis(reg)

        k = 2
        x_mean = np.mean(dfSLR["Income"])
        y_mean = np.mean(dfSLR["Expenditure"])
        f_stats, mse = anova(y_mean, dfSLR["Expenditure"], y_pred, k)


        f_tab_val = 5.318
        hypo_stmnt = "H0: B1 = 0"
        tesing_hypothesis(f_stats, f_tab_val, hypo_stmnt)


        #### variance and standard error of variance

        n = np.size(dfSLR["Income"])

        xi2 = np.sum((dfSLR["Income"] - x_mean) ** 2)

        var_b1 = round(mse/xi2, 5)
        var_b0 = round(float(1/n + (x_mean ** 2)/xi2) * mse, 5)
        se_vb0 = round(math.sqrt(var_b0), 4)
        se_vb1 = round(math.sqrt(var_b1), 4)

        data = [['b0', var_b0, se_vb0], ['b1', var_b1, se_vb1]]
        df = pd.DataFrame(data, columns=['', 'Variance', 'SE(v)'])
        print(df)


        plot_regression(dfSLR, y_pred, reg, str)




# MLR

    elif input >= 2:

        if input == 2:

            # Example 1
            dfMLR = pd.DataFrame(
                {
                    "x1": [100, 200, 300, 400, 500, 600, 700],  # Fertilizer
                    "x2": [10, 20, 10, 30, 20, 20, 30],         # Rainfall
                    "y": [40, 50, 50, 70, 65, 65, 80]           # Yield
                }
            )

            print(dfMLR)

            titlestr = "Regression Line for Yield ~ Fertilizer + Rainfall"
            xlabstr = "Fertilizer"
            ylabstr = "Rainfall"
            zlabstr = "Yield"
            str = [titlestr, xlabstr, ylabstr, zlabstr]


            f_tab_val = 6.94


        else:

            # Example 2
            dfMLR = pd.DataFrame(
                {
                    "x1": [0, 0, 10, 10, 20, 20],
                    "x2": [0, 0, 100, 100, 400, 400],
                    "y": [5, 7, 15, 17, 9, 11]
                }
            )
            print(dfMLR)

            titlestr = "Regression Line for y ~ x1 + x2"
            xlabstr = "x1"
            ylabstr = "x2"
            zlabstr = "x3"
            str = [titlestr, xlabstr, ylabstr, zlabstr]

            f_tab_val = 9.55


        reg = ols(formula = "y ~ x1 + x2", data=dfMLR).fit()

        y_pred = reg_analysis(reg)

        y_mean = np.mean(dfMLR["y"])


        k = 3
        f_stats, mse = anova(y_mean, dfMLR["y"], y_pred, k)


        hypo_stmnt = "H0: B1 = B2 = B3 = 0"
        tesing_hypothesis(f_stats, f_tab_val, hypo_stmnt)


        plot_regression(dfMLR, y_pred, reg, str)




# START OF THE PROGRAM

print("Enter a number to perform Linear Regression: \n1 for SLR\n2 for MLR (Yield)\n3 for MLR (y_x1_x2)\n")
input = numInput()
main(input)