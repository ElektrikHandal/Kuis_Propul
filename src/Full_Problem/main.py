import math
import yaml
import os


# ==========================
# CONSTANTS
# ==========================
CP = 1004.5
GAMMA = 1.4
R = 287.0
T_REF = 288.15


# ==========================
# OPERATING CONDITION
# ==========================
class OperatingCondition:
    def __init__(self, V, p, T):
        self.V = V
        self.p = p
        self.T = T

        self.Tt = self.T + V**2 / (2 * CP)
        self.pt = p * (1 + V**2 / (2 * CP * T))**(GAMMA/(GAMMA-1))
        self.M = V / math.sqrt(GAMMA * R * T)


# ==========================
# TURBOJET ENGINE (ERL METHOD)
# ==========================
class TurbojetEngine:

    def __init__(self,
                 baseline_condition,
                 FN1,
                 ma1,
                 mf1,
                 rpm1,
                 QR):

        # Baseline condition
        self.base = baseline_condition

        # Known baseline performance
        self.FN1 = FN1
        self.ma1 = ma1
        self.mf1 = mf1
        self.rpm1 = rpm1
        self.QR = QR

        # ---- DERIVED VALUES ----

        # Gross thrust at baseline
        self.FG1 = FN1 + ma1 * baseline_condition.V

        # Exit velocity (derived!)
        self.Ve = self.FG1 / ma1


    def evaluate(self, condition):

        # ---------------------------------
        # ERL Scaling (PowerPoint Method)
        # m_dot ∝ p / sqrt(T)
        # ---------------------------------

        pressure_ratio = condition.p / self.base.p
        temp_ratio = math.sqrt(self.base.T / condition.T)

        scale = pressure_ratio * temp_ratio

        # Scale mass flow and fuel flow
        ma = self.ma1 * scale
        mf = self.mf1 * scale

        # RPM scaling
        rpm = self.rpm1 * math.sqrt(condition.T / self.base.T)

        # Thrust from momentum equation
        FG = ma * self.Ve
        Fram = ma * condition.V
        FN = FG - Fram

        # Performance
        ST = FN / ma if ma != 0 else 0
        SFC = mf / FN if FN != 0 else 0

        kinetic = 0.5 * ma * (self.Ve**2 - condition.V**2)

        eta_p = (FN * condition.V) / kinetic if kinetic != 0 else 0
        eta_th = kinetic / (mf * self.QR) if mf != 0 else 0
        eta_o = (FN * condition.V) / (mf * self.QR) if mf != 0 else 0

        return {
            "Gross Thrust": FG,
            "Air Mass Flow": ma,
            "Ram Drag": Fram,
            "Net Thrust": FN,
            "Fuel Mass Flow": mf,
            "RPM": rpm,
            "Specific Thrust": ST,
            "SFC": SFC,
            "Propulsive Efficiency": eta_p,
            "Thermal Efficiency": eta_th,
            "Overall Efficiency": eta_o
        }


# ==========================
# LOAD CONFIG
# ==========================
def load_config():
    config_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "config",
        "config.yaml"
    )

    with open(config_path, "r") as file:
        return yaml.safe_load(file)


# ==========================
# MAIN
# ==========================
def main():

    config = load_config()

    # -----------------------------
    # BASELINE DATA (original input)
    # -----------------------------
    base_cfg = config["baseline"]

    baseline_condition = OperatingCondition(
        base_cfg["V"],
        base_cfg["p"],
        base_cfg["T"]
    )

    FN1 = base_cfg["net_thrust"]
    ma1 = base_cfg["air_mass_flow"]
    mf1 = base_cfg["fuel_mass_flow"]
    rpm1 = base_cfg["rpm"]
    QR = base_cfg["fuel_heating_value"]

    # -----------------------------
    # Create engine (baseline ref)
    # -----------------------------
    engine = TurbojetEngine(
        baseline_condition,
        FN1,
        ma1,
        mf1,
        rpm1,
        QR
    )

    # -----------------------------
    # Evaluate other conditions
    # -----------------------------
    for name, cond in config["conditions"].items():

        condition = OperatingCondition(
            cond["V"],
            cond["p"],
            cond["T"]
        )

        results = engine.evaluate(condition)

        print(f"\n========== {name.upper()} CONDITION ==========")
        for key, value in results.items():
            print(f"{key}: {value:.6f}")


if __name__ == "__main__":
    main()