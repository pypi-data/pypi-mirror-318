from pyod.models.lof import LOF

from unquad.utils.enums import Dataset
from unquad.data.loader import DataLoader
from unquad.estimator.detector import ConformalDetector
from unquad.strategy.jackknife import JackknifeConformal
from unquad.utils.metrics import false_discovery_rate, statistical_power

if __name__ == "__main__":
    dl = DataLoader(dataset=Dataset.MUSK)
    x_train, x_test, y_test = dl.get_example_setup(random_state=1)

    ce = ConformalDetector(detector=LOF(), strategy=JackknifeConformal(plus=True))

    ce.fit(x_train)
    estimates = ce.predict(x_test)

    print(f"Empirical FDR: {false_discovery_rate(y=y_test, y_hat=estimates)}")
    print(f"Empirical Power: {statistical_power(y=y_test, y_hat=estimates)}")
