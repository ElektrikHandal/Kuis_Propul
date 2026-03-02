# Turbojet Engine Performance -- Full Problem Documentation

**Source:** Lecture 02 -- Engine Performance Parameters\
(All formulas strictly taken from provided PowerPoint)

------------------------------------------------------------------------

# TEST CONDITIONS

## 1st Test Condition

-   Flight speed: $V_1 = 210 \ \text{m/s}$
-   Ambient pressure: $p_1 = 22612 \ \text{Pa}$
-   Ambient temperature: $T_1 = 216.65 \ \text{K}$
-   Net thrust: $T = 7482 \ \text{N}$
-   Air mass flow rate: $\dot{m}_a = 21 \ \text{kg/s}$
-   Fuel mass flow rate: $\dot{m}_f = 0.378 \ \text{kg/s}$
-   Fuel heating value: $Q_R = 42.6 \times 10^6 \ \text{J/kg}$
-   Engine speed: $N = 25000 \ \text{rpm}$

------------------------------------------------------------------------

# PART A -- Based on 1st Test Data, Calculate

## 1. Ambient Total Temperature

$$
T_t = T + \frac{V^2}{2 c_p}
$$

## 2. Ambient Total Pressure

$$
p_t = p \left(1 + \frac{V^2}{2 c_p T}\right)^{\frac{\gamma}{\gamma - 1}}
$$

## 3. Mach Number

$$
M = \frac{V}{a}
$$ $$
a = \sqrt{\gamma R T}
$$

## 4. Momentum (Ram) Drag

$$
F_{ram} = \dot{m}_v V
$$ $$
\dot{m}_v = \dot{m}_a \left(1 + \frac{V^2}{2 c_p T}\right)^{\frac{\gamma}{\gamma - 1}}
$$

## 5. Gross Thrust

$$
F_G = T \left(1 + \frac{V^2}{2 c_p T}\right)^{\frac{\gamma}{\gamma - 1}}
$$

## 6. Specific Thrust

$$
ST = \frac{T}{\dot{m}_a}
$$

## 7. Specific Fuel Consumption

$$
SFC = \frac{\dot{m}_f}{T}
$$ $$
SFC_{g/kNs} = \frac{\dot{m}_f}{T} \times 10^6
$$

## 8. Propulsive Efficiency (Turbojet)

$$
\eta_p =
\frac{T V}
{
\frac{1}{2} \dot{m}_a \left[(1+f)V_e^2 - V^2 \right]
}
$$ $$
f = \frac{\dot{m}_f}{\dot{m}_a}
$$

## 9. Thermal Efficiency (Turbojet)

$$
\eta_{th} =
\frac{
\frac{1}{2} \dot{m}_a \left[(1+f)V_e^2 - V^2 \right]
}
{
\dot{m}_f Q_R
}
$$

## 10. Total Efficiency

$$
\eta_0 = \frac{T V}{\dot{m}_f Q_R}
$$ $$
\eta_0 = \eta_p \times \eta_{th}
$$

------------------------------------------------------------------------

# PART B -- Based on 2nd Test Condition, Predict

## 2nd Condition Data

-   Flight speed: $V_2 = 270 \ \text{m/s}$
-   Ambient pressure: $p_2 = 38245 \ \text{Pa}$
-   Ambient temperature: $T_2 = 239.40 \ \text{K}$

### 1. Engine Gross Thrust

$$
F_G = T \frac{p_a}{101325}
$$

### 2. Momentum Drag

$$
F_{ram} = \dot{m}_v V
$$

### 3. Net Thrust

$$
F_N = F_G - F_{ram}
$$

### 4. Air Mass Flow Rate

$$
\dot{m}_v = \dot{m}_a \left(1 + \frac{V^2}{2 c_p T}\right)^{\frac{\gamma}{\gamma - 1}}
$$

### 5. Fuel Mass Flow Rate

$$
f = \frac{\dot{m}_f}{\dot{m}_a}
$$ $$
\dot{m}_{f,2} = f \dot{m}_{a,2}
$$

### 6. Specific Thrust

$$
ST = \frac{F_N}{\dot{m}_{a,2}}
$$

### 7. Specific Fuel Consumption

$$
SFC = \frac{\dot{m}_{f,2}}{F_N}
$$

### 8--10. Efficiencies

Same equations as Part A using updated values.

------------------------------------------------------------------------

# PART C -- Based on 3rd Test Condition (Static, ISA Sea Level)

## 3rd Condition Data

-   $p = 101325 \ \text{Pa}$
-   $T = 288.15 \ \text{K}$
-   Static condition ($V=0$)

### 1. Engine Gross Thrust

$$
F_G = T \frac{p_a}{101325}
$$

### 2. Air Mass Flow Rate

$$
\dot{m}_{a,3} = \dot{m}_a \frac{p_a}{101325}
$$

### 3. Fuel Mass Flow Rate

$$
\dot{m}_{f,3} = f \dot{m}_{a,3}
$$

### 4. Engine Speed

$$
N_{ref} = \frac{N}{\sqrt{\theta}}
$$ $$
\theta = \frac{T_t}{288.15}
$$

### 5. Specific Fuel Consumption

$$
SFC = \frac{\dot{m}_{f,3}}{F_G}
$$

------------------------------------------------------------------------

# ASSUMPTIONS

-   Exhaust nozzle is unchoked\
-   Equilibrium running line does not change with Mach number\
-   Combustion efficiency constant\
-   $c_p = 1004.5 \ \text{J/kgK}$\
-   $\gamma = 1.4$\
-   $R = 287 \ \text{J/kgK}$

------------------------------------------------------------------------

# ISA Reference Values

-   $T_{ref} = 288.15 \ \text{K}$
-   $p_{ref} = 101325 \ \text{Pa}$
