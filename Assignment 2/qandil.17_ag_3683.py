### Qandil Fatima, 17-AG-3691, MSCS(3RD)
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
import pandas as pd


df = pd.DataFrame(
    {   "fertilizer": [100, 200, 300, 400, 500, 600, 700],
        "rainfall": [10, 20, 10, 30, 20, 20, 30],
        "yield": [40, 50, 50, 70, 65, 65, 80]}
    )

print(df)

fit_model = ols(formula="yield ~ fertilizer + rainfall", data=df).fit_model()

print(fit_model.summary())
print("\n\n", fit_model.params)
print("\n\nY_hat:\n", fit_model.fittedvalues)
print("\n\nTSS =", fit_model.centered_tss)
print("\n\nAnova Table\n", anova_lm(fit_model))


plot = plt.figure().gca(projection='3d')

plot.scatter(

            df["fertilizer"]
            , df["rainfall"]
            , df["yield"]
            , color="red"
        )
plot.set_title("Linear Regression Line of Fertilizer, Rainfall and Yield")
plot.set_xlabel("Fertilizer")
plot.set_ylabel("Rainfall")
plot.set_zlabel("Yield")

x_surf = df["fertilizer"]
y_surf = df["rainfall"]

x_surf, y_surf = np.meshgrid(x_surf, y_surf)


exog = pd.core.frame.DataFrame({

    "fertilizer": x_surf.ravel(),
    "rainfall": y_surf.ravel()
})


out = fit_model.predict(exog=exog)

plot.plot_surface(

            x_surf, y_surf
            , out.values.reshape(x_surf.shape), rstride=1, cstride=1
            , alpha=0.5
        )

plt.show()